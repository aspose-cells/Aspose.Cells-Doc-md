---
title: 在 Apache POI 和 Aspose.Cells 中创建日期单元格
type: docs
weight: 90
url: /zh/java/create-date-cell-in-apache-poi-and-aspose-cells/
---

## **Aspose.Cells - 创建日期单元格**
Java

{{< highlight java >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Accessing the added worksheet in the Excel file

Worksheet worksheet = workbook.getWorksheets().get(0);

Cells cells = worksheet.getCells();

//Adding the current system date to "A1" cell

Cell cell = cells.get("A1");

cell.setValue(Calendar.getInstance());

//Setting the display format of the date to number 15 to show date as "d-mmm-yy"

Style style = cell.getStyle();

style.setCustom("d-mmm-yy");

cell.setStyle(style);

{{< /highlight >}}
## **Apache POI SS (HSSF + XSSF) - 创建日期单元格**
Java

{{< highlight java >}}

 Workbook wb = new HSSFWorkbook();

//Workbook wb = new XSSFWorkbook();

CreationHelper createHelper = wb.getCreationHelper();

Sheet sheet = wb.createSheet("new sheet");

// Create a row and put some cells in it. Rows are 0 based.

Row row = sheet.createRow(0);

// Create a cell and put a date value in it.  The first cell is not styled

// as a date.

Cell cell = row.createCell(0);

cell.setCellValue(new Date());

// we style the second cell as a date (and time).  It is important to

// create a new cell style from the workbook otherwise you can end up

// modifying the built in style and effecting not only this cell but other cells.

CellStyle cellStyle = wb.createCellStyle();

cellStyle.setDataFormat(

    createHelper.createDataFormat().getFormat("m/d/yy h:mm"));

cell = row.createCell(1);

cell.setCellValue(new Date());

cell.setCellStyle(cellStyle);

//you can also set date as java.util.Calendar

cell = row.createCell(2);

cell.setCellValue(Calendar.getInstance());

cell.setCellStyle(cellStyle);

{{< /highlight >}}
## **下载运行代码**
从以下任一社交编程网站下载 **Aspose.Cells 和 Apache POI 中创建日期单元格** 的运行示例：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells-Java-vs-POI-SS-v1.5)
## **下载源代码**
从以下社交编码网站下载**Aspose.Cells和Apache POI中创建日期单元格的源代码**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java)

{{% alert color="primary" %}} 

查看更多详情，请访问[在单元格中添加数据](/cells/zh/java/add-data-in-cells/)

{{% /alert %}}
