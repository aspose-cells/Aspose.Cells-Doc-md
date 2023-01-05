---
title: Offentlig API Ändringar i Aspose.Cells 8.2.0
type: docs
weight: 70
url: /sv/net/public-api-changes-in-aspose-cells-8-2-0/
---
{{% alert color="primary" %}} 

Det här dokumentet beskriver ändringar av Aspose.Cells API från version 8.1.2 till 8.2.0, som kan vara av intresse för modul-/applikationsutvecklare. Den innehåller inte bara nya och uppdaterade offentliga metoder, utan också en beskrivning av eventuella förändringar i beteendet bakom kulisserna i Aspose.Cells.

{{% /alert %}} 
## **Lade till MultiThreadReading-egenskap för Cells Class**
Med Aspose.Cells for .NET 8.2.0 har egenskapen MultiThreadReading lagts till i klassen Cells för att ge en mer robust mekanism för att läsa cellvärden med flera trådar samtidigt. Om du ställer in egenskapen Boolean type till true i det flertrådade programmet säkerställer du att varje tråd får rätt cellvärde.

{{% alert color="primary" %}} 

 Vänligen kontrollera den detaljerade artikeln om[Läs samtidigt Cells-värden i flertrådig miljö](http://aspose.com/docs/display/cellsnet/Reading+Cells+Values+in+Multiple+Threads+Simultaneously) för mer information.

{{% /alert %}}
## **Lade till överbelastningar för metoder för AutoFitRows och AutoFitColumns**
 Nya överbelastningar för AutoFitRows & AutoFitColumns har lagts till i Worksheet-klassen, vilket gör att utvecklarna kan anpassa raderna och kolumnerna automatiskt baserat på deras respektive intervall samtidigt som de skickar en instans av AutoFitterOptions-klassen.

Signaturerna för ovannämnda metoder är följande:

1. AutoFitRows(int startRow, int endRow, AutoFitterOptions-alternativ)
1. AutoFitColumns(int firstColumn, int lastColumn, AutoFitterOptions alternativ)

{{% alert color="primary" %}} 

 Vänligen kontrollera den detaljerade artikeln om[Autopassa rader och kolumner](http://aspose.com/docs/display/cellsnet/AutoFit+Rows+and+Columns).

{{% /alert %}}
