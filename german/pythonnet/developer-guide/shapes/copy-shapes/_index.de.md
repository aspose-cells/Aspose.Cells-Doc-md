---
title: Formen zwischen Arbeitsblättern kopieren
linktitle: Formen kopieren
type: docs
weight: 200
url: /de/python-net/copy-shapes-between-worksheets/
description: Dieser Artikel zeigt, wie Formen zwischen Arbeitsblättern durch die Aspose.Cells für Python via .NET API kopiert werden können.
keywords: Python Excel Bibliothek, Python Formen zwischen Arbeitsblättern kopieren, Python wie man ein Bild von einem Arbeitsblatt auf ein anderes kopiert, Python wie man ein Diagramm von einem Arbeitsblatt auf ein anderes kopiert, Python wie man Steuerelemente und andere Zeichenobjekte von einem Arbeitsblatt auf ein anderes kopiert.
---

{{% alert color="primary" %}}

Manchmal müssen Elemente auf einem Arbeitsblatt, wie z.B. Bilder, Diagramme und andere Zeichenobjekte, zwischen Arbeitsblättern kopiert werden. Aspose.Cells für Python via .NET unterstützt diese Funktion. Diagramme, Bilder und andere Objekte können mit höchster Genauigkeit kopiert werden.

Dieser Artikel vermittelt Ihnen ein umfassendes Verständnis dafür, wie Formen zwischen Arbeitsblättern kopiert werden.

{{% /alert %}}

## **Kopieren eines Bildes von einem Arbeitsblatt auf ein anderes**

Um ein Bild von einem Arbeitsblatt auf ein anderes zu kopieren, verwenden Sie die Methode [**Worksheet.pictures.add**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picturecollection/add/#int-int-io.RawIOBase-int-int), wie im folgenden Beispielcode gezeigt.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-ManageChartsAndShapes-CopyShapesBetweenWorksheets-CopyPictureBetweenWorksheets.py" >}}

## **Kopieren Sie ein Diagramm von einem Arbeitsblatt auf ein anderes**

Der folgende Code demonstriert die Verwendung der Methode [**Worksheet.shapes.add_copy**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_copy/#aspose.cells.drawing.Shape-int-int-int-int) zum Kopieren eines Diagramms von einem Arbeitsblatt auf ein anderes.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-ManageChartsAndShapes-CopyShapesBetweenWorksheets-CopyChartBetweenWorksheets.py" >}}

## **Kopieren von Steuerelementen und anderen Zeichenobjekten von einem Arbeitsblatt auf ein anderes**

Verwenden Sie zur Kopie von Steuerelementen und anderen Zeichenobjekten die Methode [**Worksheet.shapes.add_copy**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_copy/#aspose.cells.drawing.Shape-int-int-int-int), wie im folgenden Beispiel gezeigt.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-ManageChartsAndShapes-CopyShapesBetweenWorksheets-CopyControlsAndOtherDrawingObjects.py" >}}
