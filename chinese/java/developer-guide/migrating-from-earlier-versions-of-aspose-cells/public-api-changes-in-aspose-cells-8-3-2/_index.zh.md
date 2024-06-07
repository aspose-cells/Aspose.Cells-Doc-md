---
title: Aspose.Cells 8.3.2中的公共API更改
type: docs
weight: 130
url: /zh/java/public-api-changes-in-aspose-cells-8-3-2/
---

{{% alert color="primary" %}} 

本文描述了从版本8.3.1到8.3.2的Aspose.Cells API的变化，这可能对模块/应用程序开发人员感兴趣。 它不仅包括新的和更新的公共方法，[添加的类等](/cells/zh/java/public-api-changes-in-aspose-cells-8-3-2/)和[删除的类等](/cells/zh/java/public-api-changes-in-aspose-cells-8-3-2/)，还描述了在Aspose.Cells背后的行为中的任何更改。

{{% /alert %}} 
## **已添加API**
### **设置PivotItem绝对位置的机制**
为提供[PivotItem的绝对定位](/cells/zh/java/specifying-the-absolute-position-of-the-pivot-item/)功能，Aspose.Cells for Java 8.3.2已经公开了一系列属性和方法，如下所列。

- PivotItem.setPosition可用于在所有PivotItems中设置位置索引，而不考虑父节点。
- PivotItem.setPositionInSameParentNode可用于在同一父节点下的PivotItems中设置位置索引。
- PivotItem.move(int count, bool isSameParent)方法可用于根据计数值将项目上移或下移，其中计数值是要将PivotItem向上或向下移动的位置数。 如果计数值小于零，项目将向上移动，如果计数值大于零，则PivotItem将向下移动，布尔类型isSameParent参数指定是否要在同一父节点中执行移动操作。

{{% alert color="primary" %}} 

请注意，在使用PivotItem.setPosition，PivotItem.setPositionInSameParentNode属性和PivotItem.move(int count, bool isSameParent)方法之前，必须调用PivotTable.refreshData和PivotTable.calculateData方法。

{{% /alert %}} 
### **新增类SignatureLine**
Aspose.Cells 8.3.2为模拟MS Excel的等效功能提供了对签名行的支持。 此版本已经为此目的公开了SignatureLine类和Picture.SignatureLine属性。

以下示例代码使用Picture.SignatureLine属性向工作簿添加签名行。

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
### **添加了Chart.hasAxis方法**
随着v8.3.2的发布，Aspose.Cells API已经提供了Chart.hasAxis(AxisType axisType, bool isPrimary)方法，用于确定图表是否具有特定的轴。

以下示例代码演示了如何使用Chart.hasAxis方法来确定样本图表是否具有主要轴、次要轴和值轴。

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
### **添加了WorkbookSettings.checkWriteProtectedPassword方法**
方法 WorkbookSettings.checkWriteProtectedPassword 允许开发人员检查修改电子表格的给定密码是否正确。

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
### **重载方法 WorkbookRender.toPrinter 和 SheetRender.toPrinter 已添加**
Aspose.Cells 8.3.2 提供了 WorkbookRender.toPrinter(string printerName, int printPageIndex, int printPageCount) 和 SheetRender.toPrinter(string printerName, int printPageIndex, int printPageCount) 方法，用于分别打印工作簿和工作表的页面范围

以下示例代码说明了如何使用上述方法打印工作簿和工作表的第2-5页。

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
### **添加了Worksheet.refreshPivotTables方法**
新增方法 Worksheet.refreshPivotTables 允许在单个调用中刷新给定电子表格中的所有数据透视表

**Java**

{{< highlight csharp >}}

 worksheet.refreshPivotTables();

{{< /highlight >}}
### **添加了Workbook.getNamedStyle方法**
Aspose.Cells 8.3.2 公开了接受字符串作为参数的 Workbook.getNamedStyle 方法，并根据传递的参数检索基于样式的对象
### **添加了Cells.importTwoDimensionArray方法**
Aspose.Cells API 通过暴露 Cells.importTwoDimensionArray(object[,], object[,], int, int, TxtLoadOptions) 方法，实现了将二维数组导入到电子表格单元格的功能
### **添加了OnePagePerSheet、PageIndex和PageCount属性**
Aspose.Cells for Java 8.3.2 已公开了 OnePagePerSheet、PageIndex 和 PageCount 属性，用户可以使用 OnePagePerSheet 属性将电子表格的所有内容放在一页上，并使用 PageCount 属性检索要打印的页面数，PageIndex 属性可以获取/设置要保存的第一页的基于0的索引
### **添加了NumberDecimalSeparator和NumberGroupSeparator属性**
Aspose.Cells for Java 8.3.2 引入了 NumberDecimalSeparator 和 NumberGroupSeparator 属性，用于格式化和解析电子表格中的数字值

以下示例代码说明了如何使用 Aspose.Cells API 指定自定义分隔符，该代码指定自定义的小数和组分隔符分别为点和空格

**Java**

{{< highlight csharp >}}

 Workbook workbook = new Workbook();

//Specify custom separators

workbook.getSettings().setNumberDecimalSeparator('.');

workbook.getSettings().setNumberGroupSeparator(' ');

{{< /highlight >}}
### **添加了PdfSaveOptions.setFontSubstitutionCharGranularity属性**
Aspose.Cells for Java 8.3.2 公开了 PdfSaveOptions.setFontSubstitutionCharGranularity 属性，以解决一些 Unicode 字符无法使用特定字体族显示的问题

**Java**

{{< highlight csharp >}}

 //Save to PDF after setting PdfSaveOptions.setFontSubstitutionCharGranularity

PdfSaveOptions opts = new PdfSaveOptions();

opts.setFontSubstitutionCharGranularity(true);

{{< /highlight >}}
## **已删除APIs**
### **已移除的已过时方法**
以下方法已从公共API中移除。

- Workbook.open 和 Workbook.save 方法
- Workbook.setOleSize 方法
- Workbook.loadData 方法
- WorkbookDesigner.open 和 WorkbookDesigner.save 方法
- WorksheetCollection.deleteName 方法
### **已移除的已过时属性**
以下属性已从公共API中移除。

- Workbook.isProtected 属性
- Workbook.Language 属性。
- Workbook.Region 属性。
- WorkbookSettings.ReCalcOnOpen 属性。
- WorkbookSettings.Language 属性。
- WorkbookSettings.Encoding 属性。
- WorkbookSettings.ConvertNumericData 属性。
- WorksheetCollection.HidePivotFieldList 属性。
- WorksheetCollection.EnableHTTPCompression 属性。
- WorksheetCollection.isMinimized 属性
- WorksheetCollection.isHidden 属性
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
### **弃用了Workbook.saveOptions属性**
在设置适当的 SaveOptions 属性后，必须将 SaveOptions 对象传递给 Workbook.Save 方法。 
### **弃用了Workbook.Styles和Class StyleCollection属性**
建议使用 Workbook.createStyle 方法为 Workbook 实例创建和操作样式，而不是使用 StyleCollection.add 方法创建样式。此外，可以使用 Workbook.getNamedStyle(string) 方法获取命名样式，而不是使用 StyleCollection.get(string)
### **弃用了PivotItem.move(int count)方法**
随着 Aspose.Cells 8.3.2 的发布，API 引入了另一个重载的 PivotItem.move 方法，该方法接受整数参数用于计数并接受布尔参数在父节点内移动 PivotItem 
