---
title: Apache POI ve Aspose.Cells'de Farklı Cell Türleri Oluşturun
type: docs
weight: 100
url: /tr/java/create-different-cell-types-in-apache-poi-and-aspose-cells/
---
## **Aspose.Cells - Farklı Cell Türleri Oluşturun**
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
## **Apache POI SS (HSSF + XSSF) - Farklı Cell Türleri Oluştur**
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
## **Çalışan Kodu İndir**
 Şunun için çalışan örnekleri indirin:**Aspose.Cells ve Apache POI'de Farklı Cell Türleri Oluşturun** aşağıda belirtilen sosyal kodlama sitelerinin herhangi birinden:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells-Java-vs-POI-SS-v1.5)
## **Kaynak Kodunu İndir**
 için kaynak kodunu indirin**Aspose.Cells ve Apache POI'de Farklı Cell Türleri Oluşturun** aşağıda belirtilen sosyal kodlama sitelerinin herhangi birinden:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java)

{{% alert color="primary" %}} 

 Daha fazla ayrıntı için, ziyaret edin[Sayıların ve Tarihlerin Görüntüleme Biçimlerini Ayarlama](/cells/tr/java/data-formatting/).

{{% /alert %}}
