---
title: Konsolidierungsfunktion
type: docs
weight: 20
url: /de/java/consolidation-function/
description: Konsolidierungsfunktion auf Datenfelder der Pivot Tabelle anwenden
---

## **Konsolidierungsfunktion**

Mit Aspose.Cells kann die Konsolidierungsfunktion auf Datenfelder (oder Wertefelder) der Pivot-Tabelle angewendet werden. In Microsoft Excel können Sie mit der rechten Maustaste auf das Wertefeld klicken und dann die Option **Wertfeldeinstellungen...** auswählen, und dann den Tab **Werte zusammenfassen nach** auswählen. Von dort aus können Sie eine Konsolidierungsfunktion Ihrer Wahl wie Summe, Anzahl, Durchschnitt, Maximum, Minimum, Produkt, Eindeutige Anzahl usw. auswählen.

Aspose.Cells bietet die Aufzählung [**ConsolidationFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ConsolidationFunction), um die folgenden Konsolidierungsfunktionen zu unterstützen.

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

### **Anwendung von ConsolidationFunction auf Datenfelder des Pivot-Tabellen**

Der folgende Code wendet die Konsolidierungsfunktion **AVERAGE** auf das erste Datenfeld (oder Wertfeld) und die Konsolidierungsfunktion **STD_DEV** auf das zweite Datenfeld (oder Wertfeld) an.

Die Beispieldatei und die Ausgabedateien können von hier heruntergeladen werden, um den Beispielcode zu testen:

[Quelldatei Excel](source.xlsx)

[Ausgabedatei Excel](output.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-CreatePivotTable-ConsolidationFunction.java" >}}

{{% alert color="primary" %}}

Die Konsolidierungsfunktion DistinctCount wird nur von Microsoft Excel 2013 unterstützt.

{{% /alert %}}

{{< app/cells/assistant language="java" >}}
