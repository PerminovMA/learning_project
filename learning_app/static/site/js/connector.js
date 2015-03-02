angular.module('connector', ['ngResource']).
    factory('Project', function ($resource) {
        var u = $resource('http://127.0.0.1:8000/get_data', {});
        return u;
    });