---
title: Få alla dolda radindex efter att autofiltreringen har uppdaterats
type: docs
weight: 320
url: /sv/net/get-all-hidden-rows-indices-after-refreshing-autofilter/
description: Lär dig hur man får alla dolda radindex efter att ha uppdaterat automatiskt filter med hjälp av API et Aspose.Cells for .NET.
keywords: Hämta alla dolda radindex efter att ha uppdaterat automatiskt filter, Hämta alla dolda radindex efter att ha uppdaterat automatiskt filter, Visa alla dolda radindex efter att ha uppdaterat automatiskt filter
---

## **Möjliga användningsscenario**

När du tillämpar automatiskt filter på kalkylbladsceller, göms vissa rader automatiskt. Men det kan vara så att vissa rader redan är gömda manuellt av Excel-användaren och de göms inte av ett automatiskt filter. Det gör det därför svårt att veta vilka rader som göms av automatiskt filter och vilka som göms manuellt av Excel-användaren. Aspose.Cells hanterar detta problem med int[] [**AutoFilter.Refresh(bool hideRows)**](https://reference.aspose.com/cells/net/aspose.cells.autofilter/refresh/methods/1) metoden. Denna metod returnerar radindex för alla rader som göms av automatiskt filter och inte manuellt av Excel-användaren.

## **Hämta alla dolda radindex efter uppdatering av autofilter**

Se följande exempelkod som läser in [exempel på Excel-fil](64716909.xlsx) som innehåller några av de rader som göms manuellt av Excel-användaren. Koden tillämpar automatiskt filter och uppdaterar det med hjälp av int[] [**AutoFilter.Refresh(bool hideRows)**](https://reference.aspose.com/cells/net/aspose.cells.autofilter/refresh/methods/1) metoden som returnerar radindex för alla gömda rader av automatiskt filter. Det skriver sedan ut indexen för de gömda raderna i konsolen tillsammans med cellnamn och värden.

## **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Data-GetAllHiddenRowsIndicesAfterRefreshingAutoFilter.cs" >}}

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
