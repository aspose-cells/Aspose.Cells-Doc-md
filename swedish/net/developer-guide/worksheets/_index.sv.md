---
title: Hantera kalkylblad för Microsoft Excel-filer.
linktitle: Arbetsblad
type: docs
weight: 90
url: /sv/net/manage-worksheets/
description: Lägg till kalkylblad, ta bort kalkylblad och aktivt arbetsblad med Aspose.Cells.
---
{{% alert color="primary" %}}

Utvecklare kan enkelt skapa och hantera kalkylblad i Microsoft Excel-filer programmatiskt med hjälp av Aspose.Cells' flexibel API. Det här avsnittet beskriver metoder för att lägga till och ta bort kalkylblad i Microsoft Excel-filer.

{{% /alert %}}

 Aspose.Cells tillhandahåller en klass,[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) som representerar en Excel-fil. De[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook)klass innehåller en[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)samling som ger åtkomst till varje kalkylblad i Excel-filen.

 Ett arbetsblad representeras av[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)klass. De[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)class tillhandahåller ett brett utbud av egenskaper och metoder för att hantera kalkylblad.

## **Lägga till kalkylblad till en ny Excel-fil**

Så här skapar du en ny Excel-fil programmatiskt:

1.  Skapa ett objekt av[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook)klass.
1.  Ring[**Lägg till**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/add) metod för[**Arbetsbladssamling**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) klass. Ett tomt kalkylblad läggs automatiskt till i Excel-filen. Det kan refereras till genom att skicka arkindexet för det nya kalkylbladet till[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) samling.
1. Skaffa en kalkylbladsreferens.
1. Utför arbete på arbetsbladen.
1.  Spara den nya Excel-filen med nya kalkylblad genom att anropa[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) klass'[**Spara**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)metod.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-AddingWorksheetsToNewExcelFile-1.cs" >}}

## **Lägga till kalkylblad till ett designerkalkylblad**

 Processen att lägga till kalkylblad till ett designerkalkylblad är densamma som att lägga till ett nytt kalkylblad, förutom att Excel-filen redan finns så bör öppnas innan kalkylblad läggs till. Ett designerkalkylblad kan öppnas av[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook)klass.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-AddingWorksheetsToDesignerSpreadSheet-1.cs" >}}

## **Få åtkomst till kalkylblad med hjälp av arbetsbladsnamn**

Få åtkomst till valfritt kalkylblad genom att ange dess namn eller index.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-AccessingWorksheetsusingSheetName-1.cs" >}}

## **Ta bort kalkylblad med Sheet Name**

För att ta bort kalkylblad från en fil, ring till[**Ta bortAt**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/removeat/index) metod av[**Arbetsbladssamling**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) klass. Skicka arknamnet till[**Ta bortAt**](https://reference.aspose.com/cells/net/aspose.cells.worksheetcollection/removeat/methods/1)metod för att ta bort ett specifikt kalkylblad.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-RemovingWorksheetsUsingSheetName-1.cs" >}}

## **Ta bort kalkylblad med Sheet Index**

 Att ta bort kalkylblad efter namn fungerar bra när namnet på kalkylbladet är känt. Om du inte känner till kalkylbladets namn, använd en överbelastad version av[**Ta bortAt**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/removeat)metod som tar kalkylbladets arkindex istället för dess arknamn.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-RemovingWorksheetsUsingSheetIndex-1.cs" >}}

## **Aktivera ark och göra en aktiv Cell i arbetsbladet**

Ibland behöver du ett specifikt kalkylblad för att vara aktivt och visas när en användare öppnar en Microsoft Excel-fil i Excel. På liknande sätt kanske du vill aktivera en specifik cell och ställa in rullningslisterna så att de visar den aktiva cellen.
Aspose.Cells kan utföra alla dessa uppgifter.

 En**aktivt ark** är ett ark du arbetar med: det aktiva arkets namn på fliken är som standard fetstilt.

 En**aktiv cell** är en markerad cell, cellen som data matas in i när du börjar skriva. Endast en cell är aktiv åt gången. Den aktiva cellen markeras med en kraftig ram.

### **Aktivera ark och göra en Cell aktiv**

Aspose.Cells tillhandahåller specifika API-anrop för att aktivera ett ark och en cell. Till exempel[**Aspose.Cells.WorksheetCollection.ActiveSheetIndex**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/activesheetindex)egenskapen är användbar för att ställa in det aktiva bladet i en arbetsbok.
Liknande,[**Aspose.Cells.Worksheet.ActiveCell**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/activecell)egenskapen används för att ställa in och få en aktiv cell i kalkylbladet.

Använd[**Aspose.Cells.Worksheet.FirstVisibleRow**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/firstvisiblerow) och[**Aspose.Cells.Worksheet.FirstVisibleColumn**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/firstvisiblecolumn)egenskaper.

Följande exempel visar hur man aktiverar ett kalkylblad och gör en aktiv cell i det. I den genererade utdata kommer rullningslisterna att rullas för att göra den andra raden och den andra kolumnen som deras första synliga rad och kolumn.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-MakeCellActive-1.cs" >}}

## **Förhandsämnen**
- [Kopiera och flytta arbetsblad](/cells/sv/net/copying-and-moving-worksheets/)
- [Räkna antalet celler i arbetsbladet](/cells/sv/net/count-number-of-cells-in-the-worksheet/)
- [Upptäcka tomma arbetsblad](/cells/sv/net/detecting-empty-worksheets/)
- [Ta reda på om arbetsbladet är dialogblad](/cells/sv/net/find-if-the-worksheet-is-dialog-sheet/)
- [Få ett unikt kalkylblads-id](/cells/sv/net/get-worksheet-unique-id/)
- [Skapa, manipulera eller ta bort scenarier från arbetsblad](/cells/sv/net/create-manipulate-or-remove-scenarios-from-worksheets/)
- [Hantera sidbrytningar](/cells/sv/net/managing-page-breaks/)
- [Sidinställningsfunktioner](/cells/sv/net/page-setup-features/)
- [Skriv ut flera kopior av ett kalkylblad](/cells/sv/net/print-multiple-copies-of-a-worksheet/)
- [Använd egenskapen Sheet.SheetId för OpenXml med Aspose.Cells](/cells/sv/net/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/)
- [Arbetsbladsvyer](/cells/sv/net/worksheet-views/)

