---
title: Fügen Sie ein Bild basierend auf Zellreferenz mit Golang via C++ ein
linktitle: Bild anhand eines Zellbezugs einfügen
type: docs
weight: 150
url: /de/go-cpp/insert-a-picture-based-on-cell-reference/
description: Erfahren Sie, wie Sie ein Bild basierend auf Zellreferenz mit Aspose.Cells for C++ einfügen.
---

{{% alert color="primary" %}}

Manchmal haben Sie ein leeres Bild und müssen Daten oder Inhalte im Bild anzeigen, indem Sie einen Zellbezug in der Formel-Leiste festlegen. Aspose.Cells unterstützt diese Funktion (Microsoft Excel 2010).

{{% /alert %}}

## Einfügen eines Bildes anhand eines Zellbezugs

Aspose.Cells unterstützt das Anzeigen des Inhalts einer Arbeitsblattzelle in einer Bildform. Sie können das Bild mit der Zelle verknüpfen, die die anzuzeigenden Daten enthält. Da die Zelle oder der Zellbereich mit dem Grafikobjekt verknüpft ist, erscheinen Änderungen, die Sie an den Daten in dieser Zelle oder diesem Zellbereich vornehmen, automatisch im Grafikobjekt. Fügen Sie ein Bild dem Arbeitsblatt hinzu, indem Sie die [**AddPicture**](https://reference.aspose.com/cells/go-cpp/shapecollection/addpicture_int_int_int_int_stream/) Methode der [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) Sammlung aufrufen (die im [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) Objekt gekapselt ist). Geben Sie den Zellbereich an, indem Sie das [**Formula**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/getformula/) Attribut des [**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/) Objekts verwenden.

### Codebeispiel

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-InsertAPictureBasedOnCellReference.go" >}}
