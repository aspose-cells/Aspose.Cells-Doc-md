---
title: Fügen Sie ein Bild basierend auf dem Zellenverweis ein.
type: docs
weight: 90
url: /de/java/insert-a-picture-based-on-cell-reference/
---

{{% alert color="primary" %}}

Manchmal haben Sie ein leeres Bild und müssen Daten oder Inhalte im Bild anzeigen, indem Sie einen Zellbezug in der Formel-Leiste festlegen. Aspose.Cells unterstützt diese Funktion (Microsoft Excel 2010).

{{% /alert %}}

## Einfügen eines Bildes anhand eines Zellbezugs

Aspose.Cells unterstützt das Anzeigen des Inhalts einer Arbeitsblattzelle in einer Bildform. Sie können das Bild mit der Zelle verknüpfen, die die anzuzeigenden Daten enthält. Da die Zelle oder der Zellenbereich mit dem grafischen Objekt verknüpft ist, erscheinen Änderungen an den Daten automatisch im grafischen Objekt. Fügen Sie ein Bild dem Arbeitsblatt hinzu, indem Sie die [**addPicture**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addPicture-int-int-int-int-java.io.InputStream-)-Methode der [**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ShapeCollection)-Sammlung (die in dem [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)-Objekt gekapselt ist) aufrufen. Geben Sie den Zellenbereich an, indem Sie die [**setFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/picture#Formula)-Methode des [**Picture**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture)-Objekts verwenden.

Nachfolgend sehen Sie einen Screenshot der Datei, die durch den untenstehenden Code generiert wird.

**Einfügen eines Bildes basierend auf dem Zellenverweis**

![todo:image_alt_text](insert-a-picture-based-on-cell-reference_1.png)

## Beispielcode

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-InsertPictureCellReference-InsertPictureCellReference.java" >}}
{{< app/cells/assistant language="java" >}}
