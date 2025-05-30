<template>
  <div class="p-4 max-w-md mx-auto">
    <h2 class="text-xl font-bold mb-2">Поиск погоды по городу</h2>
    <input
        v-model="city"
        @keyup.enter="getWeather"
        type="text"
        placeholder="Введите город"
        class="border p-2 w-full rounded mb-2"
    />
    <button
        @click="getWeather"
        class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
    >
      Узнать погоду
    </button>

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
      weatherData: null
    };
  },
  methods: {
    async getWeather() {
      if (!this.city) return;

      try {
        const response = await axios.get(`/localhost/weather/${this.city}`);
        console.log('Данные погоды:', response.data);

        // Преобразуем данные в нужный формат
        this.weatherData = response.data.time.map((time, index) => ({
          time: time,
          temperature: response.data.temperature_2m[index]
        }));

      } catch (error) {
        console.error('Ошибка при запросе погоды:', error);
        this.weatherData = null;
        alert('Не удалось получить данные о погоде');
      }
    }
  }
};
</script>