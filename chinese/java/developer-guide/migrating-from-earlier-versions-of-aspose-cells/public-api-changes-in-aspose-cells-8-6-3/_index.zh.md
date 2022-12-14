---
title: 公共 API Aspose.Cells 8.6.3 的变化
type: docs
weight: 230
url: /zh/java/public-api-changes-in-aspose-cells-8-6-3/
---
{{% alert color="primary" %}} 

本文档描述了 Aspose.Cells API 从版本 8.6.2 到 8.6.3 的变化，模块/应用程序开发人员可能会感兴趣。它不仅包括新的和更新的公共方法、添加的类，还包括对 Aspose.Cells 中幕后行为的任何更改的描述。

{{% /alert %}} 
## **添加的 API**
### **导入数据时支持 HTML 解析**
此版本 Aspose.Cells for Java API 公开了 ImportTableOptions.setHtmlString 属性，该属性指示 API 在将数据导入工作表时解析 HTML 标记，并将解析结果设置为单元格值。请注意，Aspose.Cells API 已经提供了 Cell.setHtmlString 属性来为单个单元格执行此任务，但是，在批量导入数据时，ImportTableOptions.setHtmlString 属性（设置为 true 时）会尝试解析所有支持的 HTML 标签和集解析结果到相应的单元格。

这里是最简单的使用场景。

**Java**

{{< highlight "csharp" >}}

 //create an instance of ImportTableOptions

ImportTableOptions importOptions = new ImportTableOptions();

//Set IsHtmlString to true so that the API can parse the HTML

importOptions.setHtmlString(true);

//Import data from DataTable while passing instance of ImportTableOptions

cells.importData(iTable, 0, 0, importOptions);

{{< /highlight >}}
### **添加方法 Workbook.createBuiltinStyle**
Aspose.Cells for Java 8.6.3 公开了 Workbook.createBuiltinStyle 方法，可用于创建对应于其中一个的 Style 类的对象[Excel 应用程序提供的内置样式](/cells/zh/java/using-built-in-styles/)Workbook.createBuiltinStyle 方法接受来自枚举 BuiltinStyleType 的常量。请注意，对于以前版本的 Aspose.Cells API，可以通过 StyleCollection.createBuiltinStyle 方法完成相同的任务，但由于最近版本的 Aspose.Cells API 已经删除了 StyleCollection 类，因此新公开的 Workbook.createBuiltinStyle 方法可以被视为替代方法达到同样的效果。

以下是简单的使用场景。

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

//Optionally load a spreadsheet

Workbook book = new Workbook();

//Create a built-in style of type Title

Style style = book.createBuiltinStyle(BuiltinStyleType.TITLE);

{{< /highlight >}}
### **属性 LoadDataOption.OnlyVisibleWorksheet 添加**
Aspose.Cells for Java 8.6.3 公开了 LoadDataOption.OnlyVisibleWorksheet 属性，该属性在设置为 true 时会影响 Aspose.Cells for Java API 的加载机制，因此只会加载给定电子表格中的可见工作表。

以下是简单的使用场景。

**Java**

{{< highlight "csharp" >}}

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
## **过时的 API**
### **方法 Worksheet.copyConditionalFormatting 已废弃**
作为 Worksheet.copyConditionalFormatting 方法的替代方法，建议使用任何 Cells.copyRows 或 Range.copy 方法。
### **财产 Cells.End 废弃**
请使用 Cells.LastCell 属性替代 Cells.End 属性。
