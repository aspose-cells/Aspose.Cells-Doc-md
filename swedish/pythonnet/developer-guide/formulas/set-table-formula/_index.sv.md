---
title: Sprid formel i tabell eller listobjekt automatiskt när du matar in data i nya rader
linktitle: Ställer in tabellformel
type: docs
weight: 260
url: /sv/python-net/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/
---

## **Möjliga användningsscenario**
Ibland vill du att en formel i din tabell eller listobjekt automatiskt ska spridas till nya rader när du skriver in nya data. Det är standardbeteendet i Microsoft Excel. För att åstadkomma samma sak med Aspose.Cells för Python via .NET, använd [**ListColumn.formula**](https://reference.aspose.com/cells/python-net/aspose.cells.tables/listcolumn/formula)-egenskapen.

## **Sprid formel i tabell eller listobjekt automatiskt när du matar in data i nya rader**
Exemplarkoden nedan skapar en tabell eller listobjekt på ett sådant sätt att formeln i kolumn B automatiskt sprider sig till nya rader när du anger ny data. Var god kontrollera den [utdata Excelfilen](5115469.xlsx) genererad med denna kod. Om du anger något nummer i cell A3, kommer du att se att formeln i cell B2 automatiskt sprider sig till cell B3.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-PropagateFormulaInTable-1.py" >}}

