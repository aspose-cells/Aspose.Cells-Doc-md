---
title: Hantera kalkylblad 
linktitle: Arbetsblad
type: docs
weight: 60
url: /sv/java/manage-worksheets/
---

{{% alert color="primary" %}}

Utvecklare kan enkelt skapa och hantera kalkylblad i sina Excel-filer programmatiskt med den flexibla API:n för Aspose.Cells. I det här avsnittet kommer vi att diskutera olika sätt att lägga till och ta bort kalkylblad i Excel-filer.

{{% /alert %}}

Att hantera kalkylblad med Aspose.Cells är enkelt. I det här avsnittet kommer vi att beskriva hur vi kan:

1. Skapa en ny Excelfil från grunden och lägga till ett kalkylblad i den
1. Lägg till kalkylblad i designerkalkylblad
1. Tillgång till kalkylblad med hjälp av kalkylbladsnamn
1. Ta bort ett kalkylblad från en Excelfil med dess kalkylbladsnamn
1. Ta bort ett kalkylblad från en Excelfil med dess kalkylbladsindex

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) som representerar en Excelfil. [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)-klassen innehåller en [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) som tillåter åtkomst till varje kalkylblad i Excelfilen.

Ett kalkylblad representeras av [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)-klassen. [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)-klassen tillhandahåller ett brett utbud av egenskaper och metoder för att hantera ett kalkylblad. Låt oss se hur vi kan använda dessa grundläggande uppsättning APIer.

## **Lägga till kalkylblad i en ny Excelfil**

För att skapa en ny Excelfil programmatiskt måste utvecklare skapa ett objekt av [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)-klassen som representerar en Excelfil. Sedan kan utvecklare anropa [**add**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#add--)-metoden för [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection). När vi anropar [**add**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#add--)-metoden läggs automatiskt ett tomt kalkylblad till Excelfilen, vilket kan refereras genom att skicka det nya tillagda kalkylbladets index till [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection). Efter att kalkylbladsreferensen har erhållits kan utvecklare arbeta med sina kalkylblad enligt sina krav. När arbetet är klart på kalkylbladen kan utvecklare spara sin nyligen skapade Excelfil med nya kalkylblad genom att anropa [**save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save-java.io.OutputStream-com.aspose.cells.SaveOptions-)-metoden för [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)-klassen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AddingWorksheetstoNewExcelFile-AddingWorksheetstoNewExcelFile.java" >}}

## **Lägga till kalkylblad i ett designerkalkylblad**

Processen för att lägga till kalkylblad i ett designerkalkylblad är helt samma som ovanstående tillvägagångssätt förutom att Excelfilen redan är skapad och vi behöver öppna den Excelfilen först innan vi lägger till ett kalkylblad i den. Ett designerkalkylblad kan öppnas genom att skicka sökvägen eller strömmen när [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)-klassen initialiseras.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AddingWorksheetstoDesignerSpreadsheet-AddingWorksheetstoDesignerSpreadsheet.java" >}}

## **Tillgång till kalkylblad med hjälp av kalkylbladsnamn**

Utvecklare kan nå eller hämta ett kalkylblad genom att ange dess namn eller index.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AccessingWorksheetsusingSheetName-AccessingWorksheetsusingSheetName.java" >}}

## **Ta bort kalkylblad med hjälp av kalkylbladsnamn**

Ibland kan utvecklare behöva ta bort kalkylblad från befintliga Excelfiler och den uppgiften kan utföras genom att anropa [**removeAt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#removeAt-java.lang.String-)-metoden för [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)-samlingen. Vi kan skicka kalkylbladsnamnet till [**removeAt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#removeAt-java.lang.String-)-metoden för att ta bort ett specifikt kalkylblad.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemovingWorksheetsusingSheetName-RemovingWorksheetsusingSheetName.java" >}}

## **Ta bort kalkylblad med hjälp av kalkylbladsindex**

Det ovanstående tillvägagångssättet för att ta bort kalkylblad fungerar bra om utvecklare redan känner till kalkylbladsnamnen för kalkylbladen som ska tas bort. Men hur gör man om man inte vet kalkylbladsnamnet på kalkylbladet som du vill ta bort från din Excelfil?

Ja, under sådana omständigheter kan utvecklare använda en överbelastad version av [**removeAt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#removeAt-int-)-metoden som tar kalkylbladets index istället för dess kalkylbladsnamn.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemovingWorksheetsusingSheetIndex-RemovingWorksheetsusingSheetIndex.java" >}}

## **Fortsatta ämnen**
- [Aktivera kalkylblad och aktivera en cell i kalkylbladet](/cells/sv/java/activating-sheets-and-activating-a-cell-in-worksheet/)
- [Kopiera och flytta kalkylblad inom och mellan arbetsböcker](/cells/sv/java/copy-and-move-worksheets-within-and-between-workbooks/)
- [Kopiera och flytta arbetsblad](/cells/sv/java/copying-and-moving-worksheets/)
- [Räkna antalet celler i kalkylbladet](/cells/sv/java/count-number-of-cells-in-the-worksheet/)
- [Upptäcka tomma kalkylblad](/cells/sv/java/detecting-empty-worksheets/)
- [Ta reda på om kalkylbladet är Dialog sheet](/cells/sv/java/find-if-the-worksheet-is-dialog-sheet/)
- [Få arbetsbladets unika id](/cells/sv/java/get-worksheet-unique-id/)
- [Infoga en bakgrundsbild i Excel](/cells/sv/java/insert-background-image-to-excel/)
- [Skapa, manipulera eller ta bort scenarier från kalkylblad](/cells/sv/java/create-manipulate-or-remove-scenarios-from-worksheets/)
- [Hantera sidbrytningar](/cells/sv/java/managing-page-breaks/)
- [Sidlayoutfunktioner](/cells/sv/java/page-setup-features/)
- [Uppdatera referenser i andra arbetsblad samtidigt som tomma kolumner och rader tas bort i ett arbetsblad](/cells/sv/java/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/)
- [Använd Sheet.SheetId-egenskapen i OpenXml med hjälp av Aspose.Cells](/cells/sv/java/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/)
- [Arbeta med bakgrund i ODS-filer](/cells/sv/java/working-with-background-in-ods-files/)
- [Kalkylbladsvyer](/cells/sv/java/worksheet-views/)
{{< app/cells/assistant language="java" >}}
