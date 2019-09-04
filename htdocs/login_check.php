<?php

$id = $_POST['id'];
$pw = $_POST['pw'];
$mysqli = mysqli_connect("localhost", "root", "111111", "face_ad");


if (mysqli_connect_errno()) {
  ?>
   <dialog open>
    <h2>데이터베이스와 연결되지 않았습니다.</h2>
    <form action="login_screen.html" method="post">
      <input type="submit" value="확인">
    </form>
  </dialog>
  <?php
}

//echo "input ".$id."/".$pw."<br />\n";

$sql = "SELECT * FROM user_table WHERE id = '$id'";
$result = $mysqli->query($sql);

//echo $result->num_rows."<br />\n";

if ($result->num_rows == 1) {	//�˻��� row�� �Ѱ�
	$row = $result->fetch_array(MYSQLI_ASSOC);	// �� ���� �迭�� ��������
	if($row['pw'] == $pw){
		$_SESSION['user_id'] = $id;		//�α��� ������ ���� ���� ������
		if(isset($_SESSION['user_id'])){
			header('Location: ./main.php');
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
