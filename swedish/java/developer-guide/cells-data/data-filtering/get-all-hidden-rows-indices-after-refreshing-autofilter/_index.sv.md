---
title: Få alla dolda radindex efter att autofiltreringen har uppdaterats
type: docs
weight: 240
url: /sv/java/get-all-hidden-rows-indices-after-refreshing-autofilter/
---

## **Möjliga användningsscenario**

När du tillämpar ett autofilter på arbetsbladsceller, försvinner vissa rader automatiskt. Men det kan vara så att vissa rader redan är gömda manuellt av Excel slutanvändare och de är inte dolda av autofiltret. Det är därför svårt att veta vilka av raderna som är gömda av autofiltret och vilka av dem som är gömda manuellt av Excel slutanvändare. Aspose.Cells hanterar detta problem med hjälp av int[] [**AutoFilter.refresh(bool hideRows)**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#refresh(boolean)) metoden. Denna metod returnerar radindex för alla rader som är gömda av autofiltret och inte manuellt av Excel slutanvändare.

## **Hämta alla dolda radindex efter uppdatering av autofilter**

Se följande provkod som laddar [prov Excel-fil](64716913.xlsx) som innehåller några av raderna som är gömda manuellt av Excel slutanvändare. Koden tillämpar autofiltret och uppdaterar det med int[] [**AutoFilter.refresh(bool hideRows)**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#refresh(boolean)) metoden som returnerar radindex för alla gömda rader av autofiltret. Det skriver sedan ut indexen för de gömda raderna på konsolen tillsammans med cellnamn och värden.

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Data-GetAllHiddenRowsIndicesAfterRefreshingAutoFilter.java" >}}

## **Konsoloutput**

{{< highlight java >}}

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
