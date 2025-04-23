---
title: Aspose.Cells 8.7.1 中的公共 API 更改
type: docs
weight: 240
url: /zh/net/public-api-changes-in-aspose-cells-8-7-1/
---

{{% alert color="primary" %}} 

本文档描述了从版本 8.7.0 到 8.7.1 的 Aspose.Cells API 中的更改，这可能对模块/应用程序开发人员感兴趣。它不仅包括新的和更新的公共方法，添加和删除的类等，还包括了 Aspose.Cells 后台行为的任何更改的描述。

{{% /alert %}} 
## **添加的 API**
### **添加了 LookInType.OriginalValues 属性**
Aspose.Cells API 已经支持[查找或搜索数据](/cells/zh/net/find-or-search-data/)功能，以便在电子表格中查找特定的内容。但是，这一功能缺乏作用于单元格的格式方面，这可能改变内容的外观和值，因此使用原始值使文本无法被搜索。通过此次 Aspose.Cells API 的发布，另一个名为 LookInType.OriginalValues 的常量已经暴露给公共 API，允许克服上述讨论的情况。

{{% alert color="primary" %}} 

有关此功能的更多详情，请参阅[使用原始值搜索数据](/cells/zh/net/search-data-using-original-values/)的详细文章

{{% /alert %}} 

以下是简单的使用场景。

**C#**

{{< highlight csharp >}}

 //Create workbook object

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Add 10 in cell A1 and A2

worksheet.Cells["A1"].PutValue(10);

worksheet.Cells["A2"].PutValue(10);

//Add Sum formula in cell D4 but customize it as ---

Cell cell = worksheet.Cells["D4"];

Style style = cell.GetStyle();

style.Custom = "---";

cell.SetStyle(style);

//The result of formula will be 20

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


### **为 GridWeb 添加了 OnBeforeColumnFilter 事件**
Aspose.Cells.GridWeb for .NET 8.7.1 已经暴露了 OnBeforeColumnFilter 事件，用作通过 GridWeb UI 进行的过滤机制的回调。正如其名称暗示的那样，该事件在应用列过滤之前触发，并可用于获取有关过滤信息的信息，例如要应用过滤的列索引和值。

简单的使用场景如下。

**C#**

{{< highlight csharp >}}

 protected void GridWeb1_ColumnFilter(object sender, Aspose.Cells.GridWeb.RowColumnEventArgs e)

{

    string msg = "Column index: " + (e.Num) + ", Filtered Value:" + e.Argument;

}

{{< /highlight >}}

{{% alert color="primary" %}} 

Do not forget to register the event to GridWeb control <acw:gridweb OnBeforeColumnFilter="GridWeb1_ColumnFilter"/>

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
