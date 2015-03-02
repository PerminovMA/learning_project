var app = angular.module('learning_app', ['connector']);

app.config(function ($interpolateProvider) {
    //allow django templates and angular to co-exist
    $interpolateProvider.startSymbol('{[{');
    $interpolateProvider.endSymbol('}]}');
});


app.controller('LearningController', function ($scope) {
    $scope.username = "Mihail";
});

app.controller('ConnectorController', function ($scope, Project) {
    $scope.response_text = Project.get();
});