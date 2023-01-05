---
title: Offentlig API Ändringar i Aspose.Cells 8.0.1
type: docs
weight: 30
url: /sv/java/public-api-changes-in-aspose-cells-8-0-1/
---
{{% alert color="primary" %}} 

Dessa sida listar offentliga API ändringar som infördes i Aspose.Cells 8.0.1. Den innehåller inte bara nya och föråldrade offentliga metoder, utan också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells som kan påverka befintlig kod. Varje beteende som introduceras som kan ses som en regression och modifierar existerande beteende är särskilt viktigt och dokumenteras här.

{{% /alert %}} 
## **MemorySetting-egenskap tillagd till Cells-klassen**
Klassen Cells har exponerat setMemorySetting & getMemorySetting-metoder som kan användas för att optimera minnesanvändningen för celldata och därmed minska den totala minneskostnaden. Följande exempel visar hur man skriver en stor data till ett kalkylblad i optimerat läge.

**Java**

{{< highlight "csharp" >}}

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

 Minnesinställningarna fungerar inte för standardarket som skapas automatiskt av arbetsboken. För att ändra minnesinställningarna för befintliga ark, använd minnesinställningarna manuellt innan du utför någon datamanipulation.

{{% /alert %}} {{% alert color="primary" %}} 

 Vänligen kontrollera den detaljerade artikeln om[Optimera minnet när du arbetar med stora datamängder](/cells/sv/java/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)

{{% /alert %}}
