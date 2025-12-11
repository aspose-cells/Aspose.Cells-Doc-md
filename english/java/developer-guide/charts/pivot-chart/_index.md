---  
title: How to add a PivotChart using Aspose.Cells  
linktitle: Pivot Chart  
type: docs  
weight: 100  
url: /java/how-to-add-pivot-chart/  
description: How to add a PivotChart using Aspose.Cells.  
keywords: PivotChart  
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

## What is PivotChart  
A pivot chart is a visual representation of the data in a pivot table. Pivot charts provide a way to summarize, analyze, explore, and present summary data. Here are some key features and aspects of pivot charts:

1. **Dynamic Data Representation:** Pivot charts automatically update to reflect changes in the pivot table. If you add or remove fields in the pivot table, the pivot chart updates accordingly.  

2. **Interactive:** Pivot charts are interactive, allowing users to filter, sort, and drill down into data. This makes it easy to explore different aspects of the data set.  

3. **Flexible Layout:** Users can change the layout of the pivot chart by dragging and dropping fields, which offers flexibility in how data is visualized.  

4. **Various Chart Types:** Pivot charts can be created using various chart types such as bar charts, line charts, pie charts, and more, depending on the nature of the data and the insights you wish to gain.  

5. **Summarization:** Pivot charts summarize large amounts of data and can show totals, averages, counts, or other summary statistics.  

6. **Filtering:** They provide filtering capabilities, allowing you to display only the data that meets certain criteria.  

<br>  
Pivot charts are commonly used in business intelligence and data analysis to provide a clear and concise visual summary of complex data sets. They are a powerful tool for making data‑driven decisions.  

## How to add a PivotChart using Aspose.Cells  

### **Creating a Pivot Table**  

To create a pivot table using Aspose.Cells:

1. Add some data to worksheet cells using a `Cell` object's `PutValue`/`setValue` method. You can also use a template file already filled with data. The data will be used as the pivot table's data source.  
2. Add a pivot table to the worksheet by calling the `PivotTables` collection's `add` method (encapsulated in the `Worksheet` object).  
3. Access the new `PivotTable` object from the `PivotTables` collection by passing its index.  
4. Use any of the pivot‑table objects encapsulated in the `PivotTable` object to manage the table.  

A code sample is given below. Executing the code generates a new file: `pivotTable_test.xls`.  

**Input data**  

![todo:image_alt_text](create-pivot-tables-and-pivot-charts_1.png)  

**The output pivot table**  

![todo:image_alt_text](create-pivot-tables-and-pivot-charts_2.png)  

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePivotTable-CreatePivotTable.java" >}}  

### **Creating a Pivot Chart based on the Pivot Table**  

To create a pivot chart using Aspose.Cells:

1. Add a chart.  
2. Set the `PivotSource` of the chart to refer to an existing pivot table in the spreadsheet.  
3. Set other attributes.  

Below is the code used by the component to accomplish the task. Executing the code generates a new file: `pivotChart_test.xls`.  

**The pivot chart sheet**  

![todo:image_alt_text](create-pivot-tables-and-pivot-charts_3.png)  

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreatePivotChartbasedonPivotTable-CreatePivotChartbasedonPivotTable.java" >}}  

{{% alert color="primary" %}}  

This article shows how to create pivot tables and pivot charts using Aspose.Cells. Hopefully, it will help you use these features in your own scenarios.  

Aspose.Cells has benefited from years of research, design, and careful tuning.  

We welcome your queries, comments, and suggestions at the [Aspose.Cells Forum](https://forum.aspose.com/c/cells/9). We guarantee a prompt reply.  

{{% /alert %}}  

{{< app/cells/assistant language="java" >}}
