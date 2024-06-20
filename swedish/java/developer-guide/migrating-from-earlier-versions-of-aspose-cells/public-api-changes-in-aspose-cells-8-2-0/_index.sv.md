---
title: Public API förändringar i Aspose.Cells 8.2.0
type: docs
weight: 80
url: /sv/java/public-api-changes-in-aspose-cells-8-2-0/
---

{{% alert color="primary" %}} 

Detta dokument beskriver förändringar av Aspose.Cells API från version 8.1.2 till 8.2.0, som kan vara av intresse för modul/apputvecklare. Det inkluderar inte bara nya och uppdaterade offentliga metoder, utan också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Tillagd MultiThreadReading Egenskap för Cells-klassen**
Med Aspose.Cells for Java 8.2.0 har egenskapen MultiThreadReading lagts till i Cells-klassen för att tillhandahålla en mer robust mekanism för att läsa cellvärden med flera trådar samtidigt. Genom att ställa in den booleska egenskapen till true i den flertrådade applikationen säkerställs att varje tråd får rätt cellvärden.

{{% alert color="primary" %}} 

Se den detaljerade artikeln om [Samtidigt läsning av cellvärden i flertrådad miljö](/cells/sv/java/reading-cell-values-in-multiple-threads-simultaneously/) för mer information.

{{% /alert %}}
## **Tillagda överlagringar för autoutför rader & autoutför kolumner metoder**
Nya överlagringar för autoutför rader & autoutför kolumner har lagts till i Worksheet-klassen, vilket gör att utvecklare kan autofit-rader & kolumner baserat på deras respektive intervall samtidigt som de passerar en instans av klassen AutoFitterOptions. 

Signaturerna för ovanstående metoder är följande:

1. autoFitRows(int startRow, int endRow, AutoFitterOptions options)
1. autoFitColumns(int firstColumn, int lastColumn, AutoFitterOptions options)

{{% alert color="primary" %}} 

Se den detaljerade artikeln om [Autofit Rader och Kolumner](http://aspose.com/docs/display/cellsjava/AutoFit+Rows+and+Columns).

{{% /alert %}}
