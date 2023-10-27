<?php
    error_reporting(0); //Reporta errores
    session_start(); //
    $con = new mysqli("localhost", "root", "", "cliente");
    if ($con->connect_errno)
    {
        echo "Fallo al conectar a MySQL: (" . $con-> connect_errno . ")" . $con->connect_error;
        exit();
    }    
    @mysqli_query($con, "SET NAMES 'utf8'");
    if ($_POST['usuario'] == null || $_POST['contrasena'] == null)

    {
        echo '<span>Por favor complete todos los campos.</span>';
    }

    else
    {
        $user = $_POST['usuario'];
        $contrasena = $_POST["contrasena"];
        $consulta = mysqli_query($con, "SELECT * FROM login WHERE usuario = '$user' and contrasena='$contrasena'");

        if(mysqli_fetch_array($consulta)>0) {
            $_SESSION["usuario"] = $user;
            echo '<script>location.href = "indexcompleto.php"</script';
        }
        else
        {
            echo '<span>El usuario y/o clave son incorrectas, vuelva a intentarlo.</span>';
            echo '<script>location.href = "indexlogin.html"</script>';
        }
    }
?> 