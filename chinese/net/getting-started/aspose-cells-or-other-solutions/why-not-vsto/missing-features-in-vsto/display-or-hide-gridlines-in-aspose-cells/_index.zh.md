---
title: 在 Aspose.Cells 中显示或隐藏网格线
type: docs
weight: 50
url: /zh/net/display-or-hide-gridlines-in-aspose-cells/
---

{{% alert color="primary" %}}

默认情况下，所有 Excel 工作表都有网格线。它们有助于划分单元格，使得可以轻松地输入数据到特定单元格中。网格线使我们能够将工作表视为单元格的集合，其中每个单元格都很容易识别。

{{% /alert %}}

## **控制网格线的可见性**

Aspose.Cells 提供了一个代表 Microsoft Excel 文件的类，[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) 类包含一个 [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) 集合，允许访问 Excel 文件中的每个工作表。

工作表由 [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) 类表示。[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) 类提供了一系列属性和方法来管理工作表。要控制网格线的可见性，使用 [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) 类的 [**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) 属性。[**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) 是一个布尔属性，这意味着它只能存储 **true** 或 **false** 值。

下面给出了一个完整的示例，演示了如何使用 [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) 类的 [**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible) 属性隐藏 Excel 文件的第一个工作表的网格线。

在下面的截图中，您可以看到 Book1.xls 文件包含三个工作表：Sheet1、Sheet2 和 Sheet3。所有工作表都有网格线。

**Book1.xls: 修改前的工作表视图** 

![todo:image_alt_text](display-or-hide-gridlines-in-aspose-cells_1.png)

使用 Workbook 类打开 Book1.xls 文件，并将第一个工作表上的网格线隐藏。 修改后的文件将保存为 output.xls。

**Output.xls: 修改后的工作表** 

![todo:image_alt_text](display-or-hide-gridlines-in-aspose-cells_2.png)

**C#**

{{< highlight csharp >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("book1.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Hiding the gridlines of the first worksheet of the Excel file

worksheet.IsGridlinesVisible = false;

//Saving the modified Excel file

workbook.Save("output.xls");

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}

## **下载运行代码**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Display%20or%20Hide%20Gridlines)

## **下载示例代码**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
