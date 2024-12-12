<!DOCTYPE html>
<html lang="en">
<head>  
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FORMULARIO 1</title>
    <style>
        .container {
            display: grid;
            gap: 5px;
            border: 2px solid rgb(0, 0, 0);
            padding: 50px;
            width: 30%;
            margin: auto;
        }
        .container div {
            width: 100%;
        }
        .container label {
            display: flex;
            color: black;
        }
        .container label span {
            color: red;
            font-weight: normal;
            margin-left: 5px;
        }
        .container input[type="text"],
        .container select {
            width: calc(100% - 20px);
            padding: 10px;
            box-sizing: border-box;
        }
        table {
            width: 100%;
        }
        table td {
            text-align: center;
        }
        form {
            text-align: center;
        }
    </style>
</head>
<body>
    <div class="container">
        <center><h1>Beneficiario</h1></center>
        <!-- Aquí añadimos el action -->
        <form method="POST" action="buscar.php">
            <div>
                <label for="BUSCAR">Ingresar Datos: <span>*</span></label>
                <input type="text" id="BUSCAR" name="buscar" placeholder="Ingrese su Id, Nombre o Descripción">
            </div>
            <br/>
            <input type="submit" value="BUSCAR">
        </form>
        <br/>
    </div>
</body>
</html>
