<?php

session_start();
//변수 정리
$id = $_SESSION['user_id'];
$gender = $_POST['gender'];
$age = $_POST['age'];
$error = $_FILES['file']['error'];
$file_name = $_FILES['file']['name'];
$ext = array_pop(explode('.', $name));

//test
echo INPUT."<br />\nSESSION_ID : ".$_SESSION['user_id']."<br />\nID : ".$id."<br />\nGender : ".$gender."<br />\nAge : ".$age."<br />\nfile_name : ".$file_name."<br />\n";

if($id == NULL){
	echo "<a href=login_screen.html>세션이 종료되었습니다. 다시 로그인해주세요</a>";
	exit();
}

$mysqli = mysqli_connect("localhost", "root", "111111", "face_ad");
if (mysqli_connect_errno()) {		//DB 연결 확인
    die('Connect Error: '.mysqli_connect_error());
}

// 설정
$uploads_dir = './AD';
$allowed_ext = array('jpg','jpeg','png','gif','mp4');
 
// 변수 정리
//$name = $_FILES['myfile']['name'];
//$ext = array_pop(explode('.', $name));
 
// 오류 확인
if( $error != UPLOAD_ERR_OK ) {
	switch( $error ) {
		case UPLOAD_ERR_INI_SIZE:
		case UPLOAD_ERR_FORM_SIZE:
			echo "파일이 너무 큽니다. ($error)";
			break;
		case UPLOAD_ERR_NO_FILE:
			echo "파일이 첨부되지 않았습니다. ($error)";
			break;
		default:
			echo "파일이 제대로 업로드되지 않았습니다. ($error)";
	}
	exit;
}
 
// 확장자 확인
if( !in_array($ext, $allowed_ext) ) {
	echo "허용되지 않는 확장자입니다.";
	exit;
}
 
// 파일 이동
move_uploaded_file( $_FILES['myfile']['tmp_name'], "$uploads_dir/$name");

// 파일 정보 출력
echo "<h2>파일 정보</h2>
<ul>
	<li>파일명: $name</li>
	<li>확장자: $ext</li>
	<li>파일형식: {$_FILES['myfile']['type']}</li>
	<li>파일크기: {$_FILES['myfile']['size']} 바이트</li>
</ul>";