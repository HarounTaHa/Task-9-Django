from django.db import models

# Create your models here.
from django.db import models
from marketing.models import Contract
from users.models import Customer


class DesignType(models.Model):
    type_of_design = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.type_of_design


class ProjectType(models.Model):
    type_of_project = models.CharField(max_length=200)

    def __str__(self):
        return self.type_of_project


class Project(models.Model):
    project_type = models.ForeignKey(ProjectType, on_delete=models.CASCADE)
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    number_of_windows = models.IntegerField()
    project_issue_date = models.DateField(auto_now_add=True)  # starting date for the project
    project_due_date = models.DateField()
    municipal_confirmed = models.BooleanField()
    customer_finishing_confirm = models.BooleanField(default=False)
    customer_notes = models.TextField()
    current_progress = models.FloatField()

    def __str__(self):
        return f'{self.contract.project_name},Type: {self.project_type}'


class TableItem(models.Model):
    item = models.CharField(max_length=50)
    creation_time = models.FloatField()
    modification_time = models.FloatField()

    def __str__(self):
        return self.item


class MoodBoard(models.Model):
    type_of_design = models.ForeignKey(DesignType, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    note = models.TextField()

    def __str__(self):
        return self.type


class StyleMoodBoardPart(models.Model):
    style_type = models.CharField(max_length=100)

    def __str__(self):
        return self.style_type


class MoodBoardPart(models.Model):
    table_item = models.ForeignKey(TableItem, on_delete=models.CASCADE)
    mood_board_parent = models.ForeignKey(MoodBoard, on_delete=models.CASCADE)
    mood_board_style = models.ForeignKey(StyleMoodBoardPart, on_delete=models.CASCADE)
    note = models.TextField()

    def __str__(self):
        return f'{self.mood_board_parent},{self.mood_board_style},{self.table_item}'


class MoodBoardPartImages(models.Model):
    mood_board_part = models.ForeignKey(MoodBoardPart, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to="images")
    image_note = models.CharField(max_length=200)

    def __str__(self):
        return f'Url:{self.image},Note:{self.image_note}'
