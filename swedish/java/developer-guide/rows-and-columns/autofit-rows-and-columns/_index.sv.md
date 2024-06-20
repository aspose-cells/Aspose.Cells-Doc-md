---
title: Autofit Rader och Kolumner
type: docs
weight: 20
url: /sv/java/autofit-rows-and-columns/
---

{{% alert color="primary" %}} 

Microsoft Excel erbjuder en bra funktion för att automatiskt justera bredd och höjd för en cell enligt dess innehåll. Denna funktion är också tillgänglig för Aspose.Cells användare med möjligheten att automatiskt justera dimensionerna för en cell vid körning.

{{% /alert %}} 
## **Autostorlek**
Aspose.Cells tillhandahåller en klass, [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook), som representerar en Microsoft Excel-fil. Klassen [Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) innehåller en [Worksheets](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#Worksheets) kollektion som tillåter åtkomst till varje kalkylblad i Excel-filen.

Ett kalkylblad representeras av klassen [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet). Klassen [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) tillhandahåller ett brett utbud av egenskaper och metoder för hantering av ett kalkylblad. Den här artikeln tittar på att använda klassen [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) för att automatiskt anpassa rader eller kolumner.
### **AutoFit Row - Enkelt**
Det mest raka tillvägagångssättet för automatisk justering av bredd och höjd på en rad är att anropa [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)-klassens [autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow\(int\)) metod. Metoden [autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow\(int\)) tar en radindex (av den rad som ska ändras i storlek) som en parameter.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsandColumns-AutoFitRowsandColumns.java" >}}
### **Autoanpassa Rad i ett Intervall av Celler**
En rad består av många kolumner. Aspose.Cells tillåter utvecklare att automatiskt anpassa en rad baserat på innehållet i en serie celler inom raden genom att anropa en överbelastad version av [autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow\(int,%20int,%20int\)) metoden. Den tar följande parametrar:

- **Radindex**, index för raden som ska autofit.
- **Första kolumnindex**, index för radens första kolumn.
- **Sista kolumnindex**, index för radens sista kolumn.

Metoden [autoFitRow](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRow\(int,%20int,%20int\)) kontrollerar innehållet i alla kolumner i raden och anpassar sedan raden automatiskt.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsinaRangeofCells-AutoFitRowsinaRangeofCells.java" >}}
### **Autoanpassa Kolumn - Enkelt**
Det enklaste sättet att automatiskt justera bredd och höjd på en kolumn är att anropa [Worksheet](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)-klassens [autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int\)) metod. Metoden [autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int\)) tar kolumnindex (av den kolumn som ska ändras i storlek) som en parameter.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitRowsandColumns-AutoFitRowsandColumns.java" >}}
### **Autoanpassa Kolumn i ett Intervall av Celler**
En kolumn består av många rader. Det är möjligt att automatiskt anpassa en kolumn baserat på innehållet i en serie celler i kolumnen genom att anropa en överbelastad version av [autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int,%20int,%20int\)) metod som tar följande parametrar:

- **Kolumnindex**, representerar index för kolumnen vars innehåll behöver autoanpassas
- **Första radindex**, representerar index för kolumnens första rad
- **Sista radindex**, representerar index för kolumnens sista rad

Metoden [autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int,%20int,%20int\)) kontrollerar innehållet i alla rader i kolumnen och anpassar sedan kolumnen automatiskt.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-AutoFitColumnsinaRangeofCells-AutoFitColumnsinaRangeofCells.java" >}}
### **Automatisk justering av rader för sammanfogade celler**
Med Aspose.Cells är det möjligt att automatiskt anpassa rader även för celler som har slagits samman med hjälp av [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions)-API:n. Klassen [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) tillhandahåller egenskapen [AutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/autofitteroptions#AutoFitMergedCellsType) som kan användas för att automatiskt anpassa rader för sammanslagna celler. [AutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/autofitteroptions#AutoFitMergedCellsType) accepterar uppräkneliga [AutoFitMergedCellsType](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitMergedCellsType)-medlemmar.

- [NONE](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#NONE): Ignorera sammanslagna celler.
- [FIRST_LINE](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#FIRST_LINE): Expanderar endast höjden på den första raden.
- [LAST_LINE](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#LAST_LINE): Expanderar endast höjden på den sista raden.
- [EACH_LINE](https://reference.aspose.com/cells/java/com.aspose.cells/autofitmergedcellstype#EACH_LINE): Expanderar endast höjden på varje rad.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-AutofitRowsforMergedCells-1.java" >}}

Du kan också använda de överbelastade versionerna av [autoFitRows](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitRows\(\)) & [autoFitColumns](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumns\(\)) metoder som accepterar en rad/kolumn och en instans av [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) för att automatiskt anpassa de valda raderna/kolumnerna med önskad [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) i enlighet med detta.

Signaturerna för ovanstående metoder är följande:

1. autoFitRows(int startRow, int endRow, [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) options)
1. autoFitColumns(int firstColumn, int lastColumn, [AutoFitterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/AutoFitterOptions) options)
## **Viktigt att veta**
{{% alert color="primary" %}} 

Om en cell är sammanslagen tillämpas inte *AutoFit*-metoderna, vilket är samma beteende som i Microsoft Excel. Dessutom, om texten i en cell är radbunden tillämpas inte [autoFitColumn](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#autoFitColumn\(int\)) metoden heller. En annan sak du behöver veta är att *AutoFit*-metoderna tar lång tid. Så, du bör ringa dessa metoder så sällan som möjligt för att säkerställa effektiviteten av din applikation.

{{% /alert %}}
