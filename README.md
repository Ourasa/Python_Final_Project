# Project Title - Weather Trends

## Authors: 
Author 1: Steven Pham

Author 2: Tommy Agarwal

## Project Description (5 sentences): 
This is a Python-centric project that will provide the user with an interactable interface that informs them of the weather of San Jose. Upon opening, the user will be placed into an initial landing page. From here, the user may click to get data, and choose to view the information regarding the weather within a 48 hours period (24 before and 24 after present hour), or view the week forecast. These options will first show a table format of the information. There will be the option show a graph of the data, which would make a plot and point out things to note after some analysis. 

- - - - -

# Project Outline/Plan 

## Interface Plan: 
The interface will be a web interface that is created using Flask. The user will interact with this interface through the use of widgets, primarly through buttons. We will have an initial page which is used to get data, and a page that will prompt you to pick what view you want to see first. After that, there will be a pseudo-navigation bar on the top of the page, which the user can use to swap between desired views. If the user wants to refresh the data (get the most up-to-date data), they can click the refresh button which will send them back to the prompt. 

## Data Collection and Storage Plan: 
Data is obtained by using an API from Pirate Weather. The information obtained from this API would need to be filtered for our program's purposes. The data obtained would then be stored into the local machine in a predetermined format (txt), allowing it to be used for data analysis and visualization. The data we will be going for is the current weather, the week forecast, weather from yesterday, and temperatures within a 48 hour period (with the present time being the center).

## Data Analysis and Visualization Plan: 
This part is reliant on the organized data obtained using an API. The data obtained will be processed internally in the local machine to create an output that can be viewed on the interface. For the current weather and yesterday's weather, minimal processing would be needed. Meanwhile, the weather forecast will likely be placed in a plot, but trends are to be calculated. There can be one trend for both forecasted high temperatures and low temperatues. For the 48 hour temperature data, we may highlight the highest and lowest temperatures, and the trend for the before and after 24 hour period. 

- - - - -

## IMPORTANT: How to get and use the needed API Key

In order to use this program, you will need your own Pirate Weather API Key. 
<br /><br />
### To get a key, you need to do the following:
  1.) Create and confirm an account at [Pirate Weather's website.](https://pirateweather.net/en/latest/)  
  2.) Sign into the account, then click on "Get an API Key" and "Weather Data"   
  3.) Click "Subscribe" for the Free option, and name your subscription.  
  4.) You will see an automatically generated API key. Copy this and store this somewhere safe.  
<br />
### To use the key, you need to do the following: 
  1.) Download this project's files.   
  2.) Open up the 'data' folder, and access 'secret.txt' for editing.  
  3.) Paste your API key into the file. Do not add any other text.  
  4.) Save the file.  

- - - - -

## How to use this program 

To use this program, you will need to do the following:  
  1.) Download this project's files.  
  2.) Obtain and insert the API Key into secret.txt. See above API key instructions for more details.  
  3.) Run the Driver.py file. This can be done using an IDE like VSCode, or with a terminal command.  
  4.) Open a web browser, and paste **http://127.0.0.1:5000** onto the URL.  

**WARNING**: There is a chance that the API we are using will update its information for itself during use. If that happens, it will fail the program's API requests during a refresh/get, resulting in an internal server error. We cannot avoid this problem, however, restarting the program should make everything operate as usual.
  
- - - - -

## Potential Updates for the Future
  1.) Smoothing out of the program's execution time. This can be done by specifying further reductions in size for API calls. We can also reduce the preception of the wait time by having the update function only update data relevant to the current page.  
  2.) Improve UI/appearance of program. This can be completed by adding more images, reformatting some of the elements, etc.  
  3.) Allow application to work for all parts of the world. This will require us to implement a search function, which would translate typed in locations to coordinates, which can then be used to gather data for that particular location. 
