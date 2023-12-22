---
title: Positionsgröße und Designer-Diagramm manipulieren
description: Erfahren Sie, wie Sie Aspose.Cells for .NET verwenden, um Position, Größe und Designerdiagramm in Microsoft Excel effektiv zu manipulieren. Unser Leitfaden zeigt, wie Sie diese Eigenschaften anpassen, um das Layout und die Visualisierung zu verbessern.
keywords: Aspose.Cells for .NET, Position, Size, Designer Chart, Microsoft Excel, Layout, Visualization.
type: docs
weight: 45
url: /de/net/manipulate-position-size-and-designer-chart/
---
##  **Diagrammposition und -größe**
 Manchmal möchten Sie die Position oder Größe des neuen oder vorhandenen Diagramms im Arbeitsblatt ändern. Aspose.Cells bietet die[Chart.ChartObject](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/properties/chartobject) Eigenschaft, dies zu erreichen. Sie können die Untereigenschaften verwenden, um die Größe des Diagramms neu zu ändern**Höhe** Und**Breite** oder mit „Neu“ neu positionieren**X** und **Y** Koordinaten.
###  **Steuern der Diagrammposition und -größe**
Um die Position (X-, Y-Koordinaten) oder Größe (Höhe, Breite) des Diagramms zu ändern, verwenden Sie diese Eigenschaften:

1. [Chart.ChartObject.X](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/x)
1. [Chart.ChartObject.Y](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/y)
1. [Chart.ChartObject.Height](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/height)
1. [Chart.ChartObject.Width](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/width)

Das folgende Beispiel erläutert die Verwendung der oben genannten APIs. Es lädt die vorhandene Arbeitsmappe, deren erstes Arbeitsblatt ein Diagramm enthält. Anschließend wird die Größe und Position des Diagramms mithilfe von Aspose.Cells geändert.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChangeChartPosition-1.cs" >}}
##  **Bearbeiten von Designer-Diagrammen**
Es gibt Zeiten, in denen Sie Diagramme in Designer-Vorlagendateien bearbeiten oder ändern müssen. Aspose.Cells unterstützt die Bearbeitung von Inhalten und Elementen von Designer-Diagrammen vollständig. Die Daten, Diagramminhalte, Hintergrundbilder und Formatierungen können mit Genauigkeit beibehalten werden.
###  **Bearbeiten von Designer-Diagrammen in Vorlagendateien**
Um Designerdiagramme in Vorlagendateien zu bearbeiten, verwenden Sie das diagrammbezogene API. Sie können beispielsweise die Eigenschaft Worksheet.Charts verwenden, um die vorhandene Diagrammsammlung in der Vorlagendatei abzurufen.
####  **Erstellen eines Diagramms**
Das folgende Beispiel zeigt, wie man ein Pyramidendiagramm erstellt. Wir werden dieses Diagramm später bearbeiten.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-HowToCreateChart-1.cs" >}}
####  **Manipulieren des Diagramms**
Das folgende Beispiel zeigt, wie Sie das vorhandene Diagramm bearbeiten. In diesem Beispiel ändern wir das oben erstellte Diagramm. Beachten Sie in der generierten Ausgabe, dass die Datumsbezeichnung eines Datenpunkts auf „Vereinigtes Königreich, 30.000“ festgelegt wurde.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-ModifyPieChart-1.cs" >}}
####  **Bearbeiten eines Liniendiagramms in der Designer-Vorlage**
In diesem Beispiel bearbeiten wir ein Liniendiagramm. Wir werden dem bestehenden Diagramm einige Datenreihen hinzufügen und deren Linienfarben ändern.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-ModifyLineChart-1.cs" >}}

