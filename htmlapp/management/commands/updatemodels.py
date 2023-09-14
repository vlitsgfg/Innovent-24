from django.core.management.base import BaseCommand, CommandParser
import pandas as pd
from htmlapp.models import Students
class Command(BaseCommand):
    help='import booms'
    def add_arguments(self, parser):
        pass
    def handle(self,*args,**options):
        df=pd.read_csv('database.csv')
        for id,name,branch,category,totalfee,buildingfee,paid,due in zip(df.S_id,df.S_name,df.S_branch,df.S_category,df.S_totalfee,df.S_buildingfee,df.S_paid,df.S_due):
            models=Students(S_id=id,S_name=name,S_branch=branch,S_category=category,S_totalfee=totalfee,S_buildingfee=buildingfee,S_paid=paid,S_due=due)
            models.save()    
    