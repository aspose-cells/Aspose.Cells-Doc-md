---
title: Ange utskriftsområde
type: docs
weight: 40
url: /sv/java/set-print-area/
---

## **Aspose.Cells - Ange utskriftsområde**
Som standard omfattar endast utskriftsområdet alla områden av arbetsboken som innehåller data. Utvecklare kan fastställa ett specifikt utskriftsområde för arbetsboken.

För att välja ett specifikt utskriftsområde, använd PageSetup-klassens setPrintArea-metod. Tilldela en cellintervall som definierar utskriftsområdet till denna egenskap.

**Java**

{{< highlight java >}}

 // Instantiating a Workbook object

Workbook workbook = new Workbook();

// Accessing the first worksheet in the Workbook file

WorksheetCollection worksheets = workbook.getWorksheets();

Worksheet sheet = worksheets.get(0);

// Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = sheet.getPageSetup();

// Specifying the cells range (from A1 cell to F20 cell) of the print area

pageSetup.setPrintArea("A1:F20");

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - Ställ in utskriftsområde**
Workbook.setPrintArea-metoden är tillgänglig för att ställa in sidans egenskaper för utskriftsområdet.

**Java**

{{< highlight java >}}

 Workbook wb = new HSSFWorkbook();

Sheet sheet = wb.createSheet("Sheet1");

//sets the print area for the first sheet

wb.setPrintArea(0, "$A$1:$C$2");

//Alternatively:

wb.setPrintArea(

        0, //sheet index

        0, //start column

        1, //end column

        0, //start row

        0  //end row

);

{{< /highlight >}}
## **Ladda ned körbar kod**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Ladda ned provkoden**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/workbook/setprintarea)

{{% alert color="primary" %}} 

För mer information, besök [Ange utskriftsalternativ](/cells/sv/java/sida-setup-funktioner/#setting-print-options).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
