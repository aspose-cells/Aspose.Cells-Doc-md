---
title: Offentlig API Ändringar i Aspose.Cells 8.9.0
type: docs
weight: 300
url: /sv/net/public-api-changes-in-aspose-cells-8-9-0/
---
{{% alert color="primary" %}} 

Det här dokumentet beskriver ändringarna av Aspose.Cells API från version 8.8.3 till 8.9.0 som kan vara av intresse för modul-/applikationsutvecklare. Den innehåller inte bara nya och uppdaterade offentliga metoder, tillagda och borttagna klasser etc., utan också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Lade till API:er**
### **Lagt till egenskapen HtmlSaveOptions.DefaultFontName**
Aspose.Cells for .NET 8.9.0 har exponerat egenskapen DefaultFontName för klassen HtmlSaveOptions som gör det möjligt att ange standardteckensnittsnamnet samtidigt som kalkylblad renderas till formatet HTML. Standardteckensnittet kommer endast att användas när stiltypsnittet inte finns. Standardvärdet för egenskapen HtmlSaveOptions.DefaultFontName är null, vilket betyder att Aspose.Cells for .NET API kommer att använda det universella teckensnittet som har samma familj som det ursprungliga teckensnittet.

{{% alert color="primary" %}} 

 För mer information om den här funktionen, läs artikeln om[Ställ in standardteckensnitt för rendering av kalkylblad till HTML-format](/cells/sv/net/set-default-font-while-rendering-spreadsheet-to/).

{{% /alert %}} 

Följande är det enkla användningsscenariot.

**C#**

{{< highlight "csharp" >}}

 // Create an instance of HtmlSaveOptions

var options = new HtmlSaveOptions();

// Set default font name for Html rendering

options.DefaultFontName = "Arial";

// Load a spreadsheet in an instance of Workbook

var book = new Workbook(dir + "sample.xlsx");

// Save the spreadsheet in Html format while passing instance of HtmlSaveOptions

book.Save(dir + "output.html", options);

{{< /highlight >}}


### **Lagt till egenskapen ImageOrPrintOptions.DefaultFont**
Aspose.Cells for .NET 8.9.0 tillåter att ställa in standardteckensnittsnamnet för klassen ImageOrPrintOptions genom att exponera egenskapen DefaultFont. Den nämnda egenskapen kan användas när Unicode-tecken i kalkylarket inte är inställda med korrekt typsnitt i cellstil, därför kan sådana tecken visas som block i de resulterande bilderna.

{{% alert color="primary" %}} 

Ställ in egenskapen DefaultFont till MingLiu eller MS Gothic för att visa Unicode-tecken. Om egenskapen inte är inställd kommer Aspose.Cells att använda systemets standardteckensnitt för att visa Unicode-tecken.

{{% /alert %}} {{% alert color="primary" %}} 

 För mer information om den här funktionen, läs artikeln om[Ställa in standardteckensnitt för rendering av kalkylblad i bildformat](/cells/sv/net/set-default-font-while-rendering-spreadsheet-to-images/).

{{% /alert %}} 

Följande är det enkla användningsscenariot.

**C#**

{{< highlight "csharp" >}}

 // Create an instance of ImageOrPrintOptions

var options = new ImageOrPrintOptions();

// Set default font name for image rendering

options.DefaultFont = "Arial";

// Load a spreadsheet in an instance of Workbook

var book = new Workbook(dir + "sample.xlsx");

// Access the worksheet to be rendered

var sheet = book.Worksheets[0];

// Create an instance of SheetRender

var render = new SheetRender(sheet, options);

// Save spreadsheet to image

render.ToImage(0, dir + "output.png");

{{< /highlight >}}


### **Lade till PivotTable.IsExcel2003Compatible Property**
Aspose.Cells for .NET API har exponerat den booleska typen IsExcel2003Compatible-egenskapen för PivotTable-klassen som gör det möjligt att ange om PivotTable är Excel 2003-kompatibel för uppdateringsändamål. Standardvärdet för egenskapen IsExcel2003Compatible är sant, det betyder att en sträng måste vara mindre än eller lika med 255 tecken. Om strängen är större än 255 tecken kommer den att trunkeras. Om det är falskt kommer den ovannämnda begränsningen inte att införas.

{{% alert color="primary" %}} 

 För mer information om den här funktionen, läs artikeln om[Kompatibilitet för Excel 2003 för att uppdatera pivottabeller](https://docs.aspose.com/cells/net/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/).

{{% /alert %}} 

Följande är det enkla användningsscenariot.

**C#**

{{< highlight "csharp" >}}

 // Load a spreadsheet in an instance of Workbook

var book = new Workbook(dir + "sample.xlsx");

// Access the desired Pivot Table from the spreadsheet

var pivot = book.Worksheets[0].PivotTables[0];

// Set Excel 2003 compatibility to false

pivot.IsExcel2003Compatible = false;

// Refresh & recalculate Pivot Table

pivot.RefreshData();

pivot.CalculateData();

{{< /highlight >}}


### **Lade till metoden GridWeb.GetVersion**
Aspose.Cells.GridWeb for .NET 8.9.0 har exponerat fabriksmetoden {GetVersion}} som returnerar releaseversionen av GridWeb-komponenten.
