---
title: Sprid formel i tabell eller listobjekt automatiskt när du matar in data i nya rader
linktitle: Ställer in tabellformel
type: docs
weight: 260
url: /sv/net/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/
---

## **Möjliga användningsscenario**
Ibland vill du att en formel i din tabell eller listobjekt sprider automatiskt till nya rader vid inmatning av nya data. Detta är standardbeteendet i Microsoft Excel. För att uppnå samma sak med Aspose.Cells, använd [ListColumn.Formula](https://reference.aspose.com/cells/net/aspose.cells.tables/listcolumn/properties/formula) egenskapen.
## **Sprid formel i tabell eller listobjekt automatiskt när du matar in data i nya rader**
Exemplarkoden nedan skapar en tabell eller listobjekt på ett sådant sätt att formeln i kolumn B automatiskt sprider sig till nya rader när du anger ny data. Var god kontrollera den [utdata Excelfilen](5115469.xlsx) genererad med denna kod. Om du anger något nummer i cell A3, kommer du att se att formeln i cell B2 automatiskt sprider sig till cell B3.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-PropagateFormulaInTable-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
