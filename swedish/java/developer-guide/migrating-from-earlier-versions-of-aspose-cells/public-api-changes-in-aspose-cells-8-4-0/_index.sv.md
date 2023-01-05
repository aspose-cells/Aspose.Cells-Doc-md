---
title: Offentlig API Ändringar i Aspose.Cells 8.4.0
type: docs
weight: 140
url: /sv/java/public-api-changes-in-aspose-cells-8-4-0/
---
{{% alert color="primary" %}} 

Det här dokumentet beskriver ändringarna av Aspose.Cells API från version 8.3.2 till 8.4.0 som kan vara av intresse för modul-/applikationsutvecklare. Det inkluderar inte bara nya och uppdaterade offentliga metoder,[lagt till klasser etc.](/cells/sv/java/public-api-changes-in-aspose-cells-8-4-0/) och[borttagna klasser osv.](/cells/sv/java/public-api-changes-in-aspose-cells-8-4-0/), men också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Lade till API:er**
### **Mekanism för att ändra VBA/makrokoden i kalkylblad**
 För att ge funktionen av[VBA/makrokodshantering](/cells/sv/java/modifying-vba-or-macro-code-using-aspose-cells/), Aspose.Cells for Java 8.4.0 har exponerat en serie nya klasser och egenskaper i paketet com.aspose.cells.Vba. Några av de viktiga detaljerna i dessa nya klasser är följande.

- VbaProject-klassen kan användas för att hämta VBA-projektet från ett givet kalkylblad.
- Klassen VbaModuleCollection representerar samlingen av VBA-moduler som är en del av ett givet VbaProject.
- VbaModule-klassen representerar en enda modul från VbaModuleCollection.

Följande kodavsnitt visar hur du dynamiskt ändrar VBA-kodsegmenten.

**Java**

{{< highlight "csharp" >}}

 Workbook workbook = new Workbook("source.xlsm");

//Ändra VBA-modulkoden

VbaModuleCollection modules = workbook.getVbaProject().getModules();

 for(int i=0; i< modules.getCount(); i++)

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
Aspose.Cells for Java 8.4.0 har visat två metoder för PivotTableCollection för att tillhandahålla funktionen för borttagning av pivottabell från ett givet kalkylblad. Detaljerna för ovannämnda metoder är som följer.

- Metoden PivotTableCollection.remove accepterar ett objekt från PivotTable och tar bort det från samlingen.
- PivotTableCollection.removeAt-metoden accepterar ett nollindexbaserat heltalsvärde och tar bort den specifika pivottabellen från samlingen.

Följande kodavsnitt visar hur du tar bort pivottabellen med båda ovan nämnda metoder.

**Java**

{{< highlight "csharp" >}}

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
### **Stöd för olika pivottabellslayouter**
Aspose.Cells for Java 8.4.0 ger stöd för olika fördefinierade layouter för pivottabeller. För att tillhandahålla den här funktionen har API:erna Aspose.Cells exponerat tre metoder för PivotTable-klassen som beskrivs nedan.

- Metoden PivotTable.showInCompactForm återger pivottabellen i kompakt layout.
- Metoden PivotTable.showInOutlineForm återger pivottabellen i Outline-layouten.
- Metoden PivotTable.showInTabularForm återger pivottabellen i tabelllayout.

{{% alert color="primary" %}} 

 Det är viktigt att anropa PivotTable.refreshData & PivotTable.calculateData efter att ha ställt in någon av de ovan nämnda layouterna.

{{% /alert %}} 

Följande exempelkod ställer in olika layouter för en pivottabell och lagrar resultatet på skivan.

**Java**

{{< highlight "csharp" >}}

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
### **Klass TxtLoadStyleStrategy & Property TxtLoadOptions.LoadStyleStrategy tillagd**
Aspose.Cells for Java 8.4.0 har exponerat klassen TxtLoadStyleStrategy och TxtLoadOptions.LoadStyleStrategy-egenskapen för att specificera strategin för att formatera de analyserade värdena samtidigt som strängvärdet konverteras till nummer eller datum och tid.
### **Metod DataBar.ToImage tillagd**
Med lanseringen av v8.4.0 har Aspose.Cells API tillhandahållit DataBar.toImage-metoden för att spara den villkorligt formaterade DataBar i bildformat. Metoden {DataBar.toImage}} accepterar två parametrar som beskrivs nedan.

- Den första parametern är av typen com.aspose.cells.Cell på vilken villkorlig formatering har tillämpats.
- Den andra parametern är av typen com.aspose.cells.rendering.ImageOrPrintOptions för att ställa in olika parametrar för den resulterande bilden.

Följande exempelkod visar användningen av DataBar.toImage-metoden för att rendera DataBar i bildformat.

**Java**

{{< highlight "csharp" >}}

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

byte[]imgBytes = dbar.toImage(cell, opts);

//Write image bytes on the disk

FileOutputStream out = new FileOutputStream("databar.png");

out.write(imgBytes);

out.close();

{{< /highlight >}}
### **Egenskap Border.ThemeColor tillagd**
Aspose.Cells API:er gör det möjligt att extrahera temarelaterade data från kalkylarken. Med lanseringen av Aspose.Cells for Java 8.4.0 har API exponerat egenskapen Border.ThemeColor som kan användas för att hämta temafärgsattributen för Cell kanter.
### **Egenskapen DrawObject.ImageBytes tillagd**
Aspose.Cells for Java 8.4.0 har exponerat egenskapen DrawObject.ImageBytes för att hämta bilddata från Chart eller Shape.
### **Egenskapen HtmlSaveOptions.ExportBogusRowData tillagd**
 Aspose.Cells for Java 8.4.0 har tillhandahållit egenskapen {HtmlSaveOptions.ExportBogusRowData}}. Egenskapen boolesk typ avgör om API kommer att injicera falska nedre raddata när kalkylark exporteras till formatet HTML.

{{% alert color="primary" %}} 

Standardvärdet är sant.

{{% /alert %}} 

Följande exempelkod illustrerar användningen av ovannämnda egendom.

**Java**

{{< highlight "csharp" >}}

 //Create an object of HtmlSaveOptions class

HtmlSaveOptions options = new HtmlSaveOptions();

//Set the ExportBogusRowData to true

options.ExportBogusRowData = true;

//Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Save the workbook

workbook.save("output.xlsx");

{{< /highlight >}}
### **Egenskapen HtmlSaveOptions.CellCssPrefix har lagts till**
Nyligen tillagd egenskap HtmlSaveOptions.CellCssPrefix gör det möjligt att ställa in prefixet för CSS-filerna samtidigt som kalkylblad exporteras till formatet HTML.

{{% alert color="primary" %}} 

Standardvärdet är "" (tom sträng).

{{% /alert %}}
## **Föråldrade API:er**
### **Metoder Cells.getCellByIndex & Row.getCellByIndex Obsoleted**
Använd metoden getEnumerator för att iterera alla celler istället.
### **Egenskapen DrawObject.Image Obsoleted**
Använd egenskapen DrawObject.ImageBytes för att hämta bilddata istället.
