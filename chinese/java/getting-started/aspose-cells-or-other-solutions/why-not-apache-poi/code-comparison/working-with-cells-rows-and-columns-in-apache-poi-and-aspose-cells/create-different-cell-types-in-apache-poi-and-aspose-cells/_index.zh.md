---
title: 在 Apache POI 和 Aspose.Cells 中创建不同的 Cell 类型
type: docs
weight: 100
url: /zh/java/create-different-cell-types-in-apache-poi-and-aspose-cells/
---
## **Aspose.Cells - 创建不同的 Cell 类型**
**Java**

{{< highlight "java" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Accessing the added worksheet in the Excel file

Worksheet worksheet = workbook.getWorksheets().get(0);

Cells cells = worksheet.getCells();

//Adding a string value to the cell

Cell cell = cells.get("A1");

cell.setValue("Hello World");

//Adding a double value to the cell

cell = cells.get("A2");

cell.setValue(20.5);

//Adding an integer  value to the cell

cell = cells.get("A3");

cell.setValue(15);

//Adding a boolean value to the cell

cell = cells.get("A4");

cell.setValue(true);

//Adding a date/time value to the cell

cell = cells.get("A5");

cell.setValue(Calendar.getInstance());

//Setting the display format of the date

Style style = cell.getStyle();

style.setNumber(15);

cell.setStyle(style);

{{< /highlight >}}
## **Apache POI SS (HSSF + XSSF) - 创建不同的 Cell 类型**
**Java**

{{< highlight "java" >}}

 Workbook wb = new HSSFWorkbook();

Sheet sheet = wb.createSheet("new sheet");

Row row = sheet.createRow((short)2);

row.createCell(0).setCellValue(1.1);

row.createCell(1).setCellValue(new Date());

row.createCell(2).setCellValue(Calendar.getInstance());

row.createCell(3).setCellValue("a string");

row.createCell(4).setCellValue(true);

row.createCell(5).setCellType(Cell.CELL_TYPE_ERROR);

{{< /highlight >}}
## **下载运行代码**
下载运行示例**在 Aspose.Cells 和 Apache POI 中创建不同的 Cell 类型**来自以下任何社交编码网站：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells-Java-vs-POI-SS-v1.5)
## **下载源代码**
下载源代码**在 Aspose.Cells 和 Apache POI 中创建不同的 Cell 类型**来自以下任何社交编码网站：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java)

{{% alert color="primary" %}} 

欲了解更多详情，请访问[设置Numbers和日期的显示格式](/cells/zh/java/data-formatting/).

{{% /alert %}}
