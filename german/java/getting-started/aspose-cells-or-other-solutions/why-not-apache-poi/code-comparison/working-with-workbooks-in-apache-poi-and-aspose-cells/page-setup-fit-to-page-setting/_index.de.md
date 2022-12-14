---
title: Seite einrichten - An Seiteneinstellung anpassen
type: docs
weight: 30
url: /de/java/page-setup-fit-to-page-setting/
---
## **Aspose.Cells – Seite einrichten – An Seiteneinstellung anpassen**
Um den Inhalt des Arbeitsblatts auf eine bestimmte Anzahl von Seiten anzupassen, verwenden Sie die[Seiteneinrichtung](/cells/de/java/page-setup-fit-to-page-setting/)setFitToPagesTall- und setFitToPagesWide-Methoden der Klasse. Diese Methoden werden auch verwendet, um Arbeitsblätter zu skalieren.

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
## **Apache POI SS - HSSF & XSSF - Seite einrichten - An Seiteneinstellung anpassen**
Apache POI SS verwendet die Methoden setFitHeight und setFitWidth für die Einstellungen zum Anpassen an die Seite.

**Java**

{{< highlight "java" >}}

 Workbook wb = new XSSFWorkbook();  //or new HSSFWorkbook();

Sheet sheet = wb.createSheet("format sheet");

PrintSetup ps = sheet.getPrintSetup();

sheet.setAutobreaks(true);

ps.setFitHeight((short) 1);

ps.setFitWidth((short) 1);

{{< /highlight >}}
## **Laufcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Beispielcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/workbook/fittoonepage)

{{% alert color="primary" %}} 

 Weitere Informationen finden Sie unter[Seitenoptionen festlegen](http://www.aspose.com/docs/display/cellsjava/Setting+Page+Options).

{{% /alert %}}
