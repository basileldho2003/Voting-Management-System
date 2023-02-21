function ageCalculator() {
    var userinput = document.getElementById("ndob").value;
    var dob = new Date(userinput);
    var month_diff = Date.now() - dob.getTime();
    var age_dt = new Date(month_diff);
    var year = age_dt.getUTCFullYear();
    var age = parseInt(Math.abs(year - 1970));
    if (age < 18) {
        alert("Not eligible!");
        document.getElementById("nage").reset();
    }
    else {
        document.getElementById("nage").value = age;
    }
}
