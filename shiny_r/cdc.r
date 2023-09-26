# Import necessary libraries
library(shiny)
library(ggplot2)
library(dplyr)

# UI for the Shiny app
ui <- fluidPage(
  titlePanel("Arthritis Crude Prevalence in CA by County"),
  sidebarLayout(
    sidebarPanel(
      selectInput("county", "Choose a county:", choices = NULL)
    ),
    mainPanel(
      plotOutput("barPlot")
    )
  )
)

# Server logic
server <- function(input, output, session) {
  
  # Load the dataset
  df <- reactive({
    url <- "https://raw.githubusercontent.com/nimratmann/datasci_4_web_viz/main/datasets/PLACES__Local_Data_for_Better_Health__County_Data_2023_release.csv"
    read.csv(url)
  })
  
  # Filter the dataset
  df_arthritis <- reactive({
    data <- df()
    filter(data, MeasureId == "ARTHRITIS", Data_Value_Type == "Age-adjusted prevalence")
  })
  
  # Update county choices dynamically based on dataset
  observe({
    arthritis_data <- df_arthritis()
    updateSelectInput(session, "county", choices = sort(unique(arthritis_data$LocationName)))
  })
  
  # Render the bar plot
  output$barPlot <- renderPlot({
    arthritis_data <- arthritis_data()
    county_data <- arthritis_data[arthritis_data$LocationName == input$county, ]
    avg_value <- mean(arthritis_data$Data_Value, na.rm = TRUE)
    
    ggplot() +
      geom_bar(data = county_data, aes(x = LocationName, y = Data_Value, fill = LocationName), stat = "identity") +
      geom_hline(aes(yintercept = avg_value), linetype = "dotted", color = "dodgerblue") +
      labs(title = 'Arthritis Crude Prevalence by County in CA',
           y = 'Data Value (Crude prevalence) - Percent',
           x = 'Location (County)') +
      theme(axis.text.x = element_text(angle = 90, hjust = 1)) +
      ylim(0, 30) +
      scale_fill_manual(values = c("lightcoral", "dodgerblue"))
  })
  
}

# Run the Shiny app
shinyApp(ui, server)