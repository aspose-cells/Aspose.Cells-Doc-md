---
title: Using Sparklines and Settings 3D Format with Golang via C++
linktitle: Using Sparklines and Settings 3D Format
type: docs
weight: 40
url: /go-cpp/using-sparklines-and-settings-3d-format/
description: Learn how to use sparklines and apply 3D formatting in Excel files using Aspose.Cells with Golang via C++.
---

## **Using Sparklines**
Microsoft Excel 2010 can analyze information in more ways than ever before. It allows users to track and highlight important data trends with new data analysis and visualization tools. Sparklines are mini‑charts that you can place inside cells so that you can view data and a chart on the same table. When sparklines are used properly, data analysis is quicker and more to the point. They also provide a simple view of information, avoiding overcrowded worksheets with a lot of busy charts.

Aspose.Cells provides an API for manipulating sparklines in spreadsheets.
### **Sparklines in Microsoft Excel**
To insert sparklines in Microsoft Excel 2010:

1. Select the cells where you want the sparklines to appear. To make them easy to view, select cells at the side of the data.  
2. Click **Insert** on the ribbon and then choose **Column** in the **Sparklines** group.  
3. Select or enter the range of cells in the worksheet that contain the source data. The charts will appear.  

Sparklines help you to see trends, for example, the win or loss record for a softball league. Sparklines can even sum up the entire season of each team in the league.
### **Sparklines using Aspose.Cells**
Developers can create, delete, or read sparklines (in the template file) using the API provided by Aspose.Cells. The classes that manage sparklines are contained in the [Aspose.Cells.Charts](https://reference.aspose.com/cells/go-cpp/aspose.cells.charts/) namespace, so you need to import this namespace before using these features.

By adding custom graphics for a given data range, developers have the freedom to add different types of tiny charts to selected cell areas.

The example below demonstrates the Sparklines feature. The example shows how to:

1. Open a simple template file.  
2. Read sparklines information for a worksheet.  
3. Add new sparklines for a given data range to a cell area.  
4. Save the Excel file to disk.  

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-UsingSparklinesAndSettings3dFormat.go" >}}

## **Setting 3D Format**
You might need 3D charting styles to obtain the results required for your scenario. Aspose.Cells provides the relevant API to apply Microsoft Excel 2007 3D formatting.

A complete example is given below to demonstrate how to create a chart and apply Microsoft Excel 2007 3D formatting. After executing the example code, a column chart (with 3D effects) will be added to the worksheet.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-UsingSparklinesAndSettings3dFormat-1.go" >}}
{{< app/cells/assistant language="go" >}}
