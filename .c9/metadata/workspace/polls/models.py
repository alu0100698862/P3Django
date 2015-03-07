{"filter":false,"title":"models.py","tooltip":"/polls/models.py","ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":28,"column":0},"end":{"row":28,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"hash":"b83229581f0b5dc42a0566fcd8f4372f93b85071","undoManager":{"mark":100,"position":100,"stack":[[{"group":"doc","deltas":[{"start":{"row":3,"column":15},"end":{"row":3,"column":20},"action":"remove","lines":["model"]},{"start":{"row":3,"column":15},"end":{"row":3,"column":21},"action":"insert","lines":["models"]}]}],[{"group":"doc","deltas":[{"start":{"row":3,"column":21},"end":{"row":3,"column":46},"action":"insert","lines":["CharField(max_length=200)"]}]}],[{"group":"doc","deltas":[{"start":{"row":3,"column":21},"end":{"row":3,"column":22},"action":"insert","lines":["."]}]}],[{"group":"doc","deltas":[{"start":{"row":4,"column":0},"end":{"row":4,"column":4},"action":"insert","lines":["    "]}]}],[{"group":"doc","deltas":[{"start":{"row":4,"column":4},"end":{"row":4,"column":53},"action":"insert","lines":["pub_date = models.DateTimeField('date published')"]}]}],[{"group":"doc","deltas":[{"start":{"row":4,"column":53},"end":{"row":5,"column":0},"action":"insert","lines":["",""]},{"start":{"row":5,"column":0},"end":{"row":5,"column":4},"action":"insert","lines":["    "]}]}],[{"group":"doc","deltas":[{"start":{"row":5,"column":4},"end":{"row":6,"column":0},"action":"insert","lines":["",""]},{"start":{"row":6,"column":0},"end":{"row":6,"column":4},"action":"insert","lines":["    "]}]}],[{"group":"doc","deltas":[{"start":{"row":6,"column":0},"end":{"row":6,"column":4},"action":"remove","lines":["    "]}]}],[{"group":"doc","deltas":[{"start":{"row":6,"column":0},"end":{"row":9,"column":33},"action":"insert","lines":["class Choice(models.Model):","    poll = models.ForeignKey(Poll)","    choice = models.CharField(max_length=200)","    votes = models.IntegerField()"]}]}],[{"group":"doc","deltas":[{"start":{"row":10,"column":0},"end":{"row":11,"column":0},"action":"insert","lines":["",""]}]}],[{"group":"doc","deltas":[{"start":{"row":11,"column":0},"end":{"row":11,"column":1},"action":"insert","lines":["P"]}]}],[{"group":"doc","deltas":[{"start":{"row":11,"column":0},"end":{"row":11,"column":1},"action":"remove","lines":["P"]}]}],[{"group":"doc","deltas":[{"start":{"row":2,"column":9},"end":{"row":2,"column":10},"action":"remove","lines":["l"]}]}],[{"group":"doc","deltas":[{"start":{"row":2,"column":8},"end":{"row":2,"column":9},"action":"remove","lines":["l"]}]}],[{"group":"doc","deltas":[{"start":{"row":2,"column":7},"end":{"row":2,"column":8},"action":"remove","lines":["o"]}]}],[{"group":"doc","deltas":[{"start":{"row":2,"column":6},"end":{"row":2,"column":7},"action":"remove","lines":["P"]}]}],[{"group":"doc","deltas":[{"start":{"row":2,"column":6},"end":{"row":2,"column":7},"action":"insert","lines":["Q"]}]}],[{"group":"doc","deltas":[{"start":{"row":2,"column":7},"end":{"row":2,"column":8},"action":"insert","lines":["u"]}]}],[{"group":"doc","deltas":[{"start":{"row":2,"column":8},"end":{"row":2,"column":9},"action":"insert","lines":["e"]}]}],[{"group":"doc","deltas":[{"start":{"row":2,"column":9},"end":{"row":2,"column":10},"action":"insert","lines":["s"]}]}],[{"group":"doc","deltas":[{"start":{"row":2,"column":10},"end":{"row":2,"column":11},"action":"insert","lines":["t"]}]}],[{"group":"doc","deltas":[{"start":{"row":2,"column":11},"end":{"row":2,"column":12},"action":"insert","lines":["i"]}]}],[{"group":"doc","deltas":[{"start":{"row":2,"column":12},"end":{"row":2,"column":13},"action":"insert","lines":["o"]}]}],[{"group":"doc","deltas":[{"start":{"row":2,"column":13},"end":{"row":2,"column":14},"action":"insert","lines":["n"]}]}],[{"group":"doc","deltas":[{"start":{"row":3,"column":12},"end":{"row":3,"column":13},"action":"insert","lines":["_"]}]}],[{"group":"doc","deltas":[{"start":{"row":3,"column":13},"end":{"row":3,"column":14},"action":"insert","lines":["t"]}]}],[{"group":"doc","deltas":[{"start":{"row":3,"column":14},"end":{"row":3,"column":15},"action":"insert","lines":["e"]}]}],[{"group":"doc","deltas":[{"start":{"row":3,"column":15},"end":{"row":3,"column":16},"action":"insert","lines":["x"]}]}],[{"group":"doc","deltas":[{"start":{"row":3,"column":16},"end":{"row":3,"column":17},"action":"insert","lines":["t"]}]}],[{"group":"doc","deltas":[{"start":{"row":7,"column":7},"end":{"row":7,"column":8},"action":"remove","lines":["l"]}]}],[{"group":"doc","deltas":[{"start":{"row":7,"column":6},"end":{"row":7,"column":7},"action":"remove","lines":["l"]}]}],[{"group":"doc","deltas":[{"start":{"row":7,"column":5},"end":{"row":7,"column":6},"action":"remove","lines":["o"]}]}],[{"group":"doc","deltas":[{"start":{"row":7,"column":4},"end":{"row":7,"column":5},"action":"remove","lines":["p"]}]}],[{"group":"doc","deltas":[{"start":{"row":7,"column":4},"end":{"row":7,"column":5},"action":"insert","lines":["q"]}]}],[{"group":"doc","deltas":[{"start":{"row":7,"column":5},"end":{"row":7,"column":6},"action":"insert","lines":["u"]}]}],[{"group":"doc","deltas":[{"start":{"row":7,"column":6},"end":{"row":7,"column":7},"action":"insert","lines":["e"]}]}],[{"group":"doc","deltas":[{"start":{"row":7,"column":7},"end":{"row":7,"column":8},"action":"insert","lines":["s"]}]}],[{"group":"doc","deltas":[{"start":{"row":7,"column":8},"end":{"row":7,"column":9},"action":"insert","lines":["t"]}]}],[{"group":"doc","deltas":[{"start":{"row":7,"column":9},"end":{"row":7,"column":10},"action":"insert","lines":["i"]}]}],[{"group":"doc","deltas":[{"start":{"row":7,"column":10},"end":{"row":7,"column":11},"action":"insert","lines":["o"]}]}],[{"group":"doc","deltas":[{"start":{"row":7,"column":11},"end":{"row":7,"column":12},"action":"insert","lines":["n"]}]}],[{"group":"doc","deltas":[{"start":{"row":7,"column":36},"end":{"row":7,"column":37},"action":"remove","lines":["l"]}]}],[{"group":"doc","deltas":[{"start":{"row":7,"column":35},"end":{"row":7,"column":36},"action":"remove","lines":["l"]}]}],[{"group":"doc","deltas":[{"start":{"row":7,"column":34},"end":{"row":7,"column":35},"action":"remove","lines":["o"]}]}],[{"group":"doc","deltas":[{"start":{"row":7,"column":33},"end":{"row":7,"column":34},"action":"remove","lines":["P"]}]}],[{"group":"doc","deltas":[{"start":{"row":7,"column":33},"end":{"row":7,"column":34},"action":"insert","lines":["q"]}]}],[{"group":"doc","deltas":[{"start":{"row":7,"column":34},"end":{"row":7,"column":35},"action":"insert","lines":["u"]}]}],[{"group":"doc","deltas":[{"start":{"row":7,"column":35},"end":{"row":7,"column":36},"action":"insert","lines":["e"]}]}],[{"group":"doc","deltas":[{"start":{"row":7,"column":36},"end":{"row":7,"column":37},"action":"insert","lines":["s"]}]}],[{"group":"doc","deltas":[{"start":{"row":7,"column":37},"end":{"row":7,"column":38},"action":"insert","lines":["t"]}]}],[{"group":"doc","deltas":[{"start":{"row":7,"column":38},"end":{"row":7,"column":39},"action":"insert","lines":["i"]}]}],[{"group":"doc","deltas":[{"start":{"row":7,"column":38},"end":{"row":7,"column":39},"action":"remove","lines":["i"]}]}],[{"group":"doc","deltas":[{"start":{"row":7,"column":37},"end":{"row":7,"column":38},"action":"remove","lines":["t"]}]}],[{"group":"doc","deltas":[{"start":{"row":7,"column":36},"end":{"row":7,"column":37},"action":"remove","lines":["s"]}]}],[{"group":"doc","deltas":[{"start":{"row":7,"column":35},"end":{"row":7,"column":36},"action":"remove","lines":["e"]}]}],[{"group":"doc","deltas":[{"start":{"row":7,"column":34},"end":{"row":7,"column":35},"action":"remove","lines":["u"]}]}],[{"group":"doc","deltas":[{"start":{"row":7,"column":33},"end":{"row":7,"column":34},"action":"remove","lines":["q"]}]}],[{"group":"doc","deltas":[{"start":{"row":7,"column":33},"end":{"row":7,"column":34},"action":"insert","lines":["Q"]}]}],[{"group":"doc","deltas":[{"start":{"row":7,"column":34},"end":{"row":7,"column":35},"action":"insert","lines":["u"]}]}],[{"group":"doc","deltas":[{"start":{"row":7,"column":35},"end":{"row":7,"column":36},"action":"insert","lines":["e"]}]}],[{"group":"doc","deltas":[{"start":{"row":7,"column":36},"end":{"row":7,"column":37},"action":"insert","lines":["s"]}]}],[{"group":"doc","deltas":[{"start":{"row":7,"column":37},"end":{"row":7,"column":38},"action":"insert","lines":["t"]}]}],[{"group":"doc","deltas":[{"start":{"row":7,"column":38},"end":{"row":7,"column":39},"action":"insert","lines":["i"]}]}],[{"group":"doc","deltas":[{"start":{"row":7,"column":39},"end":{"row":7,"column":40},"action":"insert","lines":["o"]}]}],[{"group":"doc","deltas":[{"start":{"row":7,"column":40},"end":{"row":7,"column":41},"action":"insert","lines":["n"]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":10},"end":{"row":8,"column":11},"action":"insert","lines":["_"]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":11},"end":{"row":8,"column":12},"action":"insert","lines":["t"]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":12},"end":{"row":8,"column":13},"action":"insert","lines":["e"]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":13},"end":{"row":8,"column":14},"action":"insert","lines":["x"]}]}],[{"group":"doc","deltas":[{"start":{"row":8,"column":14},"end":{"row":8,"column":15},"action":"insert","lines":["t"]}]}],[{"group":"doc","deltas":[{"start":{"row":0,"column":0},"end":{"row":9,"column":33},"action":"remove","lines":["from django.db import models","","class Question(models.Model):","    question_text = models.CharField(max_length=200)","    pub_date = models.DateTimeField('date published')","    ","class Choice(models.Model):","    question = models.ForeignKey(Question)","    choice_text = models.CharField(max_length=200)","    votes = models.IntegerField()"]},{"start":{"row":0,"column":0},"end":{"row":11,"column":42},"action":"insert","lines":["from django.db import models","","","class Question(models.Model):","    question_text = models.CharField(max_length=200)","    pub_date = models.DateTimeField('date published')","","","class Choice(models.Model):","    question = models.ForeignKey(Question)","    choice_text = models.CharField(max_length=200)","    votes = models.IntegerField(default=0)"]}]}],[{"group":"doc","deltas":[{"start":{"row":5,"column":53},"end":{"row":6,"column":0},"action":"insert","lines":["",""]},{"start":{"row":6,"column":0},"end":{"row":6,"column":4},"action":"insert","lines":["    "]}]}],[{"group":"doc","deltas":[{"start":{"row":6,"column":4},"end":{"row":7,"column":33},"action":"insert","lines":["def __str__(self):              # __unicode__ on Python 2","        return self.question_text"]}]}],[{"group":"doc","deltas":[{"start":{"row":13,"column":42},"end":{"row":14,"column":0},"action":"insert","lines":["",""]},{"start":{"row":14,"column":0},"end":{"row":14,"column":4},"action":"insert","lines":["    "]}]}],[{"group":"doc","deltas":[{"start":{"row":14,"column":4},"end":{"row":15,"column":31},"action":"insert","lines":[" def __str__(self):              # __unicode__ on Python 2","        return self.choice_text"]}]}],[{"group":"doc","deltas":[{"start":{"row":14,"column":4},"end":{"row":14,"column":5},"action":"remove","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":1,"column":0},"end":{"row":1,"column":33},"action":"insert","lines":["from django.utils import timezone"]}]}],[{"group":"doc","deltas":[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"insert","lines":["",""]}]}],[{"group":"doc","deltas":[{"start":{"row":1,"column":0},"end":{"row":2,"column":0},"action":"insert","lines":["",""]}]}],[{"group":"doc","deltas":[{"start":{"row":0,"column":0},"end":{"row":0,"column":15},"action":"insert","lines":["import datetime"]}]}],[{"group":"doc","deltas":[{"start":{"row":9,"column":33},"end":{"row":10,"column":0},"action":"insert","lines":["",""]},{"start":{"row":10,"column":0},"end":{"row":10,"column":8},"action":"insert","lines":["        "]}]}],[{"group":"doc","deltas":[{"start":{"row":10,"column":4},"end":{"row":10,"column":8},"action":"remove","lines":["    "]}]}],[{"group":"doc","deltas":[{"start":{"row":10,"column":4},"end":{"row":11,"column":75},"action":"insert","lines":[" def was_published_recently(self):","        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)"]}]}],[{"group":"doc","deltas":[{"start":{"row":10,"column":4},"end":{"row":10,"column":5},"action":"remove","lines":[" "]}]}],[{"group":"doc","deltas":[{"start":{"row":10,"column":4},"end":{"row":11,"column":0},"action":"insert","lines":["",""]},{"start":{"row":11,"column":0},"end":{"row":11,"column":4},"action":"insert","lines":["    "]}]}],[{"group":"doc","deltas":[{"start":{"row":12,"column":75},"end":{"row":13,"column":0},"action":"insert","lines":["",""]},{"start":{"row":13,"column":0},"end":{"row":13,"column":8},"action":"insert","lines":["        "]}]}],[{"group":"doc","deltas":[{"start":{"row":13,"column":4},"end":{"row":13,"column":8},"action":"remove","lines":["    "]}]}],[{"group":"doc","deltas":[{"start":{"row":13,"column":4},"end":{"row":17,"column":68},"action":"insert","lines":["def was_published_recently(self):","        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)","    was_published_recently.admin_order_field = 'pub_date'","    was_published_recently.boolean = True","    was_published_recently.short_description = 'Published recently?'"]}]}],[{"group":"doc","deltas":[{"start":{"row":13,"column":4},"end":{"row":14,"column":75},"action":"remove","lines":["def was_published_recently(self):","        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)"]}]}],[{"group":"doc","deltas":[{"start":{"row":13,"column":0},"end":{"row":13,"column":4},"action":"remove","lines":["    "]}]}],[{"group":"doc","deltas":[{"start":{"row":12,"column":75},"end":{"row":13,"column":0},"action":"remove","lines":["",""]}]}],[{"group":"doc","deltas":[{"start":{"row":26,"column":0},"end":{"row":27,"column":0},"action":"insert","lines":["",""]}]}],[{"group":"doc","deltas":[{"start":{"row":27,"column":0},"end":{"row":28,"column":0},"action":"insert","lines":["",""]}]}],[{"group":"doc","deltas":[{"start":{"row":28,"column":0},"end":{"row":29,"column":0},"action":"insert","lines":["",""]}]}],[{"group":"doc","deltas":[{"start":{"row":29,"column":0},"end":{"row":48,"column":23},"action":"insert","lines":["import datetime","from django.db import models","from django.utils import timezone","# Create your models here.","class Question(models.Model):","question_text = models.CharField(max_length=200)","pub_date = models.DateTimeField('date published')","def __str__(self):","return self.question_text","def was_published_recently(self):","return self.pub_date >= timezone.now() - datetime.timedelta(days=1)","was_published_recently.admin_order_field = 'pub_date'","was_published_recently.boolean = True","was_published_recently.short_description = 'Published recently?'","class Choice(models.Model):","question = models.ForeignKey(Question)","choice_text = models.CharField(max_length=200)","votes = models.IntegerField(default=0)","def __str__(self):","return self.choice_text"]}]}],[{"group":"doc","deltas":[{"start":{"row":29,"column":0},"end":{"row":48,"column":23},"action":"remove","lines":["import datetime","from django.db import models","from django.utils import timezone","# Create your models here.","class Question(models.Model):","question_text = models.CharField(max_length=200)","pub_date = models.DateTimeField('date published')","def __str__(self):","return self.question_text","def was_published_recently(self):","return self.pub_date >= timezone.now() - datetime.timedelta(days=1)","was_published_recently.admin_order_field = 'pub_date'","was_published_recently.boolean = True","was_published_recently.short_description = 'Published recently?'","class Choice(models.Model):","question = models.ForeignKey(Question)","choice_text = models.CharField(max_length=200)","votes = models.IntegerField(default=0)","def __str__(self):","return self.choice_text"]}]}],[{"group":"doc","deltas":[{"start":{"row":28,"column":0},"end":{"row":29,"column":0},"action":"remove","lines":["",""]}]}],[{"group":"doc","deltas":[{"start":{"row":27,"column":0},"end":{"row":28,"column":0},"action":"remove","lines":["",""]}]}],[{"group":"doc","deltas":[{"start":{"row":11,"column":4},"end":{"row":12,"column":75},"action":"remove","lines":["def was_published_recently(self):","        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)"]},{"start":{"row":11,"column":4},"end":{"row":13,"column":67},"action":"insert","lines":["def was_published_recently(self):","    now = timezone.now()","    return now - datetime.timedelta(days=1) <= self.pub_date <= now"]}]}],[{"group":"doc","deltas":[{"start":{"row":12,"column":4},"end":{"row":12,"column":8},"action":"insert","lines":["    "]}]}],[{"group":"doc","deltas":[{"start":{"row":13,"column":4},"end":{"row":13,"column":8},"action":"insert","lines":["    "]}]}]]},"timestamp":1425672797000}