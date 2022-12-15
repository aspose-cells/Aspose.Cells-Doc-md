---
title: 在 Aspose.Cells 中显示或隐藏行列标题
type: docs
weight: 60
url: /zh/net/display-or-hide-row-column-headers-in-aspose-cells/
---
{{% alert color="primary" %}}

Excel 文件中的所有工作表均由按行和列排列的单元格组成。所有行和列都有唯一的值，用于标识它们和标识单个单元格。例如，行编号 - 1、2、3、4 等 - 列按字母顺序排序 - A、B、C、D 等。行和列值显示在标题中。使用 Aspose.Cells，开发人员可以控制这些行和列标题的可见性。

{{% /alert %}}

## **控制工作表的可见性**

Aspose.Cells提供了一个类，[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)，代表一个 Microsoft Excel 文件。这[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类包含一个[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)允许访问 Excel 文件中每个工作表的集合。

工作表由[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)班级。这[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类提供了广泛的属性和方法来管理工作表。要控制行标题和列标题的可见性，请使用[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)班级'[**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible)财产。[**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible)是一个布尔属性，这意味着它只能存储一个**真的**或者**错误的**价值。

下面给出了一个完整的示例，说明如何使用[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)班级'[**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible)隐藏文件中第一个工作表上的行和列标题的属性。

屏幕截图显示了输入文件 Book1.xls。它包含三个工作表：Sheet1、Sheet2 和 Sheet3。每个工作表都显示行和列标题。

**Book1.xls：修改前的工作表**

![待办事项：图像_替代_文本](display-or-hide-row-column-headers-in-aspose-cells_1.png)

Book1.xls 通过调用 Workbook 类的 Open 方法打开，第一个工作表上的行标题和列标题被隐藏。修改后的文件保存为 output.xls。

**Output.xls：修改后的工作表** 

![待办事项：图像_替代_文本](display-or-hide-row-column-headers-in-aspose-cells_2.png)

**C#**

{{< highlight "csharp" >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("book1.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Hiding the headers of rows and columns

worksheet.IsRowColumnHeadersVisible = false;

//Saving the modified Excel file

workbook.Save("output.xls");

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}

## **下载运行代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Display%20or%20Hide%20Row%20Column%20Headers)

## **下载示例代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
