# datasci_4_web_viz
Web-Based Data Visualization Using R, Python, Shiny and Python Flask

# Shiny R
Url: [https://nimratmann.shinyapps.io/CA_Arthritis_Crude_Prevalence/](https://nimratmann.shinyapps.io/CA_Arthritis_Crude_Prevalence/)
When I tried to run my shiny app in posit cloud using the code, my console stated that it could not find the function "arthritis_data". This was because in line 42 under "render the bar plot", my code was ``` arthritis_data <- arthritis_data``` and it prompted a "Warning: Error in arthritis_data: could not find function 'arthritis_data'" message. After I changed the code to ```arthritis_data <- df()```, I was able to run my code smoothly.


# Shiny Python
Url: [https://nimratmann.shinyapps.io/my_shiny_app/ ](https://nimratmann.shinyapps.io/my_shiny_app/ )
While trying to run my shiny app in the Linux terminal in Google shell, my command ```rsconnect deploy shiny/home/nimrat_mann/datasci_4_web_viz/shiny_python --name nimratmann --title "My Shiny App"``` prompted a "no such command" error. I had to revise the code to ``` rsconnect deploy shiny ~/datasci_4_web_viz/shiny_python --name nimratmann --title "My Shiny App" ```. I also had an issue with my requirements.txt file, as shiny was pip-freezing the Google shell environment. Therefore, I 


# Python Flask
I had no issues running my flask application in the google shell environment terminal locally.
"
