---
title: Offentliga API ändringar i Aspose.Cells 8.0.1
type: docs
weight: 20
url: /sv/net/public-api-changes-in-aspose-cells-8-0-1/
---

{{% alert color="primary" %}} 

Dessa sidor listar offentliga API-ändringar som introducerades i Aspose.Cells 8.0.1. Det inkluderar inte bara nya och föråldrade offentliga metoder, utan också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells som kan påverka befintlig kod. Eventuellt beteende som kan betraktas som en regression och ändrar befintligt beteende är särskilt viktigt och dokumenteras här.

{{% /alert %}} 
## **MemorySetting-egenskap tillagd till Cells-klassen**
Cells-klassen har exponerat MemorySetting-egenskapen som kan användas för att optimera minnesanvändningen för celldata och därmed minska den totala minneskostnaden. Följande exempel visar hur man skriver stora data till en arbetsbok i optimerat läge.

**C#**

{{< highlight csharp >}}

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

Minnesinställningarna fungerar inte automatiskt för standardarket som skapas av Workbook-objektet. För att ändra minnesinställningarna för befintliga blad, används minnesinställningen manuellt innan någon datamanipulation utförs.

{{% alert color="primary" %}} 

Kolla in den detaljerade artikeln om [Optimizing Memory while Working with Large Data Sets](/cells/sv/net/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/)

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
