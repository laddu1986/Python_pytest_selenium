import os.path
import json
from model.chat import Chat

data_file_name = 'chat_plans.json'

path_to_data_file = os.path.join(os.path.dirname((os.path.abspath(__file__))), data_file_name)
with open(path_to_data_file) as f:
    data = json.load(f)


expected_data = dict(zip(['lite', 'team', 'professional', 'enterprise'],
                         [Chat(yr_price=plan['annually'], mnth_price=plan['monthly'], agents=plan['total_agents'])
                          for plan in data.values()]))
