---
title: Public API förändringar i Aspose.Cells 8.2.0
type: docs
weight: 70
url: /sv/net/public-api-changes-in-aspose-cells-8-2-0/
---

{{% alert color="primary" %}} 

Detta dokument beskriver förändringar av Aspose.Cells API från version 8.1.2 till 8.2.0, som kan vara av intresse för modul/apputvecklare. Det inkluderar inte bara nya och uppdaterade offentliga metoder, utan också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Tillagd MultiThreadReading Egenskap för Cells-klassen**
Med Aspose.Cells for .NET 8.2.0 har MultiThreadReading-egenskapen lagts till för Cells-klassen för att tillhandahålla en mer robust mekanism för att läsa cellvärden med flera trådar samtidigt. Genom att ställa in detta boolean-egenskap till true i en flertrådad applikation säkerställs att varje tråd kommer att ta emot rätt cellvärden.

{{% alert color="primary" %}} 

Kontrollera den detaljerade artikeln om [Samtidigt läsa cellvärden i flertrådad miljö](http://aspose.com/docs/display/cellsnet/Reading+Cells+Values+in+Multiple+Threads+Simultaneously) för mer information.

{{% /alert %}}
## **Tillagda överlagringar för metoder AutoFitRows & AutoFitColumns**
Nya överlagringar för AutoFitRows & AutoFitColumns har lagts till för Worksheet-klassen, vilket ger utvecklarna möjlighet att automatiskt anpassa rader & kolumner baserat på deras respektive intervall medan de passerar en instans av AutoFitterOptions-klassen. 

Signaturerna för ovanstående metoder är följande:

1. AutoFitRows(int startRow, int endRow, AutoFitterOptions options)
1. AutoFitColumns(int firstColumn, int lastColumn, AutoFitterOptions options)

{{% alert color="primary" %}} 

Kontrollera den detaljerade artikeln om [Automatisk anpassning av rader och kolumner](http://aspose.com/docs/display/cellsnet/AutoFit+Rows+and+Columns).

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
