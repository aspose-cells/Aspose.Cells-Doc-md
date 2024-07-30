---
title: Copia delle Forme tra Fogli di Lavoro
linktitle: Copia forme
type: docs
weight: 200
url: /it/python-net/copy-shapes-between-worksheets/
description: Questo articolo mostra come copiare forme tra fogli di calcolo tramite l API Aspose.Cells per Python via .NET.
keywords: Libreria Excel di Python, Copia forme tra fogli di calcolo in Python, come copiare un immagine da un foglio di lavoro a un altro, come copiare un grafico da un foglio di lavoro a un altro, come copiare controlli e altri oggetti di disegno da un foglio di lavoro a un altro.
---

{{% alert color="primary" %}}

A volte è necessario copiare elementi su un foglio di lavoro, ad esempio immagini, grafici e altri oggetti di disegno, tra fogli di lavoro. Aspose.Cells per Python via .NET supporta questa funzionalità. Grafici, immagini e altri oggetti possono essere copiati con il massimo grado di precisione.

Questo articolo ti fornisce una comprensione dettagliata su come copiare le forme tra i fogli di lavoro.

{{% /alert %}}

## **Copia di un'Immagine da un Foglio di Lavoro a un Altro**

Per copiare un'immagine da un foglio di lavoro a un altro, utilizzare il metodo [**Worksheet.pictures.add**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picturecollection/add/#int-int-io.RawIOBase-int-int) come mostrato nel codice di esempio seguente.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-ManageChartsAndShapes-CopyShapesBetweenWorksheets-CopyPictureBetweenWorksheets.py" >}}

## **Copia di un grafico da un foglio di lavoro a un altro**

Il codice seguente dimostra l'uso del metodo [**Worksheet.shapes.add_copy**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_copy/#aspose.cells.drawing.Shape-int-int-int-int) per copiare un grafico da un foglio di lavoro a un altro.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-ManageChartsAndShapes-CopyShapesBetweenWorksheets-CopyChartBetweenWorksheets.py" >}}

## **Copia controlli e altri oggetti disegnati da un foglio di lavoro a un altro**

Per copiare controlli e altri oggetti disegnati, utilizzare il metodo [**Worksheet.shapes.add_copy**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_copy/#aspose.cells.drawing.Shape-int-int-int-int) come mostrato nell'esempio seguente.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-ManageChartsAndShapes-CopyShapesBetweenWorksheets-CopyControlsAndOtherDrawingObjects.py" >}}
