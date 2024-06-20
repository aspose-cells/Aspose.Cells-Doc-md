---
title: Konsolideringsfunktion
type: docs
weight: 20
url: /sv/net/consolidation-function/
---

## **Konsolideringsfunktion**

Aspose.Cells kan användas för att tillämpa konsolideringsfunktion på datafält (eller värdefält) i pivottabellen. I Microsoft Excel kan du högerklicka på värdefältet och sedan välja **Värdefältsinställningar...** alternativet och sedan välja fliken **Sammanfatta värden med**. Där kan du välja valfri konsolideringsfunktion som Summa, Antal, Medel, Max, Min, Produkt, Distinkt antal, etc.

Aspose.Cells tillhandahåller uppräkning för att stödja följande konsolideringsfunktioner.

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

### **Tillämpning av ConsolidationFunction på datavärderna i pivottabellen**

Följande kod tillämpar **Medelvärde** konsolideringsfunktion på det första datafältet (eller värdefältet) och **DistinktAntal** konsolideringsfunktion på det andra datafältet (eller värdefältet).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-ConsolidationFunctions-1.cs" >}}

{{% alert color="primary" %}}

Distinkt antal konsolideringsfunktionen stöds endast av Microsoft Excel 2013.

{{% /alert %}}
