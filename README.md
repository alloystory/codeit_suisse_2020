# CodeIT Suisse 2020
## Description
A coding competition held from 26 Sep 2020 to 27 Sep 2020 between Singapore and Hong Kong participants. 

The competition comprised of 20 challenges, in which the completion of each challenge will award the participant with some points.

Participants were required to deploy a REST API, and expose an endpoint for each challenge. The grader script will test the participants' algorithm by comparing the responses from the endpoint.

## Result
Awarded the 2nd prize in the Singapore Individual category. Leaderboard: [ [Local](docs/Leaderboard.pdf) | [Remote](https://cis2020-sg-individual-backend.herokuapp.com/leaderboard/index.html) ]

## Completed Challenges
1. Cluster [ [Question](docs/questions/Cluster.pdf) | [Algorithm](src/controllers/cluster.py) | Endpoint: `/cluster` ]
2. Clean Floor [ [Question](docs/questions/Clean%20the%20Floor.pdf) | [Algorithm](src/controllers/clean_floor.py) | Endpoint: `/clean_floor` ]
3. Contact Tracing [ [Question](docs/questions/Contact%20Tracing.pdf) | [Algorithm](src/controllers/contact_tracing.py) | Endpoint: `/contact_trace` ]
4. Fruit Basket [ [Question](docs/questions/Magical%20Fruit%20Basket.pdf) | [Algorithm](src/controllers/fruit_basket.py) | Endpoint: `/fruitbasket` ]
5. Intelligent Farming [ [Question](docs/questions/Intelligent%20Farming.pdf) | [Algorithm](src/controllers/intelligent_farming.py) | Endpoint: `/intelligent-farming` ]
6. Inventory Management [ [Question](docs/questions/Inventory%20Management.pdf) | [Algorithm](src/controllers/inventory_management.py) | Endpoint: `/inventory-management` ]
7. Revisit Geometry [ [Question](docs/questions/Revisit%20Geometry.pdf) | [Algorithm](src/controllers/revisit_geometry.py) | Endpoint: `/revisitgeometry` ]
8. Salad Spree [ [Question](docs/questions/Salad%20Spree.pdf) | [Algorithm](src/controllers/salad_spree.py) | Endpoint: `/salad-spree` ]
9. Social Distancing [ [Question](docs/questions/Social%20Distancing.pdf) | [Algorithm](src/controllers/social_distancing.py) | Endpoint: `/social_distancing` ]
10. Yin Yang [ [Question](docs/questions/Yin%20Yang.pdf) | [Algorithm](src/controllers/yin_yang.py) | Endpoint: `/yin-yang` ]

## Technologies
- Python 3.7
- Flask
- Heroku

## Usage
1. Run `pip install -r requirements.txt`
2. Start the API by running `./run.sh <dev|prod>`
3. Import `insomnia_config.json` to Insomnia