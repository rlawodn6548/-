<?php
session_start();

$id = $_POST['id'];
$pw = $_POST['pw'];
$mysqli = mysqli_connect("localhost", "root", "111111", "face_ad");

if (mysqli_connect_errno()) {		//DB ���� Ȯ��
    die('Connect Error: '.mysqli_connect_error());
}

//echo "input ".$id."/".$pw."<br />\n";

$sql = "SELECT * FROM user_table WHERE id = '$id'";
$result = $mysqli->query($sql);

//echo $result->num_rows."<br />\n";

if ($result->num_rows == 1) {	//�˻��� row�� �Ѱ�
	$row = $result->fetch_array(MYSQLI_ASSOC);	// �� ���� �迭�� ��������
	if($row['pw'] == $pw){
		$_SESSION['login_id'] = $id;		//�α��� ������ ���� ���� �����
		if(isset($_SESSION['user_id'])){
			//header('Location: ./adv_regist_screen.html');
			header('Location: ./session_check.php');
		}
		else {
			echo "���� ���� ����";
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