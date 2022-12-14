---
title: Erstellen und Anpassen von Diagrammen
type: docs
weight: 10
url: /de/cpp/creating-and-customizing-charts/
---
## **Mögliche Nutzungsszenarien**

Ein Diagramm ist eine visuelle Darstellung von Informationen. Aspose.Cells ermöglicht es Entwicklern, Informationen in Diagrammen zu visualisieren, genau wie Microsoft Excel es tut. Die Darstellung von Informationen in Diagrammen ist für Entscheidungsträger immer hilfreich, um schnelle und zeitnahe Entscheidungen zu treffen. Es ist einfacher, schnell Vergleiche, Muster und Trends in Daten mit Diagrammen als mit reinen Zahlen zu erkennen. Das Erstellen von Diagrammen zur Laufzeit, basierend auf den Daten in einer Tabelle, ist eine der nützlichen Funktionen von Aspose.Cells. Aspose.Cells unterstützt das Erstellen von Standard- und benutzerdefinierten Diagrammen. Nachfolgend zeigen wir einige Beispiele mit Beispieldateien zur Erstellung einiger gängiger MS-Excel-Diagrammtypen mit Aspose.Cells API.

## **Pyramidendiagramm**

 Wenn der Beispielcode ausgeführt wird, wird dem Arbeitsblatt ein Pyramidendiagramm hinzugefügt. Bitte sehen Sie sich ... an[Excel-Datei ausgeben](66519068.xlsx) des folgenden Beispielcodes.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_PyramidChart.cpp" >}}

## **Liniendiagramm**

Im obigen Beispiel ändert man einfach die[**Diagramm Typ**](https://reference.aspose.com/cells/cpp/namespace/aspose.cells.charts#a2f17e69bcefc754569019185d0621b70)zu[**ChartType_Line**](https://reference.aspose.com/cells/cpp/namespace/aspose.cells.charts#a2f17e69bcefc754569019185d0621b70ad12ff1561ab1424a0c3095b6dc07ac25) erstellt ein Liniendiagramm. Die vollständige Quelle ist unten angegeben. Wenn der Code ausgeführt wird, wird dem Arbeitsblatt ein Liniendiagramm hinzugefügt. Bitte sehen Sie sich ... an[Excel-Datei ausgeben](66519069.xlsx) des folgenden Beispielcodes.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_LineChart.cpp" >}}

## **Blasendiagramm**

Um ein Blasendiagramm zu erstellen, muss die[**Diagramm Typ**](https://reference.aspose.com/cells/cpp/namespace/aspose.cells.charts#a2f17e69bcefc754569019185d0621b70) muss eingestellt werden[**ChartType_Bubble**](https://reference.aspose.com/cells/cpp/namespace/aspose.cells.charts#a2f17e69bcefc754569019185d0621b70a5efa533b454f9415e4497dbb2ab28b3d) und einige zusätzliche Eigenschaften wie[**SetBubbleSizes**](https://reference.aspose.com/cells/cpp/class/aspose.cells.charts.i_series#a00cf890ba7ab419d31a522ab52b02e9d) & [**SetXValues**](https://reference.aspose.com/cells/cpp/class/aspose.cells.charts.i_series#a788ff4aa51dbf9bed5327298af93a6db) müssen entsprechend eingestellt werden. Beim Ausführen des folgenden Codes wird dem Arbeitsblatt ein Blasendiagramm hinzugefügt. Bitte sehen Sie sich ... an[Excel-Datei ausgeben](66519070.xlsx) des folgenden Beispielcodes.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_BubbleChart.cpp" >}}

## **Erstellen von benutzerdefinierten Diagrammen**

Bisher haben wir uns bei der Erörterung von Diagrammen mit Standarddiagrammen befasst, die ihre eigenen Standardformatierungseinstellungen haben. Wir definieren nur die Datenquelle, legen ein paar Eigenschaften fest und das Diagramm wird mit seinen Standardformateinstellungen erstellt. Aber Aspose.Cells-APIs unterstützen auch das Erstellen benutzerdefinierter Diagramme, mit denen Entwickler Diagramme mit ihren eigenen Formateinstellungen erstellen können. Entwickler können mit Aspose.Cells zur Laufzeit benutzerdefinierte Diagramme erstellen.

Ein Diagramm besteht aus einer Datenreihe. Beim Erstellen eines benutzerdefinierten Diagramms haben Entwickler die Freiheit, verschiedene Arten von Diagrammen für verschiedene Datenreihen zu verwenden.

 Der folgende Beispielcode zeigt, wie benutzerdefinierte Diagramme erstellt werden. In diesem Beispiel verwenden wir ein Säulendiagramm für die erste Datenreihe und ein Liniendiagramm für die zweite Reihe. Das Ergebnis ist, dass wir dem Arbeitsblatt ein Säulendiagramm in Kombination mit einem Liniendiagramm hinzufügen. Bitte sehen Sie sich ... an[Excel-Datei ausgeben](66519071.xlsx) des folgenden Beispielcodes.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Charts-CreatingAndCustomizingCharts_CustomChart.cpp" >}}
