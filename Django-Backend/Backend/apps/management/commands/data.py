# myapp/management/commands/custom_command.py

from django.core.management.base import BaseCommand
import json
from apps.models import EnergyData
from datetime import datetime




class Command(BaseCommand):

    def handle(self, *args, **options):

        def formate(data):
            if data == '':
                data = None
                return data
            else:
                formatted_date = datetime.strptime( data ,"%B, %d %Y %H:%M:%S")
                output_datetime_str =   formatted_date.strftime("%Y-%m-%d %H:%M:%S")
                return output_datetime_str 




        def load_data():
            
             with open('apps/management/commands/data.json', 'r') as json_file:
                data = json.load(json_file)
                for item in data:
                    end_year = item.get('end_year', None)
                    start_year = item.get('start_year', None)
                    impact = item.get('impact', None)
                    pestle = item.get('pestle', None)
                    source = item.get('source' , None)
                    title = item.get('title' , None)
                    likelihood = item.get('likelihood' , None)
                    data_added = item['added']
                    data_published = item['published']
                    added_output_datetime_str=formate(data_added)
                    published_output_datetime_str=formate(data_published)

                    




                    EnergyData.objects.create(
                        end_year= end_year,
                        intensity=item['intensity'],
                        sector=item['sector'],
                        topic=item['topic'],
                        insight=item['insight'],
                        url=item['url'],
                        region=item['region'],
                        start_year=start_year,
                        impact=impact,
                        added= added_output_datetime_str,
                        published=published_output_datetime_str,
                        country=item['country'],
                        relevance=item['relevance'],
                        pestle=pestle,
                        source=source,
                        title=title,
                        likelihood=likelihood
                    )
            


        load_data()
        self.stdout.write(self.style.SUCCESS('Json data saved in database successful '))
        

        
