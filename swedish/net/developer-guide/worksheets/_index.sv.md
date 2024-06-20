---
title: Hantera kalkylblad av Microsoft Excel filer
linktitle: Arbetsblad
type: docs
weight: 90
url: /sv/net/manage-worksheets/
description: Lägg till kalkylblad, ta bort kalkylblad och aktiva kalkylblad med hjälp av Aspose.Cells.
---


{{% alert color="primary" %}}

Utvecklare kan enkelt skapa och hantera kalkylblad i Microsoft Excel-filer programmatiskt med hjälp av Aspose.Cells flexibla API. Denna ämne beskriver tillvägagångssätt för att lägga till och ta bort kalkylblad i Microsoft Excel-filer.

{{% /alert %}}

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) som representerar en Excelfil. [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) klassen innehåller en [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) samling som ger åtkomst till varje kalkylblad i Excelfilen.

Ett kalkylblad representeras av [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klassen. [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klassen tillhandahåller ett brett utbud av egenskaper och metoder för att hantera kalkylblad.

## **Lägga till kalkylblad i en ny Excelfil**

För att skapa en ny Excel-fil programmatiskt:

1. Skapa ett objekt av [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) klassen.
1. Anropa [**Add**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/add) metoden i [**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) klassen. Ett tomt kalkylblad läggs till i Excelfilen automatiskt. Det kan refereras genom att skicka kalkylbladets index till [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) samlingen.
1. Få en referens till ett kalkylblad.
1. Arbeta med kalkylbladen.
1. Spara den nya Excelfilen med nya kalkylblad genom att anropa [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) klassens [**Save**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index) metod.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-AddingWorksheetsToNewExcelFile-1.cs" >}}

## **Lägga till kalkylblad i ett designerkalkylblad**

Processen att lägga till kalkylblad i en designerkalkylblad är densamma som att lägga till ett nytt kalkylblad, förutom att Excelfilen redan finns och ska öppnas innan kalkylblad läggs till. Ett designerkalkylblad kan öppnas av [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) klassen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-AddingWorksheetsToDesignerSpreadSheet-1.cs" >}}

## **Tillgång till kalkylblad med hjälp av kalkylbladsnamn**

Få tillgång till vilket kalkylblad som helst genom att ange dess namn eller index.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-AccessingWorksheetsusingSheetName-1.cs" >}}

## **Ta bort kalkylblad med hjälp av kalkylbladsnamn**

För att ta bort kalkylblad från en fil, anropa [**RemoveAt**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/removeat/index) metoden i [**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) klassen. Skicka kalkylbladets namn till [**RemoveAt**](https://reference.aspose.com/cells/net/aspose.cells.worksheetcollection/removeat/methods/1) metoden för att ta bort ett specifikt kalkylblad.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-RemovingWorksheetsUsingSheetName-1.cs" >}}

## **Ta bort kalkylblad med hjälp av kalkylbladsindex**

Att ta bort kalkylblad efter namn fungerar bra när namnet på kalkylbladet är känt. Om du inte vet namnet på kalkylbladet, använd en överbelastad version av [**RemoveAt**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/removeat) metoden som tar kalkylbladets index istället för dess kalkylbladsnamn.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-RemovingWorksheetsUsingSheetIndex-1.cs" >}}

## **Aktivera kalkylblad och gör en aktiv cell i kalkylbladet**

Ibland behöver du ett specifikt kalkylblad som är aktivt och visas när en användare öppnar en Microsoft Excel-fil i Excel. Likaså kanske du vill aktivera en specifik cell och ställa in rullgardinsfälten för att visa den aktiva cellen.
Aspose.Cells är kapabel att utföra alla dessa uppgifter.

Ett **aktivt kalkylblad** är ett kalkylblad du arbetar med: det aktiva kalkylbladets namn på fliken är fetstil som standard.

En **aktiv cell** är en markerad cell, den cell där data matas in när du börjar skriva. Endast en cell är aktiv åt gången. Den aktiva cellen är markerad med en tjock kantlinje.

### **Aktivera blad och göra en cell aktiv**

Aspose.Cells erbjuder specifika API-anrop för att aktivera ett blad och en cell. Till exempel är [**Aspose.Cells.WorksheetCollection.ActiveSheetIndex**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/activesheetindex)-egenskapen användbar för att ange det aktiva bladet i en arbetsbok.
På liknande sätt används [**Aspose.Cells.Worksheet.ActiveCell**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/activecell)-egenskapen för att ställa in och hämta en aktiv cell i kalkylarket.

För att säkerställa att de horisontella eller vertikala rullningsfältet är på rad- och kolumnindexpositionen du vill visa specifik data, använd egenskaperna [**Aspose.Cells.Worksheet.FirstVisibleRow**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/firstvisiblerow) och [**Aspose.Cells.Worksheet.FirstVisibleColumn**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/firstvisiblecolumn).

Följande exempel visar hur du aktiverar ett kalkylblad och gör en cell aktiv i det. I den genererade utdatan kommer rullningsfälten att skrollas för att göra den 2: a raden och den 2: a kolumnen som deras första synliga rad och kolumn.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-MakeCellActive-1.cs" >}}

## **Fortsatta ämnen**
- [Kopiera och flytta arbetsblad](/cells/sv/net/copying-and-moving-worksheets/)
- [Räkna antalet celler i kalkylbladet](/cells/sv/net/count-number-of-cells-in-the-worksheet/)
- [Upptäcka tomma kalkylblad](/cells/sv/net/detecting-empty-worksheets/)
- [Ta reda på om kalkylbladet är Dialog sheet](/cells/sv/net/find-if-the-worksheet-is-dialog-sheet/)
- [Få arbetsbladets unika id](/cells/sv/net/get-worksheet-unique-id/)
- [Skapa, manipulera eller ta bort scenarier från kalkylblad](/cells/sv/net/create-manipulate-or-remove-scenarios-from-worksheets/)
- [Hantera sidbrytningar](/cells/sv/net/managing-page-breaks/)
- [Sidlayoutfunktioner](/cells/sv/net/page-setup-features/)
- [Skriv ut flera kopior av ett arbetsblad](/cells/sv/net/print-multiple-copies-of-a-worksheet/)
- [Använd Sheet.SheetId-egenskapen i OpenXml med hjälp av Aspose.Cells](/cells/sv/net/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/)
- [Kalkylbladsvyer](/cells/sv/net/worksheet-views/)

