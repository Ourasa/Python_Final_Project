# Project Title - Weather Trends

## Authors: 
Author 1: Steven Pham
Author 2: Tommy Agarwal

## Project Description (5 sentences): 
This is a Python-centric project that will provide the user with an interactable interface that informs them of the weather. Upon opening, the user will be informed of the current weather (of the local area in San Jose?). From here, the user may choose to view the forecast of weather, or view weather from the past (history). The forecast option shows a plot of the predicted temperatures for the upcoming week. The history option would show a plot of the temperature in the past month, and highlight any anomalies.

- - - - -

# Project Outline/Plan 

## Interface Plan: 
The interface will be a web interface that is created using Flask. It is planned that the user will interact with this interface through the use of widgets such as buttons. We are thinking of having a home page first, which can then branch off to the forecast plot page and the weather history page. Ideally, these branches would also be able to directly go to the other's page as well without stopping by the home page. 

## Data Collection and Storage Plan: 
Data can be obtained by scraping from a renowned weather channel website(s). Preferably, the data collection would be done with the use of a provided API. It is highly likely that the information obtained from the site would need to be filtered before organization. The data obtained would then be stored into the local machine in a predetermined format, allowing it to be used for data analysis and visualization. The data we will be going for is the current weather, the forecast, and weather from the past, up to one month. Data even further back would be discarded.

## Data Analysis and Visualization Plan: 
This part is reliant on the organized data obtained from scraping. The data obtained will be processed internally in the local machine to create an output that can be viewed on the interface. This applies to both the weather forecast and history. The weather forecast will likely be placed in a plot. The weather history may also be placed in a plot, but outliers would also be calculated (using standard deviation presumably). Days that are identified as outliers are planned to be colored differently to be easier to identify.
