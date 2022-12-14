---
title: Offentliga API-ändringar i Aspose.Cells 8.2.0
type: docs
weight: 80
url: /sv/java/public-api-changes-in-aspose-cells-8-2-0/
---
{{% alert color="primary" %}} 

Det här dokumentet beskriver ändringar av Aspose.Cells API från version 8.1.2 till 8.2.0, som kan vara av intresse för modul-/applikationsutvecklare. Den innehåller inte bara nya och uppdaterade offentliga metoder, utan också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Lade till MultiThreadReading-egenskap för Cells Class**
Med Aspose.Cells för Java 8.2.0 har egenskapen MultiThreadReading lagts till i klassen Cells för att ge en mer robust mekanism för att läsa cellvärden med flera trådar samtidigt. Om du ställer in egenskapen Boolean type till true i det flertrådade programmet säkerställer du att varje tråd får rätt cellvärde.

{{% alert color="primary" %}} 

 Vänligen kontrollera den detaljerade artikeln om[Läs samtidigt Cells-värden i flertrådig miljö](/cells/sv/java/reading-cell-values-in-multiple-threads-simultaneously/) för mer information.

{{% /alert %}}
## **Lade till överbelastningar för metoder för autoFitRows och autoFitColumns**
 Nya överbelastningar för autoFitRows & autoFitColumns har lagts till i klassen Worksheet, vilket gör att utvecklarna kan anpassa raderna och kolumnerna automatiskt baserat på deras respektive intervall samtidigt som de skickar en instans av klassen AutoFitterOptions.

Signaturerna för ovannämnda metoder är följande:

1. autoFitRows(int startRow, int endRow, AutoFitterOptions-alternativ)
1. autoFitColumns(int firstColumn, int lastColumn, AutoFitterOptions-alternativ)

{{% alert color="primary" %}} 

 Vänligen kontrollera den detaljerade artikeln om[Autopassa rader och kolumner](http://aspose.com/docs/display/cellsjava/AutoFit+Rows+and+Columns).

{{% /alert %}}
