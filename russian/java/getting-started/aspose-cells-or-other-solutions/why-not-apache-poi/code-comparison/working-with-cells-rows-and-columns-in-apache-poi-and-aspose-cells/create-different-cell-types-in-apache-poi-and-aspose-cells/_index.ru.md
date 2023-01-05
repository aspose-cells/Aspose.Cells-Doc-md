---
title: Создание разных типов Cell в Apache POI и Aspose.Cells
type: docs
weight: 100
url: /ru/java/create-different-cell-types-in-apache-poi-and-aspose-cells/
---
## **Aspose.Cells - Создание разных типов Cell**
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
## **Apache POI SS (HSSF + XSSF) — создание разных типов Cell**
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
## **Скачать рабочий код**
 Скачать примеры работы для**Создание разных типов Cell в Aspose.Cells и Apache POI** с любого из нижеперечисленных сайтов социального кодирования:

- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells-Java-vs-POI-SS-v1.5)
## **Скачать исходный код**
 Скачать исходный код для**Создание разных типов Cell в Aspose.Cells и Apache POI** с любого из нижеперечисленных сайтов социального кодирования:

- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java)

{{% alert color="primary" %}} 

 Для получения более подробной информации посетите[Настройка форматов отображения Numbers и дат](/cells/ru/java/data-formatting/).

{{% /alert %}}
