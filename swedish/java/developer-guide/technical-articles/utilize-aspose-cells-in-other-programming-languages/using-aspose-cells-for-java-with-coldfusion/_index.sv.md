---
title: Använder Aspose.Cells för Java med ColdFusion
type: docs
weight: 40
url: /sv/java/using-aspose-cells-for-java-with-coldfusion/
---
{{% alert color="primary" %}}

Den här artikeln ger den grundläggande informationen och kodsegmentet som ColdFusion-utvecklare behöver för att använda Aspose.Cells för Java i ColdFusion-applikationen.

Den här artikeln visar hur du skapar en enkel webbsida med ColdFusion och använder Aspose.Cells för Java för att skapa en enkel Excel-fil.

{{% /alert %}}

## **Aspose.Cells: Den verkliga produkten**

Med Aspose.Cells kan utvecklare exportera data, formatera kalkylblad i varje detalj och på varje nivå, importera bilder, importera diagram, skapa diagram, manipulera diagram, strömma Microsoft Excel-data, spara i olika format inklusive XLS, CSV, SpreadsheetML, TabDelimited, TXT, XML ([Aspose.Pdf](https://products.aspose.com/pdf/java/) integrerad) och många fler.

 För att ta reda på mer om produktinformationen, funktionerna och för en programmerares guide, se Aspose.Cells-dokumentationen och online-utvalda[demos](https://github.com/aspose-cells/Aspose.Cells-for-Java) . Du kan[ladda ner](https://downloads.aspose.com/cells/java) och utvärdera det gratis.

### **Förutsättningar**

För att använda Aspose.Cells för Java i ColdFusion-program, kopiera filen Aspose.Cells.jar till mappen {InstallationFolder\\}\wwwroot\WEB-INF\lib.

Glöm inte att starta om ColdFusion-applikationsservern efter att ha lagt nya JAR:er i lib-mappen.

### **Använda Aspose.Cells för Java och ColdFusion för att skapa en Excel-fil**

Nedan skapar vi en enkel applikation som genererar en tom Microsoft Excel-fil, infogar en del innehåll och sparar det som en XLS-fil.

Följande är den faktiska koden (ColdFusion & Aspose.Cells för Java). Efter exekvering av koden genereras en Excel-fil, output.xls.

**Genererad output.xls**

![todo:image_alt_text](using-aspose-cells-for-java-with-coldfusion_1.png)

**Java**

{{< highlight "java" >}}

 <html>

<head><title>Hello World!</title></head>

<body>

    <b>This example shows how to create a simple MS Excel Workbook using Aspose.Cells</b>

    <cfset workbook=CreateObject("java", "com.aspose.cells.Workbook").init()>

    <cfset worksheets = workbook.getWorksheets()>

    <cfset sheet= worksheets.get("Sheet1")>

    <cfset cells= sheet.getCells()>

    <cfset cell= cells.getCell(0,0)>

    <cfset cell.setValue("Hello World!")>

    <cfset workbook.save("C:\output.xls")>

</body>

</html>

{{< /highlight >}}

## **Sammanfattning**

{{% alert color="primary" %}}

Den här artikeln förklarar hur du använder Aspose.Cells för Java med ColdFusion.

Aspose.Cells erbjuder stor flexibilitet och ger enastående hastighet, effektivitet och tillförlitlighet. Aspose.Cells har dragit nytta av år av forskning, design och noggrann justering.

 Vi välkomnar frågor, kommentarer och förslag i[Aspose.Cells Forum](https://forum.aspose.com/c/cells/9).

{{% /alert %}}
