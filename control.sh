#!/bin/bash

# Colores para una mejor legibilidad
G='\033[0;32m' # Verde
B='\033[0;34m' # Azul
Y='\033[1;33m' # Amarillo
NC='\033[0m'   # Sin color

# Función para mostrar los enlaces de acceso
mostrar_accesos() {
    echo -e "\n${B}-------------------------------------------------------${NC}"
    echo -e "${G}🚀 ¡Servicios de AGER listos!${NC}"
    echo -e "${B}-------------------------------------------------------${NC}"
    echo -e "${Y}🌍 Aplicación Web (Buscador):${NC}  http://localhost:8080"
    echo -e "${Y}🗄️  Base de Datos (phpMyAdmin):${NC} http://localhost:8081"
    echo -e "${B}-------------------------------------------------------${NC}\n"
}

if [ -z "$1" ]; then
    echo "Uso: ./control.sh {build|start|stop|down|status|logs}"
    exit 0
fi

case "$1" in
    build)
        echo -e "${B}Reconstruyendo entorno AGER...${NC}"
        docker compose up -d --build
        mostrar_accesos
        ;;
    start)
        echo -e "${B}Iniciando servicios...${NC}"
        docker compose up -d
        mostrar_accesos
        ;;
    stop)
        echo -e "${B}Deteniendo servicios...${NC}"
        docker compose stop
        ;;
    down)
        echo -e "${B}Eliminando contenedores y redes...${NC}"
        docker compose down
        ;;
    status)
        echo -e "${B}Estado actual de AGER:${NC}"
        docker compose ps
        ;;
    logs)
        docker compose logs -f
        ;;
    restart)
        docker compose down
        docker compose up -d --build
        ;;
    *)
        echo -e "${Y}Opción no válida.${NC} Uso: ./control.sh {build|start|stop|down|status|logs}"
        exit 1
        ;;
esac

exit 0