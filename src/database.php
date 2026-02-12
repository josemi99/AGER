<?php
/**
 * AGER - Conexión Maestra Dinámica
 */

// 1. Capturamos las variables enviadas por el Docker Compose
$host    = getenv('DB_HOST') ?: 'db'; 
$db_name = getenv('DB_NAME') ?: 'AGER_TRENES'; 
$user    = getenv('DB_USER'); 
$pass    = getenv('DB_PASS'); 
$charset = 'utf8mb4';

// 2. Configuramos el DSN (Data Source Name)
$dsn = "mysql:host=$host;dbname=$db_name;charset=$charset";

// 3. Opciones de seguridad y rendimiento de PDO
$options = [
    PDO::ATTR_ERRMODE            => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
    PDO::ATTR_EMULATE_PREPARES   => false,
];

try {
    // Intentamos la conexión
    $pdo = new PDO($dsn, $user, $pass, $options);
} catch (\PDOException $e) {
    // Si falla, devolvemos un error limpio en JSON para el frontend
    header('Content-Type: application/json');
    http_response_code(500);
    echo json_encode([
        "error" => "Error de acceso ferroviario",
        "details" => "No se pudo conectar con las credenciales proporcionadas."
    ]);
    exit;
}