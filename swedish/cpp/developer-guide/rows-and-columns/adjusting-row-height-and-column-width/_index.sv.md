---
title: Justera radhöjd och kolumnbredd
type: docs
weight: 10
url: /sv/cpp/adjusting-row-height-and-column-width/
---
{{% alert color="primary" %}} 

När du arbetar med kalkylblad och lägger till data i rader eller kolumner kan du behöva ändra höjden på raderna eller bredden på kolumner. Ibland innebär formatering på rader eller kolumner att den aktuella höjden eller bredden måste ändras för att visa data. Normalt justerar användare radhöjder och kolumnbredder i en WYSIWYG-miljö med hjälp av Microsoft Excel. Men med Aspose.Cells kan utvecklare utföra dessa operationer under körning.

{{% /alert %}} 
## **Arbeta med rader**
### **Justering av radhöjd**
 Aspose.Cells tillhandahåller en klass,[IArbetsbok](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) som representerar en Microsoft Excel-fil. De[IArbetsbok](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) klass innehåller en[IWorksheetCollection](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)som ger åtkomst till varje kalkylblad i Excel-filen. Ett arbetsblad representeras av[IArbetsblad](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) klass. De[IArbetsblad](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) klass ger en[ICells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) samling som representerar alla celler i kalkylbladet. De[ICells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)samling innehåller flera metoder för att hantera rader eller kolumner i ett kalkylblad. Några av dessa diskuteras mer i detalj nedan.
#### **Ställa in höjden på en rad**
 Det är möjligt att ställa in höjden på en enstaka rad genom att anropa[ICells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) samlingens[SetRowHeight](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a7aa441877e03639232299627261a7d1f) metod. De[SetRowHeight](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a7aa441877e03639232299627261a7d1f)metoden tar följande parametrar enligt följande:

- **Radindex**, indexet för raden som du ändrar höjden på.
- **Radhöjd**, radhöjden som ska tillämpas på raden.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingHeightOfRow.cpp" >}}


#### **Ställa in höjden på alla rader i ett kalkylblad**
 Om utvecklare behöver ställa in samma radhöjd för alla rader i kalkylbladet kan de göra det genom att använda[Ställ in Standardhöjd](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a0b79a3163e2b601aa1b6a6a1e3f1467f) metod för[ICells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell)samling.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingHeightOfAllRowsInWorksheet.cpp" >}}
## **Arbeta med kolumner**
### **Ställa in bredden på en kolumn**
 Ställ in bredden på en kolumn genom att anropa[ICells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) samlingens[SetColumnWidth](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ab1c6a4e89760d2a022d5bfba8bc40987) metod. De[SetColumnWidth](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#ab1c6a4e89760d2a022d5bfba8bc40987)metoden tar följande parametrar:

- **Kolumnindex**, indexet för kolumnen som du ändrar bredden på.
- **Kolumnbredd**, önskad kolumnbredd.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingWidthOfColumn.cpp" >}}
### **Ställa in bredden på alla kolumner i ett kalkylblad**
 För att ställa in samma kolumnbredd för alla kolumner i kalkylbladet, använd[ICells](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell) samlingens[SetStandardWidth](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_cell#a48f5dbccc3bf4bb9e6e882094b500bd7)metod.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-RowsAndColumns-AdjustingRowHeightAndColumnWidth-SettingWidthOfAllColumnsInWorksheet.cpp" >}}
