# Project 2 Architecture

```text
              Client
                |
                v
        Flask Inventory API
          (Docker Container)
                |
          Docker Network
                |
                v
        PostgreSQL Database
          (Docker Container)
                |
                v
       PostgreSQL Named Volume
       project-2-inventory_postgres_data
