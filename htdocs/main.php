<?php
session_start();
if(!isset($_SESSION['user_id']))	//세션이 존재하지 않을때
{
	header('Location: ./login_screen.html');
}
else{
	echo "login success!!<br />\n";
	header('Location: ./adv_regist_screen.html');
}

?>