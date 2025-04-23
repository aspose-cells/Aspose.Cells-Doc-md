---
title: Aspose.Cells 8.6.3的公共API更改
type: docs
weight: 220
url: /zh/net/public-api-changes-in-aspose-cells-8-6-3/
---

{{% alert color="primary" %}} 

此文档描述了从版本8.6.2到8.6.3的Aspose.Cells API中的更改，这可能对模块/应用程序开发人员感兴趣。它不仅包括新的和更新的公共方法、添加的类，还包括Aspose.Cells后台行为的任何更改的描述。

{{% /alert %}} 
## **添加的 API**
### **导入数据时支持HTML解析**
此版本的Aspose.Cells for .NET API已公开了ImportTableOptions.IsHtmlString属性，该属性指示API在导入数据到工作表时解析HTML标记，并将解析的结果设置为单元格值。请注意，Aspose.Cells API已提供Cell.HtmlString来执行此任务以单个单元格为单位，但是在大量导入数据时（例如从DataTable中），ImportTableOptions.IsHtmlString属性（设置为true时）尝试解析所有支持的HTML标记，并将解析结果设置为相应的单元格。

这是最简单的使用场景。

**C#**

{{< highlight csharp >}}

 //create an instance of ImportTableOptions

var importOptions = new ImportTableOptions();

//Set IsHtmlString to true so that the API can parse the HTML

importOptions.IsHtmlString = true;

//Import data from DataTable while passing instance of ImportTableOptions

cells.ImportData(table, 0, 0, importOptions);

{{< /highlight >}}


### **新增 Workbook.CreateBuiltinStyle 方法**
Aspose.Cells for .NET 8.6.3已公开了Workbook.CreateBuiltinStyle方法，该方法可用于创建与Excel应用程序提供的[内置样式](/cells/zh/net/using-built-in-styles/)之一对应的Style类对象。Workbook.CreateBuiltinStyle方法接受枚举BuiltinStyleType的常量。请注意，通过Aspose.Cells API的以前版本，可以通过StyleCollection.CreateBuiltinStyle方法完成相同的任务，但是由于Aspose.Cells API的最新版本已删除了StyleCollection类，因此新公开的Workbook.CreateBuiltinStyle方法可以被视为实现相同目的的替代方法。

以下是简单的使用场景。

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook

//Optionally load a spreadsheet

var book = new Workbook();

//Create a built-in style of type Title

var style = book.CreateBuiltinStyle(BuiltinStyleType.Title);

{{< /highlight >}}


### **新增 Cells.ImportGridView 方法**
Aspose.Cells for .NET 8.6.3已公开了Cells.ImportGridView的重载版本，现在可以接受一个ImportTableOptions实例，以便更好地控制导入过程。

以下是简单的使用场景。

**C#**

{{< highlight csharp >}}

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


### **新增 ImportTableOptions.ConvertGridStyle 属性**
关于上述增强功能，Aspose.Cells for .NET API的最新版本还公开了ImportTableOptions.ConvertGridStyle属性。这个布尔类型属性允许开发人员控制导入数据的外观，将ImportTableOptions.ConvertGridStyle属性设置为true表示API将应用GridView的样式到已导入数据的单元格。

以下是简单的使用场景。

**C#**

{{< highlight csharp >}}

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


### **新增 LoadDataOption.OnlyVisibleWorksheet 属性**
Aspose.Cells for .NET 8.6.3已公开了LoadDataOption.OnlyVisibleWorksheet属性，将其设置为true会影响Aspose.Cells for .NET API的加载机制，结果只会加载给定电子表格中可见的工作表。请查阅[详细文章](/cells/zh/net/different-ways-to-open-files/)以获取更多信息。

以下是简单的使用场景。

**C#**

{{< highlight csharp >}}

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
## **已弃用的API**
### **Obsolete Worksheet.CopyConditionalFormatting 方法**
作为 Worksheet.CopyConditionalFormatting 方法的替代方案，建议使用 Cells.CopyRows 或 Range.Copy 方法之一。
### **已弃用Cells.End属性**
请使用Cells.LastCell属性作为Cells.End属性的替代方法。
{{< app/cells/assistant language="csharp" >}}
