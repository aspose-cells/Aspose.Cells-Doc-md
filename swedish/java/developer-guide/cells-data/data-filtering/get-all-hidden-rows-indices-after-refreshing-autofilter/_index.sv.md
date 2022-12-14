---
title: Få alla dolda rader efter att ha uppdaterat autofiltret
type: docs
weight: 240
url: /sv/java/get-all-hidden-rows-indices-after-refreshing-autofilter/
---
## **Möjliga användningsscenarier**

När du använder ett autofilter på kalkylbladsceller döljs några av raderna automatiskt. Men det kan vara så att några av raderna redan är dolda manuellt av Excel-slutanvändare och de är inte dolda av autofiltret. Det gör därför svårt att veta vilka av raderna som döljs av autofiltret och vilka av dem som döljs manuellt av Excel-slutanvändare. Aspose.Cells hanterar detta problem med hjälp av int[][**AutoFilter.refresh(bool hideRows)**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#refresh(boolean)) metod. Denna metod returnerar radindexen för alla rader som är dolda av autofiltret och inte manuellt av Excel-slutanvändaren.

## **Få alla dolda rader efter att ha uppdaterat autofiltret**

Se följande exempelkod som laddar[exempel på Excel-fil](64716913.xlsx)som innehåller några av raderna som döljs manuellt av Excel-slutanvändare. Koden tillämpar autofiltret och uppdaterar det med int[][**AutoFilter.refresh(bool hideRows)**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#refresh(boolean)) metod som returnerar radindexen för alla dolda rader av autofiltret. Den skriver sedan ut indexen för de dolda raderna på konsolen tillsammans med cellnamn och värden.

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Data-GetAllHiddenRowsIndicesAfterRefreshingAutoFilter.java" >}}

## **Konsolutgång**

{{< highlight "java" >}}

Printing Rows Indices, Cell Names and Values Hidden By AutoFilter.

\--------------------------

1       A2      Apple

2       A3      Apple

3       A4      Apple

6       A7      Apple

7       A8      Apple

11      A12     Pear

12      A13     Pear

{{< /highlight >}}
