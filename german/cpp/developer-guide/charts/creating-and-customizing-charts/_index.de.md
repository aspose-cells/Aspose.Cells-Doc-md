---
title: Erstellen und Anpassen von Diagrammen
type: docs
weight: 10
url: /de/cpp/creating-and-customizing-charts/
---

## **Mögliche Verwendungsszenarien**

Ein Diagramm ist eine visuelle Darstellung von Informationen. Aspose.Cells ermöglicht es Entwicklern, Informationen in Diagrammen genauso anzuzeigen wie Microsoft Excel. Die Präsentation von Informationen in Diagrammen ist für Entscheidungsträger immer hilfreich, um schnelle und rechtzeitige Entscheidungen zu treffen. Mit Diagrammen lassen sich Vergleiche, Muster und Trends in Daten schnell erkennen, im Gegensatz zu reinen Zahlen. Das Erstellen von Diagrammen zur Laufzeit basierend auf den Daten in einer Tabellenkalkulation ist eine der nützlichen Funktionen von Aspose.Cells. Aspose.Cells unterstützt die Erstellung sowohl von Standard- als auch von benutzerdefinierten Diagrammen. Im Folgenden werden einige Beispiele mit Beispieldateien gezeigt, wie man mit der Aspose.Cells-API einige gängige MS-Excel-Diagrammtypen erstellt.

## **Pyramiden-Diagramm**

Wenn der Beispielcode ausgeführt wird, wird dem Arbeitsblatt ein Pyramiden-Diagramm hinzugefügt. Bitte beachten Sie die [Ausgabedatei in Excel](66519068.xlsx) des folgenden Beispielcodes.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_PyramidChart-new.cpp" >}}

## **Linien-Diagramm**

In obigem Beispiel wird durch einfaches Ändern von [**ChartType**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttype/) in **`ChartType::Line`** ein Linien-Diagramm erstellt. Der vollständige Quellcode wird unten bereitgestellt. Bei Ausführung des Codes wird dem Arbeitsblatt ein Linien-Diagramm hinzugefügt. Bitte beachten Sie die [Ausgabedatei in Excel](66519069.xlsx) des folgenden Beispielcodes.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_LineChart-new.cpp" >}}

## **Bubble-Diagramm**

Um ein Bubble-Diagramm zu erstellen, muss [**ChartType**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttype/) auf **`ChartType_Bubble`** gesetzt werden und einige zusätzliche Eigenschaften wie [**SetBubbleSizes**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/setbubblesizes/) & [**SetXValues**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/series/setxvalues/) müssen entsprechend festgelegt werden. Beim Ausführen des folgenden Codes wird dem Arbeitsblatt ein Bubble-Diagramm hinzugefügt. Bitte beachten Sie die [Ausgabedatei in Excel](66519070.xlsx) des folgenden Beispielcodes.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_BubbleChart-new.cpp" >}}

## **Erstellen von benutzerdefinierten Diagrammen**

Bisher haben wir bei der Diskussion über Diagramme Standarddiagramme betrachtet, die über ihre eigenen standardmäßigen Formatierungseinstellungen verfügen. Wir definieren lediglich die Datenquelle, setzen einige Eigenschaften und das Diagramm wird mit seinen Standardformatierungseinstellungen erstellt. Aber Aspose.Cells-APIs unterstützt auch die Erstellung benutzerdefinierter Diagramme, die es Entwicklern ermöglichen, Diagramme mit ihren eigenen Formatierungseinstellungen zu erstellen. Entwickler können zur Laufzeit benutzerdefinierte Diagramme mit Aspose.Cells erstellen.

Ein Diagramm besteht aus einer Datenreihe. Beim Erstellen eines benutzerdefinierten Diagramms haben Entwickler die Freiheit, verschiedene Arten von Diagrammen für verschiedene Datenreihen zu verwenden.

Der folgende Beispielcode zeigt, wie benutzerdefinierte Diagramme erstellt werden. In diesem Beispiel verwenden wir ein Säulendiagramm für die erste Datenserie und ein Liniendiagramm für die zweite Serie. Das Ergebnis ist, dass wir ein Säulendiagramm zusammen mit einem Liniendiagramm zum Arbeitsblatt hinzufügen. Bitte sehen Sie die [Ausgabedatei Excel](66519071.xlsx) des folgenden Beispielcodes.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_CustomChart-new.cpp" >}}
