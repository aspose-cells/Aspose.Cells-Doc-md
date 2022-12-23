---
title: Öppna och spara kalkylblad i xlsx4j
type: docs
weight: 40
url: /sv/java/open-and-save-spreadsheet-in-xlsx4j/
---
## **Aspose.Cells - Öppna och spara kalkylblad**
Utvecklare använder Aspose.Cells för att öppna filer för olika ändamål. Öppna till exempel en fil för att hämta data från den, eller använd en fördefinierad designarkfil för att påskynda utvecklingsprocessen. Aspose.Cells tillåter utvecklare att öppna olika typer av källfiler. Dessa källfiler kan vara Microsoft Excel-rapporter, SpreadsheetML, CSV eller tabbavgränsade filer.

**Aspose.Cells**tillåter utvecklare att skapa Excel-filer från grunden med hjälp av dess flexibla API. När du väl har skapat Excel-filer måste du också spara din arbetsbok (fil). Aspose.Cells tillhandahåller en mängd olika sätt att spara dessa filer.

**Java**

{{< highlight "java" >}}

 //Creating an Workbook object with an Excel file path

Workbook workbook = new Workbook(dataDir + "pivot.xlsm");

//Saving the Excel file

workbook.save(dataDir + "pivot-rtt-Aspose.xlsm");

{{< /highlight >}}
## **xlsx4j - Öppna och spara kalkylblad**
Nedan exempel visar hur du öppnar och sparar kalkylblad när du använder xlsx4j.

**Java**

{{< highlight "java" >}}

 String inputfilepath  = dataDir + "pivot.xlsm";

boolean save = true;

String outputfilepath = dataDir + "pivot-rtt-xlsx4j.xlsm";

// Open a document from the file system

// 1. Load the Package

OpcPackage pkg = OpcPackage.load(new java.io.File(inputfilepath));

// Save it

if (save) {

    SaveToZipFile saver = new SaveToZipFile(pkg);

    saver.save(outputfilepath);

}

{{< /highlight >}}
## **Ladda ner Running Code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Ladda ner provkod**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/featurescomparison/workbook/opensavespreadsheet)
