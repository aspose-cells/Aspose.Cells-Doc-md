---
title: Position, Größe und Designer des Diagramms manipulieren
description: Erfahren Sie, wie Sie Aspose.Cells for .NET verwenden können, um die Position, Größe und das Designerdiagramm in Microsoft Excel effektiv zu manipulieren. Unser Leitfaden zeigt, wie Sie diese Eigenschaften für eine verbesserte Darstellung und Visualisierung anpassen können.
keywords: Aspose.Cells for .NET, Position, Größe, Designer Chart, Microsoft Excel, Layout, Visualisierung.
type: docs
weight: 45
url: /de/net/manipulate-position-size-and-designer-chart/
---

## **Chart-Position und Größe**
Manchmal möchten Sie die Position oder Größe des neuen oder vorhandenen Diagramms im Arbeitsblatt ändern. Aspose.Cells bietet die [Chart.ChartObject](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/properties/chartobject)-Eigenschaft, um dies zu erreichen. Sie können seine Unter-Eigenschaften verwenden, um das Diagramm mit neuen **Höhe** und **Breite** neu zu dimensionieren oder es mit neuen **X**- und **Y**-Koordinaten neu zu positionieren.
### **Steuerung der Diagrammposition und -größe**
Um die Position (X, Y-Koordinaten) oder Größe (Höhe, Breite) des Diagramms zu ändern, verwenden Sie diese Eigenschaften:

1. [Chart.ChartObject.X](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/x)
1. [Chart.ChartObject.Y](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/y)
1. [Chart.ChartObject.Height](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/height)
1. [Chart.ChartObject.Width](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/width)

Das folgende Beispiel erläutert die Verwendung der obigen APIs. Es lädt die vorhandene Arbeitsmappe, die ein Diagramm im ersten Arbeitsblatt enthält. Dann ändert es die Größe und Position des Diagramms mit Aspose.Cells neu.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChangeChartPosition-1.cs" >}}
## **Manipulation von Designer-Diagrammen**
Es gibt Zeiten, in denen Sie Diagramminhalte und -elemente in Designer-Vorlagendateien manipulieren oder ändern müssen. Aspose.Cells unterstützt die vollständige Manipulation von Designer-Diagramminhalten und -elementen. Die Daten, Diagramminhalte, Hintergrundbild und Formatierungen können mit Genauigkeit beibehalten werden.
### **Manipulation von Designer-Diagrammen in Vorlagendateien**
Verwenden Sie die diagrammbezogene API, um Designer-Diagramme in Vorlagendateien zu manipulieren. Sie können beispielsweise die Eigenschaft Worksheet.Charts verwenden, um die vorhandene Diagrammsammlung in der Vorlagendatei zu erhalten.
#### **Erstellen eines Diagramms**
Das folgende Beispiel zeigt, wie man ein Pyramiden-Diagramm erstellt. Wir werden dieses Diagramm später bearbeiten.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-HowToCreateChart-1.cs" >}}
#### **Manipulation des Diagramms**
Das folgende Beispiel zeigt, wie man das vorhandene Diagramm manipuliert. In diesem Beispiel ändern wir das oben erstellte Diagramm. In der generierten Ausgabe beachten Sie, dass das Datumslabel eines Datenpunkts auf 'Vereinigtes Königreich, 30K' gesetzt wurde.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-ModifyPieChart-1.cs" >}}
#### **Manipulation eines Liniendiagramms in der Designer-Vorlage**
In diesem Beispiel werden wir ein Liniendiagramm manipulieren. Wir werden einige Datenreihen zu dem vorhandenen Diagramm hinzufügen und deren Linienfarben ändern.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-ModifyLineChart-1.cs" >}}

{{< app/cells/assistant language="csharp" >}}
