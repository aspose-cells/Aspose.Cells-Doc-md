---
title: So ermitteln Sie die Objektposition im Diagramm
description: Erfahren Sie, wie Sie mit Aspose.Cells for .NET Objektpositionen im Excel Diagramm ermitteln können. 
keywords: Aspose.Cells for .NET, Excel Diagramm, Objektpositionen ermitteln.
type: docs
weight: 74
url: /de/net/how-to-get-object-position-in-chart/
---

## Mögliche Anwendungsszenarien
In einigen Szenarien, wenn Sie Excel-Diagramme verwenden, müssen Sie möglicherweise die Position der Objekte im Diagramm ermitteln. Sie können diese Anforderung mit Aspose.Cells leicht erfüllen.

## Beispiel: Objektposition im Diagramm ermitteln

Der folgende Beispielcode lädt die [Beispieldatei](TestFile.xlsx) und erstellt die [Ausgabedatei](Output.xlsx).
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "get-object-position-in-chart.cs" >}}

Mit dem obigen Code können Sie die Position des Diagrammtitels und des Diagramm-PlotArea ermitteln. 
Mit den Positionsinformationen können die Formen an der entsprechenden Stelle im Diagramm platziert werden. 
Die Ausgabe ist in der folgenden Abbildung gezeigt, in der eine Form in der oberen linken Ecke des PlotArea platziert ist und die andere Form unterhalb des Diagrammtitels.
![todo:image_alt_text](OutputResult.png)

## Einheiten- und Umrechnungsinformationen

Es gibt drei Einheiten für die Positionierung von Objekten im Diagramm:

1. Einheiten im Verhältnis zum Diagrammbereich.

2. Einheiten von 1/4000 des Diagrammbereichs. Diese Einheit wird in älteren Versionen von Excel verwendet und ist nicht empfohlen.

3. Pixel-Einheiten.

Der Konvertierungscode für diese Einheiten ist im folgenden Code gezeigt: 

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "object-position-unit-in-chart.cs" >}}

{{< app/cells/assistant language="csharp" >}}
