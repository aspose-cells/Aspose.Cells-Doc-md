---
title: Sidinställning  Anpassa till sidan inställning
type: docs
weight: 30
url: /sv/java/page-setup-fit-to-page-setting/
---

## **Aspose.Cells - Sidinställning - Anpassa till sidan-inställning**
För att anpassa innehållet i kalkylbladet till ett specifikt antal sidor, använd klassen [PageSetup](/cells/sv/java/page-setup-fit-to-page-setting/) metoder setFitToPagesTall och setFitToPagesWide. Dessa metoder används också för att skala kalkylblad.

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
## **Apache POI SS - HSSF & XSSF - Sidinställning - Anpassa till sidan-inställning**
Apache POI SS använder setFitHeight och setFitWidth metoder för inställningar för anpassning till sidan.

**Java**

{{< highlight java >}}

 Workbook wb = new XSSFWorkbook();  //or new HSSFWorkbook();

Sheet sheet = wb.createSheet("format sheet");

PrintSetup ps = sheet.getPrintSetup();

sheet.setAutobreaks(true);

ps.setFitHeight((short) 1);

ps.setFitWidth((short) 1);

{{< /highlight >}}
## **Ladda ned körbar kod**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Ladda ned provkoden**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/workbook/fittoonepage)

{{% alert color="primary" %}} 

För mer information, besök [Inställning av sida alternativ](http://www.aspose.com/docs/display/cellsjava/Setting+Page+Options).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
