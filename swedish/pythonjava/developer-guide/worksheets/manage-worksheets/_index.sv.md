---
title: Hantera kalkylblad 
type: docs
weight: 10
url: /sv/python-java/manage-worksheets/
---

Att hantera kalkylblad med Aspose.Cells för Python via Java är mycket enkelt. I den här artikeln kommer vi att demonstrera tillägg, åtkomst och borttagning av kalkylblad med hjälp av Aspose.Cells API:n.
## **Lägga till kalkylblad i en ny Excelfil**
För att skapa en ny arbetsbok, skapa en objekt av klassen [Workbook](https://reference.aspose.com/cells/python/asposecells.api/Workbook). Klassen [Workbook](https://reference.aspose.com/cells/python/asposecells.api/Workbook) representerar en Excel-fil. Sedan genom att använda metoden [add](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection#add\(\)) av [WorksheetCollection](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection), läggs nya arbetsblad till i Excel-filen. Slutligen, för att spara den nyss skapade Excel-filen, anropa metoden [save](https://reference.aspose.com/cells/python/asposecells.api/workbook#save\(java.lang.String\)) av klassen [Workbook](https://reference.aspose.com/cells/python/asposecells.api/Workbook).

Följande kodsnutt demonstrerar hur man skapar en ny Excelfil och lägger till ett arbetsblad i den.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-AddingWorksheetsToNewExcelFile.py" >}}
## **Lägga till kalkylblad i ett designerkalkylblad**
Att lägga till arbetsblad i ett designer-kalkylblad är exakt samma sak som att lägga till arbetsblad i en ny Excelfil. Det enda skillnaden är att istället för att skapa en ny Excelfil, öppnar vi en befintlig fil med hjälp av klassen [Workbook](https://reference.aspose.com/cells/python/asposecells.api/Workbook).

Följande kodsnutt demonstrerar hur man lägger till ett arbetsblad i ett designer-kalkylblad.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-AddingWorksheetsToDesignerSpreadsheet.py" >}}
## **Tillgång till kalkylblad med hjälp av kalkylbladsnamn**
Efter att ha laddat en arbetsbok kan utvecklare komma åt vilket arbetsblad som helst genom att använda dess index eller namn. Följande kodsnutt demonstrerar åtkomst till ett arbetsblad genom att använda dess namn.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-AccessingWorksheetsUsingSheetName.py" >}}
## **Ta bort arbetsblad**
Det kan finnas tillfällen då vissa blad måste tas bort från arbetsboken. För detta tillhandahåller API:et metoden [WorksheetCollection.removeAt](https://reference.aspose.com/cells/python/asposecells.api/worksheetcollection#removeAt\(int\)). Du kan ange bladindex eller bladnamn för att ta bort bladet. Följande exempel demonstrerar borttagning av arbetsblad med hjälp av bladindex och bladnamn.
### **Ta bort arbetsblad med hjälp av bladindex**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-RemovingWorksheetsUsingSheetIndex.py" >}}
### **Ta bort kalkylblad med hjälp av kalkylbladsnamn**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-RemovingWorksheetsUsingSheetName.py" >}}
