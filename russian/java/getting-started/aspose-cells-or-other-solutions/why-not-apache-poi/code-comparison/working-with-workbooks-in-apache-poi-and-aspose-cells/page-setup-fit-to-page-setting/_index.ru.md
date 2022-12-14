---
title: Параметры страницы — настройка «По размеру страницы»
type: docs
weight: 30
url: /ru/java/page-setup-fit-to-page-setting/
---
## **Aspose.Cells - Настройка страницы - Настройка по размеру страницы**
Чтобы уместить содержимое рабочего листа в определенное количество страниц, используйте[Настройка страницы](/cells/ru/java/page-setup-fit-to-page-setting/)методы setFitToPagesTall и setFitToPagesWide класса. Эти методы также используются для масштабирования рабочих листов.

**Java**

{{< highlight "java" >}}

 // Instantiating a Workbook object

Workbook workbook = new Workbook();

// Accessing the first worksheet in the Excel file

WorksheetCollection worksheets = workbook.getWorksheets();

int sheetIndex = worksheets.add();

Worksheet sheet = worksheets.get(sheetIndex);

PageSetup pageSetup = sheet.getPageSetup();

// Setting the number of pages to which the length of the worksheet will

// be spanned

pageSetup.setFitToPagesTall(1);

// Setting the number of pages to which the width of the worksheet will be spanned

pageSetup.setFitToPagesWide(1);

{{< /highlight >}}
## **Apache POI SS — HSSF и XSSF — Настройка страницы — Настройка по размеру страницы**
Apache POI SS использует методы setFitHeight и setFitWidth для соответствия параметрам страницы.

**Java**

{{< highlight "java" >}}

 Workbook wb = new XSSFWorkbook();  //or new HSSFWorkbook();

Sheet sheet = wb.createSheet("format sheet");

PrintSetup ps = sheet.getPrintSetup();

sheet.setAutobreaks(true);

ps.setFitHeight((short) 1);

ps.setFitWidth((short) 1);

{{< /highlight >}}
## **Скачать рабочий код**
- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Скачать пример кода**
- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/workbook/fittoonepage)

{{% alert color="primary" %}} 

 Для получения более подробной информации посетите[Настройка параметров страницы](http://www.aspose.com/docs/display/cellsjava/Setting+Page+Options).

{{% /alert %}}
