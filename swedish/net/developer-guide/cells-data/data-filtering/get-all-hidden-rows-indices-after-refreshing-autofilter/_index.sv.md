---
title: Få alla dolda rader efter att ha uppdaterat autofiltret
type: docs
weight: 320
url: /sv/net/get-all-hidden-rows-indices-after-refreshing-autofilter/
description: Lär dig hur du får alla dolda radindex efter att ha uppdaterat AutoFilter genom att använda Aspose.Cells for .NET API.
keywords: Get All Hidden Rows Indices after Refreshing AutoFilter, Obtain All Hidden Rows Indices after Refreshing AutoFilter, Retrieve All Hidden Rows Indices after Refreshing AutoFilter
---
##  **Möjliga användningsscenarier**

När du använder autofiltret på kalkylbladsceller döljs några av raderna automatiskt. Men det kan vara så att några av raderna redan är dolda manuellt av Excel-slutanvändare och de är inte dolda av ett autofilter. Det gör därför svårt att veta vilka av raderna som döljs av autofiltret och vilka av dem som döljs manuellt av Excel-slutanvändare. Aspose.Cells hanterar detta problem med hjälp av int[][**AutoFilter.Refresh(bool hideRows)**](https://reference.aspose.com/cells/net/aspose.cells.autofilter/refresh/methods/1)metod. Denna metod returnerar radindexen för alla rader som är dolda av autofiltret och inte manuellt av Excel-slutanvändaren.

##  **Få alla dolda rader efter att ha uppdaterat autofiltret**

 Se följande exempelkod som laddar[exempel på Excel-fil](64716909.xlsx) som innehåller några av raderna som döljs manuellt av Excel-slutanvändare. Koden tillämpar autofiltret och uppdaterar det med int[][**AutoFilter.Refresh(bool hideRows)**](https://reference.aspose.com/cells/net/aspose.cells.autofilter/refresh/methods/1)metod som returnerar radindexen för alla dolda rader av autofiltret. Den skriver sedan ut indexen för de dolda raderna på konsolen tillsammans med cellnamn och värden.

##  **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Data-GetAllHiddenRowsIndicesAfterRefreshingAutoFilter.cs" >}}

##  **Konsolutgång**

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
