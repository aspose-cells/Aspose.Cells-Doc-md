---
title: Position, Größe und Designer des Diagramms manipulieren
description: Erfahren Sie, wie Sie Aspose.Cells für Python via .NET verwenden, um die Position, Größe und Designer Diagramme in Microsoft Excel effektiv zu manipulieren. Unser Leitfaden zeigt, wie diese Eigenschaften für eine verbesserte Anordnung und Visualisierung angepasst werden.
keywords: Aspose.Cells für Python via .NET, Position, Größe, Designer Diagramm, Microsoft Excel, Layout, Visualisierung.
type: docs
weight: 45
url: /de/python-net/manipulate-position-size-and-designer-chart/
---

## **Chart-Position und Größe**
Manchmal möchten Sie die Position oder Größe des neuen oder bestehenden Diagramms innerhalb des Arbeitsblatts ändern. Aspose.Cells für Python via .NET stellt die [Chart.chart_object](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/chart_object) Eigenschaft bereit, um dies zu erreichen. Sie können die Untereigenschaften verwenden, um das Diagramm mit neuer **Höhe** und **Breite** neu zu dimensionieren oder mit neuen **X**- und **Y**-Koordinaten neu zu positionieren.
### **Steuerung der Diagrammposition und -größe**
Um die Position (X, Y-Koordinaten) oder Größe (Höhe, Breite) des Diagramms zu ändern, verwenden Sie diese Eigenschaften:

1. [Chart.chart_object.x](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/x)
1. [Chart.chart_object.y](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/y)
1. [Chart.chart_object.height](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/height)
1. [Chart.chart_object.width](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/width)

Das folgende Beispiel zeigt die Verwendung der oben genannten APIs. Es lädt die bestehende Arbeitsmappe, die ein Diagramm im ersten Arbeitsblatt enthält. Anschließend wird das Diagramm mit Aspose.Cells für Python via .NET in Größe und Position verändert.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ChangeChartPosition-1.py" >}}
## **Manipulation von Designer-Diagrammen**
Es gibt Zeiten, in denen Sie Diagramme in Designer-Vorlagendateien manipulieren oder ändern müssen. Aspose.Cells für Python via .NET unterstützt die vollständige Manipulation von Designer-Diagramminhalten und -elementen. Die Daten, Diagramminhalte, Hintergrundbilder und Formatierungen können präzise beibehalten werden.
### **Manipulation von Designer-Diagrammen in Vorlagendateien**
Verwenden Sie die diagrammbezogene API, um Designer-Diagramme in Vorlagendateien zu manipulieren. Sie können beispielsweise die Eigenschaft Worksheet.Charts verwenden, um die vorhandene Diagrammsammlung in der Vorlagendatei zu erhalten.
#### **Erstellen eines Diagramms**
Das folgende Beispiel zeigt, wie man ein Pyramiden-Diagramm erstellt. Wir werden dieses Diagramm später bearbeiten.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-HowToCreateChart-1.py" >}}
#### **Manipulation des Diagramms**
Das folgende Beispiel zeigt, wie man das vorhandene Diagramm manipuliert. In diesem Beispiel ändern wir das oben erstellte Diagramm. In der generierten Ausgabe beachten Sie, dass das Datumslabel eines Datenpunkts auf 'Vereinigtes Königreich, 30K' gesetzt wurde.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ManipulateChart-ModifyPieChart-1.py" >}}
#### **Manipulation eines Liniendiagramms in der Designer-Vorlage**
In diesem Beispiel werden wir ein Liniendiagramm manipulieren. Wir werden einige Datenreihen zu dem vorhandenen Diagramm hinzufügen und deren Linienfarben ändern.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ManipulateChart-ModifyLineChart-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
