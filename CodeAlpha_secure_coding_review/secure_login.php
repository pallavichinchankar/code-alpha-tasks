<?php
$conn = mysqli_connect("localhost", "root", "", "testdb");

session_start();

$username = $_POST['username'];
$password = $_POST['password'];

$stmt = $conn->prepare("SELECT password FROM users WHERE username = ?");
$stmt->bind_param("s", $username);
$stmt->execute();
$result = $stmt->get_result();

if ($row = $result->fetch_assoc()) {
    if (password_verify($password, $row['password'])) {
        session_regenerate_id(true);
        $_SESSION['user'] = $username;
        echo "Login Successful";
    } else {
        echo "Invalid Credentials";
    }
} else {
    echo "Invalid Credentials";
}
?>
