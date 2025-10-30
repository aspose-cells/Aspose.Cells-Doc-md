---
title: Position, Größe und Designer Diagramm mit Golang über C++ manipulieren
linktitle: Position, Größe und Designer des Diagramms manipulieren
description: Erfahren Sie, wie Sie Aspose.Cells for C++ effektiv nutzen, um die Position, Größe und das Designer Diagramm in Microsoft Excel zu manipulieren. Unser Leitfaden zeigt, wie man diese Eigenschaften für eine verbesserte Anordnung und Visualisierung anpasst.
keywords: Aspose.Cells for C++, Position, Größe, Designer Diagramm, Microsoft Excel, Layout, Visualisierung.
type: docs
weight: 45
url: /de/go-cpp/manipulate-position-size-and-designer-chart/
---

## **Chart-Position und Größe**
Manchmal möchten Sie die Position oder Größe des neuen oder vorhandenen Diagramms in der Arbeitsmappe ändern. Aspose.Cells bietet die Eigenschaft [Chart.GetChartObject()](https://reference.aspose.com/cells/go-cpp/chart/getchartobject/), um dies zu erreichen. Sie können dessen Untereigenschaften verwenden, um das Diagramm mit neuer **Höhe** und **Breite** neu zu skalieren oder mit neuen **X**- und **Y**-Koordinaten neu zu positionieren.

### **Steuerung der Diagrammposition und -größe**
Um die Position (X, Y-Koordinaten) oder Größe (Höhe, Breite) des Diagramms zu ändern, verwenden Sie diese Eigenschaften:

1. [Chart.GetX()](https://reference.aspose.com/cells/go-cpp/shape/getx/)
1. [Chart.GetY()](https://reference.aspose.com/cells/go-cpp/shape/gety/)
1. [Chart.GetHeight()](https://reference.aspose.com/cells/go-cpp/shape/getheight/)
1. [Chart.GetWidth()](https://reference.aspose.com/cells/go-cpp/shape/getwidth/)

Das folgende Beispiel erläutert die Verwendung der obigen APIs. Es lädt die vorhandene Arbeitsmappe, die ein Diagramm im ersten Arbeitsblatt enthält. Dann ändert es die Größe und Position des Diagramms mit Aspose.Cells neu.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ManipulatePositionSizeAndDesignerChart.go" >}}
## **Manipulation von Designer-Diagrammen**
Es gibt Zeiten, in denen Sie Diagramminhalte und -elemente in Designer-Vorlagendateien manipulieren oder ändern müssen. Aspose.Cells unterstützt die vollständige Manipulation von Designer-Diagramminhalten und -elementen. Die Daten, Diagramminhalte, Hintergrundbild und Formatierungen können mit Genauigkeit beibehalten werden.

### **Manipulation von Designer-Diagrammen in Vorlagendateien**
Verwenden Sie die diagrammbezogene API, um Designer-Diagramme in Vorlagendateien zu manipulieren. Sie können beispielsweise die Eigenschaft Worksheet.Charts verwenden, um die vorhandene Diagrammsammlung in der Vorlagendatei zu erhalten.

#### **Erstellen eines Diagramms**
Das folgende Beispiel zeigt, wie man ein Pyramiden-Diagramm erstellt. Wir werden dieses Diagramm später bearbeiten.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ManipulatePositionSizeAndDesignerChart-1.go" >}}
#### **Manipulation des Diagramms**
Das folgende Beispiel zeigt, wie man das vorhandene Diagramm manipuliert. In diesem Beispiel ändern wir das oben erstellte Diagramm. In der generierten Ausgabe beachten Sie, dass das Datumslabel eines Datenpunkts auf 'Vereinigtes Königreich, 30K' gesetzt wurde.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ManipulatePositionSizeAndDesignerChart-2.go" >}}
#### **Manipulation eines Liniendiagramms in der Designer-Vorlage**
In diesem Beispiel werden wir ein Liniendiagramm manipulieren. Wir werden einige Datenreihen zu dem vorhandenen Diagramm hinzufügen und deren Linienfarben ändern.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ManipulatePositionSizeAndDesignerChart-3.go" >}}
