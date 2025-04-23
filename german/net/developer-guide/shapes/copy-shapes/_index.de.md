---
title: Formen zwischen Arbeitsblättern kopieren
linktitle: Formen kopieren
type: docs
weight: 200
url: /de/net/copy-shapes-between-worksheets/
---

{{% alert color="primary" %}}

Manchmal müssen Elemente auf einem Arbeitsblatt kopiert werden, z. B. Bilder, Diagramme und andere Zeichenobjekte, zwischen Arbeitsblättern. Aspose.Cells unterstützt diese Funktion. Diagramme, Bilder und andere Objekte können mit höchster Präzision kopiert werden.

Dieser Artikel vermittelt Ihnen ein umfassendes Verständnis dafür, wie Formen zwischen Arbeitsblättern kopiert werden.

{{% /alert %}}

## **Kopieren eines Bildes von einem Arbeitsblatt auf ein anderes**

Um ein Bild von einem Arbeitsblatt auf ein anderes zu kopieren, verwenden Sie die Methode [**Worksheet.Pictures.Add**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index), wie im folgenden Beispielcode gezeigt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CopyShapesBetweenWorksheets-CopyPictureBetweenWorksheets.cs" >}}

## **Kopieren Sie ein Diagramm von einem Arbeitsblatt auf ein anderes**

Der folgende Code demonstriert die Verwendung der Methode [**Worksheet.Shapes.AddCopy**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addcopy) zum Kopieren eines Diagramms von einem Arbeitsblatt auf ein anderes.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CopyShapesBetweenWorksheets-CopyChartBetweenWorksheets.cs" >}}

## **Kopieren von Steuerelementen und anderen Zeichenobjekten von einem Arbeitsblatt auf ein anderes**

Verwenden Sie zur Kopie von Steuerelementen und anderen Zeichenobjekten die Methode [**Worksheet.Shapes.AddCopy**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addcopy), wie im folgenden Beispiel gezeigt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-CopyShapesBetweenWorksheets-CopyControlsAndOtherDrawingObjects.cs" >}}
{{< app/cells/assistant language="csharp" >}}
