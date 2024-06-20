---
title: Justering av radhöjd och kolumnbredd
type: docs
weight: 10
url: /sv/java/adjusting-row-height-and-column-width/
---

{{% alert color="primary" %}} 

När du arbetar med kalkylblad och lägger till data i rader eller kolumner kan det hända att du behöver ändra radhöjden eller kolumnbredden. Ibland innebär tillämpning av formatering på rader eller kolumner att den aktuella höjden eller bredden behöver ändras för att visa datan. Normalt sett justerar användare radhöjder och kolumnbredder i en WYSIWYG-miljö med Microsoft Excel. Men med Aspose.Cells kan utvecklare utföra dessa operationer vid körning. Indexen för rader och kolumner kommer att börja från 0.

{{% /alert %}} 
## **Arbeta med rader**
### **Justera radhöjd**
Aspose.Cells tillhandahåller en klass, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), som representerar en Microsoft Excel-fil. Klassen [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) innehåller en [WorksheetCollection](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) som tillåter åtkomst till varje kalkylblad i Excel-filen. Ett kalkylblad representeras av klassen [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). Klassen [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) tillhandahåller en [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) samling som representerar alla celler i kalkylbladet.

[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) samlingen tillhandahåller flera metoder för att hantera rader eller kolumner i ett kalkylblad. Några av dessa diskuteras nedan mer i detalj.
### **Ange radhöjden**
Det är möjligt att ställa in höjden på en enskild rad genom att anropa [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)-kollektionens [setRowHeight](https://reference.aspose.com/cells/java/com.aspose.cells/cells#setRowHeight\(int,%20double\)) metod. Metoden [setRowHeight](https://reference.aspose.com/cells/java/com.aspose.cells/cells#setRowHeight\(int,%20double\)) tar följande parametrar:

- **Radindex**, index för den rad vars höjd du ändrar.
- **Radhöjd**, radhöjden som ska tillämpas på raden.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-SettingHeightOfRow-SettingHeightOfRow.java" >}}
### **Inställning av Höjden på Alla Rader**
För att ställa in samma radhöjd för alla rader i en arbetsbok, använd [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)-kollektionens [setStandardHeight](https://reference.aspose.com/cells/java/com.aspose.cells/cells#StandardHeight) metod.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-SettingHeightAllRows-SettingHeightAllRows.java" >}}
## **Arbeta med kolumner**
### **Inställning av bredden på en kolumn**
Ställ in bredden på en kolumn genom att anropa [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)-kollektionens [setColumnWidth](https://reference.aspose.com/cells/java/com.aspose.cells/cells#setColumnWidth\(int,%20double\)) metod. Metoden [setColumnWidth](https://reference.aspose.com/cells/java/com.aspose.cells/cells#setColumnWidth\(int,%20double\)) tar följande parametrar:

- **Kolumnindex**, index för den kolumn vars bredd du ändrar.
- **Kolumnbredd**, önskad kolumnbredd.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-SettingWidthOfColumn-SettingWidthOfColumn.java" >}}
### **Inställning av Bredden på Alla Kolumner**
För att ställa in samma kolumnbredd för alla kolumner i en arbetsbok, använd [Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)-kollektionens [setStandardWidth](https://reference.aspose.com/cells/java/com.aspose.cells/cells#StandardWidth) metod.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-SettingWidthOfAllColumns-SettingWidthOfAllColumns.java" >}}
