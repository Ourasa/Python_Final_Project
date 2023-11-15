# Project Title - Weather Trends

## Authors: 
Author 1: Steven Pham

Author 2: Tommy Agarwal

## Project Description (5 sentences): 
This is a Python-centric project that will provide the user with an interactable interface that informs them of the weather. Upon opening, the user will be informed of the current weather (of the local area in San Jose?). From here, the user may choose to view the forecast of weather of up to 7 days, or view the weather from yesterday. The forecast option shows a plot of the predicted temperatures for the upcoming week. The yesterday option would be similar to the current weather option, except it would highlight the highest and lowest temperatures of that day.

- - - - -

# Project Outline/Plan 

## Interface Plan: 
The interface will be a web interface that is created using Flask. It is planned that the user will interact with this interface through the use of widgets such as buttons. We are thinking of having a home page first, which can then branch off to the forecast plot page and the yesterday page. Ideally, these branches would also be able to directly go to the other's page as well without stopping by the home page. 

## Data Collection and Storage Plan: 
Data can be obtained by using an API from Pirate Weather. The information obtained from this API would need to be filtered for our program's purposes. The data obtained would then be stored into the local machine in a predetermined format, allowing it to be used for data analysis and visualization. The data we will be going for is the current weather, the forecast, and weather from yesterday.

## Data Analysis and Visualization Plan: 
This part is reliant on the organized data obtained using an API. The data obtained will be processed internally in the local machine to create an output that can be viewed on the interface. For the current weather and yesterday's weather, minimal processing would be needed. Meanwhile, the weather forecast will likely be placed in a plot, but outliers would also be calculated (using standard deviation presumably). Days that are identified as outliers are planned to be colored differently to be easier to identify.
