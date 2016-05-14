
var app = angular.module('myApp', []);

app.controller('newsController', function($scope, $http, $interval) {
    function load_news(){
        $http.get("http://192.168.192.47:5000/news").then(function (response) {
                $scope.news = response.data;
            });
    }
    load_news();
    $interval(function(){
        load_news();
    },300000);
});

app.controller('busesController', function($scope, $http, $interval) {
    function load_buses(){
        $http.get("http://192.168.192.47:5000/buses").then(function (response) {
                $scope.buses = response.data;
            });
    }
    load_buses();
    $interval(function(){
        load_buses();
    },30000);
});

app.controller('weatherController', function($scope, $http, $interval) {
    function load_weather(){
        $http.get("http://192.168.192.47:5000/weather").then(function (response) {
                $scope.weather = response.data;
            });
    }
    load_weather();
    $interval(function(){
        load_weather();
    },1800000);
});

app.controller('timeController', function($scope, $http, $interval) {
    function load_time(){
        $scope.currentTime=moment().format('dddd MMMM Do YYYY, HH:mm')
    }
    load_time();
    $interval(function(){
        load_time();
    },1000);
    $scope.quit_console = function(){
        $http.get("http://192.168.192.47:5000/killchromium").then(function (response) {
                        $scope.result = response.data;
                    });
    }
});

app.controller('alarmController', function($scope, $http, $interval) {
    function load_alarm(){
        $http.get("http://192.168.192.47:5000/alarm").then(function (response) {
                $scope.nextAlarm = response.data;
            });
    }
    load_alarm();
    $interval(function(){
        load_alarm();
    },60000);
});