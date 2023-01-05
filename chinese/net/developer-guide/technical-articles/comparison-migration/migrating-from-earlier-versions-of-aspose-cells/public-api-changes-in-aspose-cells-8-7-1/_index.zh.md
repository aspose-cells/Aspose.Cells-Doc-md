---
title: 公共 API Aspose.Cells 8.7.1 的变化
type: docs
weight: 240
url: /zh/net/public-api-changes-in-aspose-cells-8-7-1/
---
{{% alert color="primary" %}} 

本文档描述了 Aspose.Cells API 从版本 8.7.0 到 8.7.1 的变化，模块/应用程序开发人员可能会感兴趣。它不仅包括新的和更新的公共方法、添加和删除的类等，还包括对 Aspose.Cells 中幕后行为的任何更改的描述。

{{% /alert %}} 
## **添加的 API**
### **添加了 LookInType.OriginalValues 属性**
Aspose.Cells API 已经支持[查找或搜索数据](/cells/zh/net/find-or-search-data/)电子表格的功能，以便在单元格值和公式中找到一些特定的内容。但是，此功能缺少应用于单元格的格式方面，这可能会改变内容的外观和值，从而使文本无法使用原始值进行搜索。在此版本 Aspose.Cells API 中，名为 LookInType.OriginalValues 的另一个常量已公开给公众 API，它可以克服上述情况。

{{% alert color="primary" %}} 

有关此功能的更多详细信息，请查看详细文章[使用原始值搜索数据](/cells/zh/net/search-data-using-original-values/)

{{% /alert %}} 

以下是简单的使用场景。

**C#**

{{< highlight "csharp" >}}

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
Aspose.Cells.GridWeb for .NET 8.7.1 公开了 OnBeforeColumnFilter 事件，该事件用作对通过 GridWeb UI 完成的过滤机制的回调。顾名思义，该事件在应用列过滤之前触发，可用于获取过滤信息，例如必须应用过滤器的列索引和值。

简单的使用场景如下。

**C#**

{{< highlight "csharp" >}}

 protected void GridWeb1_ColumnFilter(object sender, Aspose.Cells.GridWeb.RowColumnEventArgs e)

{

    string msg = "Column index: " + (e.Num) + ", Filtered Value:" + e.Argument;

}

{{< /highlight >}}

{{% alert color="primary" %}} 

不要忘记将事件注册到 GridWeb 控件<acw:gridweb OnBeforeColumnFilter="GridWeb1_ColumnFilter"/>

{{% /alert %}}
