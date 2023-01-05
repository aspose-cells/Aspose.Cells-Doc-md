---
title: Legen Sie den Formtyp der Datenbeschriftungen des Diagramms fest
type: docs
weight: 110
url: /de/net/set-the-shape-type-of-data-labels-of-chart/
---
## **Mögliche Nutzungsszenarien**
Sie können den Formtyp von Datenbeschriftungen des Diagramms mithilfe der DataLabels.ShapeType-Eigenschaft ändern. Es übernimmt den Wert der DataLabelShapeType-Enumeration und ändert den Formtyp von Datenbeschriftungen entsprechend. Einige seiner Werte sind

{{< highlight "java" >}}

 DataLabelShapeType.BentLineCallout

DataLabelShapeType.DownArrowCallout

DataLabelShapeType.Ellipse

DataLabelShapeType.LineCallout

DataLabelShapeType.Rect

etc.

{{< /highlight >}}
## **Legen Sie den Formtyp der Datenbeschriftungen des Diagramms fest**
 Der folgende Beispielcode ändert den Formtyp von Datenbeschriftungen des Diagramms in DataLabelShapeType.WedgeEllipseCallout. Bitte sehen Sie sich ... an[Beispiel-Excel-Datei](60489778.xlsx) in diesem Code verwendet und die[Excel-Datei ausgeben](60489779.xlsx) dadurch erzeugt. Der Screenshot zeigt die Auswirkung des Codes auf die Beispiel-Excel-Datei.

![todo: Bild_alt_Text](set-the-shape-type-of-data-labels-of-chart_1.png)
## **Beispielcode**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SetShapeTypeOfDataLabelsOfChart.cs" >}}
