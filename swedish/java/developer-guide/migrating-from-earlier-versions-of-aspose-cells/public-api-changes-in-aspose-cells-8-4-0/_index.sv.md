---
title: Offentliga API ändringar i Aspose.Cells 8.4.0
type: docs
weight: 140
url: /sv/java/public-api-changes-in-aspose-cells-8-4-0/
---

{{% alert color="primary" %}} 

Detta dokument beskriver ändringar i Aspose.Cells API från version 8.3.2 till 8.4.0 som kan vara av intresse för modul/apputvecklare. Det inkluderar inte bara nya och uppdaterade offentliga metoder, [tillagda klasser etc.](/cells/sv/java/public-api-changes-in-aspose-cells-8-4-0/) och [borttagna klasser etc.](/cells/sv/java/public-api-changes-in-aspose-cells-8-4-0/), men också en beskrivning av eventuella ändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Tillagda API:er**
### **Mekanism för att ändra VBA/Makronkod i kalkylblad**
För att tillhandahålla funktionen [VBA/Macro Code Manipulation](/cells/sv/java/modifying-vba-or-macro-code-using-aspose-cells/), har Aspose.Cells for Java 8.4.0 exponerat en serie nya klasser och egenskaper i paketet com.aspose.cells.Vba. Några av de viktiga detaljerna för dessa nya klasser är som följer.

- VbaProject-klassen kan användas för att hämta VBA-projektet från ett givet kalkylblad.
- VbaModuleCollection-klassen representerar samlingen av VBA-moduler som ingår i ett givet VbaProject.
- VbaModule-klassen representerar en enskild modul från VbaModuleCollection.

Följande kodsnutt visar hur du dynamiskt modifierar VBA-kodsegmenten.

**Java**

{{< highlight csharp >}}

 Workbook workbook = new Workbook("source.xlsm");

//Change the VBA Module Code

VbaModuleCollection modules = workbook.getVbaProject().getModules();

for(int i=0; i < modules.getCount(); i++)

{

	VbaModule module = modules.get(i);

    String code = module.getCodes();

    //Replace the original message with the modified message

    if (code.contains("This is test message."))

    {

        code = code.replace("This is test message.", "This is Aspose.Cells message.");

        module.setCodes(code);

    }

}

//Save the output Excel file

workbook.save("output.xlsm");

{{< /highlight >}}
### **Möjlighet att ta bort pivottabell**
Aspose.Cells for Java 8.4.0 har exponerat två metoder för PivotTableCollection för att tillhandahålla funktionen för att ta bort Pivot-tabell från ett givet kalkylblad. Detaljer för ovan nämnda metoder är som följer.

- PivotTableCollection.remove metoden accepterar ett objekt av typen PivotTable, och tar bort den från samlingen.
- PivotTableCollection.removeAt metoden accepterar ett nollindexbaserat heltal och tar bort den särskilda Pivot-tabellen från samlingen.

Följande kodsnutt visar hur du tar bort pivottabellen med båda ovan nämnda metoderna.

**Java**

{{< highlight csharp >}}

 //Create workbook object from source Excel file

Workbook workbook = new Workbook("source.xlsx");

//Access the first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access the first pivot table object

PivotTable pivotTable = worksheet.getPivotTables().get(0);

//Remove pivot table using pivot table object

worksheet.getPivotTables().remove(pivotTable);

//Remove pivot table using pivot table position

worksheet.getPivotTables().removeAt(0);

//Save the workbook

workbook.save("output.xlsx");

{{< /highlight >}}
### **Stöd för olika pivottabellayouts**
Aspose.Cells for Java 8.4.0 tillhandahåller stöd för olika fördefinierade layouter för Pivot-tabeller. För att tillhandahålla denna funktion har Aspose.Cells API:erna exponerat tre metoder för klassen PivotTable enligt nedan.

- PivotTable.showInCompactForm metoden renderar Pivot-tabellen i kompakt layout.
- PivotTable.showInOutlineForm metoden renderar Pivot-tabellen i översiktslayout.
- Metoden PivotTable.showInTabularForm renderar pivottabellen i tabellayout.

{{% alert color="primary" %}} 

Det är viktigt att ringa PivotTable.refreshData & PivotTable.calculateData efter att ha ställt in någon av ovan nämnda layouter. 

{{% /alert %}} 

Följande exempelkod ställer in olika layouter för en pivottabell och lagrar resultatet på skivan.

**Java**

{{< highlight csharp >}}

 //Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access first pivot table

PivotTable pivotTable = worksheet.getPivotTables().get(0);

//1 - Show the pivot table in compact form

pivotTable.showInCompactForm();

//Refresh the pivot table

pivotTable.refreshData();

pivotTable.calculateData();

//Save the output

workbook.save("CompactForm.xlsx");

//2 - Show the pivot table in outline form

pivotTable.showInOutlineForm();

//Refresh the pivot table

pivotTable.refreshData();

pivotTable.calculateData();

//Save the output

workbook.save("OutlineForm.xlsx");

//3 - Show the pivot table in tabular form

pivotTable.showInTabularForm();

//Refresh the pivot table

pivotTable.refreshData();

pivotTable.calculateData();

//Save the output

workbook.save("TabularForm.xlsx");

{{< /highlight >}}
### **Klass TxtLoadStyleStrategy & Egenskap TxtLoadOptions.LoadStyleStrategy Tillagd**
Aspose.Cells for Java 8.4.0 har exponerat klassen TxtLoadStyleStrategy och egenskapen TxtLoadOptions.LoadStyleStrategy för att ange strategin för att formatera de parserade värdena vid konvertering av strängvärde till nummer eller datumtid.
### **Tillagd DataBar.ToImage Metod**
Med utgivningen av v8.4.0 har Aspose.Cells API tillhandahållit metoden DataBar.toImage för att spara villkorligt formaterade DataBar i bildformat. {DataBar.toImage}} metoden accepterar två parametrar enligt nedan.

- Den första parametern är av typen com.aspose.cells.Cell på vilken villkorlig formatering har tillämpats.
- Den andra parametern är av typen com.aspose.cells.rendering.ImageOrPrintOptions för att ange olika parametrar för den resulterande bilden.

Följande exempelkod visar användningen av DataBar.toImage-metoden för att rendera DataBar i bildformat.

**Java**

{{< highlight csharp >}}

 //Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access the cell which contains conditional formatting databar

Cell cell = worksheet.getCells().get("C1");

//Get the conditional formatting of the cell

FormatConditionCollection fcc = cell.getFormatConditions();

//Access the conditional formatting databar

DataBar dbar = fcc.get(0).getDataBar();

//Create image or print options

ImageOrPrintOptions opts = new ImageOrPrintOptions();

opts.setImageFormat(ImageFormat.getPng());

//Get the image bytes of the databar

byte[] imgBytes = dbar.toImage(cell, opts);

//Write image bytes on the disk

FileOutputStream out = new FileOutputStream("databar.png");

out.write(imgBytes);

out.close();

{{< /highlight >}}
### **Tillagd Border.ThemeColor Egenskap**
Aspose.Cells API:er tillåter att extrahera temarelaterade data från kalkylbladen. Med utgivningen av Aspose.Cells for Java 8.4.0 har API:et exponerat Border.ThemeColor-egenskapen som kan användas för att hämta temafärgattributen för cellgränser.
### **Tillagd DrawObject.ImageBytes Egenskap**
Aspose.Cells for Java 8.4.0 har exponerat DrawObject.ImageBytes egenskapen för att hämta bilddata från diagram eller form.
### **Tillagd HtmlSaveOptions.ExportBogusRowData Egenskap**
Aspose.Cells for Java 8.4.0 har tillhandahållit {HtmlSaveOptions.ExportBogusRowData}} egenskapen. Boolesk typ egenskapen bestämmer om API kommer att infoga falska bottenradsdata vid export av kalkylblad till HTML-format. 

{{% alert color="primary" %}} 

Standardvärdet är sant.

{{% /alert %}} 

Följande exempelkod illustrerar användningen av ovan nämnda egenskap.

**Java**

{{< highlight csharp >}}

 //Create an object of HtmlSaveOptions class

HtmlSaveOptions options = new HtmlSaveOptions();

//Set the ExportBogusRowData to true

options.ExportBogusRowData = true;

//Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Save the workbook

workbook.save("output.xlsx");

{{< /highlight >}}
### **Tillagd HtmlSaveOptions.CellCssPrefix Egenskap**
Nyinlagd egenskap HtmlSaveOptions.CellCssPrefix låter dig ange prefix för CSS-filer vid export av kalkylblad till HTML-format.

{{% alert color="primary" %}} 

Standardvärdet är "" (tom sträng).

{{% /alert %}}
## **Obsoletterade API:er**
### **Utgångna Cells.getCellByIndex & Row.getCellByIndex Metoder**
Använd getEnumerator-metoden för att iterera alla celler istället.
### **Utgånget DrawObject.Image Egenskap**
Använd DrawObject.ImageBytes-egenskapen för att hämta bilddata istället.
{{< app/cells/assistant language="java" >}}
