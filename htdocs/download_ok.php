<?php

$filename = "img2.jpg";
$newname = "00072.jpg";
//$file = $_SERVER["DOCUMENT_ROOT"]."/AD/".$filename;
$file = "./AD/".$filename;
//$size = filesize($file);

//$path_parts = pathinfo($file); 
//$ext = strtolower($path_parts["extension"]);

/*
 *  ex)   $filename = "image1.png"; 
 *        $file =  $_SERVER['DOCUMENT_ROOT'] . "/images/" .$filename;
*/

if(is_file($file)) {
	if (preg_match("MSIE", $_SERVER['HTTP_USER_AGENT'])) { 
        header('Content-Type: application/x-octetstream'); 
        header('Content-Length: '.filesize($file));
        header('Content-Disposition: attachment; filename='.$file); // �ٿ�ε�Ǵ� ���ϸ� (���� ���ϸ�� ������ ���� ����)
        header('Content-Transfer-Encoding: binary'); 
        header('Cache-Control: must-revalidate, post-check=0, pre-check=0');
        header('Pragma: public'); 
        header('Expires: 0');
    }
    else { 
        header('Content-Type: application/x-octetstream'); 
        header('Content-Length: '.filesize($file)); 
        header('Content-Disposition: attachment; filename='.$newname); // �ٿ�ε�Ǵ� ���ϸ� (���� ���ϸ�� ������ ���� ����)
        //header('Content-Description: PHP Generated Data'); 
		header('Content-Transfer-Encoding: binary'); 
        //header('Pragma: no-cache'); 
        //header('Expires: 0'); 
    }

    $fp = fopen($file, "r");
	fpassthru($fp);
	fclose($fp);
}
else {
    echo "no file";
}

/*
header('Content-Type: application/x-octetstream');
header('Content-Length: '.filesize($file));
header('Content-Disposition: attachment; filename='.$newname);
header('Content-Transfer-Encoding: binary');

$fp = fopen($file, "r");
fpassthru($fp);
fclose($fp);
*/

?>