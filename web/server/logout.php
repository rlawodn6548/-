<?php
session_start();

unset($_SESSION['login_id']);
header('Location: ./login_screen.html');

?>