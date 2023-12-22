---
title: Justera radhöjd och kolumnbredd
type: docs
weight: 10
url: /sv/cpp/adjusting-row-height-and-column-width/
---
{{% alert color="primary" %}} 

När du arbetar med kalkylblad och lägger till data i rader eller kolumner kan du behöva ändra höjden på raderna eller bredden på kolumner. Ibland innebär formatering på rader eller kolumner att den aktuella höjden eller bredden måste ändras för att visa data. Normalt justerar användare radhöjder och kolumnbredder i en WYSIWYG-miljö med hjälp av Microsoft Excel. Men med Aspose.Cells kan utvecklare utföra dessa operationer under körning.

{{% /alert %}} 
##  **Arbeta med rader**
###  **Justering av radhöjd**
 Aspose.Cells tillhandahåller en klass,[Arbetsbok](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) som representerar en Microsoft Excel-fil. De[Arbetsbok](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) klass innehåller en[Arbetsbladssamling](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)som ger åtkomst till varje kalkylblad i Excel-filen. Ett arbetsblad representeras av[Arbetsblad](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) klass. De[Arbetsblad](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) klass ger en[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) samling som representerar alla celler i kalkylbladet. De[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)samling innehåller flera metoder för att hantera rader eller kolumner i ett kalkylblad. Några av dessa diskuteras mer i detalj nedan.
####  **Ställa in höjden på en rad**
 Det är möjligt att ställa in höjden på en enstaka rad genom att anropa[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) samlingens[SetRowHeight](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setrowheight/) metod. De[SetRowHeight](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setrowheight/)metoden tar följande parametrar enligt följande:

- *Radindex**, indexet för raden som du ändrar höjden på.
- *Radhöjd**, radhöjden som ska tillämpas på raden.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingHeightOfRow-new.cpp" >}}


####  **Ställa in höjden på alla rader i ett kalkylblad**
 Om utvecklare behöver ställa in samma radhöjd för alla rader i kalkylbladet kan de göra det genom att använda[Ställ in Standardhöjd](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setstandardheight/) metod för[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/)samling.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingHeightOfAllRowsInWorksheet-new.cpp" >}}
##  **Arbeta med kolumner**
###  **Ställa in bredden på en kolumn**
 Ställ in bredden på en kolumn genom att anropa[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) samlingens[SetColumnWidth](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setcolumnwidth/) metod. De[SetColumnWidth](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setcolumnwidth/)metoden tar följande parametrar:

- *Kolumnindex**, indexet för kolumnen som du ändrar bredden på.
- *Kolumnbredd**, önskad kolumnbredd.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingWidthOfColumn-new.cpp" >}}
###  **Ställa in bredden på alla kolumner i ett kalkylblad**
 För att ställa in samma kolumnbredd för alla kolumner i kalkylbladet, använd[Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) samlingens[SetStandardWidth](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setstandardwidth/)metod.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingWidthOfAllColumnsInWorksheet-new.cpp" >}}
