---
title: Förändringar i den offentliga API et i Aspose.Cells 8.9.0
type: docs
weight: 310
url: /sv/java/public-api-changes-in-aspose-cells-8-9-0/
---

{{% alert color="primary" %}} 

Detta dokument beskriver förändringarna i Aspose.Cells API från version 8.8.3 till 8.9.0 som kan vara av intresse för modul/applikationsutvecklare. Det inkluderar inte bara nya och uppdaterade offentliga metoder, tillagda och borttagna klasser etc., utan också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Tillagda API:er**
### **Lade till HtmlSaveOptions.DefaultFontName Egenskap**
Aspose.Cells for Java 8.9.0 har exponerat DefaultFontName egenskapen för HtmlSaveOptions klassen som tillåter att specificera standardfontnamnet vid rendering av kalkylblad till HTML-format. Standardfonten används endast när fonterna i stilen inte finns. Standardvärdet för HtmlSaveOptions.DefaultFontName egenskapen är null vilket innebär att Aspose.Cells for Java API:et kommer att använda den universella fonten som har samma familj som den ursprungliga fonten.

{{% alert color="primary" %}} 

För mer detaljer om denna funktion, vänligen granska artikeln om [Sätta Standardfont vid Rendering av Kalkylblad till HTML Format](/cells/sv/java/set-default-font-while-rendering-spreadsheet-to/).

{{% /alert %}} 

Följande är det enkla användningscenariot.

**Java**

{{< highlight csharp >}}

 //Create an instance of HtmlSaveOptions

HtmlSaveOptions options = new HtmlSaveOptions();

//Set default font name for Html rendering

options.setDefaultFontName("Arial");

//Load a spreadsheet in an instance of Workbook

Workbook book = new Workbook(dir + "sample.xlsx");

//Save the spreadsheet in Html format while passing instance of HtmlSaveOptions

book.save(dir + "output.html", options);

{{< /highlight >}}
### **Lade till ImageOrPrintOptions.DefaultFont Egenskap**
Aspose.Cells for Java 8.9.0 tillåter att sätta standardfontnamnet för ImageOrPrintOptions klassen genom att exponera DefaultFont egenskapen. Den tidigare nämnda egenskapen kan användas när Unicode-tecken i kalkylbladet inte är satta med korrekt font i cellstil, därför kan sådana tecken visas som block i de resulterande bilderna. 

{{% alert color="primary" %}} 

Sätt DefaultFont egenskapen till MingLiu eller MS Gothic för att visa Unicode-tecken. Om den tidigare nämnda egenskapen inte är satt, kommer Aspose.Cells att använda systemets standardfont för att visa Unicode-tecken. 

{{% /alert %}} {{% alert color="primary" %}} 

För mer detaljer om denna funktion, vänligen granska artikeln om [Sätta Standardfont vid Rendering av Kalkylblad i Bildformat](/cells/sv/java/set-default-font-while-rendering-spreadsheet-to-images/).

{{% /alert %}} 

Följande är det enkla användningscenariot.

**Java**

{{< highlight csharp >}}

 //Create an instance of ImageOrPrintOptions

ImageOrPrintOptions options = new ImageOrPrintOptions();

//Set default font name for image rendering

options.setDefaultFont("Arial");

//Load a spreadsheet in an instance of Workbook

Workbook book = new Workbook(dir + "sample.xlsx");

//Access the worksheet to be rendered

Worksheet sheet = book.getWorksheets().get(0);

//Create an instance of SheetRender

SheetRender render = new SheetRender(sheet, options);

//Save spreadsheet to image

render.toImage(0, dir + "output.png");

{{< /highlight >}}
### **Lade till PivotTable.Excel2003Compatible Egenskap**
Aspose.Cells for Java API har exponerat den Booleska typen Excel2003Compatible-egenskapen för PivotTable-klassen som möjliggör att specificera om PivotTable är kompatibel med Excel 2003 för uppdateringsändamål. Standardvärdet för Excel2003Compatible-egenskapen är true, vilket innebär att en sträng måste vara mindre än eller lika med 255 tecken. Om strängen är större än 255 tecken kommer den att bli avkortad. Om falskt kommer ovannämnda begränsning inte att gälla.

{{% alert color="primary" %}} 

För mer information om denna funktion, vänligen granska artikeln om [Kompatibilitet för Excel 2003 för att uppdatera Pivottabeller](/cells/sv/java/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/).

{{% /alert %}} 

Följande är det enkla användningscenariot.

**Java**

{{< highlight csharp >}}

 //Load a spreadsheet in an instance of Workbook

Workbook book = new Workbook(dir + "sample.xlsx");

//Access the desired Pivot Table from the spreadsheet

PivotTable pivot = book.getWorksheets().get(0).getPivotTables().get(0);

//Set Excel 2003 compatibility to false

pivot.setExcel2003Compatible(false);

//Refresh & recalculate Pivot Table

pivot.refreshData();

pivot.calculateData();

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
