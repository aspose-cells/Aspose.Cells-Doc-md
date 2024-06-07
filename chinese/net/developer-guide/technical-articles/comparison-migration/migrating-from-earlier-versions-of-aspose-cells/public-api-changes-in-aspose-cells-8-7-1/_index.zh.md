---
title: Aspose.Cells 8.7.1的公共API变更
type: docs
weight: 240
url: /zh/net/public-api-changes-in-aspose-cells-8-7-1/
---

{{% alert color="primary" %}} 

此文档描述了从版本8.7.0到8.7.1的Aspose.Cells API的更改，这可能会对模块/应用程序开发人员感兴趣。它不仅包括新的和更新的公共方法、添加和删除的类等，还包括对Aspose.Cells后台行为的任何更改的描述。

{{% /alert %}} 
## **已添加API**
### **添加LookInType.OriginalValues属性**
Aspose.Cells APIs已经支持电子表格的查找或搜索数据功能，以查找单元格值和公式中的特定内容。

{{% alert color="primary" %}} 

有关此功能的更多详情，请查看关于使用原始值搜索数据的详细文章。

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


### **为GridWeb添加了OnBeforeColumnFilter事件**
Aspose.Cells.GridWeb for .NET 8.7.1已公开了OnBeforeColumnFilter事件，它作为通过GridWeb UI完成的过滤机制的回调。正如名称所示，该事件在应用列过滤之前触发，可用于获取过滤信息，如必须应用过滤的列索引和值。

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
