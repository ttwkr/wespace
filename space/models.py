from django.db import models


class Spaces(models.Model):
    title = models.CharField(max_length=100)
    short_intro = models.CharField(max_length=200)
    long_intro = models.TextField()
    open_time = models.CharField(max_length=30)
    close_time = models.CharField(max_length=30)
    host = models.ForeignKey(
        'account.Hosts',
        on_delete=models.SET_NULL,
        null=True)
    amenity_space = models.ManyToManyField(
        'Amenities', through='Space_Amenities')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'spaces'


class Amenities(models.Model):
    amenity = models.CharField(max_length=300)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'amenities'


class Space_Amenities(models.Model):
    amenity = models.ForeignKey(
        'Amenities', on_delete=models.SET_NULL, null=True)
    space = models.ForeignKey(
        'Spaces', on_delete=models.SET_NULL, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'space_amenities'


class Space_Categories(models.Model):
    category = models.CharField(max_length=200)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'space_categories'


class Images(models.Model):
    space_image = models.URLField(max_length=2500)
    space = models.ForeignKey(
        Spaces,
        on_delete=models.SET_NULL,
        null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'images'


class Categories_Space(models.Model):
    space = models.ForeignKey(Spaces, on_delete=models.SET_NULL, null=True)
    space_category = models.ForeignKey(
        Space_Categories,
        on_delete=models.SET_NULL,
        null=True)
    space = models.ForeignKey(Spaces, on_delete=models.SET_NULL, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'categories_space'


class Reviews(models.Model):
    user = models.ForeignKey(
        'account.Accounts', on_delete=models.SET_NULL, null=True)
    space = models.ForeignKey(Spaces, on_delete=models.SET_NULL, null=True)
    content = models.TextField()
    image = models.URLField(max_length=2500)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'reviews'


class Qeustion(models.Model):
    space = models.ForeignKey(
        'Spaces', on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(
        'account.Accounts', on_delete=models.SET_NULL, null=True)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Mata:
        db_table = 'question'


class Notices(models.Model):
    notice = models.CharField(max_length=300)
    space = models.ForeignKey('Spaces', on_delete=models.SET_NULL, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'notice'


class Holiday(models.Model):
    holiday = models.DateTimeField()
    space = models.ForeignKey('Spaces', on_delete=models.SET_NULL, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'holiday'
