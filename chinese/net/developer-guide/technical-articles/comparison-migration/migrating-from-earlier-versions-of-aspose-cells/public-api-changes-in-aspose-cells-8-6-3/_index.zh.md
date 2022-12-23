---
title: 公共 API Aspose.Cells 8.6.3 的变化
type: docs
weight: 220
url: /zh/net/public-api-changes-in-aspose-cells-8-6-3/
---
{{% alert color="primary" %}} 

本文档描述了 Aspose.Cells API 从版本 8.6.2 到 8.6.3 的变化，模块/应用程序开发人员可能会感兴趣。它不仅包括新的和更新的公共方法、添加的类，还包括对 Aspose.Cells 中幕后行为的任何更改的描述。

{{% /alert %}} 
## **添加的 API**
### **支持HTML边导入数据边解析**
此版本的 Aspose.Cells for .NET API 公开了 ImportTableOptions.IsHtmlString 属性，该属性指示 API 在将数据导入工作表时解析 HTML 标记并将解析结果设置为单元格值。请注意，Aspose.Cells API 已经提供了 Cell.HtmlString 来为单个单元格执行此任务，但是，在从 DataTable 等批量导入数据时，ImportTableOptions.IsHtmlString 属性（设置为 true 时）会尝试解析所有支持的HTML 标记并将解析的结果设置到相应的单元格中。

这里是最简单的使用场景。

**C#**

{{< highlight "csharp" >}}

 //create an instance of ImportTableOptions

var importOptions = new ImportTableOptions();

//Set IsHtmlString to true so that the API can parse the HTML

importOptions.IsHtmlString = true;

//Import data from DataTable while passing instance of ImportTableOptions

cells.ImportData(table, 0, 0, importOptions);

{{< /highlight >}}


### **添加方法 Workbook.CreateBuiltinStyle**
 Aspose.Cells for .NET 8.6.3 公开了 Workbook.CreateBuiltinStyle 方法，可用于创建对应于其中一个的 Style 类的对象[Excel 应用程序提供的内置样式](/cells/zh/net/using-built-in-styles/)Workbook.CreateBuiltinStyle 方法接受来自枚举 BuiltinStyleType 的常量。请注意，对于以前版本的 Aspose.Cells API，可以通过 StyleCollection.CreateBuiltinStyle 方法完成相同的任务，但由于最近版本的 Aspose.Cells API 已经删除了 StyleCollection 类，因此新公开的 Workbook.CreateBuiltinStyle 方法可以被视为替代方法达到同样的效果。

以下是简单的使用场景。

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

//Optionally load a spreadsheet

var book = new Workbook();

//Create a built-in style of type Title

var style = book.CreateBuiltinStyle(BuiltinStyleType.Title);

{{< /highlight >}}


### **方法 Cells.ImportGridView 添加**
Aspose.Cells for .NET 8.6.3 公开了 Cells.ImportGridView 的重载版本，现在可以接受 ImportTableOptions 的实例以更好地控制导入过程。

以下是简单的使用场景。

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

//Optionally load a spreadsheet

var book = new Workbook();

//Retrieve the Cells collection of first Worksheet in Workbook

var cells = book.Worksheets[0].Cells;

//create an instance of ImportTableOptions & set its various properties

var importOptions = new ImportTableOptions();

importOptions.IsHtmlString = true;

importOptions.IsFieldNameShown = true;

//Import data from GridView while passing instance of ImportTableOptions

cells.ImportGridView(gridView, 0, 0, importOptions);

{{< /highlight >}}


### **已添加属性 ImportTableOptions.ConvertGridStyle**
参考上述增强功能，最新版本 Aspose.Cells for .NET API 也暴露了 ImportTableOptions.ConvertGridStyle 属性。此布尔类型属性允许开发人员控制导入数据的外观，其中将 ImportTableOptions.ConvertGridStyle 属性设置为 true 表示 API 会将 GridView 的样式应用于已导入数据的单元格。

以下是简单的使用场景。

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

//Optionally load a spreadsheet

var book = new Workbook();

//Retrieve the Cells collection of first Worksheet in Workbook

var cells = book.Worksheets[0].Cells;

//create an instance of ImportTableOptions

var importOptions = new ImportTableOptions();

//Set ConvertGridStyle property to true

importOptions.ConvertGridStyle = true;



//Import data from GridView while passing instance of ImportTableOptions

cells.ImportGridView(gridView, 0, 0, importOptions);

{{< /highlight >}}


### **属性 LoadDataOption.OnlyVisibleWorksheet 添加**
 Aspose.Cells for .NET 8.6.3 公开了 LoadDataOption.OnlyVisibleWorksheet 属性，该属性在设置为 true 时会影响 Aspose.Cells for .NET API 的加载机制，因此只会加载给定电子表格中的可见工作表。请检查[详细文章](/cells/zh/net/different-ways-to-open-files/)关于这个问题。

以下是简单的使用场景。

**C#**

{{< highlight "csharp" >}}

 //Create an instance of LoadDataOption

var loadDataOptions = new LoadDataOption();

//Set OnlyVisibleWorksheet property to true

loadDataOptions.OnlyVisibleWorksheet = true;

//Create an instance of LoadOptions

var loadOptions = new LoadOptions();

//Set LoadDataOptions property to the instance of LoadDataOption created earlier

loadOptions.LoadDataOptions = loadDataOptions;



//Create an instance of Workbook & load an existing spreadsheet

//while passing the instance of LoadOptions created earlier

var book = new Workbook(inputFilePath, loadOptions);

{{< /highlight >}}
## **过时的 API**
### **方法 Worksheet.CopyConditionalFormatting 已废弃**
作为 Worksheet.CopyConditionalFormatting 方法的替代方法，建议使用任何 Cells.CopyRows 或 Range.Copy 方法。
### **财产 Cells.End 废弃**
请使用 Cells.LastCell 属性替代 Cells.End 属性。
