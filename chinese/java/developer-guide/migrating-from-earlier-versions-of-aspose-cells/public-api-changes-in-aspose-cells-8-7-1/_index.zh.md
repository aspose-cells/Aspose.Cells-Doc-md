---
title: Aspose.Cells 8.7.1的公共API变更
type: docs
weight: 250
url: /zh/java/public-api-changes-in-aspose-cells-8-7-1/
---

{{% alert color="primary" %}} 

此文档描述了从版本8.7.0到8.7.1的Aspose.Cells API的更改，这可能会对模块/应用程序开发人员感兴趣。它不仅包括新的和更新的公共方法、添加和删除的类等，还包括对Aspose.Cells后台行为的任何更改的描述。

{{% /alert %}} 
## **已添加API**
### **新增了LookInType.ORIGINAL_VALUES属性**
Aspose.Cells APIs已经支持[查找或搜索数据](/cells/zh/java/find-or-search-data/)功能，以便在电子表格中找到特定内容的内容和公式。然而，该功能缺乏应用到单元格上的格式的方面，该格式可能改变内容的外观和值，从而使原始值变得不可搜索。通过Aspose.Cells APIs的此次发布，另一个名称为LookInType.ORIGINAL_VALUES的常量已经暴露到公共API中，它允许克服上述情况。 

{{% alert color="primary" %}} 

有关此功能的更多详细信息，请查看[使用原始值搜索数据](https://docs.aspose.com/cells/java/search-data-using-original-values/)的详细文章。

{{% /alert %}} 

以下是简单的使用场景。

**Java**

{{< highlight csharp >}}

 //Create workbook object

Workbook workbook = new Workbook();

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Add 10 in cell A1 and A2

worksheet.getCells().get("A1").putValue(10);

worksheet.getCells().get("A2").putValue(10);

//Add Sum formula in cell D4 but customize it as ---

Cell cell = worksheet.getCells().get("D4");

Style style = cell.getStyle();

style.setCustom("---");

cell.setStyle(style);

//The result of formula will be 20

//but 20 will not be visible because

//the cell is formated as ---

cell.setFormula("=Sum(A1:A2)");

//Calculate the workbook

workbook.calculateFormula();

//Create find options

FindOptions options = new FindOptions();

options.setLookInType(LookInType.ORIGINAL_VALUES);

options.setLookAtType(LookAtType.ENTIRE_CONTENT);

Cell foundCell = null;

Object obj = 20;

//Find 20 which is Sum(A1:A2) and formatted as ---

foundCell = worksheet.getCells().find(obj, foundCell, options);

//Print the found cell

System.out.println(foundCell);

{{< /highlight >}}
