---
title: Offentliga API-ändringar i Aspose.Cells 8.4.0
type: docs
weight: 130
url: /sv/net/public-api-changes-in-aspose-cells-8-4-0/
---
{{% alert color="primary" %}} 

Det här dokumentet beskriver ändringarna av Aspose.Cells API från version 8.3.2 till 8.4.0 som kan vara av intresse för modul-/applikationsutvecklare. Det inkluderar inte bara nya och uppdaterade offentliga metoder,[lagt till klasser etc.](/cells/sv/net/public-api-changes-in-aspose-cells-8-4-0/) och[borttagna klasser osv.](/cells/sv/net/public-api-changes-in-aspose-cells-8-4-0/), men också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Lade till API:er**
### **Mekanism för att ändra VBA/makrokoden i kalkylblad**
 För att ge funktionen av[VBA/makrokodshantering](/cells/sv/net/modifying-vba-or-macro-code-using-aspose-cells/), Aspose.Cells för .NET 8.4.0 har exponerat en serie nya klasser och egenskaper i namnområdet Aspose.Cells.Vba. Några av de viktiga detaljerna i dessa nya klasser är följande.

- VbaProject-klassen kan användas för att hämta VBA-projektet från ett givet kalkylblad.
- Klassen VbaModuleCollection representerar samlingen av VBA-moduler som är en del av ett givet VbaProject.
- VbaModule-klassen representerar en enda modul från VbaModuleCollection.

Följande kodavsnitt visar hur du dynamiskt ändrar VBA-kodsegmenten.

**C#**

{{< highlight "csharp" >}}

 //Create workbook object from source Excel file

Workbook workbook = new Workbook("source.xlsm");

//Change the VBA Module Code

foreach (VbaModule module in workbook.VbaProject.Modules)

{

    string code = module.Codes;

    //Replace the original message with the modified message

    if (code.Contains("This is test message."))

    {

        code = code.Replace("This is test message.", "This is Aspose.Cells message.");

        module.Codes = code;

    }

}

//Save the output Excel file

workbook.Save("output.xlsm");

{{< /highlight >}}


### **Möjlighet att ta bort pivottabell**
Aspose.Cells för .NET 8.4.0 har avslöjat två metoder för PivotTableCollection för att tillhandahålla funktionen för borttagning av pivottabell från ett givet kalkylblad. Detaljerna för ovannämnda metoder är som följer.

- Metoden PivotTableCollection.Remove accepterar ett objekt från PivotTable och tar bort det från samlingen.
- PivotTableCollection.RemoveAt-metoden accepterar ett nollindexbaserat heltalsvärde och tar bort den specifika pivottabellen från samlingen.

Följande kodavsnitt visar hur du tar bort pivottabellen med båda ovan nämnda metoder.

**C#**

{{< highlight "csharp" >}}

 //Create workbook object from source Excel file

Workbook workbook = new Workbook("source.xlsx");

//Access the first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access the first pivot table object

PivotTable pivotTable = worksheet.PivotTables[0];

//Remove pivot table using pivot table object

worksheet.PivotTables.Remove(pivotTable);

//Remove pivot table using pivot table position

worksheet.PivotTables.RemoveAt(0);

//Save the workbook

workbook.Save("output.xlsx");

{{< /highlight >}}


### **Stöd för olika pivottabellslayouter**
Aspose.Cells för .NET 8.4.0 ger stöd för olika fördefinierade layouter för pivottabeller. För att tillhandahålla den här funktionen har API:erna Aspose.Cells exponerat tre metoder för PivotTable-klassen som beskrivs nedan.

- PivotTable.ShowInCompactForm-metoden återger pivottabellen i kompakt layout.
- Metoden PivotTable.ShowInOutlineForm återger pivottabellen i Outline-layouten.
- Metoden PivotTable.ShowInTabularForm återger pivottabellen i tabelllayout.

{{% alert color="primary" %}} 

Det är viktigt att anropa PivotTable.RefreshData & PivotTable.CalculateData efter att ha ställt in någon av de ovan nämnda layouterna.

{{% /alert %}} 

Följande exempelkod ställer in olika layouter för en pivottabell och lagrar resultatet på skivan.

**C#**

{{< highlight "csharp" >}}

 //Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access first pivot table

PivotTable pivotTable = worksheet.PivotTables[0];

//Render the pivot table in compact form

pivotTable.ShowInCompactForm();

//Refresh the pivot table

pivotTable.RefreshData();

pivotTable.CalculateData();

//Save the output

workbook.Save("CompactForm.xlsx");

//Render the pivot table in outline form

pivotTable.ShowInOutlineForm();

//Refresh the pivot table

pivotTable.RefreshData();

pivotTable.CalculateData();

//Save the output

workbook.Save("OutlineForm.xlsx");

//Render the pivot table in tabular form

pivotTable.ShowInTabularForm();

//Refresh the pivot table

pivotTable.RefreshData();

pivotTable.CalculateData();

//Save the output

workbook.Save("TabularForm.xlsx");

{{< /highlight >}}


### **Klass TxtLoadStyleStrategy & Property TxtLoadOptions.LoadStyleStrategy tillagd**
Aspose.Cells för .NET 8.4.0 har exponerat klassen TxtLoadStyleStrategy och TxtLoadOptions.LoadStyleStrategy-egenskapen för att specificera strategin för att formatera de analyserade värdena samtidigt som strängvärdet konverteras till nummer eller datum och tid.
### **Metod DataBar.ToImage tillagd**
Med lanseringen av v8.4.0 har API:et Aspose.Cells tillhandahållit DataBar.ToImage-metoden för att spara de villkorligt formaterade DataBars i bildformat. Metoden {DataBar.ToImage}} accepterar två parametrar som beskrivs nedan.

- Den första parametern är av typen Aspose.Cells.Cell på vilken villkorlig formatering har tillämpats.
- Den andra parametern är av typen Aspose.Cells.Rendering.ImageOrPrintOptions för att ställa in olika parametrar för den resulterande bilden.

Följande exempelkod visar hur DataBar.ToImage-metoden används för att rendera DataBar i bildformat.

**C#**

{{< highlight "csharp" >}}

 //Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access the cell which contains conditional formatting databar

Cell cell = worksheet.Cells["C1"];

//Get the conditional formatting of the cell

FormatConditionCollection fcc = cell.GetFormatConditions();

//Access the conditional formatting databar

DataBar dbar = fcc[0].DataBar;

//Create image or print options

ImageOrPrintOptions opts = new ImageOrPrintOptions();

opts.ImageFormat = ImageFormat.Png;

//Get the image bytes of the databar

byte[]imgBytes = dbar.ToImage(cell, opts);

//Write image bytes on the disk

File.WriteAllBytes("databar.png", imgBytes);

{{< /highlight >}}


### **Egenskap Border.ThemeColor tillagd**
Aspose.Cells API:er gör det möjligt att extrahera temarelaterade formateringsdata från kalkylarken. I och med lanseringen av Aspose.Cells för .NET 8.4.0 har API:t exponerat egenskapen Border.ThemeColor som kan användas för att hämta temafärgsattributen för Cell-gränser.
### **Egenskapen DrawObject.ImageBytes tillagd**
Aspose.Cells för .NET 8.4.0 har exponerat egenskapen DrawObject.ImageBytes för att hämta bilddata från Chart eller Shape.
### **Egenskapen HtmlSaveOptions.ExportBogusRowData tillagd**
Aspose.Cells för .NET 8.4.0 har tillhandahållit egenskapen {HtmlSaveOptions.ExportBogusRowData}}. Egenskapen boolesk typ avgör om API kommer att injicera falska nedre raddata när kalkylark exporteras till HTML-format.

{{% alert color="primary" %}} 

Standardvärdet är sant.

{{% /alert %}} 

Följande exempelkod illustrerar användningen av ovannämnda egendom.

**C#**

{{< highlight "csharp" >}}

 //Create an object of HtmlSaveOptions class

HtmlSaveOptions options = new HtmlSaveOptions();

//Set the ExportBogusRowData to true

options.ExportBogusRowData = true;

//Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Save the workbook

workbook.Save("output.xlsx");

{{< /highlight >}}


### **Egenskapen HtmlSaveOptions.CellCssPrefix har lagts till**
Den nyligen tillagda egenskapen HtmlSaveOptions.CellCssPrefix gör det möjligt att ställa in prefixet för CSS-filerna samtidigt som kalkylblad exporteras till HTML-format.

{{% alert color="primary" %}} 

Standardvärdet är "" (tom sträng).

{{% /alert %}}
## **Föråldrade API:er**
### **Metoder Cells.GetCellByIndex & Row.GetCellByIndex Obsoleted**
Använd metoden GetEnumerator för att iterera alla celler istället.
### **Egenskapen DrawObject.Image Obsoleted**
Använd egenskapen DrawObject.ImageBytes för att hämta bilddata istället.
