#!/bin/bash

echo "------------------------------------------"
echo "🏗️  GENERADOR MAESTRO AGER"
echo "------------------------------------------"

# 1. Solicitar credenciales
read -p "👤 Usuario App: " USER_APP
read -s -p "🔑 Pass App: " PASS_APP
echo -e "\n"
read -s -p "👑 Pass ROOT: " PASS_ROOT
echo -e "\n"


# 2. Generar el Docker-Compose (Inyectando valores directamente)
cat <<EOF > docker-compose.yml
services:
  db:
    image: mysql:8.0
    container_name: ager_db
    restart: always
    environment:
      MYSQL_DATABASE: AGER_TRENES
      MYSQL_USER: $USER_APP
      MYSQL_PASSWORD: $PASS_APP
      MYSQL_ROOT_PASSWORD: $PASS_ROOT
    volumes:
      - ./db-init/init.sql:/docker-entrypoint-initdb.d/init.sql

  php:
    build:
      context: .
      dockerfile: ./docker/php.Dockerfile
    container_name: ager_php
    environment:
      DB_HOST: db
      DB_NAME: AGER_TRENES
      DB_USER: $USER_APP
      DB_PASS: $PASS_APP
    volumes:
      - ./src:/var/www/html
    depends_on:
      - db

  web:
    image: nginx:alpine
    container_name: ager_web
    ports:
      - "8080:80"
    volumes:
      - ./src:/var/www/html
      - ./docker/nginx.conf:/etc/nginx/conf.d/default.conf
    depends_on:
      - php

  phpmyadmin:
    image: phpmyadmin:latest
    container_name: ager_pma
    ports:
      - "8081:80"
    environment:
      PMA_HOST: db
      PMA_USER: root
      PMA_PASSWORD: $PASS_ROOT
    depends_on:
      - db
EOF

echo "✅ Dockerfile y Docker-Compose generados con éxito."
echo "🚀 Iniciando construcción..."
bash control.sh build