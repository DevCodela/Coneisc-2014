#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User

from django.template.defaultfilters import slugify


class AuditModel(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False, editable=False)
    updated = models.DateTimeField(auto_now=True)
    #create_by = models.ForeignKey(User, related_name="%(app_label)s_%(class)s_related")

    class Meta:
        abstract = True


class Course(AuditModel):

    enrolled = models.ManyToManyField(User, through="UserEnrolled")
    title = models.CharField(max_length=200)
    slug = models.SlugField(editable=True, unique=True)
    summary = models.CharField(max_length=300)
    isfree = models.BooleanField("Is free?", default=False)
    released = models.BooleanField("Released?", default=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Course, self).save(*args, **kwargs)

    def __unicode__(self):
        return u'%s' % (self.title)


class UserEnrolled(models.Model):

    course = models.ForeignKey(Course)
    user = models.ForeignKey(User)

    class Meta:
        unique_together = ('course', 'user')
        verbose_name_plural = "User Enrolled"

    def __unicode__(self):
        return u"%s %s" % (self.course, self.user)


class ChapterManager(models.Manager):

    def by_course_and_released_asc(self, slug):
        return self.filter(course__slug=slug, released=True).order_by("created")


class Chapter(AuditModel):

    progress = models.ManyToManyField(User, through='UserProgress')
    course = models.ForeignKey(Course, related_name='chapters')
    title = models.CharField(max_length=200)
    slug = models.SlugField(editable=True, unique=True)
    summary = models.CharField(max_length=300)
    video = models.URLField()
    released = models.BooleanField(default=False)

    objects = ChapterManager()

    def get_kind(self):
        return u"chapter"

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Chapter, self).save(*args, **kwargs)

    def __unicode__(self):
        return u'%s' % (self.title)

class UserProgress(models.Model):

    chapter = models.ForeignKey(Chapter)
    user = models.ForeignKey(User)
    progress = models.PositiveSmallIntegerField(default=0, editable=True)

    class Meta:
        unique_together = ('chapter', 'user')
        verbose_name_plural = "User progress"

    def __unicode__(self):
        return u'%s %s %s' % (self.chapter, self.user, self.progress)


class ArticleManager(models.Manager):

    def by_course_and_released_asc(self, slug):
        return self.filter(course__slug=slug, released=True).order_by("created")


class Article(AuditModel):

    course = models.ForeignKey(Course, related_name='articles')
    title = models.CharField(max_length=200)
    slug = models.SlugField(editable=True, unique=True)
    summary = models.CharField(max_length=300)
    content = models.TextField()
    released = models.BooleanField(default=False)

    objects = ArticleManager()

    def get_kind(self):
        return u"article"

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)
    
    def __unicode__(self):
        return u'%s' % (self.title)