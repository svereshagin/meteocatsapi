FROM node:lts-alpine

RUN npm install -g http-server

WORKDIR /app

COPY frontend/forecastapi/package*.json ./
RUN npm install

COPY frontend/forecastapi .

RUN npm run build

EXPOSE 5143
CMD ["http-server", "dist", "-p", "5143"]
