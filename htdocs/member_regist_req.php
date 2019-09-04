<?php

//<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
//header("Content-Type:text/html; charset=utf-8");

$new_id = $_POST['new_id'];
$new_pw = $_POST['new_pw'];
$new_pwc = $_POST['new_pwc'];
$e_mail = $_POST['e_mail'];

if($new_pw != $new_pwc){
	echo "비밀번호와 비밀번호 확인이 서로 다릅니다.<br />\n<br />\n";
	echo "<a href=member_regist_screen.html>돌아가기</a>";
	exit();
}

if($new_id == NULL || $new_pw == NULL || $new_pwc == NULL || $e_mail == NULL){
	echo "빈 칸을 모두 채워주세요.<br />\n<br />\n";
	echo "<a href=member_regist_screen.html>돌아가기</a>";
	exit();
}

$mysqli = mysqli_connect("localhost", "root", "111111", "face_ad");
if (mysqli_connect_errno()) {		//DB 연결 확인
    die('Connect Error: '.mysqli_connect_error());
}

$sql = "SELECT * FROM user_table WHERE id = '$id'";
$result = $mysqli->query($sql);
if ($result->num_rows == 1){
	echo "중복된 ID 입니다.";
	echo "<a href=member_regist_screen.html>돌아가기</a>";
	exit();
}

$regist_sql = mysqli_query($mysqli, "INSERT INTO user_table (id, pw, auth)
VALUES ('$new_id','$new_pw','normal')");
if($regist_sql){
	echo "가입 성공!! 감사합니다.<br />\n<br />\n";
	echo "<a href= main.php>로그인 바로가기</a>";
	exit();
}

?>