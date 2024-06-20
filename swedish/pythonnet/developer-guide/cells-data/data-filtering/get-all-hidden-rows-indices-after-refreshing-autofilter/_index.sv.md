---
title: Få alla dolda radindex efter att autofiltreringen har uppdaterats
type: docs
weight: 320
url: /sv/python-net/get-all-hidden-rows-indices-after-refreshing-autofilter/
description: Lär dig hur du får alla dolda radindex efter att autofiltreringen har uppdaterats genom att använda Aspose.Cells for Python via .NET API.
keywords: Python Excel bibliotek, Python Hämta alla dolda radindex efter att autofiltreringen har uppdaterats, Python Hämta alla dolda radindex efter att autofiltreringen har uppdaterats, Python Hämta alla dolda radindex efter att autofiltreringen har uppdaterats
---

## **Möjliga användningsscenario**

När du tillämpar autofilter på kalkylbladsceller göms vissa rader automatiskt. Men det kan hända att vissa rader redan är dolda manuellt av Excel-användaren och de är inte dolda av en autofilter. Det gör det därför svårt att veta vilka av raderna som är dolda av autofiltret och vilka av dem som är dolda manuellt av Excel-användaren. Aspose.Cells for Python via .NET hanterar detta problem med hjälp av metoden [**AutoFilter.refresh(hide_rows)**](https://reference.aspose.com/cells/python-net/aspose.cells/autofilter/refresh/#bool). Denna metod returnerar radindex för alla rader som är dolda av autofiltret och inte manuellt av Excel-användaren.

## **Hämta alla dolda radindex efter uppdatering av autofilter**

Se följande exemplarkod som laddar den [exempelfil för Excel](64716909.xlsx) som innehåller några av raderna som är gömda manuellt av Excel-användaren. Koden tillämpar autofiltret och uppdaterar det med hjälp av metoden [**AutoFilter.refresh(hide_rows)**](https://reference.aspose.com/cells/python-net/aspose.cells/autofilter/refresh/#bool) som returnerar radindex för alla dolda rader av autofiltret. Den skriver sedan ut index för de dolda raderna på konsollen tillsammans med cellnamn och värden.

## **Exempelkod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-GetAllHiddenRowsIndicesAfterRefreshingAutoFilter.py" >}}

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
