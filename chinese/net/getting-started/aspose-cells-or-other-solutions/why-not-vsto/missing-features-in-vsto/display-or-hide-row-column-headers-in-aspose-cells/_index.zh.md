---
title: 在 Aspose.Cells 中显示或隐藏行列标题
type: docs
weight: 60
url: /zh/net/display-or-hide-row-column-headers-in-aspose-cells/
---

{{% alert color="primary" %}}

Excel文件中的所有工作表都由排列在行和列中的单元格组成。所有行和列都有用于标识它们和标识单个单元格的唯一值。例如，行是编号的 - 1、2、3、4等，而列以字母顺序排列 - A、B、C、D等。行和列的值显示在标头中。使用Aspose.Cells，开发人员可以控制这些行和列标头的可见性。

{{% /alert %}}

## **控制工作表的可见性**

Aspose.Cells 提供了代表 Microsoft Excel 文件的 [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) 类。 [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) 类包含一个 [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) 集合，允许访问 Excel 文件中的每个工作表。

工作表由 [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) 类表示。 [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) 类提供了广泛的属性和方法，用于管理工作表。要控制行和列标题的可见性，请使用 [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) 类的 [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) 属性。 [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) 是一个布尔属性，只能存储 **true** 或 **false** 值。

下面是一个完整的示例，演示如何使用 [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) 类的 [**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible) 属性隐藏文件中第一个工作表上的行和列标题。

屏幕截图显示了 Book1.xls，输入文件。它包含三个工作表：Sheet1、Sheet2 和 Sheet3。每个工作表显示了行和列标题。

**Book1.xls：修改前的工作表**

![todo:image_alt_text](display-or-hide-row-column-headers-in-aspose-cells_1.png)

通过调用 Workbook 类的 Open 方法打开 Book1.xls，然后隐藏第一个工作表上的行和列标题。修改后的文件将保存为 output.xls。

**Output.xls: 修改后的工作表** 

![todo:image_alt_text](display-or-hide-row-column-headers-in-aspose-cells_2.png)

**C#**

{{< highlight csharp >}}

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
