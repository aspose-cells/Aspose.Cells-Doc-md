---
title: Bild anhand eines Zellbezugs einfügen
type: docs
weight: 150
url: /de/net/insert-a-picture-based-on-cell-reference/
---

{{% alert color="primary" %}}

Manchmal haben Sie ein leeres Bild und müssen Daten oder Inhalte im Bild anzeigen, indem Sie einen Zellbezug in der Formel-Leiste festlegen. Aspose.Cells unterstützt diese Funktion (Microsoft Excel 2010).

{{% /alert %}}

## Einfügen eines Bildes anhand eines Zellbezugs

Aspose.Cells unterstützt das Anzeigen des Inhalts einer Arbeitsblattzelle in einer Bildform. Sie können das Bild mit der Zelle verknüpfen, die die anzuzeigenden Daten enthält. Da die Zelle oder der Zellbereich mit dem Grafikobjekt verknüpft ist, erscheinen Änderungen, die Sie an den Daten in dieser Zelle oder diesem Zellbereich vornehmen, automatisch im Grafikobjekt. Fügen Sie ein Bild dem Arbeitsblatt hinzu, indem Sie die [**AddPicture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addpicture/index) Methode der [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) Sammlung aufrufen (die im [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Objekt gekapselt ist). Geben Sie den Zellbereich an, indem Sie das [**Formula**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture/properties/formula) Attribut des [**Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture) Objekts verwenden.

### Codebeispiel

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-InsertPictureCellReference-1.cs" >}}
