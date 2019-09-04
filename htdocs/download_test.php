<?php

$filename = "3명.png";                      
$file_dir = "./AD/".$filename;
$newname = "test_img17.jpg";	//주석이 주석주석 한글주석

header('Content-Type: application/x-octetstream');
header('Content-Length: '.filesize($file_dir));
header('Content-Disposition: attachment; filename='.$newname);
header('Content-Transfer-Encoding: binary');

$fp = fopen($file_dir, "r");
fpassthru($fp);
fclose($fp);

?>