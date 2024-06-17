---
title: Aspose.Cells 8.7.1 中的公共 API 更改
type: docs
weight: 250
url: /zh/java/public-api-changes-in-aspose-cells-8-7-1/
---

{{% alert color="primary" %}} 

本文档描述了从版本 8.7.0 到 8.7.1 的 Aspose.Cells API 中的更改，这可能对模块/应用程序开发人员感兴趣。它不仅包括新的和更新的公共方法，添加和删除的类等，还包括了 Aspose.Cells 后台行为的任何更改的描述。

{{% /alert %}} 
## **添加的 API**
### **添加了 LookInType.ORIGINAL_VALUES 属性**
Aspose.Cells API已经支持电子表格的[查找或搜索数据](/cells/zh/java/find-or-search-data/)功能，以便在单元格值和公式中找到特定内容。但是，此功能缺乏应用于可能更改内容外观和值的单元格的格式方面，因此可能导致使用原始值无法搜索文本。通过此次Aspose.Cells API的发布，将另一个名为LookInType.ORIGINAL_VALUES的常量暴露给公共API，允许克服上述情况。 

{{% alert color="primary" %}} 

有关此功能的更多详细信息，请查看有关[使用原始值搜索数据](https://docs.aspose.com/cells/java/search-data-using-original-values/)的详细文章。

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
