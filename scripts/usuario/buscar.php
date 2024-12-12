<center>
<?php
// Configuración de conexión a la base de datos
$host = 'localhost'; // Cambia si tu servidor es diferente
$user = 'root';      // Cambia si tienes otro usuario
$password = '';      // Cambia si tienes una contraseña
$dbname = 'prac4_db';

try {
    // Crear una conexión PDO
    $pdo = new PDO("mysql:host=$host;dbname=$dbname;charset=utf8", $user, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    if ($_SERVER['REQUEST_METHOD'] === 'POST') {
        if (!empty($_POST['buscar'])) {
            $buscar = htmlspecialchars($_POST['buscar']); // Sanitizar el input

            // Consulta preparada para evitar inyección SQL
            $stmt = $pdo->prepare("SELECT * FROM registros WHERE id = :id OR Nombre LIKE :buscar OR descripcion LIKE :buscar");

            // Vinculamos los valores a la consulta preparada
            $stmt->execute([
                'id' => is_numeric($buscar) ? $buscar : -1, // Usamos el ID si es un número; de lo contrario, asignamos un valor imposible
                'buscar' => "%$buscar%"
            ]);

            $resultados = $stmt->fetchAll(PDO::FETCH_ASSOC);

            if (count($resultados) > 0) {
                echo "<h1>Resultados de la búsqueda</h1>";
                echo "<table border='1'>";
                echo "<tr><th>ID</th><th>Nombre</th><th>Descripción</th></tr>";
                foreach ($resultados as $fila) {
                    echo "<tr>";
                    echo "<td>" . $fila['id'] . "</td>";
                    echo "<td>" . htmlspecialchars($fila['Nombre']) . "</td>";
                    echo "<td>" . htmlspecialchars($fila['descripcion']) . "</td>";
                    echo "</tr>";
                }
                echo "</table>";
            } else {
                echo "<p>No se encontraron resultados para: <strong>" . $buscar . "</strong></p>";
            }
        } else {
            echo "<p>Por favor, ingresa un término para buscar.</p>";
        }
    }
} catch (PDOException $e) {
    // Manejo de errores de conexión
    echo "Error de conexión a la base de datos: " . $e->getMessage();
}
?>

<!-- Botón "Atrás" -->
<div style="margin-top: 20px; text-align: center;">
    <a href="BuscarUsuario.php" style="text-decoration: none; padding: 10px 20px; background-color: #007bff; color: white; border-radius: 5px; font-size: 16px;">Atrás</a>
</div>
</center>