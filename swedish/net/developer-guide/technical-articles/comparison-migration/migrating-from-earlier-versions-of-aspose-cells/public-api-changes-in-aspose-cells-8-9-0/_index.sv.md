---
title: Förändringar i den offentliga API et i Aspose.Cells 8.9.0
type: docs
weight: 300
url: /sv/net/public-api-changes-in-aspose-cells-8-9-0/
---

{{% alert color="primary" %}} 

Detta dokument beskriver förändringarna i Aspose.Cells API från version 8.8.3 till 8.9.0 som kan vara av intresse för modul/applikationsutvecklare. Det inkluderar inte bara nya och uppdaterade offentliga metoder, tillagda och borttagna klasser etc., utan också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Tillagda API:er**
### **Lade till HtmlSaveOptions.DefaultFontName Egenskap**
Aspose.Cells for .NET 8.9.0 har utsatt DefaultFontName-egenskapen för HtmlSaveOptions-klassen som tillåter att specificera standardfontnamnet vid rendering av kalkylblad till HTML-format. Standardfonten kommer endast att användas när stilen inte existerar. Standardvärdet för HtmlSaveOptions.DefaultFontName-egenskapen är null vilket betyder att Aspose.Cells for .NET API:et kommer att använda den universella fonten som har samma familj som originalfonten.

{{% alert color="primary" %}} 

För mer information om den här funktionen, vänligen granska artikeln om [Ställa in standardfont vid rendering av kalkylblad till HTML-format](/cells/sv/net/set-default-font-while-rendering-spreadsheet-to/).

{{% /alert %}} 

Följande är det enkla användningscenariot.

**C#**

{{< highlight csharp >}}

 // Create an instance of HtmlSaveOptions

var options = new HtmlSaveOptions();

// Set default font name for Html rendering

options.DefaultFontName = "Arial";

// Load a spreadsheet in an instance of Workbook

var book = new Workbook(dir + "sample.xlsx");

// Save the spreadsheet in Html format while passing instance of HtmlSaveOptions

book.Save(dir + "output.html", options);

{{< /highlight >}}


### **Lade till ImageOrPrintOptions.DefaultFont Egenskap**
Aspose.Cells for .NET 8.9.0 tillåter att ställa in standardfontnamnet för ImageOrPrintOptions-klassen genom att exponera DefaultFont-egenskapen. Den nämnda egenskapen kan användas när Unicode-tecken i kalkylarket inte är inställda med korrekt font i cellstil, sådana tecken kan visas som block i resulterande bilder.

{{% alert color="primary" %}} 

Sätt DefaultFont egenskapen till MingLiu eller MS Gothic för att visa Unicode-tecken. Om den tidigare nämnda egenskapen inte är satt, kommer Aspose.Cells att använda systemets standardfont för att visa Unicode-tecken.

{{% /alert %}} {{% alert color="primary" %}} 

För mer detaljer om denna funktion, vänligen granska artikeln om [Inställning av standardfont för att rendera kalkylblad i bildformat](/cells/sv/net/set-default-font-while-rendering-spreadsheet-to-images/).

{{% /alert %}} 

Följande är det enkla användningscenariot.

**C#**

{{< highlight csharp >}}

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


### **Tillagd PivotTable.IsExcel2003Compatible Egenskap**
Aspose.Cells for .NET API har exponerat den booleska typen IsExcel2003Compatible-egenskap för PivotTable-klassen som tillåter att ange om PivotTable är kompatibel med Excel 2003 för uppdateringsändamål. Standardvärdet för IsExcel2003Compatible-egenskapen är sant, vilket innebär att en sträng måste vara mindre än eller lika med 255 tecken. Om strängen är större än 255 tecken kommer den att bli avkortad. Om falskt, kommer den nämnda begränsningen inte att gälla.

{{% alert color="primary" %}} 

För mer detaljer om denna funktion, vänligen granska artikeln om [Kompatibilitet för Excel 2003 för uppdatering av pivottabeller](https://docs.aspose.com/cells/net/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/).

{{% /alert %}} 

Följande är det enkla användningscenariot.

**C#**

{{< highlight csharp >}}

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


### **Tillagd GridWeb.GetVersion Metod**
Aspose.Cells.GridWeb för .NET 8.9.0 har exponerat {GetVersion}} fabriksmetoden som returnerar utgåva av GridWeb-komponenten.
