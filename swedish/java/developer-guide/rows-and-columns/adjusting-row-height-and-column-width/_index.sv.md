---
title: Justera radhöjd och kolumnbredd
type: docs
weight: 10
url: /sv/java/adjusting-row-height-and-column-width/
---
{{% alert color="primary" %}} 

När du arbetar med kalkylblad och lägger till data i rader eller kolumner kan du behöva ändra höjden på raderna eller bredden på kolumner. Ibland innebär formatering på rader eller kolumner att den aktuella höjden eller bredden måste ändras för att visa data. Normalt justerar användare radhöjder och kolumnbredder i en WYSIWYG-miljö med hjälp av Microsoft Excel. Men med Aspose.Cells kan utvecklare utföra dessa operationer under körning. Index för rader och kolumner börjar från 0.

{{% /alert %}} 
## **Arbeta med rader**
### **Justering av radhöjd**
 Aspose.Cells tillhandahåller en klass,[Arbetsbok](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , som representerar en Microsoft Excel-fil. De[Arbetsbok](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) klass innehåller en[Arbetsbladssamling](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)som ger åtkomst till varje kalkylblad i Excel-filen. Ett arbetsblad representeras av[Arbetsblad](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) klass. De[Arbetsblad](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) klass ger en[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)samling som representerar alla celler i kalkylbladet.

 De[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)samling innehåller flera metoder för att hantera rader eller kolumner i ett kalkylblad. Några av dessa diskuteras mer i detalj nedan.
### **Ställa in radhöjden**
 Det är möjligt att ställa in höjden på en enstaka rad genom att anropa[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) samlingens[setRowHeight](https://reference.aspose.com/cells/java/com.aspose.cells/cells#setRowHeight\(int,%20double\) ) metod. De[setRowHeight](https://reference.aspose.com/cells/java/com.aspose.cells/cells#setRowHeight\(int,%20double\)) metod tar följande parametrar:

- **Radindex**, indexet för raden som du ändrar höjden på.
- **Radhöjd**, radhöjden som ska tillämpas på raden.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-SettingHeightOfRow-SettingHeightOfRow.java" >}}
### **Ställa in höjden på alla rader**
 För att ställa in samma radhöjd för alla rader i ett kalkylblad, använd[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) samlingens[setStandardHeight](https://reference.aspose.com/cells/java/com.aspose.cells/cells#StandardHeight)metod.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-SettingHeightAllRows-SettingHeightAllRows.java" >}}
## **Arbeta med kolumner**
### **Ställa in bredden på en kolumn**
 Ställ in bredden på en kolumn genom att anropa[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) samlingens[setColumnWidth](https://reference.aspose.com/cells/java/com.aspose.cells/cells#setColumnWidth\(int,%20double\) ) metod. De[setColumnWidth](https://reference.aspose.com/cells/java/com.aspose.cells/cells#setColumnWidth\(int,%20double\)) metod tar följande parametrar:

- **Kolumnindex**, indexet för kolumnen som du ändrar bredden på.
- **Kolumnbredd**, önskad kolumnbredd.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-SettingWidthOfColumn-SettingWidthOfColumn.java" >}}
### **Ställa in bredden på alla kolumner**
 För att ställa in samma kolumnbredd för alla kolumner i ett kalkylblad, använd[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) samlingens[setStandardWidth](https://reference.aspose.com/cells/java/com.aspose.cells/cells#StandardWidth)metod.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-SettingWidthOfAllColumns-SettingWidthOfAllColumns.java" >}}
