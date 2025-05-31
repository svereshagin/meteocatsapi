<template>
  <div class="p-4 max-w-md mx-auto">
    <h2 class="text-xl font-bold mb-2">Поиск погоды по городу</h2>

    <!-- Поле ввода с автодополнением -->
    <div class="relative mb-2">
      <input
          v-model="city"
          @input="onInputChange"
          @keydown.down="moveHighlightDown"
          @keydown.up="moveHighlightUp"
          @keydown.enter="selectHighlighted"
          @blur="hideSuggestions"
          type="text"
          placeholder="Введите город"
          class="border p-2 w-full rounded"
          ref="searchInput"
      />

      <!-- Список подсказок -->
      <ul
          v-if="showSuggestions && filteredSuggestions.length"
          class="absolute z-10 w-full mt-1 bg-white border border-gray-300 rounded shadow-lg max-h-60 overflow-y-auto"
      >
        <li
            v-for="(item, index) in filteredSuggestions"
            :key="index"
            @mousedown="selectSuggestion(item)"
            :class="['p-2 hover:bg-blue-50 cursor-pointer', { 'bg-blue-100': highlightedIndex === index }]"
        >
          {{ item.full_name }}
        </li>
      </ul>
    </div>

    <button
        @click="fetchWeather"
        class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
    >
      Узнать погоду
    </button>

    <!-- Блок с погодой -->
    <div v-if="weatherData" class="mt-4 p-4 border rounded bg-gray-50">
      <h3 class="font-bold mb-2">Прогноз погоды для {{ city }}</h3>
      <div v-for="(item, index) in weatherData" :key="index" class="mb-2">
        <p><strong>Время:</strong> {{ item.time }}</p>
        <p><strong>Температура:</strong> {{ item.temperature }} °C</p>
        <hr class="my-2">
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'WeatherSearch',
  data() {
    return {
      city: '',
      weatherData: null,
      allSuggestions: [],
      showSuggestions: false,
      highlightedIndex: -1,
      lastRequest: null
    };
  },
  computed: {
    filteredSuggestions() {
      if (!this.city) return this.allSuggestions;
      return this.allSuggestions.filter(item =>
          item.full_name.toLowerCase().includes(this.city.toLowerCase())
      );
    }
  },
  methods: {
    async fetchWeather() {
      if (!this.city) return;

      try {
        const response = await axios.get(`http://localhost:8123/weather/${encodeURIComponent(this.city)}`);
        this.weatherData = response.data.time.map((time, index) => ({
          time: time,
          temperature: response.data.temperature_2m[index]
        }));
      } catch (error) {
        console.error('Ошибка при запросе погоды:', error);
        this.weatherData = null;
      }
    },

    async fetchSuggestions() {
      if (this.city.length < 2) {
        this.allSuggestions = [];
        return;
      }

      // Отменяем предыдущий запрос, если он существует
      if (this.lastRequest) {
        this.lastRequest.cancel();
      }

      // Создаем новый токен отмены
      this.lastRequest = axios.CancelToken.source();

      try {
        const response = await axios.get('http://localhost:8123/suggestions/${encodeURIComponent(this.city)}', {
          params: { q: this.city },
          cancelToken: this.lastRequest.token
        });

        this.allSuggestions = response.data.suggestion || [];
        this.showSuggestions = true;
      } catch (error) {
        if (!axios.isCancel(error)) {
          console.error('Ошибка при получении подсказок:', error);
        }
      }
    },

    onInputChange() {
      this.fetchSuggestions();
      this.highlightedIndex = -1;
    },

    selectSuggestion(item) {
      this.city = item.full_name;
      this.showSuggestions = false;
      this.fetchWeather();
    },

    moveHighlightDown() {
      if (this.highlightedIndex < this.filteredSuggestions.length - 1) {
        this.highlightedIndex++;
      }
    },

    moveHighlightUp() {
      if (this.highlightedIndex > 0) {
        this.highlightedIndex--;
      }
    },

    selectHighlighted() {
      if (this.showSuggestions && this.highlightedIndex >= 0) {
        this.selectSuggestion(this.filteredSuggestions[this.highlightedIndex]);
      } else {
        this.fetchWeather();
      }
    },

    hideSuggestions() {
      setTimeout(() => {
        this.showSuggestions = false;
      }, 200);
    }
  }
};
</script>

<style scoped>
.relative {
  position: relative;
}

.suggestions-list {
  position: absolute;
  width: 100%;
  max-height: 300px;
  overflow-y: auto;
  border: 1px solid #ddd;
  border-radius: 8px;
  background: white;
  z-index: 1000;
  margin-top: 4px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.suggestion-item {
  padding: 10px 16px;
  cursor: pointer;
  transition: background-color 0.2s;
}

.suggestion-item:hover,
.highlighted {
  background-color: #f5f5f5;
}
</style>