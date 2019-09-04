<?php
session_start();

$id = $_POST['id'];
$pw = $_POST['pw'];
$mysqli = mysqli_connect("localhost", "root", "111111", "face_ad");

if (mysqli_connect_errno()) {		//DB 연결 확인
    die('Connect Error: '.mysqli_connect_error());
}

//echo "input ".$id."/".$pw."<br />\n";

$sql = "SELECT * FROM user_table WHERE id = '$id'";
$result = $mysqli->query($sql);

//echo $result->num_rows."<br />\n";

if ($result->num_rows == 1) {	//검색된 row가 한개
	$row = $result->fetch_array(MYSQLI_ASSOC);	// 한 열을 배열로 가져오기
	if($row['pw'] == $pw){
		$_SESSION['login_id'] = $id;		//로그인 성공시 세션 변수 만들기
		if(isset($_SESSION['user_id'])){
			//header('Location: ./adv_regist_screen.html');
			header('Location: ./session_check.php');
		}
		else {
			echo "세션 저장 실패";
		}
	}
	else {
		echo "wrong id or pw #0001";
	}
}
else {
	echo "wrong id or pw #0002";
}


?>