---
title: 向 Aspose.Cells 中的链接数据添加超链接
type: docs
weight: 10
url: /zh/net/adding-hyperlinks-to-link-data-in-aspose-cells/
---
{{% alert color="primary" %}}

超链接用于在两个实体之间创建链接。每个人都熟悉超链接的使用，尤其是在网站上。

使用 Aspose.Cells，开发人员可以在 Microsoft Excel 文件中创建不同种类的超链接。本主题讨论 Aspose.Cells 支持哪些类型的超链接以及如何在我们的 Excel 文件中使用它们。

{{% /alert %}}

## **添加超链接**

使用 Aspose.Cells 可以将三种类型的超链接添加到单元格：

- [添加指向 URL 的链接](#adding-link-to-a-url).
- [添加指向同一文件中另一个单元格的链接](#adding-a-link-to-a-cell-in-the-same-file).
- [添加指向外部文件的链接](#adding-a-link-to-an-external-file).

Aspose.Cells 允许开发人员使用 API 或[设计师电子表格](/cells/zh/net/what-is-a-designer-spreadsheet/)（手动创建超链接并使用 Aspose.Cells 将它们导入其他电子表格的电子表格）。

Aspose.Cells提供了一个类，[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)表示 Microsoft Excel 文件。这[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类包含一个[**工作表集合**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)允许访问 Excel 文件中的每个工作表。工作表由[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)班级。这[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类提供了向 Excel 文件添加不同超链接的不同方法。

### **将链接添加到 URL**

这[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类包含一个[**超级链接**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/hyperlinks)收藏。超链接集合中的每一项代表一个超链接。通过调用 Hyperlinks 集合的 Add 方法将超链接添加到 URL。添加方法采用以下参数：

- Cell name，超链接将添加到的单元格的名称。
- Number of rows，这个超链接范围内的行数。
- Number of columns，这个超链接范围内的列数
- 网址，网址地址。

**C#**

{{< highlight "csharp" >}}

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

### **在同一文件中添加指向 Cell 的链接**

通过调用 Hyperlink 集合的 Add 方法，可以将超链接添加到同一 Excel 文件中的单元格。 Add 方法适用于内部和外部超链接。重载方法的一种版本采用以下参数：

- Cell name，要添加超链接的单元格的名称。
- Number of rows，这个超链接范围内的行数。
- Number of columns，这个超链接范围内的列数。
- URL，目标单元格的地址。

**C#**

{{< highlight "csharp" >}}

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

### **添加指向外部文件的链接**

可以通过调用 Hyperlinks 集合的 Add 方法向外部 Excel 文件添加超链接。添加方法采用以下参数：

- Cell name，超链接将添加到的单元格的名称。
- Number of rows，这个超链接范围内的行数。
- Number of columns，这个超链接范围内的列数。
- URL，目标地址，外部Excel文件。

**C#**

{{< highlight "csharp" >}}

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
