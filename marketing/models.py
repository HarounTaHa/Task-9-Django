from django.db import models

# Create your models here.
from users.models import Customer, Employee


class ContractType(models.Model):
    type = models.CharField(max_length=70)

    def __str__(self):
        return self.type


class WorkingScope(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class WorkingPart(models.Model):
    project = models.ForeignKey(WorkingScope, on_delete=models.CASCADE)
    partName = models.CharField(max_length=200)

    def __str__(self):
        return self.partName


class WorkingPartItem(models.Model):
    workingPart = models.ForeignKey(WorkingPart, on_delete=models.CASCADE)
    itemName = models.CharField(max_length=200)

    def __str__(self):
        return self.itemName


class ProjectComponent(models.Model):
    type = models.CharField(max_length=200)

    def __str__(self):
        return self.type


class ComponentPart(models.Model):
    project = models.ForeignKey(ProjectComponent, on_delete=models.CASCADE)
    partName = models.CharField(max_length=200)


class Contract(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    contract_type = models.ForeignKey(ContractType, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=200)
    statement = models.TextField()
    price_in_numbers = models.IntegerField()
    total_area = models.IntegerField()
    total_time_period = models.DurationField(help_text='Expects data in the format "DD HH:MM:SS ex: 4 12:00:00')
    gregorian_date = models.DateTimeField(auto_now_add=True)
    contract_subject = models.TextField()
    additional_details = models.TextField()
    municipal_confirmed = models.BooleanField()
    is_approval = models.BooleanField(default=False)

    def __str__(self):
        return f'Project : {self.project_name},Contract type : {self.contract_type},Date : {self.gregorian_date}, Approval : {self.is_approval}'


class PriceOfferType(models.Model):
    price_offer_type = models.CharField(max_length=200)

    def __str__(self):
        return self.price_offer_type


class PriceOffer(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    price_offer_type = models.ForeignKey(PriceOfferType, null=True, on_delete=models.SET_NULL)
    price_in_letters = models.CharField(max_length=100)
    price_in_numbers = models.FloatField()

    def __str__(self):
        return f'Project:{self.contract.project_name},Total Area:{self.contract.total_area},Price:{self.price_in_numbers}'


class MeetingType(models.Model):
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.type


class MarketingMeeting(models.Model):
    CHOICES = [('C ', 'Canceled'),
               ('D', 'Done'),
               ('P', 'Pending'),
               ('S', 'Shifted')]
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    meeting_type = models.ForeignKey(MeetingType, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    subject = models.CharField(max_length=100)
    notes = models.TextField()
    status = models.CharField(choices=CHOICES, max_length=40)

    def __str__(self):
        return f'{self.subject},{self.status}, Date :{self.date_time}'
