+++
title = "Data Formatting in Charts" 
description = "" 
weight = 12270 
+++

Aspose.Cells for .NET : Data Formatting in Charts  

# Aspose.Cells for .NET : Data Formatting in Charts


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Setting Chart Data](#DataFormattinginCharts-SettingChartData)
    *   1.1 [Chart Data](#DataFormattinginCharts-ChartData)
    *   1.2 [Category Data](#DataFormattinginCharts-CategoryData)
{{< /panel >}}
 

In our previous topics, we have already provided many examples to demonstrate that how can you set a data source for your chart but in this topic, we are going to provide more details about the types of data that can be set for a chart.

### Setting Chart Data

There are two types of data to deal with while working on charts using Aspose.Cells as follows:

*   Chart data.
*   Category data.

#### Chart Data

Chart data is the data that we use as a data source to build our charts. We can add a range of the cells (containing chart data) by calling the [SeriesCollection](https://apireference.aspose.com/cells/net/aspose.cells.charts/seriescollection) object's [Add](https://apireference.aspose.com/cells/net/aspose.cells.charts/seriescollection/methods/add) method.

#### Category Data

Category data is used for the labeling of chart data and can be added to [SeriesCollection](https://apireference.aspose.com/cells/net/aspose.cells.charts/seriescollection) by using its [CategoryData](https://apireference.aspose.com/cells/net/aspose.cells.charts/seriescollection/properties/categorydata) property. A complete example is given below to demonstrate the use of chart and category data. After executing the above example code, a column chart will be added to the worksheet as shown below.

