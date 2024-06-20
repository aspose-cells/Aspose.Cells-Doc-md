---
title: Copia delle Forme tra Fogli di Lavoro
linktitle: Copia forme
type: docs
weight: 200
url: /it/net/copy-shapes-between-worksheets/
---

{{% alert color="primary" %}}

A volte è necessario copiare elementi su un foglio di calcolo, ad esempio immagini, grafici e altri oggetti disegnati, tra fogli di lavoro. Aspose.Cells supporta questa funzionalità. Grafici, immagini e altri oggetti possono essere copiati con il massimo livello di precisione.

Questo articolo ti fornisce una comprensione dettagliata su come copiare le forme tra i fogli di lavoro.

{{% /alert %}}

## **Copia di un'Immagine da un Foglio di Lavoro a un Altro**

Per copiare un'immagine da un foglio di lavoro a un altro, utilizzare il metodo [**Worksheet.Pictures.Add**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index) come mostrato nel codice di esempio seguente.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CopyShapesBetweenWorksheets-CopyPictureBetweenWorksheets.cs" >}}

## **Copia di un grafico da un foglio di lavoro a un altro**

Il codice seguente dimostra l'uso del metodo [**Worksheet.Shapes.AddCopy**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addcopy) per copiare un grafico da un foglio di lavoro a un altro.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CopyShapesBetweenWorksheets-CopyChartBetweenWorksheets.cs" >}}

## **Copia controlli e altri oggetti disegnati da un foglio di lavoro a un altro**

Per copiare controlli e altri oggetti disegnati, utilizzare il metodo [**Worksheet.Shapes.AddCopy**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addcopy) come mostrato nell'esempio seguente.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CopyShapesBetweenWorksheets-CopyControlsAndOtherDrawingObjects.cs" >}}
