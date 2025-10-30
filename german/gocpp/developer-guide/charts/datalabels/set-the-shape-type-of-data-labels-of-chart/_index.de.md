---
title: Festlegen des Shape Typs der Datenbeschriftungen des Diagramms mit Golang über C++
linktitle: Legen Sie den Formtyp der Datenbeschriftungen des Diagramms fest
description: Erfahren Sie, wie Sie den Shape Typ der Datenbeschriftungen in Diagrammen mit Aspose.Cells for C++ festlegen. Unser Leitfaden erklärt die verfügbaren Shape Typen und zeigt, wie Sie den passenden Shape Typ für Ihre Datenbeschriftungen auswählen, um die Präsentation und Benutzerfreundlichkeit Ihrer Diagramme zu verbessern.
keywords: Aspose.Cells for C++, Diagrammerstellung, Datenbeschriftungen, Shape Typen, Präsentation, Benutzerfreundlichkeit.
type: docs
weight: 110
url: /de/go-cpp/set-the-shape-type-of-data-labels-of-chart/
---

## **Mögliche Verwendungsszenarien**
Sie können den Shape-Typ der Datenbeschriftungen im Diagramm ändern, indem Sie die Eigenschaft `DataLabels.ShapeType` verwenden. Sie akzeptiert den Wert des `DataLabelShapeType`-Enums und ändert entsprechend den Shape-Typ der Datenbeschriftungen. Einige seiner Werte sind:

{{< highlight java >}}

 DataLabelShapeType.BentLineCallout

DataLabelShapeType.DownArrowCallout

DataLabelShapeType.Ellipse

DataLabelShapeType.LineCallout

DataLabelShapeType.Rect

etc.

{{< /highlight >}}

## **Festlegen des Formtyps von Datenbeschriftungen des Diagramms**
Das folgende Beispiel ändert den Shape-Typ der Datenbeschriftungen im Diagramm auf `DataLabelShapeType.WedgeEllipseCallout`. Bitte beachten Sie die [Beispieldatei Excel](60489778.xlsx), die in diesem Beispiel verwendet wird, und die [Ausgabedatei Excel](60489779.xlsx), die daraus generiert wurde. Der Screenshot zeigt die Wirkung des Codes auf die Beispiel-Excel-Datei. 

![todo:image_alt_text](set-the-shape-type-of-data-labels-of-chart_1.png)

## **Beispielcode**
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SetTheShapeTypeOfDataLabelsOfChart.go" >}}
