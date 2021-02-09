<?php
date_default_timezone_set('Europe/Istanbul');

$now = strtotime("now");

if ($now >= strtotime("06:00:00") and $now <= strtotime("10:00:00")) {
    echo "Günaydınlar!";
    echo "<br>";
} elseif ($now > strtotime("10:00:00") and $now <= strtotime("17:00:00")) {
    echo "İyi günler!";
} elseif ($now > strtotime("17:00:00") and $now <= strtotime("20:00:00")) {
    echo "İyi Akşamlar!";
} elseif ($now > strtotime("20:00:00") and $now <= strtotime("00:00:00")) {
    echo "İyi Geceler!";
} else {
    echo "Esenlikler Dilerim";
}