---
title: Offentlig API Ändringar i Aspose.Cells 8.8.2
type: docs
weight: 280
url: /sv/net/public-api-changes-in-aspose-cells-8-8-2/
---
{{% alert color="primary" %}} 

Det här dokumentet beskriver ändringarna av Aspose.Cells API från version 8.8.1 till 8.8.2 som kan vara av intresse för modul-/applikationsutvecklare. Den innehåller inte bara nya och uppdaterade offentliga metoder, tillagda och borttagna klasser etc., utan också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Lade till API:er**
### **Uppdatera referenser automatiskt medan du tar bort tomma rader och kolumner**
Aspose.Cells for .NET 8.8.2 har avslöjat de överbelastade versionerna av metoderna Cells.DeleteBlankRows & Cells.DeleteBlankColumns. De nya metoderna kan acceptera en instans av DeleteOptions-klassen och kan användas för att övervinna de situationer som kan uppstå på grund av de trasiga referenserna i formler, diagramseriedata och så vidare. Klassen DeleteOptions har för närvarande bara en medlem, en egenskap av boolesk typ med namnet UpdateReference. Om egenskapen är satt till true och instansen av DeleteOptions-klassen skickas till metoderna Cells.DeleteBlankRows & Cells.DeleteBlankColumns, kommer API internt att justera formelreferenserna (om några) för att anpassas till ändringarna.

{{% alert color="primary" %}} 

 För mer information om den här funktionen, läs den detaljerade artikeln om[Ta bort tomma rader och kolumner med uppdaterade referenser](/cells/sv/net/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/).

{{% /alert %}} 

Följande är det enkla användningsscenariot.

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook & load an existing spreadsheet

var book = new Workbook(dir + "sample.xlsx");

//Access worksheet from which blank rows/columns have to be deleted

var sheet = book.Worksheets[0];

//Access cells of the desired worksheet

var cells = sheet.Cells;

//Create an instance of DeleteOptions class

DeleteOptions options = new DeleteOptions();

//Set UpdateReference property to true;

options.UpdateReference = true;

//Delete all blank rows and columns

cells.DeleteBlankColumns(options);

cells.DeleteBlankRows(options);

{{< /highlight >}}
