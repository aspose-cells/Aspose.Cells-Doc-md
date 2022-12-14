---
title: Konsolidierungsfunktion
type: docs
weight: 20
url: /de/java/consolidation-function/
description: ConsolidationFunction auf Datenfelder der Pivot-Tabelle anwenden.
---
## **Konsolidierungsfunktion**

 Aspose.Cells kann verwendet werden, um ConsolidationFunction auf Datenfelder (oder Wertfelder) der Pivot-Tabelle anzuwenden. In Microsoft Excel können Sie mit der rechten Maustaste auf das Wertefeld klicken und dann auswählen**Wertfeldeinstellungen...** Option und wählen Sie dann die Registerkarte aus**Werte zusammenfassen nach**. Von dort aus können Sie eine beliebige Konsolidierungsfunktion Ihrer Wahl auswählen, z. B. Summe, Anzahl, Durchschnitt, Max, Min, Produkt, Distinct Count usw.

 Aspose.Cells bietet[**Konsolidierungsfunktion**](https://reference.aspose.com/cells/java/com.aspose.cells/ConsolidationFunction) Enumeration zur Unterstützung der folgenden Konsolidierungsfunktionen.

- Konsolidierungsfunktion.SUM
- Konsolidierungsfunktion.COUNT
- Konsolidierungsfunktion.AVERAGE
- Konsolidierungsfunktion.MAX
- Konsolidierungsfunktion.MIN
- Konsolidierungsfunktion.PRODUKT
- Konsolidierungsfunktion.COUNT_NUMS
- Konsolidierungsfunktion.STD_DEV
- Konsolidierungsfunktion.STD_DEVP
- Konsolidierungsfunktion.VAR
- Konsolidierungsfunktion.VARP
- Konsolidierungsfunktion.DISTINCT_COUNT

### **ConsolidationFunction auf Datenfelder der Pivot-Tabelle anwenden**

 Es gilt der folgende Code**DURCHSCHNITT** Konsolidierungsfunktion zum ersten Datenfeld (oder Wertfeld) und**STD_DEV** Konsolidierungsfunktion auf das zweite Datenfeld (oder Wertefeld).

Beispielquelldatei und Ausgabedateien können hier zum Testen des Beispielcodes heruntergeladen werden:

[Excel-Quelldatei](source.xlsx)

[Excel-Datei ausgeben](output.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-PivotTables-CreatePivotTable-ConsolidationFunction.java" >}}

{{% alert color="primary" %}}

Die DistinctCount-Konsolidierungsfunktion wird nur von Microsoft Excel 2013 unterstützt.

{{% /alert %}}

