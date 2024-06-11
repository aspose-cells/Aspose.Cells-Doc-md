---
title: Aspose.Cells 8.3.2中的公共API更改
type: docs
weight: 120
url: /zh/net/public-api-changes-in-aspose-cells-8-3-2/
---

{{% alert color="primary" %}} 

本文档描述了Aspose.Cells API从版本8.3.1到8.3.2的变化，可能会对模块/应用程序开发人员感兴趣。它不仅包括新的和更新的公共方法，[已添加的类等](/cells/zh/net/public-api-changes-in-aspose-cells-8-3-2/)和[已删除的类等](/cells/zh/net/public-api-changes-in-aspose-cells-8-3-2/)，还描述了Aspose.Cells背后的行为的任何更改。

{{% /alert %}} 
## **添加的 API**
### **设置PivotItem的绝对位置的机制**
为了提供[PivotItem的绝对定位特性](/cells/zh/net/specifying-the-absolute-position-of-the-pivot-item/)，Aspose.Cells for .NET 8.3.2已公开了一系列属性和辅助方法，如下所列。

- PivotItem.Position属性可用于指定所有PivotItems中的位置索引，而不考虑父节点。
- PivotItem.PositionInSameParentNode属性可用于指定同一父节点下的PivotItems的位置索引。
- PivotItem.Move(int count, bool isSameParent)方法可用于根据计数值上移或下移项目，其中计数是要将PivotItem上移或下移的位置数。如果计数值小于零，项目将向上移动，而如果计数值大于零，PivotItem将向下移动，布尔类型的isSameParent参数指定是否在同一父节点中执行移动操作。

{{% alert color="primary" %}} 

请注意，在使用PivotItem.Position、PivotItem.PositionInSameParentNode属性和PivotItem.Move(int count, bool isSameParent)方法之前，有必要调用PivotTable.RefreshData和PivotTable.CalculateData方法。

{{% /alert %}} 
### **添加了类 SignatureLine**
Aspose.Cells for .NET 8.3.2提供了支持签名线来模拟MS Excel的等效功能。这个版本的Aspose.Cells for .NET已经公开了SignatureLine类和Picture.SignatureLine属性以实现这一目的。

以下示例代码使用 Picture.SignatureLine 属性向工作簿添加了签名行。

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


### **新增Chart.HasAxis方法**
随着v8.3.2的发布，Aspose.Cells API提供了Chart.HasAxis(AxisType axisType, bool isPrimary)方法，确定图表是否有特定轴。

以下示例代码演示了使用Chart.HasAxis方法来确定样本图表是否具有主轴、次要轴和值轴。

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


### **添加了WorkbookSettings.CheckWriteProtectedPassword方法**
WorkbookSettings.CheckWriteProtectedPassword方法使开发人员能够检查修该电子表格的给定密码是否正确。

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


### **添加了重载方法WorkbookRender.ToPrinter和SheetRender.ToPrinter**
Aspose.Cells for .NET 8.3.2已提供了WorkbookRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount)和SheetRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount)方法，用于分别打印工作簿和工作表的页面范围。

以下示例代码说明了上述方法的用法，以打印工作簿和工作表的页面 2-5。

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


### **添加了Worksheet.RefreshPivotTables方法**
新添加的Worksheet.RefreshPivotTables方法可以在一次调用中刷新给定电子表格中的所有数据透视表。

**C#**

{{< highlight csharp >}}

 worksheet.RefreshPivotTables();

{{< /highlight >}}


### **添加了Workbook.GetNamedStyle方法**
Aspose.Cells for .NET API公开了Workbook.GetNamedStyle方法，接受字符串作为参数，并根据传递的参数检索Style对象。
### **添加了Cells.ImportTwoDimensionArray方法**
Aspose.Cells for .NET API通过公开Cells.ImportTwoDimensionArray(object[,], object[,], int, int, TxtLoadOptions)方法，使得可以将二维数组导入到电子表格单元格中。所述方法将数据的二维数组导入到工作表中，并且具有在TxtLoadOptions中定义的更灵活的选项。
### **新增了OnePagePerSheet、PageIndex和PageCount属性**
Aspose.Cells for .NET 8.3.2已为XpsSaveOptions类公开了OnePagePerSheet、PageIndex和PageCount属性。用户可以使用OnePagePerSheet属性将电子表格的所有内容适合XPS的单个页面上，并/或使用PageCount属性检索要打印的页数。PageIndex属性获取/设置要保存的第一页的从0开始的索引。
### **添加了 NumberDecimalSeparator 和 NumberGroupSeparator 属性**
Aspose.Cells for .NET 8.3.2已引入了NumberDecimalSeparator和NumberGroupSeparator属性，可获取/设置用于格式化和解析电子表格中的数值的自定义分隔符。

以下示例代码演示了如何使用Aspose.Cells API指定自定义分隔符。以下代码将自定义的小数和分组分隔符分别指定为点和空格。

**C#**

{{< highlight csharp >}}

 Workbook workbook = new Workbook();

//Specify custom separators

workbook.Settings.NumberDecimalSeparator = '.';

workbook.Settings.NumberGroupSeparator = ' ';

{{< /highlight >}}


### **添加了PdfSaveOptions.IsFontSubstitutionCharGranularity属性**
Aspose.Cells for .NET 8.3.2已为PdfSaveOptions.IsFontSubstitutionCharGranularity属性提供了支持，以解决某些Unicode字符使用特定字体族无法显示的问题。当PdfSaveOptions.IsFontSubstitutionCharGranularity属性设置为true时，只有无法显示的特定字符的字体将更改为可显示的字体，其余单词或句子应保留原始字体。

**C#**

{{< highlight csharp >}}

 //Save to Pdf after setting PdfSaveOptions.IsFontSubstitutionCharGranularity to true

PdfSaveOptions opts = new PdfSaveOptions();

opts.IsFontSubstitutionCharGranularity = true;

{{< /highlight >}}


## **删除了 API**
### **删除了已弃用的方法**
以下方法已从公共 API 中删除。

- Workbook.Open 和 Workbook.Save 方法。
- Workbook.SetOleSize 方法。
- Workbook.LoadData 方法。
- WorkbookDesigner.Open 和 WorkbookDesigner.Save 方法。
- WorksheetCollection.DeleteName 方法。
### **删除了已弃用的属性**
以下属性已从公共 API 中删除。

- Workbook.IsProtected 属性。
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
## **弃用的API**
### **已弃用的 Workbook.SaveOptions 属性**
在设置适当的 SaveOptions 属性后，应将 SaveOptions 对象传递给 Workbook.Save 方法。
### **已弃用的 Workbook.Styles 属性和 Class StyleCollection**
建议使用 Workbook.CreateStyle 方法为 Workbook 实例创建和操作样式，而不是使用 StyleCollection.Add 方法创建样式。此外，建议使用 Workbook.GetNamedStyle(string) 方法来获取命名样式，而不是使用 StyleCollection[string]。
### **已弃用的 PivotItem.Move(int count) 方法**
随着 Aspose.Cells 8.3.2 的发布，API 引入了 PivotItem.Move 方法的另一个重载，该方法接受整数参数用于计数和布尔参数用于在父节点内移动 PivotItem。
