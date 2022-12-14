---
title: Sammanfogning och upphävande Cells
type: docs
weight: 140
url: /sv/java/merging-and-unmerging-cells/
---
{{% alert color="primary" %}}

Du vill inte alltid ha samma antal celler i varje rad eller kolumn. Du kanske till exempel vill sätta en titel i en cell som sträcker sig över flera kolumner. Eller, om du skapar en faktura, kanske du vill ha färre kolumner för summan. För att göra en cell från två eller flera celler, slå samman dem. Microsoft Excel låter användare välja celler och slå samman dem för att strukturera kalkylarket som de vill.

**Resultatet av att slå samman och sedan dela upp ett cellområde formaterat som cellerna till vänster i Microsoft Excel** 

![todo:image_alt_text](merging-and-unmerging-cells_1.png)

Aspose.Cells stöder den här funktionen och kan även slå samman celler i ett kalkylblad. Du kan ta bort sammanslagningen eller dela de sammanslagna cellerna också. En sammanslagen cells cellreferens är referensen för den övre vänstra cellen i det ursprungligen valda området.

Observera att när celler slås samman behålls endast data i den övre vänstra cellen. Om det finns data i de andra cellerna i intervallet raderas den datan.

Formatering baseras på samma sätt på referenscellen så att när du slår samman celler tillämpas formateringsinställningarna för den övre vänstra cellen i intervallet på den sammanslagna cellen. När cellen delas upp behåller de nya cellerna sina ursprungliga formatinställningar.

{{% /alert %}}

## **Slår samman Cells i ett arbetsblad.**

### **Använder Microsoft Excel**

Följande steg beskriver hur du slår samman celler i kalkylbladet med Microsoft Excel.

1. Kopiera de data du vill ha till den övre vänstra cellen inom intervallet.
1. Välj de celler du vill slå samman.
1.  Klicka på för att slå samman celler i en rad eller kolumn och centrera cellinnehållet**Slå samman och centrera** ikonen på**Formatering** verktygsfältet.

### **Använder Aspose.Cells**

 De[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) klass har några användbara metoder för uppgiften. Till exempel metoden[**sammanfoga()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#merge(int,%20int,%20int,%20int)) slår samman cellerna till en enda cell inom ett specificerat intervall av cellerna.

Följande utdata genereras efter exekvering av koden nedan.

**Cellerna (C6:E7) har slagits samman** 

![todo:image_alt_text](merging-and-unmerging-cells_2.png)

#### **Kodexempel**

Följande exempel visar hur man slår samman celler (C6:E7) i ett kalkylblad.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-MergingCellsInWorksheet-MergingCellsInWorksheet.java" >}}

## **Avsluta (delning) Sammanfogad Cells**

### **Använder Microsoft Excel**

Följande steg beskriver hur man delar upp sammanslagna celler med Microsoft Excel.

1.  Välj den sammanslagna cellen.
 När cellerna har kombinerats,**Slå samman och centrera** väljs på**Formatering** verktygsfältet.
1.  Klick**Slå samman och centrera** på**Formatering** verktygsfältet.

#### **Använder Aspose.Cells**

 De[**Cells**](https://reference.aspose.com/cells/java/com.aspose.cells/Cells) klass har en metod som heter[**unmerge()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#unMerge(int,%20int,%20int,%20int)) som delar upp celler till deras ursprungliga tillstånd. Metoden tar bort sammanslagningen av cellerna med hjälp av cellens referens i det sammanslagna cellområdet.

#### **Kodexempel**

Följande exempel visar hur man delar de sammanslagna cellerna (C6). Exemplet använder filen som skapades i föregående exempel och delar upp de sammanslagna cellerna.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-UnMergingCellsInWorksheet-UnMergingCellsInWorksheet.java" >}}

## **relaterade artiklar**

- [Hitta och dela sammanslagna celler](/cells/sv/java/detect-merged-cells-in-a-worksheet/).
- [Slå samman och dela ett cellområde med metoderna Range.merge() och Range.unMerge()](/cells/sv/java/merge-or-unmerge-range-of-cells/).

