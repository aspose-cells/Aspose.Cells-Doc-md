---
title: Imposta il tipo di forma delle etichette dati del grafico con Golang via C++
linktitle: Imposta il tipo di forma dell etichetta dati del grafico
description: Impara come impostare il tipo di forma delle etichette dati nei grafici usando Aspose.Cells for C++. La nostra guida spiegherà i diversi tipi di forma disponibili e ti mostrerà come scegliere la forma appropriata per le tue etichette dati per migliorare la presentazione e l usabilità dei grafici.
keywords: Aspose.Cells for C++, tracciamento, etichette dati, tipi di forma, presentazione, usabilità.
type: docs
weight: 110
url: /it/go-cpp/set-the-shape-type-of-data-labels-of-chart/
---

## **Possibili Scenari di Utilizzo**
Puoi cambiare il tipo di forma delle etichette dati del grafico usando la proprietà `DataLabels.ShapeType`. Essa prende il valore dell'enumerazione `DataLabelShapeType` e modifica il tipo di forma delle etichette dati di conseguenza. Alcuni dei suoi valori sono:

{{< highlight java >}}

 DataLabelShapeType.BentLineCallout

DataLabelShapeType.DownArrowCallout

DataLabelShapeType.Ellipse

DataLabelShapeType.LineCallout

DataLabelShapeType.Rect

etc.

{{< /highlight >}}

## **Imposta il tipo di forma delle etichette dati del grafico**
Il seguente esempio di codice cambia il tipo di forma delle etichette dei dati del grafico in `DataLabelShapeType.WedgeEllipseCallout`. Consulta il [file Excel di esempio](60489778.xlsx) utilizzato in questo codice e il [file Excel di output](60489779.xlsx) generato. Lo screenshot mostra l'effetto del codice sul file Excel di esempio. 

![todo:image_alt_text](set-the-shape-type-of-data-labels-of-chart_1.png)

## **Codice di Esempio**
{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SetTheShapeTypeOfDataLabelsOfChart.go" >}}
