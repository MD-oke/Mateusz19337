var portfolioApp = angular.module('portfolioApp',[]); 

portfolioApp.controller('GalleryListCtrl', function($scope) {
$scope.galleries = [
{ 'title':'Devil May Cry V',
 'when':'2019-03-08',
 'thumbnailUrl':'img/1.jpg'
},
{ 'title':'Monster Hunter Freedom',
 'when':'2007-02-22',
 'thumbnailUrl':'img/2.jpg'
}
,
{ 'title':'Monster Hunter Rise',
 'when':'2021-03-26',
 'thumbnailUrl':'img/3.png'
}
,
{ 'title':'Resident Evil 2',
 'when':'2019-01-25',
 'thumbnailUrl':'img/4.jpeg'
}
,
{ 'title':'Resident Evil 3',
 'when':'2020-04-03',
 'thumbnailUrl':'img/5.jpeg'
}
,
{ 'title':'Resident Evil V',
 'when':'2009-03-05',
 'thumbnailUrl':'img/6.jpg'
}
,
{ 'title':'Resident Evil VI',
 'when':'2012-10-02',
 'thumbnailUrl':'img/7.jpg'
}
,
{ 'title':'Resident Evil Village',
 'when':'2021-05-07',
 'thumbnailUrl':'img/8.png'
}
,
{ 'title':'Street Fight V',
 'when':'2016-02-16',
 'thumbnailUrl':'img/9.jpg'
}
,
{ 'title':'Okami',
 'when':'2006-04-20',
 'thumbnailUrl':'img/10.jpg'
}
,
{ 'title':'Mega Man 11',
 'when':'2018-10-02',
 'thumbnailUrl':'img/11.jpg'
}
,
{ 'title':'Devil May Cry',
 'when':'2001-08-23',
 'thumbnailUrl':'img/12.jpg'
}
,
{ 'title':'Devil May Cry 2',
 'when':'2003-01-25',
 'thumbnailUrl':'img/13.jpg'
}
,
{ 'title':'Devil May Cry 3',
 'when':'2005-02-17',
 'thumbnailUrl':'img/14.jpg'
}
];
		$scope.sortlist = 
		[
			{
				'label':'Alfabetycznie',
				'value':'title'
			},
			{
			'label':'Chronologicznie',
			'value':'when'
			},
			{
			'label':'Najwczesniej',
			'value':'-when'
			}
		];
});