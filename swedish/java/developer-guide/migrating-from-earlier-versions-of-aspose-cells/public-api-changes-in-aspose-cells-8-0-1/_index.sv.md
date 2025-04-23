---
title: Offentliga API ändringar i Aspose.Cells 8.0.1
type: docs
weight: 30
url: /sv/java/public-api-changes-in-aspose-cells-8-0-1/
---

{{% alert color="primary" %}} 

Dessa sidor listar offentliga API-ändringar som introducerades i Aspose.Cells 8.0.1. Det inkluderar inte bara nya och föråldrade offentliga metoder, utan också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells som kan påverka befintlig kod. Eventuellt beteende som kan betraktas som en regression och ändrar befintligt beteende är särskilt viktigt och dokumenteras här.

{{% /alert %}} 
## **MemorySetting-egenskapen tillagd till Cells-klassen**
Cells-klassen har exponerat setMemorySetting- och getMemorySetting-metoder som kan användas för att optimera minnesanvändningen för celldata och därmed minska den totala minneskostnaden. Följande exempel visar hur man skriver stora data till ett arbetsblad i optimerat läge.

**Java**

{{< highlight csharp >}}

 //Instantiate a new Workbook

Workbook book = new Workbook();

//Set the memory preferences

book.getSettings().setMemorySetting(MemorySetting.MEMORY_PREFERENCE);

//To change the memory setting of existing sheets, please change memory setting for them manually:

Cells cells = book.getWorksheets().get(0).getCells();

cells.setMemorySetting(MemorySetting.MEMORY_PREFERENCE);

//Input large dataset into the cells of the worksheet.

//Your code goes here

{{< /highlight >}}

{{% alert color="primary" %}} 

Minnesinställningarna fungerar inte automatiskt för det standardark som skapas automatiskt av Arbetsbok. För att ändra minnesinställningarna för befintliga ark, tillämpa minnesinställningarna manuellt innan några datamanipulationer utförs. 

{{% /alert %}} {{% alert color="primary" %}} 

Vänligen kontrollera den detaljerade artikeln om [Optimering av minne vid arbete med stora datamängder](/cells/sv/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
