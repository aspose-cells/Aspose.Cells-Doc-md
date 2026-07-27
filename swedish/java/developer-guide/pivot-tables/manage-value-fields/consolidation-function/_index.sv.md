---
title: Konsolideringsfunktion
type: docs
weight: 20
url: /sv/java/consolidation-function/
description: Tillämpa konsolideringsfunktion på datapositioner i pivot tabellen.
---

## **Konsolideringsfunktion**

Aspose.Cells kan användas för att tillämpa konsolideringsfunktion på datafält (eller värdefält) i pivottabellen. I Microsoft Excel kan du högerklicka på värdefältet och sedan välja **Värdefältsinställningar...** alternativet och sedan välja fliken **Sammanfatta värden med**. Där kan du välja valfri konsolideringsfunktion som Summa, Antal, Medel, Max, Min, Produkt, Distinkt antal, etc.

Aspose.Cells tillhandahåller uppräkning för att stödja följande konsolideringsfunktioner.

- ConsolidationFunction.SUM
- ConsolidationFunction.COUNT
- ConsolidationFunction.AVERAGE
- ConsolidationFunction.MAX
- ConsolidationFunction.MIN
- ConsolidationFunction.PRODUCT
- ConsolidationFunction.COUNT_NUMS
- ConsolidationFunction.STD_DEV
- ConsolidationFunction.STD_DEVP
- ConsolidationFunction.VAR
- ConsolidationFunction.VARP
- ConsolidationFunction.DISTINCT_COUNT

### **Tillämpning av ConsolidationFunction på datavärderna i pivottabellen**

Följande kod tillämpar konsolideringsfunktionen **MEDEL** på den första datapositionen (eller värdepsitionen) och **STD_AVVIK** konsolideringsfunktion på den andra datapositionen (eller värdepsitionen).

Provfil och utdatafiler kan laddas ner här för att testa provkoden:

[Käll-Excel-fil](source.xlsx)

[Utdata Excel-fil](output.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-CreatePivotTable-ConsolidationFunction.java" >}}

{{% alert color="primary" %}}

Distinkt antal konsolideringsfunktionen stöds endast av Microsoft Excel 2013.

{{% /alert %}}

{{< app/cells/assistant language="java" >}}
