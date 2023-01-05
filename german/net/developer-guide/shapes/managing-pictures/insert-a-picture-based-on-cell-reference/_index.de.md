---
title: Fügen Sie ein Bild basierend auf der Referenz Cell ein
type: docs
weight: 150
url: /de/net/insert-a-picture-based-on-cell-reference/
---
{{% alert color="primary" %}}

Manchmal haben Sie ein leeres Bild und müssen Daten oder Inhalte im Bild anzeigen, indem Sie in der Formelleiste einen Zellbezug setzen. Aspose.Cells unterstützt diese Funktion (Microsoft Excel 2010).

{{% /alert %}}

## Einfügen eines Bildes basierend auf der Referenz Cell

Aspose.Cells unterstützt die Anzeige des Inhalts einer Arbeitsblattzelle in einer Bildform. Sie können das Bild mit der Zelle verknüpfen, die die Daten enthält, die Sie anzeigen möchten. Da die Zelle oder der Zellbereich mit dem Grafikobjekt verknüpft ist, werden Änderungen, die Sie an den Daten in dieser Zelle oder diesem Zellbereich vornehmen, automatisch im Grafikobjekt angezeigt. Fügen Sie dem Arbeitsblatt ein Bild hinzu, indem Sie die aufrufen[**Bild hinzufügen**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addpicture/index) Methode der[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) Sammlung (eingekapselt in der[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Objekt). Geben Sie den Zellbereich mithilfe von an[**Formel**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture/properties/formula) Attribut der[**Bild**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture)Objekt.

### Codebeispiel

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-InsertPictureCellReference-1.cs" >}}
