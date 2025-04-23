---
title: Verknüpftes Bild aus Webadresse einfügen
type: docs
weight: 450
url: /de/python-net/insert-a-linked-picture-from-web-address/
---

{{% alert color="primary" %}}

Manchmal müssen Sie ein Bild von der Webseite (http://) in ein Arbeitsblatt einfügen. Geben Sie dazu die URL des Bildes an, und das Bild wird jedes Mal heruntergeladen, wenn die Tabelle in Microsoft Excel geöffnet wird. Das Bild ist nicht physisch in das Excel-Dokument eingebettet, sondern verweist auf eine Webressource.

{{% /alert %}}

## **Verwendung von Microsoft Excel**

In Microsoft Excel (zum Beispiel 2007):

1. Klicken Sie auf das **Einfügen** Menü und wählen Sie **Bild** aus.
1. Geben Sie die Webadresse für das Bild im Dialogfeld Bild einfügen an.

## **Mit Aspose.Cells für Python via .NET**

Aspose.Cells für Python via .NET unterstützt das Hinzufügen eines verknüpften Bilds mit [**ShapeCollection.add_linked_picture(int upper_left_row, int upper_left_column, int height_pixels, int width_pixels, str source_full_name)**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_linked_picture). Die Methode gibt ein [**Picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture)-Objekt zurück.

Das folgende Beispiel zeigt, wie ein verknüpftes Bild von einer Webadresse in ein Arbeitsblatt eingefügt wird.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Pictures-InsertLinkedPicture-1.py" >}}
