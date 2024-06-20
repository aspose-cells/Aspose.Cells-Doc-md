---
title: Hantera kalkylblad av Microsoft Excel filer
linktitle: Arbetsblad
type: docs
weight: 90
url: /sv/python-net/manage-worksheets/
description: Denna artikel visar hur man hanterar kalkylblad i Microsoft Excel filer med hjälp av Aspose.Cells för Python via .NET API.
keywords: Python Excel Library, Python Hantera kalkylblad i Microsoft Excel filer, Lägg till kalkylblad i Python, Ta bort kalkylblad i Python, Python Så här lägger du till kalkylblad i en ny Excel fil, Python Så här lägger du till kalkylblad i en formaterad kalkylblad, Python Så här går du till väga för att komma åt kalkylblad med hjälp av kalkylbladnamn, Python Så här tar du bort kalkylblad med hjälp av kalkylbladsnamn, Python Så här tar du bort kalkylblad med hjälp av kalkylbladsindex, Python Så här aktiverar du kalkylblad och markerar en cell.
---


{{% alert color="primary" %}}

Utvecklare kan enkelt skapa och hantera kalkylblad i Microsoft Excel-filer programmatiskt med hjälp av Aspose.Cells flexibla API. Denna ämne beskriver tillvägagångssätt för att lägga till och ta bort kalkylblad i Microsoft Excel-filer.

{{% /alert %}}

Aspose.Cells tillhandahåller en klass, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) som representerar en Excelfil. [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) klassen innehåller en [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/) samling som ger åtkomst till varje kalkylblad i Excelfilen.

Ett kalkylblad representeras av [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klassen. [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) klassen tillhandahåller ett brett utbud av egenskaper och metoder för att hantera kalkylblad.

## **Så här lägger du till kalkylblad i en ny Excel-fil**

För att skapa en ny Excel-fil programmatiskt:

1. Skapa ett objekt av [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) klassen.
1. Anropa [**add**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/add/#str) metoden i [**WorksheetCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection) klassen. Ett tomt kalkylblad läggs till i Excelfilen automatiskt. Det kan refereras genom att skicka kalkylbladets index till [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/) samlingen.
1. Få en referens till ett kalkylblad.
1. Arbeta med kalkylbladen.
1. Spara den nya Excelfilen med nya kalkylblad genom att anropa [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) klassens [**save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveFormat) metod.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Management-AddingWorksheetsToNewExcelFile-1.py" >}}

## **Så här lägger du till kalkylblad i en formaterad kalkylblad**

Processen att lägga till kalkylblad i en designerkalkylblad är densamma som att lägga till ett nytt kalkylblad, förutom att Excelfilen redan finns och ska öppnas innan kalkylblad läggs till. Ett designerkalkylblad kan öppnas av [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) klassen.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Management-AddingWorksheetsToDesignerSpreadSheet-1.py" >}}

## **Så här fås tillgång till kalkylblad med hjälp av kalkylbladnamn**

Få tillgång till vilket kalkylblad som helst genom att ange dess namn eller index.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Management-AccessingWorksheetsusingSheetName-1.py" >}}

## **Så här tar du bort kalkylblad med hjälp av kalkylbladnamn**

För att ta bort kalkylblad från en fil, anropa [**remove_by_name**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/remove_by_name/#str) metoden i [**WorksheetCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection) klassen. Skicka kalkylbladets namn till [**remove_by_name**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/remove_by_name/#str) metoden för att ta bort ett specifikt kalkylblad.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Management-RemovingWorksheetsUsingSheetName-1.py" >}}

## **Så här tar du bort kalkylblad med hjälp av kalkylbladsindex**

Att ta bort kalkylblad med namnet fungerar bra när namnet på kalkylbladet är känt. Om du inte vet namnet på kalkylbladet, används [**remove_by_index**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/remove_by_index/#int)-metoden som tar kalkylbladets index istället för dess namn.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Management-RemovingWorksheetsUsingSheetIndex-1.py" >}}

## **Så här aktiverar du kalkylblad och gör en cell aktiv.**

Ibland behöver du ett specifikt kalkylblad som är aktivt och visas när en användare öppnar en Microsoft Excel-fil i Excel. Likaså kanske du vill aktivera en specifik cell och ställa in rullgardinsfälten för att visa den aktiva cellen.
Aspose.Cells är kapabel att utföra alla dessa uppgifter.

Ett **aktivt kalkylblad** är ett kalkylblad du arbetar med: det aktiva kalkylbladets namn på fliken är fetstil som standard.

En **aktiv cell** är en markerad cell, den cell där data matas in när du börjar skriva. Endast en cell är aktiv åt gången. Den aktiva cellen är markerad med en tjock kantlinje.

### **Så här aktiverar du kalkylblad och gör en cell aktiv**

Aspose.Cells erbjuder specifika API-anrop för att aktivera ett blad och en cell. Till exempel är [**Aspose.Cells.WorksheetCollection.active_sheet_index**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/active_sheet_index/)-egenskapen användbar för att ange det aktiva bladet i en arbetsbok.
På liknande sätt används [**Aspose.Cells.Worksheet.active_cell**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/active_cell/)-egenskapen för att ställa in och hämta en aktiv cell i kalkylarket.

För att säkerställa att de horisontella eller vertikala rullningsfältet är på rad- och kolumnindexpositionen du vill visa specifik data, använd egenskaperna [**Aspose.Cells.Worksheet.first_visible_row**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/first_visible_row/) och [**Aspose.Cells.Worksheet.first_visible_column**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/first_visible_column/).

Följande exempel visar hur du aktiverar ett kalkylblad och gör en cell aktiv i det. I den genererade utdatan kommer rullningsfälten att skrollas för att göra den 2: a raden och den 2: a kolumnen som deras första synliga rad och kolumn.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Management-MakeCellActive-1.py" >}}

