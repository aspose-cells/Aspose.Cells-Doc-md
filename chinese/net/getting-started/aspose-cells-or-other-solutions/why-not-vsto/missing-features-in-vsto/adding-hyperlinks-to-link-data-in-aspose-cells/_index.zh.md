---
title: 在Aspose.Cells中添加超链接以链接数据
type: docs
weight: 10
url: /zh/net/adding-hyperlinks-to-link-data-in-aspose-cells/
---

{{% alert color="primary" %}}

超链接用于在两个实体之间创建链接。每个人都熟悉超链接的使用，特别是在网站上。

使用Aspose.Cells，开发人员可以在Microsoft Excel文件中创建不同类型的超链接。本主题讨论了Aspose.Cells支持哪些类型的超链接以及如何在我们的Excel文件中使用它们。

{{% /alert %}}

## **添加超链接**

使用Aspose.Cells可以向单元格添加三种类型的超链接：

- [向URL添加链接](#adding-link-to-a-url).
- [向同一文件中的其他单元格添加链接](#adding-a-link-to-a-cell-in-the-same-file).
- [向外部文件添加链接](#adding-a-link-to-an-external-file).

Aspose.Cells允许开发人员使用API或[设计者电子表格](/cells/zh/net/what-is-a-designer-spreadsheet/)（手动创建超链接并使用Aspose.Cells将其导入到其他电子表格）向Excel文件添加超链接。

Aspose.Cells提供了一个类，[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)，表示一个Microsoft Excel文件。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类包含一个[**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)，允许访问Excel文件中的每个工作表。工作表由[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类表示。[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类提供了向Excel文件添加不同超链接的不同方法。

### **添加指向URL的链接**

这个[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类包含一个[**Hyperlinks**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/hyperlinks)集合。超链接集合中的每个项目表示一个超链接。通过调用超链接集合的Add方法向URL添加超链接。Add方法有以下参数：

- 单元格名称，超链接将添加到的单元格的名称。
- 行数，超链接范围中的行数。
- 列数，该超链接范围的列数
- URL，URL地址。

**C#**

{{< highlight csharp >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Workbook object

int i = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[i];

//Adding a hyperlink to a URL at "A1" cell

worksheet.Hyperlinks.Add("A1", 1, 1, "http://www.aspose.com");

//Saving the Excel file

workbook.Save("C:\\book1.xls");

{{< /highlight >}}

### **将链接添加到同一文件中的单元格**

通过调用超链接集合的Add方法，可以将超链接添加到同一Excel文件中的单元格中。Add方法适用于内部和外部超链接。其中一个重载方法采用以下参数：

- 单元格名称，将要添加超链接的单元格名称。
- 行数，超链接范围中的行数。
- 列数，超链接范围中的列数。
- URL，目标单元格的地址。

**C#**

{{< highlight csharp >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Obtaining the reference of the first (default) worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Adding an internal hyperlink to the "B9" cell of the other worksheet "Sheet2" in

//the same Excel file

worksheet.Hyperlinks.Add("B3", 1, 1, "Sheet2!B9");

//Saving the Excel file

workbook.Save("C:\\book1.xls");

{{< /highlight >}}

### **向外部文件添加链接**

可以通过调用超链接集合的Add方法向外部的Excel文件添加超链接。Add方法采用以下参数：

- 单元格名称，超链接将添加到的单元格的名称。
- 行数，超链接范围中的行数。
- 列数，超链接范围中的列数。
- URL，目标外部Excel文件的地址。

**C#**

{{< highlight csharp >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Excel object

int i = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[i];

//Adding an internal hyperlink to the "B9" cell of the other worksheet "Sheet2" in

//the same Excel file

worksheet.Hyperlinks.Add("A5", 1, 1, "C:\\book1.xls");

//Saving the Excel file

workbook.Save("C:\\book2.xls");

{{< /highlight >}}

## **下载运行代码**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Adding%20Hyperlinks%20to%20Link%20Data)

## **下载示例代码**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
{{< app/cells/assistant language="csharp" >}}
