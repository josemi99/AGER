<?php
require_once 'database.php';
header("Content-Type: application/json");

$method = $_SERVER['REQUEST_METHOD'];
$id = isset($_GET['delete_id']) ? intval($_GET['delete_id']) : null;

try {
    if ($method === 'GET' && $id) {
        // Tabla corregida: AGER_TRENES
        $stmt = $pdo->prepare("DELETE FROM AGER_TRENES WHERE id = ?");
        $stmt->execute([$id]);
        echo json_encode(["success" => "Tren eliminado"]);
    } 
    elseif ($method === 'GET') {
        $q = isset($_GET['q']) ? $_GET['q'] : '';
        if ($q) {
            // Tabla corregida: AGER_TRENES
            $stmt = $pdo->prepare("SELECT * FROM AGER_TRENES WHERE numero LIKE ? OR origen LIKE ? OR destino LIKE ?");
            $stmt->execute(["%$q%", "%$q%", "%$q%"]);
        } else {
            $stmt = $pdo->query("SELECT * FROM AGER_TRENES ORDER BY id DESC");
        }
        echo json_encode($stmt->fetchAll());
    } 
    elseif ($method === 'POST') {
        $data = json_decode(file_get_contents('php://input'), true);
        // Tabla corregida: AGER_TRENES
        $sql = "INSERT INTO AGER_TRENES (numero, origen, destino, empresa, fecha, estatus, situacion) VALUES (?, ?, ?, ?, ?, ?, ?)";
        $stmt = $pdo->prepare($sql);
        $stmt->execute([
            $data['numero'], $data['origen'], $data['destino'], 
            $data['empresa'], $data['fecha'], $data['estatus'], $data['situacion']
        ]);
        echo json_encode(["success" => true]);
    }
} catch (Exception $e) {
    http_response_code(500);
    echo json_encode(["error" => $e->getMessage()]);
}