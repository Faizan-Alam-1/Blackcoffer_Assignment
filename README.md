
# Energy Insight API

This project is a REST API built using Django, providing insights into energy-related data. The data is sourced from various reports, and the API exposes information about energy topics, intensity, sectors, and more.

## Data Example

Here is an example of the data structure used in the API:

```json
{
  "id": 1,
  "end_year": "",
  "intensity": 6,
  "sector": "Energy",
  "topic": "gas",
  "insight": "Annual Energy Outlook",
  "url": "http://www.eia.gov/outlooks/aeo/pdf/0383(2017).pdf",
  "region": "Northern America",
  "start_year": "",
  "impact": "",
  "added": "2017-01-20T03:51:25Z",
  "published": "2017-01-09T00:00:00Z",
  "country": "United States of America",
  "relevance": 2,
  "pestle": "Industries",
  "source": "EIA",
  "title": "U.S. natural gas consumption forecast for the projection period.",
  "likelihood": 3
}
``` 


## Installation

To run this API in localhost ,then  follow these steps:

### Clone the repository:

```bash
  https://github.com/Faizan-Alam-1/energy-insight-api.git
  
```


### Install dependencies::

```bash
  pip install -r requirements.txt

```

### Run the Django development server:

```bash
  python manage.py runserver
    
```
    
    


## API Endpoints

```http
    127.0.0.1:8000/api/energy-data/
```




## Screenshots

![hello](https://github.com/Faizan-Alam-1/Python_Raam/assets/51821426/669b5d95-4cdd-4b04-b2b8-5d2508d30a5e)

![data](https://github.com/Faizan-Alam-1/Python_Raam/assets/51821426/717efe3f-8a39-4693-a98f-c12dbb6e9896)

