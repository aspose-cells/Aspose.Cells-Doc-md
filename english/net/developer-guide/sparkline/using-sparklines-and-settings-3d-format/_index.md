---
title: Using Sparklines and Settings 3D Format
type: docs
weight: 40
url: /net/using-sparklines-and-settings-3d-format/
---

## **Using Sparklines**
Microsoft Excel 2010 can analyze information in more ways than ever before. It allows users to track and highlight important data trends with new data analysis and visualization tools. Sparklines are mini-charts that you can place inside cells so that you can view data and chart on the same table. When sparklines are used properly, data analysis is quicker and more to the point. They also provide a simple view of information, avoiding over-crowded worksheets with a lot of busy charts.

Aspose.Cells provides an API for manipulating sparklines in spreadsheets.
### **Sparklines in Microsoft Excel**
To insert sparklines in Microsoft Excel 2010:

1. Select the cells where you want the sparklines to appear. To make them easy to view, select cells at the side of the data.
1. Click **Insert** on the ribbon and then choose **column** in the **Sparklines** group.
1. Select or enter the range of cells in the worksheet that contain the source data. The charts will appear.

Sparklines help you to see trends, for example, the win or loss record for a softball league. Sparklines can even sum up the entire season of each team in the league.
### **Sparklines using Aspose.Cells**
Developers can create, delete or read sparklines (in the template file) using the API provided by Aspose.Cells. The classes that manage sparklines are contained in the [Aspose.Cells.Charts](https://reference.aspose.com/cells/net/aspose.cells.charts) namespace so you need to import this namespace before using these features.

By adding custom graphics for a given data range, developers have the freedom to add different types of tiny charts to selected cell areas.

The example below demonstrates the Sparklines feature. The example shows how to:

1. Open a simple template file.
1. Read sparklines information for a worksheet.
1. Add new sparklines for a given data range to a cell area.
1. Save the Excel file to disk.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-UsingSparklines-1.cs" >}}
## **Setting 3D Format**
You might need 3D charting styles so you can get just the results for your scenario. Aspose.Cells does provide the relevant API to apply Microsoft Excel 2007 3D formatting.

A complete example is given below to demonstrate how to create a chart and apply Microsoft Excel 2007 3D formatting. After executing the example code, a column chart (with 3D effects) will be added to the worksheet.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-Applying3DFormat-1.cs" >}}
