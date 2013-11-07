var App = angular.module('intranet');


App.controller('latenessCtrl', function($scope, $http, $dialog, $timeout, dialog, $callerScope) {
    $scope.errors = {};

    $scope.close = function() {
        dialog.close();
    };

    $scope.add = function() {
        $scope.form_submitted = true;

        $http.post('/api/lateness', {
            lateness: {
                popup_date: $scope.lateness.popup_date,
                popup_explanation: $scope.lateness.popup_explanation,
                late_start: $scope.lateness.late_start,
                late_end: $scope.lateness.late_end,
                work_from_home: $scope.lateness.work_from_home
            }
        }).success(function(data) {
            $scope.close();
        }).error(function(data) {
            angular.forEach(data, function(errors, field) {
                $scope.latenessForm[field].$setValidity('server', false);
                $scope.errors[field] = errors.join('<br/>');
            });
        });
    };
});