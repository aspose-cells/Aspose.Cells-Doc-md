---
title: Konsolideringsfunktion
type: docs
weight: 20
url: /sv/python-net/consolidation-function/
description: Hur man tillämpar konsolideringsfunktion på datapunkterna i pivottabellen med Aspose.Cells för Python via .NET.
keywords: Aspose.Cells for Python Excel, Excel Python bibliotek, konsolideringsfunktion till datapunkterna i pivottabellen med hjälp av Aspose.Cells för Python Excel Library.
---

## **Konsolideringsfunktion**

Aspose.Cells for Python via .NET kan användas för att tillämpa konsolideringsfunktion på datapunkterna (eller värdespunkterna) i pivottabellen. I Microsoft Excel kan du högerklicka på värdefältet och sedan välja **Alternativ för värdefält...** och sedan välja fliken **Summera värden efter**. Där kan du välja valfri konsolideringsfunktion som Summa, Antal, Medel, Max, Min, Produkt, Unikt antal, osv.

Aspose.Cells för Python via .NET tillhandahåller [**ConsolidationFunction**](https://reference.aspose.com/cells/python-net/aspose.cells/consolidationfunction/) uppräkning för att stödja följande konsolideringsfunktioner.

- ConsolidationFunction.AVERAGE
- ConsolidationFunction.COUNT
- ConsolidationFunction.COUNT_NUMS
- ConsolidationFunction.DISTINCT_COUNT
- ConsolidationFunction.MAX
- ConsolidationFunction.MIN
- ConsolidationFunction.PRODUCT
- ConsolidationFunction.STD_DEV
- ConsolidationFunction.STD_DEVP
- ConsolidationFunction.SUM
- ConsolidationFunction.VAR
- ConsolidationFunction.VARP

## **Hur man tillämpar konsolideringsfunktion på datapunkterna i pivottabellen med hjälp av Aspose.Cells för Python Excel-bibliotek**

Följande kod tillämpar **MEDEL** konsolideringsfunktion på det första datapunkten (eller värdespunkten) och **DISTINCT_COUNT** konsolideringsfunktion på den andra datapunkten (eller värdespunkten).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTables-ConsolidationFunctions-1.py" >}}

{{% alert color="primary" %}}

DISTINCT_COUNT konsolideringsfunktion stöds endast av Microsoft Excel 2013.

{{% /alert %}}
