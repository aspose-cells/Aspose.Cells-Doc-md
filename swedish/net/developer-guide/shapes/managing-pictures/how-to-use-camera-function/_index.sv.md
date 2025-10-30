---
title: Hur man lägger till kamera för räckvidd
type: docs
weight: 10
url: /sv/net/how-to-add-camera-for-range/
description: Denna artikel kommer att introducera hur man lägger till kamera för innehåll i API Aspose.Cells for .NET för räckvidd.
keywords: Hur man använder kamerafunktion, Hur man lägger till kamera för innehåll i räckvidd, Hur man använder kameraverktyg, Kamera i Excel, Hur man använder kamerafunktion i Aspose.Cells for .NET
---

## **Möjliga användningsscenario**
Kameraverktyget i Excel är en dold men kraftfull funktion som låter dig skapa ett live, kopplat ögonblicksbild av ett cellområde. Här är varför och när du kan använda det.

Vad kameraverktyget gör:
1. Tar en "bild" av ett markerat cellområde.
2. "Bilden" är en live-länk — om ursprungscellerna ändras uppdateras bilden automatiskt.
3. Du kan flytta eller omstorla bilden var som helst på bladet eller till ett annat blad.


## **Hur man använder kamerafunktion i Excel**
Här är en steg-för-steg-guide för att använda kameraverktyget i Excel — ett kraftfullt sätt att skapa live, dynamiska bilder av cellområden.

### Aktivera kameraverktyget

Kameraverktyget är dolt som standard. Så här lägger du till det:

1. Klicka på pilen nedåt i Snabbåtkomstverktygsfältet (övre vänstra hörnet i Excel).
2. Välj Fler kommandon....
3. I dialogrutan: Välj Kommandon som inte finns i menyfliksområdet från rullgardinsmenyn. Bläddra ner och välj Kamera. Klicka på Lägg till >> för att lägga till det i verktygsfältet.
4. Klicka på OK. Du kommer nu att se en liten kamerikon i verktygsfältet.

### Använd kameraverktyget
1. Välj det cellområde du vill fånga (t.ex. A1:C5).
2. Klicka på kamerasymbolen i Snabbåtkomstverktyget.
3. Din markör kommer att ändras till ett korshår.
4. Klicka var som helst på kalkylbladet där du vill placera bilden. En levande bild av det valda området infogas.

### Dynamisk länkning
Bilden är länkad till de ursprungliga cellerna. Om värdena eller formateringen i källdatasatsen ändras, uppdateras bilden automatiskt.


## **Hur man lägger till Camera för område i Aspose.Cells for .NET**
Aspose.Cells stöder att visa innehållet i en cell eller ett område i en bildform. Du kan länka bilden till cellen eller området som innehåller data du vill visa. Eftersom cellen eller området är länkad till grafikt object, visas ändringar som du gör i datan i cellen eller området automatiskt i grafiken. 

Här är ett grundläggande exempel på hur man använder Kamera-funktionen med [exempelfil](camera.xlsx) i Aspose.Cells for .NET:

1. Ladda exempel filen med hjälp av klassen [Workbook](https://apireference.aspose.com/cells/net/aspose.cells/workbook).
1. Lägg till en bild i kalkylbladet genom att använda metoden [**AddPicture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addpicture/index) för samlingen [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) (inkapslad i objektet [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)). 
1. Ange cellområdet med hjälp av attributet [**Formula**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture/properties/formula) i objektet [**Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture).
1. Uppdatera det valda formen i kalkylbladet.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Shapes-how-to-use-camera-function.cs" >}}

## **Utdataresultat**
Följande skärmbild visar kameran för området (A1:E12) skapad av Aspose.Cells for .NET i utdatafilen Excel.
<br>
Före tillägg av data:
<br>
<img src="1.png" width=70% />
<br>
Efter tillägg av data:
<br>
<img src="2.png" width=70% />
{{< app/cells/assistant language="csharp" >}}
