<html lang="en">
<head>
    <title>Find Perfect number </title>
</head>
<body>

<form method="post">
    <label for="num">Enter a Number: </label>
    <input id="num" type="text" name="number"/>
    <button type="submit">Check</button>
</form>
</body>

</html>
<?php
if ($_POST) {
//get the post value from form
    $num = $_POST['number'];
    $i = 1;
    $sum = 0;
    while ($i < $num) {
        if ($num % $i == 0) {
            $sum = $sum + $i;
        }
        $i++;
    }
    if ($num == $sum) {
        echo " <span style = 'color:green'> The number is Perfect Number!!</span> ";
    } else {
        echo " <span style = 'color:red'> The number is not a Perfect Number!!</span> ";
    }
}
?>