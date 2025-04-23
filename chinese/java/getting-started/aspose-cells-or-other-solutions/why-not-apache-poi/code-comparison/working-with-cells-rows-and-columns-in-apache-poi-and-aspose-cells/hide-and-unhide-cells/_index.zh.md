---
title: 隐藏和取消隐藏单元格
type: docs
weight: 30
url: /zh/java/hide-and-unhide-cells/
---

## **Aspose.Cells - 隐藏和取消隐藏行和列**
Aspose.Cells提供了一个代表Microsoft Excel文件的类[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)，Workbook类包含一个WorksheetCollection，允许访问Excel文件中的每个工作表。工作表由[Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)类表示。Worksheet类提供了一个表示工作表中所有单元格的Cells集合。Cells集合提供了几种方法来管理工作表中的行或列。 

**Java**

{{< highlight java >}}

 Workbook workbook = new Workbook("workbook.xls");

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.getWorksheets().get(0);

Cells cells = worksheet.getCells();

cells.hideRow(2); //Hiding the 3rd row of the worksheet

cells.hideColumn(1); //Hiding the 2nd column of the worksheet

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - 隐藏/取消隐藏单元格**
要隐藏行或列，Apache POI SS 提供了 Row.setZeroHeight(boolean) 方法。

**Java**

{{< highlight java >}}

 InputStream inStream = new FileInputStream("workbook.xls");

Workbook workbook = WorkbookFactory.create(inStream);

Sheet sheet = workbook.createSheet();

Row row = sheet.createRow(0);

row.setZeroHeight(true);

{{< /highlight >}}
## **下载运行代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **下载示例代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/hideunhidecells)

{{% alert color="primary" %}} 

有关更多详细信息，请访问[Hiding and Showing Rows and Columns](/java/hiding-and-showing-rows-and-columns)。

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
