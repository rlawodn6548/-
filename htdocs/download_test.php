<?php

$filename = "3��.png";                      
$file_dir = "./AD/".$filename;
$newname = "test_img17.jpg";	//�ּ��� �ּ��ּ� �ѱ��ּ�

header('Content-Type: application/x-octetstream');
header('Content-Length: '.filesize($file_dir));
header('Content-Disposition: attachment; filename='.$newname);
header('Content-Transfer-Encoding: binary');

$fp = fopen($file_dir, "r");
fpassthru($fp);
fclose($fp);

?>