---  
title: How to add a PivotChart with Golang via C++  
linktitle: Pivot Chart  
type: docs  
weight: 100  
url: /go-cpp/how-to-add-pivot-chart/  
description: How to add a PivotChart using Aspose.Cells with Golang via C++.  
keywords: PivotChart  
---  

## What is PivotChart  

A pivot chart is a visual representation of the data in a pivot table. Pivot charts provide a way to summarize, analyze, explore, and present summary data. Here are some key features and aspects of pivot charts:

1. **Dynamic Data Representation**: Pivot charts automatically update to reflect changes in the pivot table. If you add or remove fields in the pivot table, the pivot chart updates accordingly.  

2. **Interactive**: Pivot charts are interactive, allowing users to filter, sort, and drill down into data. This makes it easy to explore different aspects of the data set.  

3. **Flexible Layout**: Users can change the layout of the pivot chart by dragging and dropping fields, which offers flexibility in how data is visualized.  

4. **Various Chart Types**: Pivot charts can be created using various chart types such as bar charts, line charts, pie charts, and more, depending on the nature of the data and the insights you wish to gain.  

5. **Summarization**: Pivot charts summarize large amounts of data and can show totals, averages, counts, or other summary statistics.  

6. **Filtering**: They provide filtering capabilities, allowing you to display only the data that meets certain criteria.  

<br>  
Pivot charts are commonly used in business intelligence and data analysis to provide a clear and concise visual summary of complex data sets. They are a powerful tool for making data‑driven decisions.

## How to add a PivotChart using Aspose.Cells  

### **Adding a Pivot Table**  

To create a pivot table using Aspose.Cells:

1. Add some data to worksheet cells using a `Cell` object's `PutValue` or `SetValue` method. You can also use a template file already filled with data. The data will be used as the pivot table's data source.  
2. Add a pivot table to the worksheet by calling the `PivotTables` collection's `Add` method (encapsulated in the `Worksheet` object).  
3. Access the new `PivotTable` object from the `PivotTables` collection by passing its index. Use any of the objects encapsulated in the `PivotTable` object to manage the table.  

Code examples are given below.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-PivotChart.go" >}}

### **Adding a Pivot Chart**  

To create a PivotChart using Aspose.Cells:

1. Add a chart.  
2. Set the `PivotSource` of the chart to refer to an existing pivot table in the spreadsheet.  
3. Set other attributes.  

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-PivotChart-1.go" >}}