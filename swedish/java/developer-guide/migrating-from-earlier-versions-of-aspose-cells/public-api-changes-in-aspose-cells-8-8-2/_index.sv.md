---
title: Offentliga API ändringar i Aspose.Cells 8.8.2
type: docs
weight: 290
url: /sv/java/public-api-changes-in-aspose-cells-8-8-2/
---

{{% alert color="primary" %}} 

Detta dokument beskriver ändringarna av Aspose.Cells API från version 8.8.1 till 8.8.2 som kan vara av intresse för modul/apputvecklare. Det inkluderar inte bara nya och uppdaterade offentliga metoder, tillagda och borttagna klasser etc., men också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Tillagda API:er**
### **Uppdatera automatiskt referenser vid borttagning av tomma rader och kolumner**
Aspose.Cells for Java 8.8.2 har exponerat de överbelastade versionerna av Cells.deleteBlankRows & Cells.deleteBlankColumns-metoderna. De nya metoderna kan acceptera en instans av DeleteOptions-klassen och kan användas för att övervinna situationer som kan uppstå på grund av de brutna referenserna i formler, diagramserie data och så vidare. DeleteOptions-klassen har för närvarande endast en medlem, en Boolean-typ egenskap med namnet UpdateReference. Om den angivna egenskapen är inställd på true och instansen av DeleteOptions-klassen skickas till Cells.deleteBlankRows & Cells.deleteBlankColumns metoderna, justerar API: et internt formelreferenserna (om några) för att rymma ändringarna. 

{{% alert color="primary" %}} 

För mer information om denna funktion, vänligen granska den detaljerade artikeln om [Radera tomma rader och kolumner med uppdaterade referenser](/cells/sv/java/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/).

{{% /alert %}} 

Följande är det enkla användningscenariot.

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook & load an existing spreadsheet

Workbook book = new Workbook(dir + "sample.xlsx");

//Access worksheet from which blank rows/columns have to be deleted

Worksheet sheet = book.getWorksheets().get(0);

//Access cells of the desired worksheet

Cells cells = sheet.getCells();

//Create an instance of DeleteOptions class

DeleteOptions options = new DeleteOptions();

//Set UpdateReference property to true;

options.setUpdateReference(true);

//Delete all blank rows and columns

cells.deleteBlankColumns(options);

cells.deleteBlankRows(options);

{{< /highlight >}}
