
var app = angular.module("notesKeeper", ['ui.router']);  
// define route configurations inside app.config 
// injecting dependencies 
app.config(function($stateProvider, $urlRouterProvider, $httpProvider) { 
  
    // creating routes or states
    var loginState = {
        name: 'login',
        url: '/',
        templateUrl: '/login-page.html',
        controller: 'LoginCtrl'
    };
    $stateProvider.state(loginState);
    /*$stateProvider 
        .state('Login', { 
            url : '/', 
            templateUrl: "login-page.html", 
            controller : "LoginCtrl"
        }) 
        .state('Signup', { 
            url : '/signup', 
            templateUrl : "<h1>Signup Page</h1>", 
            controller : "SignupCtrl"
        });*/ 
  
    // Redirect to home page if url does not  
    // matches any of the three mentioned above 
    $urlRouterProvider.otherwise("/"); 
}); 
  
// create empty controllers for the states as we are 
// not doing anything but just displaying message 
app.controller('MainCtrl', function($scope, $http, $state, $stateParams) {}); 
app.controller('LoginCtrl', function($scope, $http, $state, $stateParams) {});
