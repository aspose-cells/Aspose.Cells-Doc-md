---
title: Sprid formel i tabell eller listobjekt automatiskt när du matar in data i nya rader
type: docs
weight: 980
url: /sv/java/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/
---

## **Möjliga användningsscenario**
Ibland vill du att en formel i din tabell eller listobjekt automatiskt sprider sig till nya rader när du matar in nya data. Detta är standardbeteendet för Microsoft Excel. För att uppnå samma sak med Aspose.Cells, använd egenskapen [ListColumn.Formula](https://reference.aspose.com/cells/java/com.aspose.cells/listcolumn#Formula).
## **Sprid formel i tabell eller listobjekt automatiskt när du matar in data i nya rader**
Följande exempelkod skapar en tabell eller listobjekt på ett sådant sätt att formeln i kolumn B automatiskt sprider sig till nya rader när du matar in nya data. Vänligen kontrollera resultatet för excelfilen som genereras med denna kod. Om du anger något nummer i cell A3, kommer du att se att formeln i cell B2 automatiskt sprider sig till cell B3.
## **Exempelkod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PropagateFormulaInTableorListObject-PropagateFormulaInTableorListObject.java" >}}
