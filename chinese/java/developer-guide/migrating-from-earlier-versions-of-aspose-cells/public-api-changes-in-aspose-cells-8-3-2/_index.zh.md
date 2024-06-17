---
title: Aspose.Cells 8.3.2中的公共API更改
type: docs
weight: 130
url: /zh/java/public-api-changes-in-aspose-cells-8-3-2/
---

{{% alert color="primary" %}} 

本文描述了从Aspose.Cells API 8.3.1版本到8.3.2版本的更改，这可能对模块/应用程序开发人员感兴趣。它不仅包括新的和更新的公共方法，[添加的类等](/cells/zh/java/public-api-changes-in-aspose-cells-8-3-2/)和[已删除的类等](/cells/zh/java/public-api-changes-in-aspose-cells-8-3-2/)，还描述了在Aspose.Cells后台行为中的任何更改。

{{% /alert %}} 
## **添加的 API**
### **设置PivotItem的绝对位置的机制**
为了提供[PivotItem的绝对定位](/cells/zh/java/specifying-the-absolute-position-of-the-pivot-item/)功能，Aspose.Cells for Java 8.3.2已公开了一系列属性和方法。

- PivotItem.setPosition可用于设置所有PivotItems的位置索引，而不管父节点如何。
- PivotItem.setPositionInSameParentNode可用于设置相同父节点下的PivotItems的位置索引。
- PivotItem.move(int count, bool isSameParent)方法可用于根据计数值向上或向下移动项，其中计数是向上或向下移动PivotItem的位置的数量。如果计数值小于零，则项目将向上移动，而如果计数值大于零，则PivotItem将向下移动，Boolean类型的isSameParent参数指定移动操作是否在同一父节点中执行。

{{% alert color="primary" %}} 

请注意，在使用 PivotItem.setPosition、PivotItem.setPositionInSameParentNode 属性和 PivotItem.move(int count, bool isSameParent) 方法之前，必须调用PivotTable.refreshData 和 PivotTable.calculateData方法。

{{% /alert %}} 
### **添加了类 SignatureLine**
Aspose.Cells 8.3.2 版本提供了对签名行的支持，以模拟 MS Excel 中等效的功能。这个版本已经暴露了SignatureLine类和Picture.SignatureLine属性以实现这个目的。

以下示例代码使用 Picture.SignatureLine 属性向工作簿添加了签名行。

**Java**

{{< highlight csharp >}}

 //Create workbook object

Workbook workbook = new Workbook();

//Insert picture of your choice

int index = workbook.getWorksheets().get(0).getPictures().add(0, 0, "signature.jpg");

//Access picture and add signature line inside it

Picture pic = workbook.getWorksheets().get(0).getPictures().get(index);

//Create signature line object

SignatureLine s = new SignatureLine();

s.setSigner("John Doe");

s.setTitle("Development Lead");

s.setEmail("john.doe@aspose.com");

//Assign the signature line object to Picture.SignatureLine property

pic.setSignatureLine(s);

{{< /highlight >}}
### **添加了 Chart.hasAxis 方法**
随着 v8.3.2 版本的发布，Aspose.Cells API 提供了 Chart.hasAxis(AxisType axisType, bool isPrimary) 方法，用于确定图表是否有特定的轴。

下面的示例代码演示了 Chart.hasAxis 方法的用法，以确定示例图表是否具有主轴、次轴和值轴。

**Java**

{{< highlight csharp >}}

 //Create workbook object

Workbook workbook = new Workbook("source.xlsx");

//Access the first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access the chart

Chart chart = worksheet.getCharts().get(0);

//Determine which axis exists in chart

boolean ret = chart.hasAxis(AxisType.CATEGORY, true);

System.out.println("Has Primary Category Axis: " + ret);

ret = chart.hasAxis(AxisType.CATEGORY, false);

System.out.println("Has Secondary Category Axis: " + ret);

ret = chart.hasAxis(AxisType.VALUE, true);

System.out.println("Has Primary Value Axis: " + ret);

ret = chart.hasAxis(AxisType.VALUE, false);

System.out.println("Has Seconary Value Axis: " + ret);

{{< /highlight >}}
### **添加了 WorkbookSettings.checkWriteProtectedPassword 方法**
WorkbookSettings.checkWriteProtectedPassword 方法使开发人员能够检查用于修改电子表格的密码是否正确。

**Java**

{{< highlight csharp >}}

 //Specify password to open inside the load options

LoadOptions opts = new LoadOptions();

opts.setPassword("1234");

//Open the source Excel file with load options

Workbook workbook = new Workbook("Book1.xlsx", opts);

//Check if 567 is Password to modify

boolean ret = workbook.checkWriteProtectedPassword("567");

System.out.println("Is 567 correct Password to modify: " + ret);

{{< /highlight >}}
### **新增了 WorkbookRender.toPrinter 和 SheetRender.toPrinter 的重载方法**
Aspose.Cells 8.3.2 版本提供了 WorkbookRender.toPrinter(string printerName, int printPageIndex, int printPageCount) 和 SheetRender.toPrinter(string printerName, int printPageIndex, int printPageCount) 方法，用于打印工作簿和工作表的页面范围。

以下示例代码说明了上述方法的用法，以打印工作簿和工作表的页面 2-5。

**Java**

{{< highlight csharp >}}

 //Create workbook from source Excel file

Workbook workbook = new Workbook("source.xlsx");

//Print the workbook specifying the range of pages

//Here we are printing pages 2-5

WorkbookRender wr = new WorkbookRender(workbook, new ImageOrPrintOptions());

wr.toPrinter(printerName, 1, 4);

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Print the worksheet specifying the range of pages

//Here we are printing pages 2-5

SheetRender sr = new SheetRender(worksheet, new ImageOrPrintOptions());

sr.toPrinter(printerName, 1, 4);

{{< /highlight >}}
### **新增了 Worksheet.refreshPivotTables 方法**
新增的 Worksheet.refreshPivotTables 方法可以在单个调用中刷新给定电子表格中的所有数据透视表。

**Java**

{{< highlight csharp >}}

 worksheet.refreshPivotTables();

{{< /highlight >}}
### **新增了 Workbook.getNamedStyle 方法**
Aspose.Cells 8.3.2 版本暴露了 Workbook.getNamedStyle 方法，该方法接受字符串参数并根据传递的参数检索Style对象。
### **新增了 Cells.importTwoDimensionArray 方法**
Aspose.Cells API 通过暴露Cells.importTwoDimensionArray(object[,], object[,], int, int, TxtLoadOptions)方法，使得可以将二维数组导入到电子表格单元格中。该方法可以根据TxtLoadOptions定义的更灵活的选项将数据的二维数组导入到工作表中。
### **新增了OnePagePerSheet、PageIndex和PageCount属性**
Aspose.Cells for Java 8.3.2已经为XpsSaveOptions类暴露了OnePagePerSheet、PageIndex和PageCount属性。用户可以使用OnePagePerSheet属性将电子表格的所有内容适应到XPS的单个页面上，并且可以使用PageCount属性检索要打印的页面数。PageIndex属性获取/设置要保存的第一个页面的基于0的索引。
### **添加了 NumberDecimalSeparator 和 NumberGroupSeparator 属性**
Aspose.Cells for Java 8.3.2已经引入了NumberDecimalSeparator和NumberGroupSeparator属性，可以获取/设置电子表格中数值的自定义分隔符进行格式化和解析。

以下示例代码演示了如何使用Aspose.Cells API指定自定义分隔符。以下代码将自定义的小数点和分组分隔符分别指定为点和空格。

**Java**

{{< highlight csharp >}}

 Workbook workbook = new Workbook();

//Specify custom separators

workbook.getSettings().setNumberDecimalSeparator('.');

workbook.getSettings().setNumberGroupSeparator(' ');

{{< /highlight >}}
### **添加了 PdfSaveOptions.setFontSubstitutionCharGranularity 属性**
Aspose.Cells for Java 8.3.2已经为PdfSaveOptions.setFontSubstitutionCharGranularity属性暴露，以解决某些Unicode字符不能使用特定字体族显示的问题。当PdfSaveOptions.setFontSubstitutionCharGranularity属性设置为true时，只有不可显示的特定字符的字体将被更改为可显示的字体，其余单词或句子应保持在原始字体中。

**Java**

{{< highlight csharp >}}

 //Save to PDF after setting PdfSaveOptions.setFontSubstitutionCharGranularity

PdfSaveOptions opts = new PdfSaveOptions();

opts.setFontSubstitutionCharGranularity(true);

{{< /highlight >}}
## **删除了 API**
### **删除了已弃用的方法**
以下方法已从公共 API 中删除。

- Workbook.open 和 Workbook.save 方法。
- Workbook.setOleSize 方法。
- Workbook.loadData 方法。
- WorkbookDesigner.open 和 WorkbookDesigner.save 方法。
- WorksheetCollection.deleteName 方法。
### **删除了已弃用的属性**
以下属性已从公共 API 中删除。

- Workbook.isProtected 属性。
- Workbook.Language 属性。
- Workbook.Region 属性。
- WorkbookSettings.ReCalcOnOpen 属性。
- WorkbookSettings.Language 属性。
- WorkbookSettings.Encoding 属性。
- WorkbookSettings.ConvertNumericData 属性。
- WorksheetCollection.HidePivotFieldList 属性。
- WorksheetCollection.EnableHTTPCompression 属性。
- WorksheetCollection.isMinimized 属性。
- WorksheetCollection.isHidden 属性。
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
### **已弃用的 Workbook.saveOptions 属性**
在设置适当的 SaveOptions 属性后，应将 SaveOptions 对象传递给 Workbook.Save 方法。 
### **已弃用的 Workbook.Styles 和 Class StyleCollection 属性**
建议使用 Workbook.createStyle 方法为 Workbook 实例创建和操纵样式，而不是使用 StyleCollection.add 方法创建样式。此外，应使用 Workbook.getNamedStyle(string) 方法获取命名样式，而不是使用 StyleCollection.get(string)。
### **已弃用的 PivotItem.move(int count) 方法**
Aspose.Cells 8.3.2 版本推出了另一个 PivotItem.move 方法的重载，它接受整数参数用于计数，并接受布尔参数用于在父节点内移动 PivotItem。 
