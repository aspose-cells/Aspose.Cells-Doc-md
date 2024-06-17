---
title: Aspose.Cells 8.6.3的公共API更改
type: docs
weight: 230
url: /zh/java/public-api-changes-in-aspose-cells-8-6-3/
---

{{% alert color="primary" %}} 

此文档描述了从版本8.6.2到8.6.3的Aspose.Cells API中的更改，这可能对模块/应用程序开发人员感兴趣。它不仅包括新的和更新的公共方法、添加的类，还包括Aspose.Cells后台行为的任何更改的描述。

{{% /alert %}} 
## **添加的 API**
### **导入数据时支持HTML解析**
Aspose.Cells for Java API的此版本已公开了ImportTableOptions.setHtmlString属性，该属性指示API在导入数据到工作表时解析HTML标记，并将解析后的结果设置为单元格值。请注意，Aspose.Cells API已经提供了Cell.setHtmlString属性来执行此任务，但是在批量导入数据时，ImportTableOptions.setHtmlString属性（设置为true）会尝试解析所有支持的HTML标记，并将解析后的结果设置到相应的单元格。

这是最简单的使用场景。

**Java**

{{< highlight csharp >}}

 //create an instance of ImportTableOptions

ImportTableOptions importOptions = new ImportTableOptions();

//Set IsHtmlString to true so that the API can parse the HTML

importOptions.setHtmlString(true);

//Import data from DataTable while passing instance of ImportTableOptions

cells.importData(iTable, 0, 0, importOptions);

{{< /highlight >}}
### **添加了Workbook.createBuiltinStyle方法**
Aspose.Cells for Java 8.6.3已公开了Workbook.createBuiltinStyle方法，可用于创建与Excel应用程序提供的[内置样式](/cells/zh/java/using-built-in-styles/)之一对应的Style类的对象。Workbook.createBuiltinStyle方法接受来自枚举BuiltinStyleType的常量。请注意，以前的Aspose.Cells API版本可以通过StyleCollection.createBuiltinStyle方法完成同样的任务，但是随着最新版本的Aspose.Cells API移除了StyleCollection类，因此新公开的Workbook.createBuiltinStyle方法可以被视为实现相同任务的替代方法。

以下是简单的使用场景。

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

//Optionally load a spreadsheet

Workbook book = new Workbook();

//Create a built-in style of type Title

Style style = book.createBuiltinStyle(BuiltinStyleType.TITLE);

{{< /highlight >}}
### **添加了LoadDataOption.OnlyVisibleWorksheet属性**
Aspose.Cells for Java 8.6.3已公开了LoadDataOption.OnlyVisibleWorksheet属性，设置为true时将影响Aspose.Cells for Java API的加载机制，结果只会加载给定电子表格中的可见工作表。

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
## **已弃用的API**
### **已弃用Worksheet.copyConditionalFormatting方法**
建议使用任何一个Cells.copyRows或Range.copy方法作为Worksheet.copyConditionalFormatting方法的替代方法。
### **已弃用Cells.End属性**
请使用Cells.LastCell属性作为Cells.End属性的替代方法。
