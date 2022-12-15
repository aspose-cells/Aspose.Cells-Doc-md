---
title: Aspose.Cells for Java 8.5.1 Release Notes
type: docs
weight: 40
url: /sv/java/aspose-cells-for-java-8-5-1-release-notes/
---
{{% alert color="primary" %}} 

 Den här sidan innehåller release notes för[Aspose.Cells for Java 8.5.1](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-8.5.1/)

{{% /alert %}} 

 Följande är en lista över förbättringar och ändringar i denna version av Aspose.Cells



\1) Aspose.Cells 


## **Andra förbättringar och förändringar**

## **Buggar**


 (CELLSJAVA-41378) - Justering av vissa celler bibehålls inte i den genererade HTML-koden

 (CELLSJAVA-41376) - Felmeddelande dyker upp efter att arbetsboken har sparats

 (CELLSJAVA-41412) - ListColumn.getRange returnerar null

 (CELLSJAVA-41407) - VBA-kod i .xlsb förloras efter att ha sparats

(CELLSJAVA-41396) - Att beräkna formler fungerar inte när vi har fler än 65536 namngivna celler

 (CELLSJAVA-41389) - Aktivering av ShowTotal för ListObject infogar en tom rad ovanför totalen

 (CELLSJAVA-41388) - Excel TREND-funktion kan inte beräkna med CalculateFormula

 (CELLSJAVA-41379) - Flikfärger förlorade efter att ha sparat om XLSB

 (CELLSJAVA-41370) - När en arbetsbok instansieras med ett skadat Excel-dokument och LoadOptions, uppstår hängning

 (CELLSJAVA-41411) - Konstigt teckensnittsersättning vid uppgradering till 8.5.0 från 8.4.x

 (CELLSJAVA-41410) - Bildfärgsproblem i Excel till PDF-transformation

 (CELLSJAVA-41406) - Textrutan i diagrammet förskjuts efter att kalkylarket har renderats till PDF

 (CELLSJAVA-41403) - Källa: Kemikalien åsidosätts av sjökortsgränsen i PDF

 (CELLSJAVA-41402) - Källa: Kemikalie åsidosätts av sjökortsgräns i PNG

 (CELLSJAVA-41387) - Dataetiketter åsidosätts av rubriksektionen

 (CELLSJAVA-41380) - Konvertering av diagram till bild/PDF exporterar inte den inneslutna textrutan i licensieringsläge

(CELLSJAVA-41244) - Markörer och pilar ser inte bra ut eller är vanställda

 (CELLSJAVA-40929) - Ord i en textruta har inte mellanslag mellan varandra i utdata-pdf


## **Undantag**


 (CELLSJAVA-41405) - Undantag: java.lang.ArrayIndexOutOfBoundsException på metoden Workbook.save()

 (CELLSJAVA-41399) - CellsException vid öppning av källfilen xlsb

 (CELLSJAVA-41391) - CELLSJAVA-41225 ArrayIndexOutOfBoundsUndantag förekommer i 8.5.0

 (CELLSJAVA-41383) - java.lang.ArrayIndexOutOfBoundsException: 42, på Workbook.save

 (CELLSJAVA-41408) - CellsException: Form till bild Fel! medan du konverterar kalkylblad till PDF


## **Offentlig API och bakåtinkompatibla ändringar**


 Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for Java. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.



 Lägger till enum TableDataSourceType och ListObject.DataSourceType

 Den används för att få datakällans typ av tabellen.



 Lägger till metoden Workbook.Dispose().

 Det används för att frigöra ohanterade resurser.



 Lägger till metoden Cell.GetHeightOfValue().

 Det används för att få höjden på värdet i pixelenhet.





 Notera

Eftersom kodbasen för Aspose.Cells for Java matchar koden för relevant version .NET, ingår de flesta av ändringarna, förbättringarna och korrigeringarna som ingår i Aspose.Cells for .NET v8.5.1 också i denna 076157318.4 v.4181.
