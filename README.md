## OCPP Backend Server
This project provides two main functionalities
1. Websocket server for charging stations to communicate
    1. OCPP 1.6 J based implementation
    2. Start transaction
    3. Stop Transaction
    4. Capture status of an active session
    5. Reset Connector
    6. Unlock Connector
    7. Send configurations
    8. Clock Alignment
    9. Diagnostic
   
2. Rest API's for Application or Dashboard to send requests which will be relayed to connected charging stations.


### Tech Stack:
1. FASTAPI
2. Mobility House OCPP 1.6 J base library
3. Uvicorn
4. Nginx

### Deployment Mechanism
Comming soon


