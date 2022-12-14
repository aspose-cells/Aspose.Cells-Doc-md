---
title: Offentliga API-ändringar i Aspose.Cells 8.0.1
type: docs
weight: 20
url: /sv/net/public-api-changes-in-aspose-cells-8-0-1/
---
{{% alert color="primary" %}} 

Dessa sidor listar offentliga API-ändringar som introducerades i Aspose.Cells 8.0.1. Den innehåller inte bara nya och föråldrade offentliga metoder, utan också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells som kan påverka befintlig kod. Varje beteende som introduceras som kan ses som en regression och modifierar existerande beteende är särskilt viktigt och dokumenteras här.

{{% /alert %}} 
## **MemorySetting-egenskap tillagd till Cells Klass**
Klassen Cells har exponerat MemorySetting-egenskapen som kan användas för att optimera minnesanvändningen för celldata och därmed minska den totala minneskostnaden. Följande exempel visar hur man skriver en stor data till ett kalkylblad i optimerat läge.

**C#**

{{< highlight "csharp" >}}

 //Instantiate a new Workbook

Workbook book = new Workbook();

//Set the memory preferences

book.Settings.MemorySetting = MemorySetting.MemoryPreference;

//To change the memory setting of existing sheets, please change memory setting for them manually:

Cells cells = book.Worksheets[0].Cells;

cells.MemorySetting = MemorySetting.MemoryPreference;

//Input large dataset into the cells of the worksheet

//Your code goes here

{{< /highlight >}}

Minnesinställningarna fungerar inte för standardarket som skapas automatiskt av Workbook-objektet. För att ändra minnesinställningarna för befintliga ark, använd minnesinställningen manuellt innan du utför någon datamanipulation.

{{% alert color="primary" %}} 

 Vänligen kontrollera den detaljerade artikeln om[Optimera minnet när du arbetar med stora datamängder](/cells/sv/net/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)

{{% /alert %}}
