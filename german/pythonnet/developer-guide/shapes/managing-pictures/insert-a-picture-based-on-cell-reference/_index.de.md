---
title: Bild anhand eines Zellbezugs einfügen
type: docs
weight: 150
url: /de/python-net/insert-a-picture-based-on-cell-reference/
---

{{% alert color="primary" %}}

Manchmal haben Sie ein leeres Bild und möchten Daten oder Inhalte im Bild anzeigen, indem Sie eine Zellenreferenz in der Formelleiste setzen. Aspose.Cells für Python via .NET unterstützt diese Funktion (Microsoft Excel 2010).

{{% /alert %}}

## Einfügen eines Bildes anhand eines Zellbezugs

Aspose.Cells für Python via .NET unterstützt die Anzeige des Inhalts einer Zelle in einem Bildshape. Sie können das Bild mit der Zelle verknüpfen, die die Daten enthält, die angezeigt werden sollen. Da die Zelle oder der Zellbereich mit dem grafischen Objekt verknüpft ist, erscheinen Änderungen an den Daten in der Zelle oder dem Zellbereich automatisch im Grafikobjekt. Fügen Sie ein Bild zum Arbeitsblatt hinzu, indem Sie die Methode [**add_picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_picture) der Sammlung [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection) aufrufen (eingeschlossen im Objekt [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)). Bestimmen Sie den Zellbereich durch die Verwendung des Attributs [**formula**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture/formula) des Objekts [**Picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture).

### Codebeispiel

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Pictures-InsertPictureCellReference-1.py" >}}
