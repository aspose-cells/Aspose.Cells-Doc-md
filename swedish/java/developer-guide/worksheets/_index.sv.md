---
title: Hantera arbetsblad
linktitle: Arbetsblad
type: docs
weight: 60
url: /sv/java/manage-worksheets/
---
{{% alert color="primary" %}}

Utvecklare kan enkelt skapa och hantera kalkylblad i sina Excel-filer programmatiskt med hjälp av den flexibla API eller Aspose.Cells. I det här ämnet kommer vi att diskutera några metoder för att lägga till och ta bort kalkylblad i Excel-filer.

{{% /alert %}}

Att hantera kalkylblad med Aspose.Cells är lika enkelt som ABC. I det här avsnittet kommer vi att beskriva hur vi kan:

1. Skapa en ny Excel-fil från början och lägg till ett kalkylblad till den
1. Lägg till kalkylblad till designerkalkylblad
1. Få åtkomst till kalkylblad med hjälp av arbetsbladsnamn
1. Ta bort ett kalkylblad från en Excel-fil med dess arknamn
1. Ta bort ett kalkylblad från en Excel-fil med hjälp av dess arkindex

 Aspose.Cells tillhandahåller en klass,[**Arbetsbok**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) som representerar en Excel-fil.[**Arbetsbok**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) klass innehåller en[**Arbetsbladssamling**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)som ger åtkomst till varje kalkylblad i Excel-filen.

 Ett arbetsblad representeras av[**Arbetsblad**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) klass.[**Arbetsblad**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)klass tillhandahåller ett brett utbud av egenskaper och metoder för att hantera ett kalkylblad. Låt oss se hur vi kan använda dessa grundläggande API:er.

## **Lägga till kalkylblad till en ny Excel-fil**

 För att skapa en ny Excel-fil programmatiskt skulle utvecklare behöva skapa ett objekt av[**Arbetsbok**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) klass som representerar en Excel-fil. Då kan utvecklare ringa[**Lägg till**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#add() ) metod för[**Arbetsbladssamling**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) . När vi ringer[**Lägg till**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#add() )-metoden läggs ett tomt kalkylblad till i Excel-filen automatiskt, som kan refereras till genom att skicka arkindexet för det nyligen tillagda kalkylbladet till[**Arbetsbladssamling**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) . Efter att kalkylbladsreferensen har erhållits kan utvecklare arbeta med sina kalkylblad enligt deras krav. När arbetet är klart med kalkylbladen kan utvecklare spara sin nyskapade Excel-fil med nya kalkylblad genom att anropa[**spara**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions) ) metod för[**Arbetsbok**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)klass.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AddingWorksheetstoNewExcelFile-AddingWorksheetstoNewExcelFile.java" >}}

## **Lägga till kalkylblad till ett designerkalkylblad**

Processen att lägga till kalkylblad till ett designerkalkylblad är helt samma som ovanstående tillvägagångssätt förutom att Excel-filen redan är skapad och vi måste öppna den Excel-filen först innan vi lägger till ett kalkylblad till den. Ett designerkalkylblad kan öppnas genom att skicka filsökvägen eller strömmen medan du initierar[**Arbetsbok**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)klass.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AddingWorksheetstoDesignerSpreadsheet-AddingWorksheetstoDesignerSpreadsheet.java" >}}

## **Få åtkomst till kalkylblad med hjälp av arbetsbladsnamn**

Utvecklare kan komma åt eller få vilket kalkylblad som helst genom att ange dess namn eller index.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AccessingWorksheetsusingSheetName-AccessingWorksheetsusingSheetName.java" >}}

## **Ta bort kalkylblad med Sheet Name**

 Ibland kan utvecklare behöva ta bort kalkylblad från befintliga Excel-filer och den uppgiften kan utföras genom att anropa[**ta bortAt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#removeAt(java.lang.String) ) metod för[**Arbetsbladssamling**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) samling. Vi kan skicka arknamnet till[**ta bortAt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#removeAt(java.lang.String)) metod för att ta bort ett specifikt kalkylblad.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemovingWorksheetsusingSheetName-RemovingWorksheetsusingSheetName.java" >}}

## **Ta bort kalkylblad med Sheet Index**

Ovanstående tillvägagångssätt för att ta bort kalkylblad fungerar bra om utvecklare redan känner till arknamnen på kalkylbladen som ska raderas. Men vad händer om du inte känner till arknamnet på kalkylbladet som du vill ta bort från din Excel-fil?

 Tja, under sådana omständigheter kan utvecklare använda en överbelastad version av[**ta bortAt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#removeAt(int)metod som tar kalkylbladets arkindex istället för dess arknamn.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemovingWorksheetsusingSheetIndex-RemovingWorksheetsusingSheetIndex.java" >}}

## **Förhandsämnen**
- [Aktivera ark och aktivera en Cell i kalkylblad](/cells/sv/java/activating-sheets-and-activating-a-cell-in-worksheet/)
- [Kopiera och flytta arbetsblad inom och mellan arbetsböcker](/cells/sv/java/copy-and-move-worksheets-within-and-between-workbooks/)
- [Kopiera och flytta arbetsblad](/cells/sv/java/copying-and-moving-worksheets/)
- [Räkna antalet celler i arbetsbladet](/cells/sv/java/count-number-of-cells-in-the-worksheet/)
- [Upptäcka tomma arbetsblad](/cells/sv/java/detecting-empty-worksheets/)
- [Ta reda på om arbetsbladet är dialogblad](/cells/sv/java/find-if-the-worksheet-is-dialog-sheet/)
- [Få ett unikt kalkylblads-id](/cells/sv/java/get-worksheet-unique-id/)
- [Infoga bakgrundsbild till Excel](/cells/sv/java/insert-background-image-to-excel/)
- [Skapa, manipulera eller ta bort scenarier från arbetsblad](/cells/sv/java/create-manipulate-or-remove-scenarios-from-worksheets/)
- [Hantera sidbrytningar](/cells/sv/java/managing-page-breaks/)
- [Sidinställningsfunktioner](/cells/sv/java/page-setup-features/)
- [Uppdatera referenser i andra kalkylblad samtidigt som du tar bort tomma kolumner och rader i ett kalkylblad](/cells/sv/java/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/)
- [Använd egenskapen Sheet.SheetId för OpenXml med Aspose.Cells](/cells/sv/java/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/)
- [Arbeta med bakgrund i ODS-filer](/cells/sv/java/working-with-background-in-ods-files/)
- [Arbetsbladsvyer](/cells/sv/java/worksheet-views/)
