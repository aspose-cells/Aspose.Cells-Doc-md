---
title: Hantera arbetsblad
type: docs
weight: 10
url: /sv/python-java/manage-worksheets/
---
Att hantera kalkylblad med Aspose.Cells for Python via Java är mycket enkelt. I den här artikeln kommer vi att demonstrera tillagda, komma åt och ta bort kalkylblad med hjälp av Aspose.Cells API.
## **Lägga till kalkylblad till en ny Excel-fil**
 För att skapa en ny arbetsbok, skapa ett objekt av[Arbetsbok](https://reference.aspose.com/cells/python/asposecells.api/Workbook) klass. De[Arbetsbok](https://reference.aspose.com/cells/python/asposecells.api/Workbook) klass representerar en Excel-fil. Sedan genom att använda[Lägg till](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection#add\(\) ) metod för[Arbetsbladssamling](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection) , nya kalkylblad läggs till i Excel-filen. Slutligen, för att spara den nyskapade Excel-filen, ring till[spara](https://reference.aspose.com/cells/python/asposecells.api/workbook#save\(java.lang.String\) ) metod för[Arbetsbok](https://reference.aspose.com/cells/python/asposecells.api/Workbook)klass.

Följande kodavsnitt visar hur du skapar en ny Excel-fil och lägger till ett kalkylblad till den.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-AddingWorksheetsToNewExcelFile.py" >}}
## **Lägga till kalkylblad till ett designerkalkylblad**
Att lägga till kalkylblad i ett designerkalkylblad är exakt samma sak som att lägga till kalkylbladet i en ny Excel-fil. Den enda skillnaden är att istället för att skapa en ny Excel-fil, öppnar vi en befintlig fil av[Arbetsbok](https://reference.aspose.com/cells/python/asposecells.api/Workbook)klass.

Följande kodavsnitt visar hur man lägger till ett kalkylblad till ett designerkalkylblad.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-AddingWorksheetsToDesignerSpreadsheet.py" >}}
## **Få åtkomst till kalkylblad med hjälp av arbetsbladsnamn**
Efter att ha laddat en arbetsbok kan utvecklare komma åt alla kalkylblad genom att använda dess index eller namn. Följande kodavsnitt visar hur du kommer åt ett kalkylblad genom att använda dess namn.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-AccessingWorksheetsUsingSheetName.py" >}}
## **Ta bort arbetsblad**
Det kan finnas tillfällen då vissa ark möts för att tas bort från arbetsboken. För detta tillhandahåller API[WorksheetCollection.removeAt](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection#removeAt\(int\)) metod. Du kan skicka det arkindex eller arknamnet på arket som ska tas bort. Följande exempel visar hur du tar bort kalkylblad med hjälp av arkindex och arknamn.
### **Ta bort kalkylblad med Sheet Index**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-RemovingWorksheetsUsingSheetIndex.py" >}}
### **Ta bort kalkylblad med Sheet Name**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-RemovingWorksheetsUsingSheetName.py" >}}
