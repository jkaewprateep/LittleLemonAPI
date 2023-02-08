# LittleLemonAPI
 
### Does the web application use Django to serve static HTML content? ###
> Yes, please see the screenshots inside folder name '1. Does the web application use Django to serve static HTML content'.

```
### Project assignment ###
## Question 1 ##    Does the web application use Django to serve static HTML content?
import json;
from datetime import datetime;
from django.http import HttpResponse;
from django.views.decorators.csrf import csrf_exempt;
from django.core import serializers;

@csrf_exempt
def bookings(request):
    if request.method == 'POST':
        data = json.load(request)
        exist = Booking.objects.filter(BookingDate=data['BookingDate']).exists()
        if exist==False:
            booking = Booking(
                Name = data['Name'],
                No_of_guests = data['No_of_guests'],
                BookingDate = data['BookingDate'],
            )
            booking.save()
        else:
            return HttpResponse("{'error':1}", content_type='application/json')
    
    date = request.GET.get('date', datetime.today().date())

    bookings = Booking.objects.all().filter(BookingDate=date)
    booking_json = serializers.serialize('json', bookings)

    return HttpResponse(booking_json, content_type='application/json')
```

### Has the learner committed the project to a Git repository? ###
> Yes, please see the screenshots inside the folder name '2. Has the learner committed the project to a Git repository'.

### Does the application connect the backend to a MySQL database? ###
> Yes, please see the screenshots inside the folder name '3. Does the application connect the backend to a MySQL database'.

### Are the menu and table booking APIs implemented? ###
> Yes, please see the screenshots inside the folder name '4. Are the menu and table booking APIs implemented'.

### Is the application set up with user registration and authentication? ###
> Yes, please see the screenshots inside the folder name '5. Is the application set up with user registration and authentication'.

### Does the application contain unit tests? ###
> Yes, please see the screenshots inside the folder name '6. Does the application contain unit tests'.

```
from django_test import TestCase
from LittleLemonAPI.models import Menu;


# TestCase class
class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(item, "IceCream : 80")


class MenuViewTest(TestCase):
    class TestCase:
        def setUp(self):
            Menu.objects.create(name="lion", sound="roar")
            Menu.objects.create(name="cat", sound="meow")

        def test_getall(self):
            item = Menu.objects.all()
            self.assertEqual(item, "IceCream : 80")
```

### Can the API be tested with the Insomnia REST client? ###
> Yes, please see the screenshots inside the folder name '7. Can the API be tested with the Insomnia REST client'.


## Web Path ##

| Path    | Description |
| ------------- | ------------- |
| http://localhost:8000/  | index.html  |
| http://localhost:8000/bookings?date=2023-02-08  | GET query bookings date  |
| http://localhost:8000/auth/ | GET query authentication location  |
| http://localhost:8000/api-token-auth/  | POST authentication for Token string  |
| http://localhost:8000/menu/  | GET POST : CRUD menu items   |

#### GET Bookings date ####
![alt text](https://github.com/jkaewprateep/LittleLemonAPI/blob/main/HTML%20index.png)
![alt text](https://github.com/jkaewprateep/LittleLemonAPI/blob/main/GET%20reservation%20date.png)
![alt text](https://github.com/jkaewprateep/LittleLemonAPI/blob/main/GET%20reservation%20date%202.png)

#### POST create Bookings queue ####
![alt text](https://github.com/jkaewprateep/LittleLemonAPI/blob/main/POST%20create%20new%20booking%20queue.png)
