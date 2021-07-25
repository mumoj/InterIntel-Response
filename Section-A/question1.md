### Examples of Integration Protocols.
#### (i) REST API
A REST API is an Application Programming Interface that conforms to the Representational State Transfer Architectural 
design principals first set forth by Dr.Roy Fielding in 2000. An API can be defined as mechanism that allows a service
or an application to access a resource in different application or service. A client is the application/service 
requesting the resource and a server is the application/service hosting the resource.

The REST design principals are:  
 1. Client-server decoupling. Client and server must completely be independent of each other. The client should only 
    know of the URI of the requested resource in the server.  
 2. Statelessness. Server-side sessions are not kept, such that each request contains all the information necessary
    for processing it.  
 3. Cacheability. Resource should be cacheble on the server or client side.  
 4. Layered system architecture: Requests and call can seamlessly go through different intermediaries in the 
    communication loop; the client and server don't have to communicate directly.  
 5. Uniform Interface. All API calls for a resource should use the same Uniform Resource Identifier(URI).  
 6. Code on demand. If responses contain executable code, it should only run on demand.  
 
 REST APIs commonly communicate through HTTP requests to do POST, GET, DELETE and PUT operations on data in JSON format.
 Python can handle such operations through the requests library as illustrated below:
 
 ```python
""" A RESTul implementation of a client interfacing with an  attendance register server using HTTP. The client shall post 
new attendee, update their details, retrieve them and delete attendees as needed. An attendee JSON object shall be 
as depicted below:

    {
        "national_id" : 34567891
        "first_name": Jane
        "last_name" : Mlachake
    }
"""

import requests


def get_url(path):
    """Define the register's URL."""
    return 'https://attendance-register.com/' + path
   
def get_attendants():
    """ A GET request for all the attendees in the register. """
    return requests.get(get_url('attendees/'))

def get_attendant_details(national_id):
    """A GET request for a specific attendees's details."""
    return requests.get(get_url(f'attendees/{national_id}') )

def register_attendant(national_id, first_name, last_name):
    """A POST request with all the attendee's details. A POST requests makes a new addition to the register."""
    return requests.post(get_url('attendees/'),
        json= {
            "national_id": national_id,
            "first_name": first_name,
            "last_name": last_name
        })
def update_attendant_details(national_id, first_name, last_name):
    """A PUT request to alter details of a specific attendee in the register."""
    return requests.put(get_url(f'attendees/{national_id}'),
    json= {
            "first_name": first_name,
            "last_name": last_name
        })
    
def unregister_attendant(national_id): 
    """A DELETE request to remove an attendee from the register"""  
    return  requests.delete(get_url(f'attendees/{national_id}'))
    
```
 

#### (ii) GraphQL
GraphQL is a data query and manipulation language for APIs. It consists of a type system, query language and execution 
semantics, static validation and type introspection. It allows clients to define the structure of the data they
want returned and the exact structure is returned from the server without the overhead of other irrelevant data. In this 
aspect GraphQl gets it edge on REST APIs. Another advantage it has over REST APIs is that you only need only one endpoint
to query different data objects.   

In python it can be implemented through the graphene-python library. Graphene- python is availed to Django through the
django-graphene package.   

```python
""" Implementation of the attendance register app with GraphQl and Django. The Django model class shall be as 
    depicted below:

        class Attendee(models.Model):
            national_id = models.NumberField(primary_key=True)
            first_name  = models.CharField()
            second_name = models.Charfield()
"""
import graphene

from graphene_django import DjangoObjectType, DjangoListField 
from .models import Attendee


class AttendeeType(DjangoObjectType):
    """ Define the model object Type."""
    class Meta:
        model = Attendee
        fields = '__all__'

class Query(graphene.ObjectTpe):
    """Define a queries  for retrieving data from the API."""
    all_attendees = graphene.List(AttendeeType) # Get a list of all the attendees
    attendee = graphene.Field(AttendeeType, national_id=graphene.Int()) # Get a specific attendee.
    
    def resolve_all_attendees(self, info, **kwargs):
        return Attendee.objects.all()
    
    def resolve_attendee(self, info, national_id):
        return Attendee.objects.get(pk=national_id)

# To post or update or delete data, mutations are used

class DeleteAttendee(graphene.Mutation):
    """A example delete mutation"""
    class Arguments:
        national_id = graphene.ID()
        
    attendee = graphene.Field(AttendeeType)
    
    @static_method
    def mutate (root, info, national_id):
        attendee_instance = Attendee.objects.get(pk=national_id)
        attendee_instance.delete()
        
        return None

class Mutation(graphene.ObjectType):
    delete_book = DeleteAttendee.Field()
    

schema = graphene.Schema(query=Query, mutation=Mutation) # Registartion into the single endpoint.
```

The following GraphQL code is for querying all the attendees and their details in the API.
```graphql

query {
    allAttendees {
        nationalID
        first_name
        last_name  
    }   
}
```
To request a certain attendee's details you can construct a query like below:

```graphql

query{
    attendee(nationalID: 34897861){
        first_name
        last_name
    }
}
```   

To delete an attendee one can use a query like below:

```graphql
mutation deleteMutation {
    deleteAttendee(nationalID:34897862 {
        book {
            nationalID
        }
    }
    
}
```

#### (iii) Simple Object Access Protocol(SOAP)
SOAP is a communication protocol for exchanging structured information in the implementation of web services.SOAP 
messages are purely encoded in XML which makes them language and platform independent. It relies on application layer 
protocols; most often HTTP, though others like SMTP may be used. 

A SOAP message contains:
 1. An Envelope that indicates the start and end of a messages.
 2. An optional Header element that includes attributes used to process the message.
 3. A mandatory Body part that contains the XML message.
 4. An optional Fault which provides the errors messages.
 
Languages like python often use Web Service Definition Language(WSDL)  to reduce  the complexity of XML by making use 
of its shortcuts.A WSDL file defines and describes the services available in the web service of interest. In python, 
the Zeep library can be used to consume WSDL SOAP services.

```python

from zeep import Client

client = Client('http://www.webservicex.net/ConvertSpeed.asmx?WSDL')
result = client.service.ConvertSpeed(
    100, 'kilometersPerhour', 'milesPerhour')

assert result == 62.137

```

 




