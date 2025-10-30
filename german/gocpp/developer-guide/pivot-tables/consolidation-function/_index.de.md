---
title: Konsolidierungsfunktion mit Golang via C++
linktitle: Konsolidierungsfunktion
type: docs
weight: 20
url: /de/go-cpp/consolidation-function/
description: Erlernen, wie man die Konsolidierungsfunktion auf Datenfelder einer Pivot Tabelle mit Aspose.Cells und Golang via C++ anwendet.
---

## **Konsolidierungsfunktion**

Mit Aspose.Cells kann die Konsolidierungsfunktion auf Datenfelder (oder Wertefelder) der Pivot-Tabelle angewendet werden. In Microsoft Excel können Sie mit der rechten Maustaste auf das Wertefeld klicken und dann die Option **Wertfeldeinstellungen...** auswählen, und dann den Tab **Werte zusammenfassen nach** auswählen. Von dort aus können Sie eine Konsolidierungsfunktion Ihrer Wahl wie Summe, Anzahl, Durchschnitt, Maximum, Minimum, Produkt, Eindeutige Anzahl usw. auswählen.

Aspose.Cells bietet die Aufzählung [**ConsolidationFunction**](https://reference.aspose.com/cells/go-cpp/consolidationfunction/), um die folgenden Konsolidierungsfunktionen zu unterstützen.

- Konsolidierungsfunktion::Durchschnitt
- Konsolidierungsfunktion::Anzahl
- Konsolidierungsfunktion::ZähleNummern
- Konsolidierungsfunktion::EindeutigeAnzahl
- Konsolidierungsfunktion::Max
- Konsolidierungsfunktion::Min
- Konsolidierungsfunktion::Produkt
- Konsolidierungsfunktion::Standardabweichung
- Konsolidierungsfunktion::PopStandardabweichung
- Konsolidierungsfunktion::Summe
- Konsolidierungsfunktion::Varianz
- Konsolidierungsfunktion::PopVarianz

### **Anwendung von ConsolidationFunction auf Datenfelder des Pivot-Tabellen**

Der folgende Code wendet die **Durchschnitt**-Konsolidierungsfunktion auf das erste Datenfeld (oder Wertefeld) und die **DistinctCount**-Konsolidierungsfunktion auf das zweite Datenfeld (oder Wertefeld) an.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConsolidationFunction.go" >}}
{{% alert color="primary" %}}

Die Konsolidierungsfunktion DistinctCount wird nur von Microsoft Excel 2013 unterstützt.

{{% /alert %}}
