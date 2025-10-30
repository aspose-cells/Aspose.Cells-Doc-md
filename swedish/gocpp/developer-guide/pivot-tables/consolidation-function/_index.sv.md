---
title: Konsolideringsfunktion med Golang via C++
linktitle: Konsolideringsfunktion
type: docs
weight: 20
url: /sv/go-cpp/consolidation-function/
description: Lär dig hur du tillämpar konsolideringsfunktion på datafält i en pivottabell med Aspose.Cells med Golang via C++.
---

## **Konsolideringsfunktion**

Aspose.Cells kan användas för att tillämpa konsolideringsfunktion på datafält (eller värdefält) i pivottabellen. I Microsoft Excel kan du högerklicka på värdefältet och sedan välja **Värdefältsinställningar...** alternativet och sedan välja fliken **Sammanfatta värden med**. Där kan du välja valfri konsolideringsfunktion som Summa, Antal, Medel, Max, Min, Produkt, Distinkt antal, etc.

Aspose.Cells tillhandahåller uppräkning för att stödja följande konsolideringsfunktioner.

- ConsolidationFunction::Average
- ConsolidationFunction::Count
- ConsolidationFunction::CountNums
- ConsolidationFunction::DistinctCount
- ConsolidationFunction::Max
- ConsolidationFunction::Min
- ConsolidationFunction::Product
- ConsolidationFunction::StdDev
- ConsolidationFunction::StdDevp
- ConsolidationFunction::Sum
- ConsolidationFunction::Var
- ConsolidationFunction::Varp

### **Tillämpning av ConsolidationFunction på datavärderna i pivottabellen**

Följande kod tillämpar **Medelvärde** konsolideringsfunktion på det första datafältet (eller värdefältet) och **DistinktAntal** konsolideringsfunktion på det andra datafältet (eller värdefältet).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConsolidationFunction.go" >}}
{{% alert color="primary" %}}

Distinkt antal konsolideringsfunktionen stöds endast av Microsoft Excel 2013.

{{% /alert %}}
