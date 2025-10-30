---
title: Justering av radhöjd och kolumnbredd
type: docs
weight: 10
url: /sv/cpp/adjusting-row-height-and-column-width/
---

{{% alert color="primary" %}} 

När du arbetar med kalkylblad och lägger till data i rader eller kolumner kan du behöva ändra höjden på rader eller bredden på kolumner. Ibland innebär att tillämpa formatering på rader eller kolumner att den aktuella höjden eller bredden behöver ändras för att visa datan. Normalt justerar användare radhöjder och kolumnbredder i en WYSIWYG-miljö med hjälp av Microsoft Excel. Men med Aspose.Cells kan utvecklare utföra dessa operationer vid runtime.

{{% /alert %}} 
## **Arbeta med rader**
### **Justera radhöjd**
Aspose.Cells tillhandahåller en klass, [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) som representerar en Microsoft Excel-fil. [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) klassen innehåller en [WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) som möjliggör åtkomst till varje arbetsblad i Excel-filen. Ett arbetsblad representeras av [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) klassen. [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) klassen tillhandahåller en [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) samling som representerar alla celler i arbetsbladet. [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) samlingen tillhandahåller flera metoder för att hantera rader eller kolumner i ett arbetsblad. Några av dessa diskuteras nedan mer detaljerat.
#### **Inställning av radhöjd**
Det är möjligt att ange höjden på en enskild rad genom att anropa [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) samlingens [SetRowHeight](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setrowheight/) metod. [SetRowHeight](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setrowheight/) metoden tar följande parametrar som följer:

- **Radindex**, index för den rad vars höjd du ändrar.
- **Radhöjd**, radhöjden som ska tillämpas på raden.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingHeightOfRow-new.cpp" >}}


#### **Inställning av höjden på alla rader i ett arbetsblad**
Om utvecklare behöver ange samma radhöjd för alla rader i arbetsbladet kan de göra det genom att använda [SetStandardHeight](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setstandardheight/) metoden i [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) samlingen.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingHeightOfAllRowsInWorksheet-new.cpp" >}}
## **Arbeta med kolumner**
### **Inställning av bredden på en kolumn**
Ställ in bredden på en kolumn genom att anropa [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) samlingens [SetColumnWidth](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setcolumnwidth/) metod. [SetColumnWidth](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setcolumnwidth/) metoden tar följande parametrar:

- **Kolumnindex**, index för den kolumn vars bredd du ändrar.
- **Kolumnbredd**, önskad kolumnbredd.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingWidthOfColumn-new.cpp" >}}
### **Inställning av bredden på alla kolumner i ett arbetsblad**
För att ställa in samma kolumnbredd för alla kolumner i arbetsbladet, använd [SetStandardWidth](https://reference.aspose.com/cells/cpp/aspose.cells/cells/setstandardwidth/) metod i [Cells](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) samlingen.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingWidthOfAllColumnsInWorksheet-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
