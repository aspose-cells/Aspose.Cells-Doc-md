---
title: Konsolideringsfunktion
type: docs
weight: 20
url: /sv/java/consolidation-function/
description: Använd ConsolidationFunction på datafälten i pivottabellen.
---
## **Konsolideringsfunktion**

 Aspose.Cells kan användas för att tillämpa ConsolidationFunction på datafält (eller värdefält) i pivottabellen. I Microsoft Excel kan du högerklicka på värdefältet och sedan välja**Inställningar för värdefält...** och välj sedan fliken**Sammanfatta värden efter**. Därifrån kan du välja valfri konsolideringsfunktion som Summa, Antal, Genomsnitt, Max, Min, Produkt, Distinkt antal, etc.

 Aspose.Cells tillhandahåller[**Konsolideringsfunktion**](https://reference.aspose.com/cells/java/com.aspose.cells/ConsolidationFunction) uppräkning för att stödja följande konsolideringsfunktioner.

- ConsolidationFunction.SUM
- ConsolidationFunction.COUNT
- ConsolidationFunction.AVERAGE
- ConsolidationFunction.MAX
- Consolidation Function.MIN
- ConsolidationFunction.PRODUCT
- Consolidation Function.COUNT_NUMS
- ConsolidationFunction.STD_DEV
- ConsolidationFunction.STD_DEVP
- ConsolidationFunction.VAR
- ConsolidationFunction.VARP
- ConsolidationFunction.DISTINCT_COUNT

### **Tillämpa ConsolidationFunction på datafält i pivottabellen**

 Följande kod gäller**MEDEL** konsolideringsfunktion till det första datafältet (eller värdefältet) och**STD_DEV** konsolideringsfunktion till det andra datafältet (eller värdefältet).

Exempel på källfil och utdatafiler kan laddas ner härifrån för att testa exempelkoden:

[Excel-källfil](source.xlsx)

[Utdata Excel-fil](output.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-CreatePivotTable-ConsolidationFunction.java" >}}

{{% alert color="primary" %}}

DistinctCount-konsolideringsfunktionen stöds endast av Microsoft Excel 2013.

{{% /alert %}}

