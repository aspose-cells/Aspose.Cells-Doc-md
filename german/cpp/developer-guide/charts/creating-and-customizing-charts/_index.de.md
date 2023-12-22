---
title: Diagramme erstellen und anpassen
type: docs
weight: 10
url: /de/cpp/creating-and-customizing-charts/
---
##  **Mögliche Nutzungsszenarien**

Ein Diagramm ist eine visuelle Darstellung von Informationen. Aspose.Cells ermöglicht Entwicklern die Visualisierung von Informationen in Diagrammen, genau wie Microsoft Excel. Die Darstellung von Informationen in Diagrammen ist für Entscheidungsträger immer hilfreich, um schnelle und zeitnahe Entscheidungen zu treffen. Mit Diagrammen ist es einfacher, Vergleiche, Muster und Trends in Daten schnell zu erkennen als mit reinen Zahlen. Das Erstellen von Diagrammen zur Laufzeit basierend auf den Daten in einer Tabellenkalkulation ist eine der nützlichen Funktionen von Aspose.Cells. Aspose.Cells unterstützt die Erstellung von Standard- und benutzerdefinierten Diagrammen. Im Folgenden zeigen wir einige Beispiele mit Beispieldateien zum Erstellen einiger gängiger MS-Excel-Diagrammtypen mit Aspose.Cells API.

##  **Pyramidendiagramm**

 Wenn der Beispielcode ausgeführt wird, wird dem Arbeitsblatt ein Pyramidendiagramm hinzugefügt. Bitte sehen Sie sich ... an[Excel-Datei ausgeben](66519068.xlsx) des folgenden Beispielcodes.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_PyramidChart-new.cpp" >}}

##  **Liniendiagramm**

Im obigen Beispiel einfach die ändern[**Diagramm Typ**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttype/)Zu**„ChartType::Line“.**erstellt ein Liniendiagramm. Die vollständige Quelle finden Sie unten. Wenn der Code ausgeführt wird, wird dem Arbeitsblatt ein Liniendiagramm hinzugefügt. Bitte sehen Sie sich ... an[Excel-Datei ausgeben](66519069.xlsx) des folgenden Beispielcodes.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_LineChart-new.cpp" >}}

##  **Blasendiagramm**

Um ein Blasendiagramm zu erstellen, muss das[**Diagramm Typ**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttype/) muss eingestellt werden**„ChartType_Bubble“.** und einige zusätzliche Eigenschaften wie[**SetBubbleSizes**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/setbubblesizes/) & [**SetXValues**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/setxvalues/) müssen entsprechend eingestellt werden. Beim Ausführen des folgenden Codes wird dem Arbeitsblatt ein Blasendiagramm hinzugefügt. Bitte sehen Sie sich ... an[Excel-Datei ausgeben](66519070.xlsx) des folgenden Beispielcodes.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_BubbleChart-new.cpp" >}}

##  **Erstellen benutzerdefinierter Diagramme**

Bisher haben wir uns bei der Besprechung von Diagrammen mit Standarddiagrammen befasst, die ihre eigenen Standardformatierungseinstellungen haben. Wir definieren nur die Datenquelle, legen einige Eigenschaften fest und das Diagramm wird mit seinen Standardformateinstellungen erstellt. Aber Aspose.Cells APIs unterstützen auch die Erstellung benutzerdefinierter Diagramme, die es Entwicklern ermöglichen, Diagramme mit ihren eigenen Formateinstellungen zu erstellen. Entwickler können mit Aspose.Cells zur Laufzeit benutzerdefinierte Diagramme erstellen.

Ein Diagramm besteht aus einer Datenreihe. Beim Erstellen eines benutzerdefinierten Diagramms haben Entwickler die Freiheit, verschiedene Diagrammtypen für verschiedene Datenreihen zu verwenden.

 Der folgende Beispielcode zeigt, wie Sie benutzerdefinierte Diagramme erstellen. In diesem Beispiel verwenden wir ein Säulendiagramm für die erste Datenreihe und ein Liniendiagramm für die zweite Reihe. Das Ergebnis ist, dass wir dem Arbeitsblatt ein Säulendiagramm in Kombination mit einem Liniendiagramm hinzufügen. Bitte sehen Sie sich ... an[Excel-Datei ausgeben](66519071.xlsx) des folgenden Beispielcodes.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_CustomChart-new.cpp" >}}
