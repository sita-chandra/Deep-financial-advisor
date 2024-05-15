<?php

$conn = new mysqli('localhost','root','','dfa');

$ip1 = $_POST['input1'];
$ip2 = $_POST['input2'];
$ip3 = $_POST['input3'];
$ip4 = $_POST['input4'];
$ip5 = $_POST['input5'];
$ip6 = $_POST['input6'];
$ip7 = $_POST['input7'];
$ip8 = $_POST['input8'];
$ip9 = $_POST['input9'];
$ip10 = $_POST['input10'];

if ($conn->connect_error) {
    die('Connection Failed : ' . $conn->connect_error);
} else {
    $stmt = $conn->prepare("INSERT INTO userinput (ip1, ip2, ip3, ip4, ip5, ip6, ip7, ip8, ip9, ip10) VALUES (?,?,?,?,?,?,?,?,?,?)");
    $stmt->bind_param("ssssssssss", $ip1, $ip2, $ip3, $ip4, $ip5, $ip6, $ip7, $ip8, $ip9, $ip10);
    $stmt->execute();
    echo 'start';
    $output = shell_exec("python C:\Users\Admin\Downloads\Algofordfa.py 2>&1");
    echo "<pre>$output</pre>";
    echo 'stop';
    $stmt->close();
    $conn->close();
}

?>