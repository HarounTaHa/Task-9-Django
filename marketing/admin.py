from django.contrib import admin

from .models import MarketingMeeting, MeetingType, Contract, ContractType, PriceOffer, PriceOfferType

# Register your models here.
admin.site.register([Contract, ContractType, MarketingMeeting, MeetingType, PriceOffer, PriceOfferType])
