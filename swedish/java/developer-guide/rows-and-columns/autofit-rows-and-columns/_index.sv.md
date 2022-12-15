---
title: Autopassa rader och kolumner
type: docs
weight: 20
url: /sv/java/autofit-rows-and-columns/
---
{{% alert color="primary" %}} 

Microsoft Excel är en bra funktion för att automatiskt anpassa bredden och höjden på en cell enligt dess innehåll. Den här funktionen är också tillgänglig för Aspose.Cells-användare med kraften att automatiskt anpassa storleken på en cell under körning.

{{% /alert %}} 
## **Autopassning**
 Aspose.Cells tillhandahåller en klass,[Arbetsbok](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) , som representerar en Microsoft Excel-fil. De[Arbetsbok](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) klass innehåller en[Arbetsblad](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets)samling som ger åtkomst till varje kalkylblad i Excel-filen.

 Ett arbetsblad representeras av[Arbetsblad](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) klass. De[Arbetsblad](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) klass tillhandahåller ett brett utbud av egenskaper och metoder för att hantera ett kalkylblad. Den här artikeln handlar om att använda[Arbetsblad](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)klass för att automatiskt anpassa rader eller kolumner.
### **AutoFit Row - Enkel**
 Det enklaste sättet att automatiskt anpassa bredden och höjden på en rad är att anropa[Arbetsblad](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) klass'[autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow\(int\) ) metod. De[autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow\(int\)) metoden tar ett radindex (för raden som ska storleksändras) som en parameter.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsandColumns-AutoFitRowsandColumns.java" >}}
### **AutoFit-rad i intervallet Cells**
 En rad består av många kolumner. Aspose.Cells tillåter utvecklare att automatiskt anpassa en rad baserat på innehållet i ett antal celler inom raden genom att anropa en överbelastad version av[autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow\(int,%20int,%20int\)) metod. Den kräver följande parametrar:

- **Radindex**, indexet för raden som ska anpassas automatiskt.
- **Första kolumnindex**, indexet för radens första kolumn.
- **Sista kolumnindex**, indexet för radens sista kolumn.

 De[autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow\(int,%20int,%20int\))-metoden kontrollerar innehållet i alla kolumner i raden och anpassar sedan raden automatiskt.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsinaRangeofCells-AutoFitRowsinaRangeofCells.java" >}}
### **AutoFit Kolumn - Enkel**
 Det enklaste sättet att automatiskt anpassa bredden och höjden på en kolumn är att anropa[Arbetsblad](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) klass'[autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int\) ) metod. De[autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int\))-metoden tar kolumnindex (för kolumnen som ska storleksändras) som en parameter.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsandColumns-AutoFitRowsandColumns.java" >}}
### **AutoFit-kolumn i intervallet Cells**
 En kolumn består av många rader. Det är möjligt att automatiskt anpassa en kolumn baserat på innehållet i ett antal celler i kolumnen genom att anropa en överbelastad version av[autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int,%20int,%20int\)) metod som tar följande parametrar:

- **Kolumnindex**, representerar indexet för den kolumn vars innehåll måste anpassas automatiskt
- **Första radens index**, representerar indexet för den första raden i kolumnen
- **Sista radens index**, representerar indexet för den sista raden i kolumnen

 De[autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int,%20int,%20int\))-metoden kontrollerar innehållet i alla rader i kolumnen och anpassar sedan kolumnen automatiskt.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitColumnsinaRangeofCells-AutoFitColumnsinaRangeofCells.java" >}}
### **AutoFit-rader för sammanslagna Cells**
Med Aspose.Cells är det möjligt att autopassa rader även för celler som har slagits samman med hjälp av[AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) API. [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions)klass ger[AutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/autofitteroptions#AutoFitMergedCellsType)egenskap som kan användas för att automatiskt anpassa rader för sammanslagna celler.[AutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/autofitteroptions#AutoFitMergedCellsType)accepterar[AutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitMergedCellsType)enumerable som har följande medlemmar.

- [INGEN](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#NONE): Ignorera sammanslagna celler.
- [FÖRSTA LINJEN](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#FIRST_LINE): Expanderar endast höjden på den första raden.
- [SISTA RADEN](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#LAST_LINE): Expanderar endast höjden på den sista raden.
- [VARJE LINJE](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#EACH_LINE): Ökar endast höjden på varje rad.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-AutofitRowsforMergedCells-1.java" >}}

 Du kan också använda de överbelastade versionerna av[autoFitRows](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRows\(\)) & [autoFitColumns](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumns\(\) ) metoder som accepterar ett intervall av rader/kolumner och en instans av[AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) för att automatiskt anpassa de valda raderna/kolumnerna med önskad[AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions)följaktligen.

Signaturerna för ovannämnda metoder är följande:

1.  autoFitRows(int startRow, int endRow,[AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions)alternativ)
1.  autoFitColumns(int firstColumn, int lastColumn,[AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions)alternativ)
## **Viktigt att veta**
{{% alert color="primary" %}} 

 Om en cell slås samman är*AutoFit* metoder kommer inte att tillämpas, vilket är samma beteende som i Microsoft Excel. Dessutom, om texten i en cell är radbruten,[autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int\) ) metod kommer inte heller att tillämpas. En annan sak du behöver veta är att*AutoFit*metoder är tidskrävande. Så du bör anropa dessa metoder så sällan som möjligt för att säkerställa effektiviteten i din applikation.

{{% /alert %}}
