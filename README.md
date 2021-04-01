# solverstack
Software for modularized analytical solutions.

## about the project
The management of the solverstack project is completely open-sourced at the top. We want to provide transparency with where vision stands and how it's being executed.

## about the product
We plan to release free services at solverstack.com. Users can also sign up and create user-driven modules. In the future we plan to recycle tons of code for a native app. Our goal is to contribute plenty of open-sourced services and tools, as well as some unique d3.js visualizations.

### information about technologies used

**Client applications**

- [`solverstack-web`](https://github.com/cnpls/solverstack-web) browser client
  - [next.js](https://github.com/vercel/next.js)
  - UI-driven [d3](https://github.com/d3/d3) visualization
  
**<code><img height="20" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png"></code> [flask](https://github.com/pallets/flask) services**

- [`solverstack-user`](https://github.com/cnpls/solverstack-user)
  - solverstack Authentication
  - Gmail Authentication
  - Github Authentication

- [`solverstack-geocode`](https://github.com/cnpls/solverstack-geocode)
  - [pgeocode](https://github.com/symerio/pgeocode) geocoding service

- [`solverstack-route`](https://github.com/cnpls/solverstack-route)
  - [Vehicle routing](https://en.wikipedia.org/wiki/Vehicle_routing_problem) module
  - [NumPy](https://github.com/numpy/numpy) optimized service

- [`solverstack-depot`](https://github.com/cnpls/solverstack-depot)
  - [clustering](https://en.wikipedia.org/wiki/K-means_clustering) service for depot position and size optimization

- [`solverstack-crud`](https://github.com/cnpls/solverstack-crud)
  - [postgreSQL](https://github.com/postgres/postgres) for module component data storage
