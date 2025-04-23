---
title: Offentliga API ändringar i Aspose.Cells 8.8.2
type: docs
weight: 280
url: /sv/net/public-api-changes-in-aspose-cells-8-8-2/
---

{{% alert color="primary" %}} 

Detta dokument beskriver ändringarna av Aspose.Cells API från version 8.8.1 till 8.8.2 som kan vara av intresse för modul/apputvecklare. Det inkluderar inte bara nya och uppdaterade offentliga metoder, tillagda och borttagna klasser etc., men också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Tillagda API:er**
### **Uppdatera Referenser Automatiskt medan du Tar bort Tomma Rader & Kolumner**
Aspose.Cells for .NET 8.8.2 har exponerat överbelastade versioner av Cells.DeleteBlankRows & Cells.DeleteBlankColumns metoder. De nya metoderna kan acceptera en instans av DeleteOptions-klassen och kan användas för att övervinna situationer som kan uppstå på grund av brutna referenser i formler, diagramseriedata och så vidare. DeleteOptions-klassen har för närvarande endast en medlem, en Boolesk-typ egenskap med namnet UpdateReference. Om nämnda egenskap är inställd på true och instansen av DeleteOptions-klassen skickas till Cells.DeleteBlankRows & Cells.DeleteBlankColumns metoderna, kommer API:et internt justera formelreferenser (om några) för att ryma ändringarna.

{{% alert color="primary" %}} 

För mer information om denna funktion, vänligen se den detaljerade artikeln om [Ta bort Tomma Rader & Kolumner med Uppdaterade Referenser](/cells/sv/net/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/).

{{% /alert %}} 

Följande är det enkla användningscenariot.

**C#**

{{< highlight csharp >}}

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
{{< app/cells/assistant language="csharp" >}}
