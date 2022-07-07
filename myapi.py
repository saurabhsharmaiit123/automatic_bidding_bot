from webbrowser import get
from freelancersdk.session import Session
from freelancersdk.resources.projects.projects import search_projects
from freelancersdk.resources.projects.exceptions import \
    ProjectsNotFoundException
from freelancersdk.resources.projects.helpers import (
    create_search_projects_filter,
    create_get_projects_user_details_object,
    create_get_projects_project_details_object,
)
from freelancersdk.resources.projects import place_project_bid
from freelancersdk.session import Session
from freelancersdk.resources.users \
    import get_self_user_id
from freelancersdk.exceptions import BidNotPlacedException
from matplotlib.pyplot import title
from numpy import minimum
from keys import(oauth_token, bidder_id)

import os


def sample_search_projects():

    session = Session(oauth_token=oauth_token,
                      url='https://www.freelancer.com')
    query = 'Power BI'
    search_filter = create_search_projects_filter(
        sort_field='time_updated',
        or_search_query=True,
    )

    try:
        p = search_projects(
            session,
            query=query,
            search_filter=search_filter
        )

    except ProjectsNotFoundException as e:
        print('Error message: {}'.format(e.message))
        print('Server response: {}'.format(e.error_code))
        return None
    else:
        return p


p = sample_search_projects()
if p:
    for x in p.get('projects'):
        title = x.get('title')
        print(title)
        id=x.get('id')
        amount=x.get('budget').get('minimum')
        bid_data = {
        'project_id': id,
        'bidder_id': bidder_id,
        'amount': amount,
        'period': 10,
        'milestone_percentage': 20,
        'description':'Hi,

I am a Certified Business Analyst from IIT Hyderabad.

I work with PowerBI Pro & Premium Licenses.

I am a candidate with five years of Experience in Data Science and Market Research.

I have professionally worked as a Data Scientist for over 3.5 Years and am well versed in Statistical Techniques, Machine Learning, and Business Analysis.

Additionally, I have worked on the Development, Testing, and Deployment of PowerBI Reports.

I know DAX, PowerQ, PowerBI Desktop, Row Level Security, gateway configuration, paginated reports, and embedding.

I have previously built the following Dashboards:

Sales Analytics Dashboard (using SQL Server)
Sales Performance Dashboard (using SQL Server)
Tender Sales Dashboard (using SQL Server)
Cost and Equipment Dashboard (using SQL Server)
Man-Power Forecasting Dashboard (Using SharePoint)

DM me so that we can discuss the project further

Regards,
Sangamesh KS
   ',
         }
    print(bid_data)
    session = Session(oauth_token=oauth_token,
                      url='https://www.freelancer.com')
    try:
        b = place_project_bid(session, **bid_data)
        if b:
            print(("Bid placed: %s" % b))
    except BidNotPlacedException as e:
        
        print(('Error message: %s' % e.message))
        print(('Error code: %s' % e.error_code))
       
        

