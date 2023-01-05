---
title: Sprid formel i tabell eller listobjekt automatiskt medan du anger data i nya rader
linktitle: Ställer tabellformel
type: docs
weight: 260
url: /sv/net/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/
---
## **Möjliga användningsscenarier**
 Ibland vill du att en formel i din tabell eller listobjekt automatiskt ska spridas till nya rader samtidigt som ny data skrivs in. Detta är standardbeteendet för Microsoft Excel. För att uppnå samma sak med Aspose.Cells, använd[ListColumn.Formula](https://reference.aspose.com/cells/net/aspose.cells.tables/listcolumn/properties/formula)fast egendom.
## **Sprid formel i tabell eller listobjekt automatiskt medan du anger data i nya rader**
Följande exempelkod skapar ett tabell- eller listobjekt på ett sådant sätt att formeln i kolumn B automatiskt sprids till nya rader när du anger nya data. Vänligen kontrollera[output excel-fil](5115469.xlsx) genereras med denna kod. Om du anger valfritt tal i cell A3 kommer du att se att formeln i cell B2 automatiskt fortplantas till cell B3.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-PropagateFormulaInTable-1.cs" >}}
