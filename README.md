# 🚂 AGER - Sistema de registro de circulaciones ferroviarias

AGER es una plataforma integral para el registro de circulaciones ferroviarias que una persona haya visto. Este proyecto utiliza una arquitectura moderna basada en microservicios con Docker, facilitando su despliegue en entornos de desarrollo como **WSL**.

## 🛠️ Tecnologías utilizadas
* **Frontend:** HTML5, CSS3, JavaScript (Buscador RFIG en tiempo real).
* **Backend:** PHP 8.2 (Motor de procesamiento).
* **Base de Datos:** MySQL 8.0 (Almacenamiento persistente).
* **Servidor Web:** Nginx (Proxy inverso).
* **Gestión:** phpMyAdmin (Administración de BD).

---

## 🚀 Guía de Inicio Rápido

Sigue estos pasos para levantar el entorno en menos de 2 minutos:

### 1. Preparación del entorno
Asegúrate de tener instalado Docker Desktop y configurado el backend de WSL en tu sistema.

### 1. Preparación
Asegúrate de tener Docker Desktop ejecutándose y estar en un terminal Bash (WSL2 recomendado).

### 2. Configuración Inicial
Ejecuta el script maestro de configuración:
```bash
chmod +x setup.sh control.sh
./setup.sh
```
### 3 Control.sh
Luego tienes el archivo control.sh [parámetro] en el que puedes hacer cualquier cosa sin necesidad de usar el comando docker compose.

Uso: ./control.sh {restart|build|start|stop|down|status|logs}

Automáticamente te hace cualquier proceso que quieras.