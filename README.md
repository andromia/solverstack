[![Discord](https://img.shields.io/discord/721862473132540007?label=discord&style=plastic)](https://discord.gg/wg7xSAf)
[![Slack](https://img.shields.io/badge/slack-workspace-green)](https://join.slack.com/t/andromiasoftware/shared_invite/zt-felqfjhs-Tvma8OYuCExxdmQgHOIGsg)

# solverstack
Software for modularized analytical solutions.

## about the project
The management of the solverstack project is completely open-sourced at the top. We want to provide transparancy with where vision stands and how it's being executed.

## about the product
We plan to release free services at solverstack.com. Users can also sign up and create user-driven modules. In the future we plan to recycle tons of code for a native app. Our goal is to contribute plenty of open-sourced services and tools, as well as some unique d3.js visualizations.

### information about technologies used

**Client applications**

- [`solverstack-client`](https://github.com/andromia/solverstack-client)
  - [next.js](https://github.com/vercel/next.js)
  - UI-driven [d3](https://github.com/d3/d3) visualization

**[<code><img height="20" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/typescript/typescript.png"></code>](https://github.com/microsoft/TypeScript) [Node.js](https://github.com/nodejs) services**

- [`solverstack-user-auth`](https://github.com/andromia/solverstack-user-auth)
  - Gmail Authentication
  - Github Authentication

- [`solverstack-user-crud`](https://github.com/andromia/solverstack-user-crud)
  - [mongodb](https://github.com/mongodb) user module service
  
**<code><img height="20" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png"></code> [flask](https://github.com/pallets/flask) services**

- [`solverstack-vrp`](https://github.com/andromia/solverstack-vrp)
  - [Vehicle routing](https://en.wikipedia.org/wiki/Vehicle_routing_problem) module
  - [NumPy](https://github.com/numpy/numpy) optimized service

- [`solverstack-vrp-crud`](https://github.com/andromia/solverstack-vrp-crud)
  - [postgreSQL](https://github.com/postgres/postgres) vrp module service
  
**[<code><img height="20" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/rust/rust.png"></code>](https://github.com/rust-lang/rust) services**
  
- [`solverstack-queue`](https://github.com/andromia/solverstack-queue)
  - Scalable asynchronous rpc integration service

**Open-source contributions**

- _TODO_: [`solverstack-gallery`](https://github.com/andromia/solverstack-gallery)
  - [d3](https://github.com/d3/d3) sandboxes
