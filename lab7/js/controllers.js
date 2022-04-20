var portfolioApp = angular.module('portfolioApp',[]); 

portfolioApp.controller('GalleryListCtrl', function($scope) {
$scope.galleries = [
{ 'title':'Rzym',
 'when':'2015-12-14',
 'thumbnailUrl':'img/1_sm.jpg'
},
{ 'title':'Maroko',
 'when':'2014-08-04',
 'thumbnailUrl':'img/2_sm.jpg'
}
,
{ 'title':'Hiszpania',
 'when':'2014-01-24',
 'thumbnailUrl':'img/3_sm.jpg'
}
,
{ 'title':'Grecja',
 'when':'2014-08-07',
 'thumbnailUrl':'img/4_sm.jpg'
}
,
{ 'title':'Anglia',
 'when':'2014-08-24',
 'thumbnailUrl':'img/5_sm.jpg'
}
,
{ 'title':'Maroko',
 'when':'2016-03-14',
 'thumbnailUrl':'img/6_sm.jpg'
}
];
});
$scope.orderProp = 'when';