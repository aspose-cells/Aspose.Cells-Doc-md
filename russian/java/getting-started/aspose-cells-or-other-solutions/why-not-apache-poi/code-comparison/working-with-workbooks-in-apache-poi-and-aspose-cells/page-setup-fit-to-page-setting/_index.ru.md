---
title: Настройка страницы  установка подгонки по размеру страницы
type: docs
weight: 30
url: /ru/java/page-setup-fit-to-page-setting/
---

## **Aspose.Cells - Настройка страницы - установка подгонки по размеру страницы**
Чтобы подогнать содержимое листа к определенному количеству страниц, используйте методы setFitToPagesTall и setFitToPagesWide класса PageSetup. Эти методы также используются для масштабирования листов.

**Java**

{{< highlight java >}}

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
## **Apache POI SS - HSSF & XSSF - Настройка страницы - установка подгонки по размеру страницы**
Apache POI SS использует методы setFitHeight и setFitWidth для настройки подгонки по размеру страницы.

**Java**

{{< highlight java >}}

 Workbook wb = new XSSFWorkbook();  //or new HSSFWorkbook();

Sheet sheet = wb.createSheet("format sheet");

PrintSetup ps = sheet.getPrintSetup();

sheet.setAutobreaks(true);

ps.setFitHeight((short) 1);

ps.setFitWidth((short) 1);

{{< /highlight >}}
## **Скачать работающий код**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Загрузить образец кода**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/workbook/fittoonepage)

{{% alert color="primary" %}} 

Для получения дополнительной информации посетите [Настройка параметров страницы](http://www.aspose.com/docs/display/cellsjava/Setting+Page+Options).

{{% /alert %}}
