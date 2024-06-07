---
title: Aspose.Cells 8.3.2中的公共API更改
type: docs
weight: 120
url: /zh/net/public-api-changes-in-aspose-cells-8-3-2/
---

{{% alert color="primary" %}} 

本文档描述了Aspose.Cells API从8.3.1版本到8.3.2版本的变化，可能对模块/应用程序开发人员感兴趣。它不仅包括新的和更新的公共方法、[添加的类等](/cells/zh/net/public-api-changes-in-aspose-cells-8-3-2/)和[删除的类等](/cells/zh/net/public-api-changes-in-aspose-cells-8-3-2/)，还描述了Aspose.Cells在幕后行为的任何变化

{{% /alert %}} 
## **已添加API**
### **设置PivotItem绝对位置的机制**
为了提供[PivotItem的绝对定位特性](/cells/zh/net/specifying-the-absolute-position-of-the-pivot-item/)，Aspose.Cells for .NET 8.3.2已公开了一系列属性和辅助方法，如下所列

- PivotItem.Position属性可用于指定所有PivotItems中的位置索引，而不考虑父节点。
- PivotItem.PositionInSameParentNode属性可用于指定相同父节点下的PivotItems中的位置索引。
- PivotItem.Move(int count, bool isSameParent)方法可用于根据count值向上或向下移动项目，其中count是向上或向下移动PivotItem的位置数。如果count值小于零，则将向上移动项目，如果count值大于零，则PivotItem将向下移动，布尔类型的isSameParent参数指定是否必须在同一父节点中执行移动操作。

{{% alert color="primary" %}} 

请注意，在使用PivotItem.Position、PivotItem.PositionInSameParentNode属性和PivotItem.Move(int count, bool isSameParent)方法之前，必须调用PivotTable.RefreshData和PivotTable.CalculateData方法。

{{% /alert %}} 
### **新增类SignatureLine**
Aspose.Cells for .NET 8.3.2提供对Signature Line的支持，以模仿MS Excel的等效功能。此版本的Aspose.Cells for .NET已经为此目的暴露了SignatureLine类和Picture.SignatureLine属性。

以下示例代码使用Picture.SignatureLine属性向工作簿添加签名行。

**C#**

{{< highlight csharp >}}

 //Create workbook object

Workbook workbook = new Workbook();

//Insert picture of your choice

int index = workbook.Worksheets[0].Pictures.Add(0, 0, "signature.jpg");

//Access picture and add signature line inside it

Picture pic = workbook.Worksheets[0].Pictures[index];

//Create signature line object

SignatureLine s = new SignatureLine();

s.Signer = "John Doe";

s.Title = "Development Lead";

s.Email = "john.doe@aspose.com";

//Assign the signature line object to Picture.SignatureLine property

pic.SignatureLine = s;

{{< /highlight >}}


### **新增了Chart.HasAxis方法**
随着版本8.3.2的发布，Aspose.Cells API提供了Chart.HasAxis(AxisType axisType, bool isPrimary)方法，用于确定图表是否具有特定的坐标轴。

以下示例代码演示了使用Chart.HasAxis方法来确定示例图表是否具有主轴、次级轴和值轴。

**C#**

{{< highlight csharp >}}

 //Create workbook object

Workbook workbook = new Workbook("source.xlsx");

//Access the first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access the chart

Chart chart = worksheet.Charts[0];

//Determine which axis exists in chart

bool ret = chart.HasAxis(AxisType.Category, true);

Console.WriteLine("Has Primary Category Axis: " + ret);

ret = chart.HasAxis(AxisType.Category, false);

Console.WriteLine("Has Secondary Category Axis: " + ret);

ret = chart.HasAxis(AxisType.Value, true);

Console.WriteLine("Has Primary Value Axis: " + ret);

ret = chart.HasAxis(AxisType.Value, false);

Console.WriteLine("Has Secondary Value Axis: " + ret);

{{< /highlight >}}


### **新增 WorkbookSettings.CheckWriteProtectedPassword 方法**
方法WorkbookSettings.CheckWriteProtectedPassword使开发人员能够检查给定用于修改电子表格的密码是否正确。

**C#**

{{< highlight csharp >}}

 //Specify password to open inside the load options

LoadOptions opts = new LoadOptions();

opts.Password = "1234";

//Open the source Excel file with load options

Workbook workbook = new Workbook("Book1.xlsx", opts);

//Check if 567 is Password to modify

bool ret = workbook.CheckWriteProtectedPassword("567");

Console.WriteLine("Is 567 correct Password to modify: " + ret);

{{< /highlight >}}


### **新增方法WorkbookRender.ToPrinter和SheetRender.ToPrinter**
Aspose.Cells for .NET 8.3.2提供了WorkbookRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount)和SheetRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount)方法，用于分别打印工作簿和工作表的页面范围。

以下示例代码说明了如何使用上述方法打印工作簿和工作表的第2-5页。

**C#**

{{< highlight csharp >}}

 //Create workbook from source Excel file

Workbook workbook = new Workbook("source.xlsx");

//Print the workbook specifying the range of pages

//Here we are printing pages 2-5

WorkbookRender wr = new WorkbookRender(workbook, new ImageOrPrintOptions());

wr.ToPrinter(printerName, 1, 4);

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Print the worksheet specifying the range of pages

//Here we are printing pages 2-5

SheetRender sr = new SheetRender(worksheet, new ImageOrPrintOptions());

sr.ToPrinter(printerName, 1, 4);

{{< /highlight >}}


### **新增 Worksheet.RefreshPivotTables 方法**
新增方法Worksheet.RefreshPivotTables允许一次刷新给定电子表格中的所有数据透视表。

**C#**

{{< highlight csharp >}}

 worksheet.RefreshPivotTables();

{{< /highlight >}}


### **新增 Workbook.GetNamedStyle 方法**
Aspose.Cells for .NET API公开了接受字符串作为参数的Workbook.GetNamedStyle方法，并根据传递的参数返回Style对象。
### **新增 Cells.ImportTwoDimensionArray 方法**
Aspose.Cells for .NET API通过公开Cells.ImportTwoDimensionArray(object[,], object[,], int, int, TxtLoadOptions)方法，实现了将二维数组导入到电子表格单元格中。该方法将数据的二维数组导入到工作表中，并支持在TxtLoadOptions中定义更灵活的选项。
### **添加了OnePagePerSheet、PageIndex和PageCount属性**
Aspose.Cells for .NET 8.3.2为XpsSaveOptions类公开了属性OnePagePerSheet、PageIndex和PageCount。用户可以使用OnePagePerSheet属性将电子表格的所有内容适配到XPS的单个页面上，并使用PageCount属性检索要打印的页面数。PageIndex属性获取/设置要保存的第一个页面的基于0的索引。
### **添加了NumberDecimalSeparator和NumberGroupSeparator属性**
Aspose.Cells for .NET 8.3.2引入了NumberDecimalSeparator和NumberGroupSeparator属性，可以用于格式化和解析电子表格中的数字值的自定义分隔符。

以下示例代码说明了如何使用Aspose.Cells API指定自定义分隔符。以下代码将自定义的Decimal和Group分隔符分别指定为点和空格。

**C#**

{{< highlight csharp >}}

 Workbook workbook = new Workbook();

//Specify custom separators

workbook.Settings.NumberDecimalSeparator = '.';

workbook.Settings.NumberGroupSeparator = ' ';

{{< /highlight >}}


### **新增 PdfSaveOptions.IsFontSubstitutionCharGranularity 属性**
Aspose.Cells for .NET 8.3.2为PdfSaveOptions.IsFontSubstitutionCharGranularity属性提供了访问权限，以解决某些Unicode字符使用特定字体族无法显示的问题。当PdfSaveOptions.IsFontSubstitutionCharGranularity属性设置为true时，只有无法显示的特定字符的字体将更改为可显示的字体，剩余的单词或句子应保持在原始字体中。

**C#**

{{< highlight csharp >}}

 //Save to Pdf after setting PdfSaveOptions.IsFontSubstitutionCharGranularity to true

PdfSaveOptions opts = new PdfSaveOptions();

opts.IsFontSubstitutionCharGranularity = true;

{{< /highlight >}}


## **已删除APIs**
### **已移除的已过时方法**
以下方法已从公共API中移除。

- Workbook.Open和Workbook.Save方法。
- Workbook.SetOleSize方法。
- Workbook.LoadData方法。
- WorkbookDesigner.Open和WorkbookDesigner.Save方法。
- WorksheetCollection.DeleteName方法。
### **已移除的已过时属性**
以下属性已从公共API中移除。

- Workbook.IsProtected属性。
- Workbook.Language 属性。
- Workbook.Region 属性。
- WorkbookSettings.ReCalcOnOpen 属性。
- WorkbookSettings.Language 属性。
- WorkbookSettings.Encoding 属性。
- WorkbookSettings.ConvertNumericData 属性。
- WorksheetCollection.HidePivotFieldList 属性。
- WorksheetCollection.EnableHTTPCompression 属性。
- WorksheetCollection.IsMinimized 属性。
- WorksheetCollection.IsHidden 属性。
- WorksheetCollection.SheetTabBarWidth 属性。
- WorksheetCollection.WindowLeft 属性。
- WorksheetCollection.WindowLeftInch 属性。
- WorksheetCollection.WindowLeftCM 属性。
- WorksheetCollection.WindowTop 属性。
- WorksheetCollection.WindowTopInch 属性。
- WorksheetCollection.WindowTopCM 属性。
- WorksheetCollection.WindowWidth 属性。
- WorksheetCollection.WindowWidthInch 属性。
- WorksheetCollection.WindowWidthCM 属性。
- WorksheetCollection.WindowHeight 属性。
- WorksheetCollection.WindowHeightInch 属性。
- WorksheetCollection.WindowHeightCM 属性。
- Worksheet.HPageBreaks 属性。
- Worksheet.VPageBreaks 属性。
- HtmlSaveOptions.DisplayHTMLCrossString 属性。
- HtmlSaveOptions.ExportChartImageFormat 属性。
- SaveOptions.ExpCellNameToXLSX 属性。
- SaveOptions.DefaultFont 属性。
- SaveOptions.Compliance 属性。
- SaveOptions.PdfBookmark 属性。
- SaveOptions.PdfImageCompression 属性。
- TxtSaveOptions.AlwaysQuoted 属性。
## **已弃用的API**
### **已弃用 Workbook.SaveOptions 属性**
在设置适当的 SaveOptions 属性后，必须将 SaveOptions 对象传递给 Workbook.Save 方法。
### **已弃用 Workbook.Styles 属性 和 类 StyleCollection**
建议使用 Workbook.CreateStyle 方法为 Workbook 实例创建和操纵样式，而不是使用 StyleCollection.Add 方法创建样式。此外，可以使用 Workbook.GetNamedStyle(string) 方法获取命名样式，而不是使用 StyleCollection[string]。
### **已弃用 PivotItem.Move(int count) 方法**
随着 Aspose.Cells 8.3.2 的发布，该 API 引入了另一个重载的 PivotItem.Move 方法，接受整数参数作为计数，并接受布尔参数将 PivotItem 移动到父节点内。
