---
title: Offentlig API Ändringar i Aspose.Cells 8.9.0
type: docs
weight: 310
url: /sv/java/public-api-changes-in-aspose-cells-8-9-0/
---
{{% alert color="primary" %}} 

Det här dokumentet beskriver ändringarna av Aspose.Cells API från version 8.8.3 till 8.9.0 som kan vara av intresse för modul-/applikationsutvecklare. Den innehåller inte bara nya och uppdaterade offentliga metoder, tillagda och borttagna klasser etc., utan också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Lade till API:er**
### **Lagt till egenskapen HtmlSaveOptions.DefaultFontName**
Aspose.Cells for Java 8.9.0 har exponerat egenskapen DefaultFontName för klassen HtmlSaveOptions som gör det möjligt att ange standardteckensnittsnamnet samtidigt som kalkylblad renderas till formatet HTML. Standardteckensnittet kommer endast att användas när stiltypsnittet inte finns. Standardvärdet för egenskapen HtmlSaveOptions.DefaultFontName är null, vilket betyder att Aspose.Cells for Java API kommer att använda det universella teckensnittet som har samma familj som det ursprungliga teckensnittet.

{{% alert color="primary" %}} 

 För mer information om den här funktionen, läs artikeln om[Ställ in standardteckensnitt för rendering av kalkylblad till HTML-format](/cells/sv/java/set-default-font-while-rendering-spreadsheet-to/).

{{% /alert %}} 

Följande är det enkla användningsscenariot.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of HtmlSaveOptions

HtmlSaveOptions options = new HtmlSaveOptions();

//Set default font name for Html rendering

options.setDefaultFontName("Arial");

//Load a spreadsheet in an instance of Workbook

Workbook book = new Workbook(dir + "sample.xlsx");

//Save the spreadsheet in Html format while passing instance of HtmlSaveOptions

book.save(dir + "output.html", options);

{{< /highlight >}}
### **Lagt till egenskapen ImageOrPrintOptions.DefaultFont**
 Aspose.Cells for Java 8.9.0 tillåter att ställa in standardteckensnittsnamnet för klassen ImageOrPrintOptions genom att exponera egenskapen DefaultFont. Den nämnda egenskapen kan användas när Unicode-tecken i kalkylarket inte är inställda med korrekt typsnitt i cellstil, därför kan sådana tecken visas som block i de resulterande bilderna.

{{% alert color="primary" %}} 

 Ställ in egenskapen DefaultFont till MingLiu eller MS Gothic för att visa Unicode-tecken. Om egenskapen inte är inställd kommer Aspose.Cells att använda systemets standardteckensnitt för att visa Unicode-tecken.

{{% /alert %}} {{% alert color="primary" %}} 

 För mer information om den här funktionen, läs artikeln om[Ställa in standardteckensnitt för rendering av kalkylblad i bildformat](/cells/sv/java/set-default-font-while-rendering-spreadsheet-to-images/).

{{% /alert %}} 

Följande är det enkla användningsscenariot.

**Java**

{{< highlight "csharp" >}}

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
### **Lade till pivottabell.Excel2003kompatibel egendom**
Aspose.Cells for Java API har exponerat den booleska typen Excel2003Compatible-egenskapen för PivotTable-klassen som gör det möjligt att ange om pivottabellen är Excel 2003-kompatibel för uppdateringsändamål. Standardvärdet för egenskapen Excel2003Compatible är sant, det betyder att en sträng måste vara mindre än eller lika med 255 tecken. Om strängen är större än 255 tecken kommer den att trunkeras. Om det är falskt kommer den ovannämnda begränsningen inte att införas.

{{% alert color="primary" %}} 

 För mer information om den här funktionen, läs artikeln om[Kompatibilitet för Excel 2003 för att uppdatera pivottabeller](/cells/sv/java/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/).

{{% /alert %}} 

Följande är det enkla användningsscenariot.

**Java**

{{< highlight "csharp" >}}

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
