---
title: Impostare il tipo di forma delle etichette dati del grafico
type: docs
weight: 110
url: /it/net/set-the-shape-type-of-data-labels-of-chart/
---
## **Possibili scenari di utilizzo**
È possibile modificare il tipo di forma delle etichette dati del grafico utilizzando la proprietà DataLabels.ShapeType. Prende il valore dell'enumerazione DataLabelShapeType e modifica di conseguenza il tipo di forma delle etichette dei dati. Alcuni dei suoi valori lo sono

{{< highlight "java" >}}

 DataLabelShapeType.BentLineCallout

DataLabelShapeType.DownArrowCallout

DataLabelShapeType.Ellipse

DataLabelShapeType.LineCallout

DataLabelShapeType.Rect

etc.

{{< /highlight >}}
## **Impostare il tipo di forma delle etichette dati del grafico**
 Il codice di esempio seguente modifica il tipo di forma delle etichette dati del grafico in DataLabelShapeType.WedgeEllipseCallout. Si prega di consultare il[esempio di file Excel](60489778.xlsx) utilizzato in questo codice e il[file Excel di output](60489779.xlsx) generato da esso. Lo screenshot mostra l'effetto del codice sul file Excel di esempio.

![cose da fare:immagine_alt_testo](set-the-shape-type-of-data-labels-of-chart_1.png)
## **Codice di esempio**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-SetShapeTypeOfDataLabelsOfChart.cs" >}}
