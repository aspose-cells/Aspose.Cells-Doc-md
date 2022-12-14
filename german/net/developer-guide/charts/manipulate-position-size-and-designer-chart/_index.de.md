---
title: Manipulieren Sie die Positionsgröße und das Designer-Diagramm
type: docs
weight: 45
url: /de/net/manipulate-position-size-and-designer-chart/
---
## **Diagrammposition und -größe**
 Manchmal möchten Sie die Position oder Größe des neuen oder vorhandenen Diagramms innerhalb des Arbeitsblatts ändern. Aspose.Cells bietet die[Chart.ChartObject](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/properties/chartobject) Eigenschaft, dies zu erreichen. Sie können die Untereigenschaften verwenden, um die Größe des Diagramms mit neu zu ändern**Höhe** und**Breite** oder mit new neu positionieren** X** und**Y**-Koordinaten.
### **Steuern von Position und Größe des Diagramms**
Um die Position (X-, Y-Koordinaten) oder die Größe (Höhe, Breite) des Diagramms zu ändern, verwenden Sie diese Eigenschaften:

1. [Chart.ChartObject.X](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/x)
1. [Chart.ChartObject.Y](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/y)
1. [Chart.ChartObject.Height](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/height)
1. [Chart.ChartObject.Width](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/width)

Das folgende Beispiel erläutert die Verwendung der oben genannten APIs, es lädt die vorhandene Arbeitsmappe, die ein Diagramm in ihrem ersten Arbeitsblatt enthält. Dann wird das Diagramm mit Aspose.Cells skaliert und neu positioniert.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChangeChartPosition-1.cs" >}}
## **Bearbeiten von Designer-Diagrammen**
Es gibt Zeiten, in denen Sie Diagramme in Designer-Vorlagendateien manipulieren oder ändern müssen. Aspose.Cells unterstützt vollständig die Manipulation von Inhalten und Elementen von Designer-Diagrammen. Die Daten, Diagramminhalte, Hintergrundbilder und Formatierungen können genau beibehalten werden.
### **Bearbeiten von Designer-Diagrammen in Vorlagendateien**
Um Designer-Diagramme in Vorlagendateien zu bearbeiten, verwenden Sie das diagrammbezogene API. Beispielsweise können Sie die Worksheet.Charts-Eigenschaft verwenden, um die vorhandene Diagrammsammlung in der Vorlagendatei abzurufen.
#### **Erstellen eines Diagramms**
Das folgende Beispiel zeigt, wie Sie ein Pyramidendiagramm erstellen. Wir werden dieses Diagramm später manipulieren.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-HowToCreateChart-1.cs" >}}
#### **Manipulation des Diagramms**
Das folgende Beispiel zeigt, wie das vorhandene Diagramm bearbeitet wird. In diesem Beispiel ändern wir das oben erstellte Diagramm. Beachten Sie in der generierten Ausgabe, dass die Datumsbezeichnung eines Datenpunkts auf „Vereinigtes Königreich, 30.000“ festgelegt wurde.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-ModifyPieChart-1.cs" >}}
#### **Bearbeiten eines Liniendiagramms in der Designer-Vorlage**
In diesem Beispiel bearbeiten wir ein Liniendiagramm. Wir werden dem bestehenden Diagramm einige Datenreihen hinzufügen und ihre Linienfarben ändern.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-ModifyLineChart-1.cs" >}}

