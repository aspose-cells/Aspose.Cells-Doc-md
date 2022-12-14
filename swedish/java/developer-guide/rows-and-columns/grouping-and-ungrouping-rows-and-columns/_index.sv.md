---
title: Gruppera och dela upp rader och kolumner
type: docs
weight: 40
url: /sv/java/grouping-and-ungrouping-rows-and-columns/
---
## **Introduktion**
en Microsoft Excel-fil kan du skapa en disposition för data så att du kan visa och dölja detaljnivåer med ett enda musklick.

 Klicka på**Kontursymboler**, 1,2,3, + och - för att snabbt visa bara de rader eller kolumner som ger sammanfattningar eller rubriker för avsnitt i ett kalkylblad, eller så kan du använda symbolerna för att se detaljer under en enskild sammanfattning eller rubrik som visas nedan i figuren :

 Gruppering av rader och kolumner

![todo:image_alt_text](grouping-and-ungrouping-rows-and-columns_1.png)
## **Grupphantering av rader och kolumner**
 Aspose.Cells tillhandahåller en klass,[Arbetsbok](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) som representerar en Microsoft Excel-fil. De[Arbetsbok](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) klass innehåller en[Arbetsblad](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) samling som ger åtkomst till varje kalkylblad i Excel-filen. Ett arbetsblad representeras av[Arbetsblad](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) klass. De[Arbetsblad](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) klass ger en[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)samling som representerar alla celler i kalkylbladet.

 De[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)samling innehåller flera metoder för att hantera rader eller kolumner i ett kalkylblad, några av dessa diskuteras mer i detalj nedan.
### **Gruppera rader och kolumner**
 Det är möjligt att gruppera rader eller kolumner genom att anropa[grupprader](https://reference.aspose.com/cells/java/com.aspose.cells/cells#groupRows\(int,%20int,%20boolean\) ) och[gruppKolumner](https://reference.aspose.com/cells/java/com.aspose.cells/cells#groupColumns\(int,%20int,%20boolean\) ) metoder för[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)samling. Båda metoderna tar följande parametrar:

- Första rad-/kolumnindex, den första raden eller kolumnen i gruppen.
- Sista raden/kolumnindex, den sista raden eller kolumnen i gruppen.
- Är dold, en boolesk parameter som anger om rader/kolumner ska döljas efter gruppering eller inte.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-GroupingRowsandColumns-1.java" >}}
## **Gruppinställningar**
Microsoft Excel tillåter också att konfigurera gruppinställningar för att visa:

- Sammanfattningsrader nedan detalj.
- Sammanfattningskolumner till höger om detaljer.

**Gruppinställningar** 

![todo:image_alt_text](grouping-and-ungrouping-rows-and-columns_2.png)

Det är möjligt att konfigurera dessa gruppinställningar med hjälp av egenskapen Outline för Worksheet-klassen.
### **Sammanfattningsrader under detalj**
 Utvecklare kan styra visning av sammanfattningsrader nedanför detalj genom att använda[Översikt](https://reference.aspose.com/cells/java/com.aspose.cells/Outline) klass'[SammanfattningRowBelow](https://reference.aspose.com/cells/java/com.aspose.cells/outline#SummaryRowBelow) metod.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-SummaryRowBelow-1.java" >}}
### **Sammanfattningskolumner till höger om detalj**
Det är möjligt att styra om sammanfattningskolumner ska visas till höger om detaljerna med[Översikt](https://reference.aspose.com/cells/java/com.aspose.cells/Outline) klass'[Sammanfattning KolumnHöger](https://reference.aspose.com/cells/java/com.aspose.cells/outline#SummaryColumnRight)metod.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-RowsAndColumns-SummaryRowRight-1.java" >}}
### **Dela upp rader och kolumner**
 Dela upp grupperade rader eller kolumner genom att anropa[Cells](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) samlingens[Dela upp rader](https://reference.aspose.com/cells/java/com.aspose.cells/cells#ungroupRows\(int,%20int\) ) och[Dela upp kolumner](https://reference.aspose.com/cells/java/com.aspose.cells/cells#ungroupColumns\(int,%20int\)) metoder. Båda metoderna tar samma parametrar:

- Första raden eller kolumnindex, den första raden/kolumnen som ska delas upp.
- Sista raden eller kolumnindex, den sista raden/kolumnen som ska delas upp.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-UngroupingRowsandColumns-UngroupingRowsandColumns.java" >}}
