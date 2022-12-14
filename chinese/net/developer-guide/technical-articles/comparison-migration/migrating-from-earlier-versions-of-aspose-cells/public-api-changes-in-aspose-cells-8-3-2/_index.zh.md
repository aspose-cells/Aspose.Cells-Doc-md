---
title: 公共 API Aspose.Cells 8.3.2 的变化
type: docs
weight: 120
url: /zh/net/public-api-changes-in-aspose-cells-8-3-2/
---
{{% alert color="primary" %}} 

本文档描述了 Aspose.Cells API 从版本 8.3.1 到 8.3.2 的变化，模块/应用程序开发人员可能会感兴趣。它不仅包括新的和更新的公共方法，[添加类等](/cells/zh/net/public-api-changes-in-aspose-cells-8-3-2/)和[删除的类等](/cells/zh/net/public-api-changes-in-aspose-cells-8-3-2/)还描述了 Aspose.Cells 中幕后行为的任何变化。

{{% /alert %}} 
## **添加的 API**
### **设置 PivotItem 绝对位置的机制**
为了提供功能[PivotItem 的绝对定位](/cells/zh/net/specifying-the-absolute-position-of-the-pivot-item/)Aspose.Cells for .NET 8.3.2暴露了一系列的属性和帮助方法如下。

- PivotItem.Position 属性可用于指定所有 PivotItem 中的位置索引，而不考虑父节点。
- PivotItem.PositionInSameParentNode 属性可用于指定同一父节点下的 PivotItems 中的位置索引。
- PivotItem.Move(int count, bool isSameParent) 方法可用于根据计数值向上或向下移动项目，其中计数是将 PivotItem 向上或向下移动的位置数。如果计数值小于零，item将向上移动，如果计数值大于零，则PivotItem将向下移动，布尔类型isSameParent参数指定是否必须在同一父节点进行移动操作或不。

{{% alert color="primary" %}} 

请注意，在使用 PivotItem.Position、PivotItem.PositionInSameParentNode 属性和 PivotItem.Move(int count, bool isSameParent) 方法之前，有必要调用 PivotTable.RefreshData 和 PivotTable.CalculateData 方法。

{{% /alert %}} 
### **添加了类 SignatureLine**
Aspose.Cells for .NET 8.3.2 提供对签名行的支持以模仿 MS Excel 的等效功能。此版本 Aspose.Cells for .NET 为此目的公开了 SignatureLine 类和 Picture.SignatureLine 属性。

以下示例代码使用 Picture.SignatureLine 属性将签名行添加到工作簿。

**C#**

{{< highlight "csharp" >}}

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


### **方法 Chart.HasAxis 添加**
随着 v8.3.2 的发布，Aspose.Cells API 提供了 Chart.HasAxis(AxisType axisType, bool isPrimary) 方法来确定图表是否具有特定轴。

以下示例代码演示了使用 Chart.HasAxis 方法来确定示例图表是否具有主轴、辅助轴和值轴。

**C#**

{{< highlight "csharp" >}}

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


### **方法 WorkbookSettings.CheckWriteProtectedPassword 添加**
方法 WorkbookSettings.CheckWriteProtectedPassword 使开发人员能够检查给定的修改电子表格的密码是否正确。

**C#**

{{< highlight "csharp" >}}

 //Specify password to open inside the load options

LoadOptions opts = new LoadOptions();

opts.Password = "1234";

//Open the source Excel file with load options

Workbook workbook = new Workbook("Book1.xlsx", opts);

//Check if 567 is Password to modify

bool ret = workbook.CheckWriteProtectedPassword("567");

Console.WriteLine("Is 567 correct Password to modify: " + ret);

{{< /highlight >}}


### **添加了重载方法 WorkbookRender.ToPrinter 和 SheetRender.ToPrinter**
Aspose.Cells for .NET 8.3.2提供了WorkbookRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount)和SheetRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount)方法分别打印工作簿和工作表的页码范围。

下面的示例代码演示了使用上述方法打印工作簿和工作表的第2-5页。

**C#**

{{< highlight "csharp" >}}

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


### **添加了方法 Worksheet.RefreshPivotTables**
新添加的方法 Worksheet.RefreshPivotTables 允许在一次调用中刷新给定电子表格中的所有数据透视表。

**C#**

{{< highlight "csharp" >}}

 worksheet.RefreshPivotTables();

{{< /highlight >}}


### **添加了方法 Workbook.GetNamedStyle**
Aspose.Cells for .NET API 公开了Workbook.GetNamedStyle 方法，该方法接受字符串作为参数，并根据传递的参数检索Style 对象。
### **添加方法 Cells.ImportTwoDimensionArray**
Aspose.Cells for .NET API 通过公开 Cells.ImportTwoDimensionArray(object[,], object[,], int, int, TxtLoadOptions) 方法，可以将二维数组导入电子表格单元格。所述方法将二维数据数组导入到工作表中，并在 TxtLoadOptions 中定义了更灵活的选项。
### **添加了 OnePagePerSheet、PageIndex 和 PageCount 属性**
Aspose.Cells for .NET 8.3.2 公开了 XpsSaveOptions 类的 OnePagePerSheet、PageIndex 和 PageCount 属性。用户可以使用 OnePagePerSheet 属性将电子表格的所有内容放在 XPS 的单个页面上，和/或使用 PageCount 属性检索要打印的页数。 PageIndex 属性获取/设置要保存的第一个页面的从 0 开始的索引。
### **添加了属性 NumberDecimalSeparator 和 NumberGroupSeparator**
Aspose.Cells for .NET 8.3.2 引入了 NumberDecimalSeparator 和 NumberGroupSeparator 属性，它们可以获取/设置用于格式化和解析电子表格中数值的自定义分隔符。

以下示例代码说明了如何使用 Aspose.Cells API 指定自定义分隔符。以下代码将自定义小数分隔符和组分隔符分别指定为点和空格。

**C#**

{{< highlight "csharp" >}}

 Workbook workbook = new Workbook();

//Specify custom separators

workbook.Settings.NumberDecimalSeparator = '.';

workbook.Settings.NumberGroupSeparator = ' ';

{{< /highlight >}}


### **属性 PdfSaveOptions.IsFontSubstitutionCharGranularity 添加**
Aspose.Cells for .NET 8.3.2 公开了 PdfSaveOptions.IsFontSubstitutionCharGranularity 属性，以解决某些 Unicode 字符无法使用特定字体系列显示的问题。当 PdfSaveOptions.IsFontSubstitutionCharGranularity 属性设置为 true 时，只有不可显示的特定字符的字体将更改为可显示的字体，其余单词或句子应保留原始字体。

**C#**

{{< highlight "csharp" >}}

 //Save to Pdf after setting PdfSaveOptions.IsFontSubstitutionCharGranularity to true

PdfSaveOptions opts = new PdfSaveOptions();

opts.IsFontSubstitutionCharGranularity = true;

{{< /highlight >}}


## **删除的 API**
### **删除过时的方法**
以下方法已从公共 API 中删除。

- Workbook.Open & Workbook.Save 方法。
- Workbook.SetOleSize 方法。
- 工作簿.LoadData 方法。
- WorkbookDesigner.Open & WorkbookDesigner.Save 方法。
- WorksheetCollection.DeleteName 方法。
### **删除过时的属性**
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
## **废弃的 API**
### **属性 Workbook.SaveOptions 已过时**
在设置适当的 SaveOptions 属性后，必须将 SaveOptions 的对象传递给 Workbook.Save 方法。
### **属性 Workbook.Styles 和类 StyleCollection 已过时**
建议使用 Workbook.CreateStyle 方法为 Workbook 实例创建和操作样式，而不是使用 StyleCollection.Add 方法创建样式。此外，可以使用 Workbook.GetNamedStyle(string) 方法代替 StyleCollection[string] 来获取命名样式。
### **方法 PivotItem.Move(int count) 已废弃**
随着 Aspose.Cells 8.3.2 的发布，API 引入了 PivotItem.Move 方法的另一个重载，该方法接受计数的整数参数和布尔参数以在父节点内移动 PivotItem。
