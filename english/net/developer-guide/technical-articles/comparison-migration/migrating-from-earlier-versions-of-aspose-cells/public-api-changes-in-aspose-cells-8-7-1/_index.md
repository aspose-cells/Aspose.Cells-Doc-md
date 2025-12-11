---
title: Public API Changes in Aspose.Cells 8.7.1
type: docs
weight: 240
url: /net/public-api-changes-in-aspose-cells-8-7-1/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

This document describes the changes to the Aspose.Cells API from version 8.7.0 to 8.7.1 that may be of interest to module/application developers. It includes not only new and updated public methods, added & removed classes, etc., but also a description of any changes in the behavior behind the scenes in Aspose.Cells.

{{% /alert %}} 
## **Added APIs**
### **Added LookInType.OriginalValues Property**
Aspose.Cells APIs already support the [Find or Search Data](/cells/net/find-or-search-data/) feature for spreadsheets in order to find a particular piece of content in cell value & formula. However, this feature was lacking the aspect of formatting applied to the cell that may change the appearance as well as the value of the contents, consequently making the text unsearchable using the original value. With this release of Aspose.Cells APIs, another constant by the name `LookInType.OriginalValues` has been exposed to the public API which allows you to overcome the situation as discussed above.

{{% alert color="primary" %}} 

For more details on this feature, please review the detailed article on [Search Data Using Original Values](/cells/net/search-data-using-original-values/)

{{% /alert %}} 

Following is the simple usage scenario.

**C#**

{{< highlight csharp >}}

 //Create workbook object

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Add 10 to cell A1 and A2

worksheet.Cells["A1"].PutValue(10);

worksheet.Cells["A2"].PutValue(10);

//Add Sum formula in cell D4 but customize it as ---

Cell cell = worksheet.Cells["D4"];

Style style = cell.GetStyle();

style.Custom = "---";

cell.SetStyle(style);

//The result of the formula will be 20

//but 20 will not be visible because

//the cell is formatted as ---

cell.Formula = "=Sum(A1:A2)";

//Calculate the workbook

workbook.CalculateFormula();

//Create find options

FindOptions options = new FindOptions();

options.LookInType = LookInType.OriginalValues;

options.LookAtType = LookAtType.EntireContent;

Cell foundCell = null;

object obj = 20;

//Find 20 which is Sum(A1:A2) and formatted as ---

foundCell = worksheet.Cells.Find(obj, foundCell, options);

//Print the found cell

Console.WriteLine(foundCell);

{{< /highlight >}}


### **Added OnBeforeColumnFilter Event for GridWeb**
Aspose.Cells.GridWeb for .NET 8.7.1 has exposed the `OnBeforeColumnFilter` event which serves as a callback to the filtering mechanism performed through the GridWeb UI. As the name suggests, the event is triggered before the column filtering is applied and can be used to get the filtering information such as column index and the value on which the filter has to be applied.

A simple usage scenario looks as follows.

**C#**

{{< highlight csharp >}}

 protected void GridWeb1_ColumnFilter(object sender, Aspose.Cells.GridWeb.RowColumnEventArgs e)

{

    string msg = "Column index: " + (e.Num) + ", Filtered Value:" + e.Argument;

}

{{< /highlight >}}

{{% alert color="primary" %}} 

Do not forget to register the event to GridWeb control `<acw:gridweb OnBeforeColumnFilter="GridWeb1_ColumnFilter"/>`

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
