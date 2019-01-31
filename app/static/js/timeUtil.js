function timeStampToDatetime (s) {
    var datetime = new Date();
    datetime.setTime(s * 1000);
    var year = datetime.getFullYear();
    var month = datetime.getMonth() + 1;
    var date = datetime.getDate();
    var hour = datetime.getHours();
    var minute = datetime.getMinutes();
    var second = datetime.getSeconds();
    return year + "-" + month + "-" + date + " " + hour + ":"+ minute + ":" + second;
}