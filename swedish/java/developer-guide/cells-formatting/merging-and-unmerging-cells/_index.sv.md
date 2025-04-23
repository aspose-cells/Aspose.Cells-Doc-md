---
title: Sammanfoga och dela upp celler
type: docs
weight: 140
url: /sv/java/merging-and-unmerging-cells/
---

{{% alert color="primary" %}}

Du vill inte alltid ha samma antal celler i varje rad eller kolumn. Till exempel kan du vilja sätta en rubrik i en cell som sträcker sig över flera kolumner. Eller om du skapar en faktura kan du vilja ha färre kolumner för totalen. För att göra en cell av två eller flera celler, sammanfoga dem. Microsoft Excel låter användare välja celler och sammanfoga dem för att strukturera kalkylbladet på det sätt de vill.

**Resultatet av sammanfogning och sedan dela upp ett område med celler formaterat som cellerna till vänster i Microsoft Excel** 

![todo:image_alt_text](merging-and-unmerging-cells_1.png)

Aspose.Cells stöder den här funktionen och kan också sammanfoga celler i ett arbetsblad. Du kan också dela upp de sammanslagna cellerna. En sammanslagnas cellreferens är referensen för den översta vänstra cellen i det ursprungligen valda området.

Observera att när celler sammanfogas behålls endast datan i den översta vänstra cellen. Om det finns data i de andra cellerna i området raderas den datan.

Formatering är baserad på hänvisningscellen så att när du sammanfogar celler tillämpas formateringsinställningarna för den översta vänstra cellen i området på den sammanslagna cellen. När cellen delas upp behåller de nya cellerna sina ursprungliga formatinställningar.

{{% /alert %}}

## **Sammanfoga celler i ett arbetsblad.**

### **Använda Microsoft Excel**

Följande steg beskriver hur man sammanfogar celler i arbetsbladet med Microsoft Excel.

1. Kopiera den data du vill ha till den övre vänstra cellen inom området.
1. Välj cellerna du vill sammanfoga.
1. För att sammanfoga celler i en rad eller kolumn och centrera cellinnehållet klickar du på ikonen **Sammanfoga och centrerat** på verktygsfältet **Formatering**.

### **Använda Aspose.Cells**

[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells)-klassen har några användbara metoder för uppgiften. Till exempel sammanslår metoden [**merge()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#merge-int-int-int-int-) cellerna till en enda cell inom en angiven cellintervall.

Följande utdata genereras efter att koden nedan har körts.

**Cellerna (C6:E7) har slagits samman** 

![todo:image_alt_text](merging-and-unmerging-cells_2.png)

#### **Kodexempel**

Följande exempel visar hur man slår samman celler (C6:E7) i en arbetsbok.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-MergingCellsInWorksheet-MergingCellsInWorksheet.java" >}}

## **Avfussning (delning) av sammanslagna celler**

### **Använda Microsoft Excel**

Följande steg beskriver hur man delar sammanslagna celler med hjälp av Microsoft Excel.

1. Välj den sammanslagna cellen. 
   När cellerna har kombinerats väljs **Slå samman och centrera** på **Formateringsverktygsfältet**.
1. Klicka på **Slå samman och centrera** på **Formateringsverktygsfältet**.

#### **Använda Aspose.Cells**

Klassen [**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) har en metod som heter [**unMerge()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#unMerge-int-int-int-int-) som delar celler till deras ursprungliga tillstånd. Metoden slår samman cellerna med hjälp av cellens referens i den sammanslagna cellintervallen.

#### **Kodexempel**

Följande exempel visar hur man delar de sammanslagna cellerna (C6). Exemplet använder filen som skapades i det föregående exemplet och delar de sammanslagna cellerna.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-UnMergingCellsInWorksheet-UnMergingCellsInWorksheet.java" >}}

## **Relaterade artiklar**

- [Hitta och dela sammanslagna celler](/cells/sv/java/hitta-sammanslagna-celler-i-en-arbetsbok/).
- [Slå samman och dela en cellintervall med Range.merge() och Range.unMerge()-metoderna](/cells/sv/java/sla-samman-eller-dela-intervall-av-celler/).

{{< app/cells/assistant language="java" >}}
