from freelancersdk.session import Session
from freelancersdk.resources.users \
    import get_self_user_id
import os

oauth_token='y4OwAnq4GRgArzK2YLdakB1t0kuN5y'
url='https://freelancer.com'
session = Session(oauth_token=oauth_token, url=url)
my_user_id = get_self_user_id(session)

bidder_id=my_user_id