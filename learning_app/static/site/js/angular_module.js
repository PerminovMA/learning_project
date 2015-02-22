var app = angular.module('learning_app', []);

app.config(function ($interpolateProvider) {
    //allow django templates and angular to co-exist
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
});


app.controller('LearningController', function ($scope) {
    $scope.username = "Mihail";
});