{"filter":false,"title":"urls.py","tooltip":"/p3djang/urls.py","undoManager":{"mark":11,"position":11,"stack":[[{"group":"doc","deltas":[{"start":{"row":7,"column":0},"end":{"row":7,"column":4},"action":"insert","lines":["    "]}]}],[{"group":"doc","deltas":[{"start":{"row":7,"column":4},"end":{"row":7,"column":43},"action":"insert","lines":["url(r'^polls/', include('polls.urls')),"]}]}],[{"group":"doc","deltas":[{"start":{"row":1,"column":32},"end":{"row":2,"column":0},"action":"insert","lines":["",""]}]}],[{"group":"doc","deltas":[{"start":{"row":2,"column":0},"end":{"row":3,"column":0},"action":"insert","lines":["",""]}]}],[{"group":"doc","deltas":[{"start":{"row":3,"column":0},"end":{"row":4,"column":32},"action":"insert","lines":["from django.conf.urls import patterns, include, url","from django.contrib import admin"]}]}],[{"group":"doc","deltas":[{"start":{"row":2,"column":0},"end":{"row":4,"column":32},"action":"remove","lines":["","from django.conf.urls import patterns, include, url","from django.contrib import admin"]}]}],[{"group":"doc","deltas":[{"start":{"row":11,"column":0},"end":{"row":15,"column":0},"action":"insert","lines":["urlpatterns = patterns('',","    url(r'^polls/', include('polls.urls', namespace=\"polls\")),","    url(r'^admin/', include(admin.site.urls)),",")",""]}]}],[{"group":"doc","deltas":[{"start":{"row":12,"column":4},"end":{"row":12,"column":62},"action":"remove","lines":["url(r'^polls/', include('polls.urls', namespace=\"polls\")),"]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":43},"end":{"row":9,"column":0},"action":"insert","lines":["",""]},{"start":{"row":9,"column":0},"end":{"row":9,"column":4},"action":"insert","lines":["    "]}]}],[{"group":"doc","deltas":[{"start":{"row":9,"column":4},"end":{"row":9,"column":62},"action":"insert","lines":["url(r'^polls/', include('polls.urls', namespace=\"polls\")),"]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":4},"end":{"row":8,"column":5},"action":"insert","lines":["#"]}]}],[{"group":"doc","deltas":[{"start":{"row":12,"column":0},"end":{"row":15,"column":1},"action":"remove","lines":["urlpatterns = patterns('',","    ","    url(r'^admin/', include(admin.site.urls)),",")"]}]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":12,"column":0},"end":{"row":12,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1425671166857,"hash":"10f510b5aa84ececaf4c6d87fab815f2d55cda74"}