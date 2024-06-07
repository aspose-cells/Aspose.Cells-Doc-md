---
title: Aspose.Cells 8.6.3 中的公共API更改
type: docs
weight: 220
url: /zh/net/public-api-changes-in-aspose-cells-8-6-3/
---

{{% alert color="primary" %}} 

本文档描述了从版本 8.6.2 到 8.6.3 的 Aspose.Cells API 的更改，可能对模块/应用程序开发人员感兴趣。它不仅包括新的和更新的公共方法、添加的类，还描述了在 Aspose.Cells 后台行为中的任何更改。

{{% /alert %}} 
## **已添加API**
### **在导入数据时支持HTML解析**
此版本的Aspose.Cells for .NET API已暴露了ImportTableOptions.IsHtmlString属性，该属性在将数据导入工作表时指示API解析HTML标记，并将解析结果设置为单元格值。请注意，Aspose.Cells API已经提供了Cell.HtmlString来执行此任务适用于单个单元格；然而，在批量导入数据时，例如从DataTable中导入数据时，ImportTableOptions.IsHtmlString属性（设置为true时）尝试解析所有支持的HTML标记，并将解析结果设置为相应的单元格。

这里是最简单的使用场景。

**C#**

{{< highlight csharp >}}

 //create an instance of ImportTableOptions

var importOptions = new ImportTableOptions();

//Set IsHtmlString to true so that the API can parse the HTML

importOptions.IsHtmlString = true;

//Import data from DataTable while passing instance of ImportTableOptions

cells.ImportData(table, 0, 0, importOptions);

{{< /highlight >}}


### **添加Workbook.CreateBuiltinStyle方法**
Aspose.Cells for .NET 8.6.3公开了Workbook.CreateBuiltinStyle方法，可用于创建与Excel应用程序提供的内置样式之一对应的Style类对象。

以下是简单的使用场景。

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook

//Optionally load a spreadsheet

var book = new Workbook();

//Create a built-in style of type Title

var style = book.CreateBuiltinStyle(BuiltinStyleType.Title);

{{< /highlight >}}


### **添加Cells.ImportGridView方法**
Aspose.Cells for .NET 8.6.3已暴露了Cells.ImportGridView的重载版本，现在可以接受一个ImportTableOptions的实例，从而更好地控制导入过程。

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


### **添加ImportTableOptions.ConvertGridStyle属性**
关于上述提到的增强功能，Aspose.Cells for .NET API的最新版本还暴露了ImportTableOptions.ConvertGridStyle属性。该布尔类型属性允许开发人员控制导入数据的外观，设置ImportTableOptions.ConvertGridStyle属性为true表示API将应用GridView的样式到已导入数据的单元格。

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


### **已添加属性LoadDataOption.OnlyVisibleWorksheet**
Aspose.Cells for .NET 8.6.3已暴露了LoadDataOption.OnlyVisibleWorksheet属性，将其设置为true将影响Aspose.Cells for .NET API的加载机制，因此只会加载给定电子表格中的可见工作表。请查看关于此主题的详细文章。

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
## **已废弃的API**
### **已弃用Worksheet.CopyConditionalFormatting方法**
建议使用Cells.CopyRows或Range.Copy方法替代Worksheet.CopyConditionalFormatting方法。
### **已废弃 Cells.End 属性**
请使用Cells.LastCell属性作为Cells.End属性的替代方法。
