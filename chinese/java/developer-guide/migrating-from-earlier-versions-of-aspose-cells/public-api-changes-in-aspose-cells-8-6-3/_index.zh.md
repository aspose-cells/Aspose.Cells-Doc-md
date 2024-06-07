---
title: Aspose.Cells 8.6.3 中的公共API更改
type: docs
weight: 230
url: /zh/java/public-api-changes-in-aspose-cells-8-6-3/
---

{{% alert color="primary" %}} 

本文档描述了从版本 8.6.2 到 8.6.3 的 Aspose.Cells API 的更改，可能对模块/应用程序开发人员感兴趣。它不仅包括新的和更新的公共方法、添加的类，还描述了在 Aspose.Cells 后台行为中的任何更改。

{{% /alert %}} 
## **已添加API**
### **在导入数据时支持HTML解析**
这个版本的Aspose.Cells for Java API暴露了ImportTableOptions.setHtmlString属性，该属性指示API在导入数据到工作表时解析HTML标记，并将解析结果设置为单元格值。请注意，Aspose.Cells API已经提供了Cell.setHtmlString属性来执行单个单元格的此任务，但是，在批量导入数据时，如果将ImportTableOptions.setHtmlString属性设置为true，则尝试解析所有受支持的HTML标记，并将解析结果设置为相应的单元格。

这里是最简单的使用场景。

**Java**

{{< highlight csharp >}}

 //create an instance of ImportTableOptions

ImportTableOptions importOptions = new ImportTableOptions();

//Set IsHtmlString to true so that the API can parse the HTML

importOptions.setHtmlString(true);

//Import data from DataTable while passing instance of ImportTableOptions

cells.importData(iTable, 0, 0, importOptions);

{{< /highlight >}}
### **已添加 Workbook.createBuiltinStyle 方法**
Aspose.Cells for Java 8.6.3已经公开了Workbook.createBuiltinStyle方法，可用于创建与Excel应用程序提供的[内置样式](/cells/zh/java/using-built-in-styles/)之一对应的Style类对象。Workbook.createBuiltinStyle方法接受来自BuiltinStyleType枚举的常量。请注意，通过Aspose.Cells API的先前版本，同样的任务可以通过StyleCollection.createBuiltinStyle方法完成，但是由于Aspose.Cells API的最新版本已经移除了StyleCollection类，因此新公开的Workbook.createBuiltinStyle方法可视为实现相同功能的替代方法。

以下是简单的使用场景。

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

//Optionally load a spreadsheet

Workbook book = new Workbook();

//Create a built-in style of type Title

Style style = book.createBuiltinStyle(BuiltinStyleType.TITLE);

{{< /highlight >}}
### **已添加 LoadDataOption.OnlyVisibleWorksheet 属性**
Aspose.Cells for Java 8.6.3已经公开了LoadDataOption.OnlyVisibleWorksheet属性，设置为true时将影响Aspose.Cells for Java API的加载机制，结果将仅加载给定电子表格中可见的工作表。

以下是简单的使用场景。

**Java**

{{< highlight csharp >}}

 //Create an instance of LoadDataOption

LoadDataOption loadDataOptions = new LoadDataOption();

//Set OnlyVisibleWorksheet property to true

loadDataOptions.setOnlyVisibleWorksheet(true);

//Create an instance of LoadOptions

LoadOptions loadOptions = new LoadOptions();

//Set LoadDataOptions property to the instance of LoadDataOption created earlier

loadOptions.setLoadDataOptions(loadDataOptions);

//Create an instance of Workbook & load an existing spreadsheet

//while passing the instance of LoadOptions created earlier

Workbook book = new Workbook(inputFilePath, loadOptions);

{{< /highlight >}}
## **已废弃的API**
### **已废弃 Worksheet.copyConditionalFormatting 方法**
作为Worksheet.copyConditionalFormatting方法的替代方法，建议使用Cells.copyRows或Range.copy方法之一。
### **已废弃 Cells.End 属性**
请使用Cells.LastCell属性作为Cells.End属性的替代方法。
