---
title: Fügen Sie ein Bild ein, das auf der Referenz Cell basiert
type: docs
weight: 90
url: /de/java/insert-a-picture-based-on-cell-reference/
---
{{% alert color="primary" %}}

Manchmal haben Sie ein leeres Bild und müssen Daten oder Inhalte im Bild anzeigen, indem Sie in der Formelleiste einen Zellbezug setzen. Aspose.Cells unterstützt diese Funktion (Microsoft Excel 2010).

{{% /alert %}}

## Einfügen eines Bildes basierend auf der Referenz Cell

Aspose.Cells unterstützt die Anzeige des Inhalts einer Arbeitsblattzelle in einer Bildform. Sie können das Bild mit der Zelle verknüpfen, die die Daten enthält, die Sie anzeigen möchten. Da die Zelle bzw. der Zellbereich mit dem Grafikobjekt verknüpft ist, erscheinen Änderungen an den Daten automatisch im Grafikobjekt. Fügen Sie dem Arbeitsblatt ein Bild hinzu, indem Sie die aufrufen[**Bild hinzufügen**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addPicture(int,%20int,%20int,%20int,%20java.io.InputStream) ) Methode der[**ShapeCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/ShapeCollection) Sammlung (eingekapselt in der[**Arbeitsblatt**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) Objekt). Geben Sie den Zellbereich mithilfe von an[**setFormel**](https://reference.aspose.com/cells/java/com.aspose.cells/picture#Formula) Methode der[**Bild**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture)Objekt.

Unten ist ein Screenshot der Datei, die der unten stehende Code generiert.

**Einfügen eines Bildes basierend auf Zellbezug**

![todo: Bild_alt_Text](insert-a-picture-based-on-cell-reference_1.png)

## Beispielcode

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-InsertPictureCellReference-InsertPictureCellReference.java" >}}
