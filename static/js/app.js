
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
    dashBoardState = {
        name: 'dashboard',
        url: '/dashboard',
        templateUrl: '/dashboard.html'
    }
    $stateProvider.state(loginState);
    $stateProvider.state(createAccountState);
    $stateProvider.state(dashBoardState);
  
    // Redirect to home page if url does not matches any of the three mentioned above 
    $urlRouterProvider.otherwise("/"); 
}); 

app.controller('LoginCtrl', function($scope, http, $state, $stateParams) {
    $scope.createUser = function(){
        $state.transitionTo('createAccount');
    };
    $scope.signIn = function() {
        http.post('/sign_in', $scope.userDetails).then(function(response) {
            var response = response.data;
            if(response.result){
                $state.transitionTo('dashboard');
            }else{
                return false;
            }
        });
    };
});
app.controller('createAccountCtrl', function($scope, http, $state) {
    $scope.addUser = function() {
        http.post('/add_user', $scope.userDetails).then(function(response) {
            $state.transitionTo('login');
        });
    };
});
app.controller('dashboardCtrl', function($scope, http, $state) {
    _getUser = function() {
        http.get('/get_user').then(function(response) {
            $scope.userDetails = response.data.data;
        });
    };
    _getUser();
});


//Start http

app.factory('http', ['$http', '$q', '$state', '$window',
  function($http, $q, $state, $window) {
    return {
      get: function(url) {
          var deferred =  $q.defer();
          $http.get(url).then(
            function(response) {
              //To show session time out in logout html
              var session_valid = (response.data.is_session_valid == false) ? true: false;
              if(response.data.is_session_valid){
                deferred.resolve(response);
              } else {
                $state.transitionTo('login');
              }
            },
            function(response) {
                deferred.reject(response)
            }
          );
        return deferred.promise;
      },

      post: function(url, formData) {
        var deferred =  $q.defer();
        $http.post(url, formData).then(
          function(response) {
            //To show session time out in logout html
            var session_valid = (response.data.is_session_valid == false) ? true: false;
            if(response.data.is_session_valid){
                deferred.resolve(response);
            } else {
                $state.transitionTo('login');
            }
          },
            function(response) {
                deferred.reject(response)
            }
        );
        return deferred.promise;
      }
    };
}]);
