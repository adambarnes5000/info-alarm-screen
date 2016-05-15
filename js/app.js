
var back_end = 'http://dev.pi.com:5000/';

var app = angular.module('myApp', ['jkuri.timepicker']);

app.controller('newsController', function($scope, $http, $interval) {
    function load_news(){
        $http.get(back_end+"news").then(function (response) {
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
        $http.get(back_end+"buses").then(function (response) {
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
        $http.get(back_end+"weather").then(function (response) {
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
        $http.get(back_end+"killchromium").then(function (response) {
                        $scope.result = response.data;
                    });
    }
});

app.controller('alarmController', function($scope, $http, $interval, $window) {
    function load_next_alarm(){
        $http.get(back_end+"nextalarm").then(function (response) {
                $scope.nextAlarm = response.data;
            });
    }
    $http.get(back_end+"alarms").then(function (response) {
                $scope.alarms = response.data;
            });
    load_next_alarm();
    $interval(function(){
        load_next_alarm();
    },60000);
    $scope.delete = function (idx){
        $scope.alarms.splice(idx, 1);
    }
    $scope.add_new = function (){
        $scope.alarms.push(['07:30','WORKDAY'])
    }
    $scope.save = function (){
        $http.post(back_end+"alarms",$scope.alarms).then(function (response) {
                $window.location.href = 'index.html';
            });
    }
    $scope.cancel = function (){
        $window.location.href = 'index.html';
    }
    $scope.edit_alarms = function (){
        $window.location.href = 'alarms.html';
    }
    $scope.day_types={'Every Day':'EVERYDAY','Work Day':'WORKDAY','Weekend':'WEEKEND'}
});