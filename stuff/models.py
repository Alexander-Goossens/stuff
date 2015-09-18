from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class User(models.Model):
	Artist = 'artist'
	Producer = 'producer' 
	General = 'general' 
	Type_Of_User_List = (
		(Artist, 'Artist'),
		(Producer, 'Producer'),
		(General, 'General'),
	)
	username = models.CharField(max_length=24, unique=True)
	date_joined = models.DateTimeField()
	first_name = models.CharField(max_length=16)
	last_name = models.CharField(max_lengt=16)
	password = models.CharField(max_length=16)
	is_active = models.BooleanField()
	type_of_user = modelsCharField(max_length=2, choices=Type_Of_User_List, default=General)
	type_of_instrument=(models.Charfield(max_length=16)

class reviews(models.Model)
	title = models.CharField(max_length = 40, required=TRUE)
	body = models.CharField(max_length = 250, required=TRUE)
	review_rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
 
