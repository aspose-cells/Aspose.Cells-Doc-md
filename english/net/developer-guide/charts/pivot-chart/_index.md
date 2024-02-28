---
title: How to add a PivotChart using Aspose.Cells
linktitle: Pivot Chart
type: docs
weight: 100
url: /net/how-to-add-pivot-chart/
description: How to add a PivotChart using Aspose.Cells.
keywords: PivotChart
---
## What is PivotChart

A PivotChart in Excel is a graphical representation of data created from a PivotTable. It allows users to visualize and analyze data dynamically by summarizing and displaying information in chart form. PivotCharts are interactive and can be easily modified to show different perspectives of the data, making it a powerful tool for data analysis and presentation in Excel.

## How to add a PivotChart using Aspose.Cells

### **Adding a Pivot Table**

To create a pivot table using Aspose.Cells:

1. Add some data to a worksheet cells using a Cell object's PutValue/setValue method. You also use a template file already filled with data. The data will be used as the pivot table's data source.
1. Add a pivot table to the worksheet by calling the PivotTables collection's add method (encapsulated in the Worksheet object).
1. Access the new PivotTable object from the PivotTables collection by passing its index. # Use any of the pivot table objects encapsulated in the PivotTable object to manage the table.

Code examples are given below.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreatePivotTablesPivotCharts-CreatePivotTable-1.cs" >}}

### **Adding a Pivot Chart**

To create a PivotChart using Aspose.Cells:

1. Add a chart.
1. Set the PivotSource of the chart to refer to an existing pivot table in the spreadsheet.
1. Set other attributes.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreatePivotTablesPivotCharts-CreatePivotChart-1.cs" >}}

