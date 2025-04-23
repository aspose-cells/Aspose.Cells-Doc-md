---
title: Konsolideringsfunktion
type: docs
weight: 20
url: /sv/nodejs-cpp/consolidation-function/
description: Hur man tillämpar ConsolidationFunction på Datafält i Pivot tabell med Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells for Node.js via C++ Excel, Excel Node.js bibliotek, ConsolidationFunction till Datafält i Pivot tabell med Aspose.Cells for Node.js via C++ Excel bibliotek.
---

## **Konsolideringsfunktion**

Aspose.Cells for Node.js via C++ kan användas för att tillämpa ConsolidationFunction på datafält (eller värdefält) i pivot-tabellen. I Microsoft Excel kan du högerklicka på värdefältet och välja **Value Field Settings...**, och sedan välja fliken **Summarize Values By**. Där kan du välja vilken ConsolidationFunction du vill ha, som Summa, Räkna, Medel, Max, Min, Produkt, Distinkt räknare, etc.

Aspose.Cells for Node.js via C++ tillhandahåller [**ConsolidationFunction**](https://reference.aspose.com/cells/nodejs-cpp/consolidationfunction/)-enum för att stödja följande konsolidationsfunktioner.

- ConsolidationFunction.Average
- ConsolidationFunction.Count
- ConsolidationFunction.CountNums
- ConsolidationFunction.DistinctCount
- ConsolidationFunction.Max
- ConsolidationFunction.Min
- ConsolidationFunction.Product
- ConsolidationFunction.StdDev
- ConsolidationFunction.StdDevp
- ConsolidationFunction.Sum
- ConsolidationFunction.Var
- ConsolidationFunction.Varp

## **Hur man tillämpar ConsolidationFunction på Datafält i Pivot-tabell med Aspose.Cells for Node.js via C++**

Följande kod tillämpar **Medelvärde** konsolideringsfunktion på det första datafältet (eller värdefältet) och **DistinktAntal** konsolideringsfunktion på det andra datafältet (eller värdefältet).

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-ConsolidationFunctions-1.js" >}}

{{% alert color="primary" %}}

DISTINCT_COUNT konsolideringsfunktion stöds endast av Microsoft Excel 2013.

{{% /alert %}}
