---
title: Offentliga API ändringar i Aspose.Cells 8.4.0
type: docs
weight: 130
url: /sv/net/public-api-changes-in-aspose-cells-8-4-0/
---

{{% alert color="primary" %}} 

Detta dokument beskriver ändringarna i Aspose.Cells API från version 8.3.2 till 8.4.0 som kan vara av intresse för modul/apputvecklare. Det inkluderar inte bara nya och uppdaterade offentliga metoder, [tillagda klasser osv.](/cells/sv/net/public-api-changes-in-aspose-cells-8-4-0/) och [borttagna klasser osv.](/cells/sv/net/public-api-changes-in-aspose-cells-8-4-0/), utan också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Tillagda API:er**
### **Mekanism för att ändra VBA/Makronkod i kalkylblad**
För att tillhandahålla funktionen för [VBA/Makronkodsmanipulation](/cells/sv/net/modifying-vba-or-macro-code-using-aspose-cells/) har Aspose.Cells for .NET 8.4.0 exponerat en serie nya klasser och egenskaper i Aspose.Cells.Vba-namnområdet. Några av de viktiga detaljerna om dessa nya klasser är följande.

- VbaProject-klassen kan användas för att hämta VBA-projektet från ett givet kalkylblad.
- VbaModuleCollection-klassen representerar samlingen av VBA-moduler som ingår i ett givet VbaProject.
- VbaModule-klassen representerar en enskild modul från VbaModuleCollection.

Följande kodsnutt visar hur du dynamiskt modifierar VBA-kodsegmenten.

**C#**

{{< highlight csharp >}}

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
Aspose.Cells for .NET 8.4.0 har exponerat två metoder för PivotTableCollection för att tillhandahålla funktionen för att ta bort pivottabell från en given kalkyl. Detaljerna för ovanstående metoder är som följer.

- Pivottabellcollection.Remove-metoden tar emot ett objekt av Pivottabell och tar bort den från samlingen.
- Pivottabellcollection.RemoveAt-metoden tar emot ett nollindexbaserat heltalsvärde och tar bort den specifika Pivottabellen från samlingen.

Följande kodsnutt visar hur du tar bort pivottabellen med båda ovan nämnda metoderna.

**C#**

{{< highlight csharp >}}

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


### **Stöd för olika pivottabellayouts**
Aspose.Cells for .NET 8.4.0 ger stöd för olika fördefinierade layouts för pivottabeller. För att tillhandahålla denna funktion har Aspose.Cells API:er exponerat tre metoder för Pivottabellklassen enligt nedan.

- Pivottabell.ShowInCompactForm-metoden renderar pivottabellen i kompakt layout.
- Metoden PivotTable.ShowInOutlineForm renderar Pivot-tabellen i översiktslayout.
- Metoden PivotTable.ShowInTabularForm renderar Pivot-tabellen i tabellayout.

{{% alert color="primary" %}} 

Det är viktigt att anropa PivotTable.RefreshData & PivotTable.CalculateData efter att ha ställt in någon av ovan nämnda layouter.

{{% /alert %}} 

Följande exempelkod ställer in olika layouter för en pivottabell och lagrar resultatet på skivan.

**C#**

{{< highlight csharp >}}

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


### **Klass TxtLoadStyleStrategy & Egenskap TxtLoadOptions.LoadStyleStrategy Tillagd**
Aspose.Cells for .NET 8.4.0 har exponerat klassen TxtLoadStyleStrategy och egenskapen TxtLoadOptions.LoadStyleStrategy för att specificera strategin för att formatera de analyserade värdena vid konvertering av strängvärde till nummer eller datumtid.
### **Tillagd DataBar.ToImage Metod**
Med utgåvan av v8.4.0 har Aspose.Cells API tillhandahållit DataBar.ToImage-metoden för att spara villkorligt formaterade DataBars i bildformat. Metoden {DataBar.ToImage}} godtar två parametrar enligt nedan.

- Den första parametern är av typen Aspose.Cells.Cell på vilken villkorlig formatering har tillämpats.
- Den andra parametern är av typen Aspose.Cells.Rendering.ImageOrPrintOptions för att ställa in olika parametrar för den resulterande bilden.

Följande exempelkod visar användningen av DataBar.ToImage-metoden för att rendera DataBar i bildformat.

**C#**

{{< highlight csharp >}}

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

byte[] imgBytes = dbar.ToImage(cell, opts);

//Write image bytes on the disk

File.WriteAllBytes("databar.png", imgBytes);

{{< /highlight >}}


### **Tillagd Border.ThemeColor Egenskap**
Aspose.Cells API:er tillåter att extrahera tema relaterad formateringsdata från kalkylbladen. Med utgåvan av Aspose.Cells for .NET 8.4.0, har API:et exponerat Border.ThemeColor-egenskapen som kan användas för att hämta färgattributen för cellgränserna.
### **Tillagd DrawObject.ImageBytes Egenskap**
Aspose.Cells for .NET 8.4.0 har exponerat DrawObject.ImageBytes-egenskapen för att hämta bilddata från diagram eller form.
### **Tillagd HtmlSaveOptions.ExportBogusRowData Egenskap**
Aspose.Cells for .NET 8.4.0 har tillhandahållit {HtmlSaveOptions.ExportBogusRowData}}-egenskapen. Egenskapen av typen Boolesk bestämmer om API:et ska infoga falska bottendata vid export av kalkylblad till HTML-format.

{{% alert color="primary" %}} 

Standardvärdet är sant.

{{% /alert %}} 

Följande exempelkod illustrerar användningen av ovan nämnda egenskap.

**C#**

{{< highlight csharp >}}

 //Create an object of HtmlSaveOptions class

HtmlSaveOptions options = new HtmlSaveOptions();

//Set the ExportBogusRowData to true

options.ExportBogusRowData = true;

//Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Save the workbook

workbook.Save("output.xlsx");

{{< /highlight >}}


### **Tillagd HtmlSaveOptions.CellCssPrefix Egenskap**
Nyinlagd egenskap HtmlSaveOptions.CellCssPrefix låter dig ange prefix för CSS-filer vid export av kalkylblad till HTML-format.

{{% alert color="primary" %}} 

Standardvärdet är "" (tom sträng).

{{% /alert %}}
## **Obsoletterade API:er**
### **Föråldrade Cells.GetCellByIndex & Row.GetCellByIndex-metoder**
Använd GetEnumerator-metoden för att iterera igenom alla celler istället.
### **Utgånget DrawObject.Image Egenskap**
Använd DrawObject.ImageBytes-egenskapen för att hämta bilddata istället.
{{< app/cells/assistant language="csharp" >}}
