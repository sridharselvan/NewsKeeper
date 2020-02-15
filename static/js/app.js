
var app = angular.module("notesKeeper", ['ui.router']);  
// define route configurations inside app.config 
// injecting dependencies 
app.config(function($stateProvider, $urlRouterProvider, $httpProvider) { 
  
    // creating routes or states
    var loginState, signupState;
    loginState = {
        name: 'login',
        url: '/',
        templateUrl: '/login-page.html',
        controller: 'LoginCtrl'
    };
    createAccountState = {
        name: 'createAccount',
        url: '/createAccount',
        templateUrl: '/create-account-page.html'
    };
    $stateProvider.state(loginState);
    $stateProvider.state(createAccountState);
  
    // Redirect to home page if url does not matches any of the three mentioned above 
    $urlRouterProvider.otherwise("/"); 
}); 

app.controller('LoginCtrl', function($scope, $http, $state, $stateParams) {
    $scope.createUser = function(){
        $state.transitionTo('createAccount');
    };
});
app.controller('createAccountCtrl', function($scope, $http, $state) {
    $scope.addUser = function() {
        $http.post('/add_user', {'formObj' : $scope.userDetails}).then(function(response) {
            $state.transitionTo('login');
        });
    };
});
