---
title: Gruppera och dela upp rader och kolumner
type: docs
weight: 50
url: /sv/net/grouping-and-ungrouping-rows-and-columns/
---
## **Introduktion**

en Microsoft Excel-fil kan du skapa en disposition för data så att du kan visa och dölja detaljnivåer med ett enda musklick.

 Klicka på**Kontursymboler**, 1,2,3, + och - för att snabbt visa bara de rader eller kolumner som ger sammanfattningar eller rubriker för avsnitt i ett kalkylblad, eller så kan du använda symbolerna för att se detaljer under en enskild sammanfattning eller rubrik som visas nedan i figuren :

|**Gruppera rader och kolumner.**|
|:- |
|![todo:image_alt_text](grouping-and-ungrouping-rows-and-columns_1.png)|

## **Grupphantering av rader och kolumner**

 Aspose.Cells tillhandahåller en klass,[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) som representerar en Microsoft Excel-fil. De[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) klass innehåller en[**Arbetsbladssamling**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) som ger åtkomst till varje kalkylblad i Excel-filen. Ett arbetsblad representeras av[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass. De[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass ger en[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)samling som representerar alla celler i kalkylbladet.

 De[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)samling innehåller flera metoder för att hantera rader eller kolumner i ett kalkylblad, några av dessa diskuteras mer i detalj nedan.

### **Gruppera rader och kolumner**

 Det är möjligt att gruppera rader eller kolumner genom att anropa[**Grupprader**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/grouprows/index) och[**Gruppkolumner**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/groupcolumns/index) metoder för[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) samling. Båda metoderna tar följande parametrar:

- Första rad-/kolumnindex, den första raden eller kolumnen i gruppen.
- Sista raden/kolumnindex, den sista raden eller kolumnen i gruppen.
- Är dold, en boolesk parameter som anger om rader/kolumner ska döljas efter gruppering eller inte.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Grouping-GroupingRowsAndColumns-1.cs" >}}

#### **Gruppinställningar**

Microsoft Excel låter dig konfigurera gruppinställningar för att visa:

- Sammanfattningsrader nedan detalj.
- Sammanfattningskolumner till höger om detaljer.

 Utvecklare kan konfigurera dessa gruppinställningar med hjälp av[**Översikt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/outline) egendom av[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)klass.

### **Sammanfattning rader till nedan med detaljer**

 Det är möjligt att kontrollera om sammanfattningsrader ska visas nedanför detalj genom att ställa in[**Översikt**](https://reference.aspose.com/cells/net/aspose.cells/outline) klass'[**SammanfattningRowBelow**](https://reference.aspose.com/cells/net/aspose.cells/outline/properties/summaryrowbelow) egendom till**Sann** eller**falsk**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Grouping-SummaryRowBelow-1.cs" >}}

### **Sammanfattningskolumner till höger om detalj**

 Utvecklare kan också styra visning av sammanfattningskolumner till höger om detaljer genom att ställa in[**Sammanfattning KolumnHöger**](https://reference.aspose.com/cells/net/aspose.cells/outline/properties/summarycolumnright) egendom av[**Översikt**](https://reference.aspose.com/cells/net/aspose.cells/outline) klass till**Sann** eller**falsk**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Grouping-SummaryRowRight-1.cs" >}}

## **Dela upp rader och kolumner**

 För att avgruppera grupperade rader eller kolumner, anropa[**Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells) samlingens[**Dela upp rader**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/ungrouprows/index) och[**Dela upp kolumner**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/ungroupcolumns)metoder. Båda metoderna tar två parametrar:

- Första raden eller kolumnindex, den första raden/kolumnen som ska delas upp.
- Sista raden eller kolumnindex, den sista raden/kolumnen som ska delas upp.

[**Dela upp rader**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/ungrouprows/index) har en överbelastning som tar en boolesk tredje parameter. Ställer in den på**Sann**tar bort all grupperad information. Annars tas bara den yttre gruppinformationen bort.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-RowsColumns-Grouping-UngroupingRowsAndColumns-1.cs" >}}
