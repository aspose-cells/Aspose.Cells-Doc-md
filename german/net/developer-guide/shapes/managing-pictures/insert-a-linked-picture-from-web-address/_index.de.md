---
title: Verknüpftes Bild aus Webadresse einfügen
type: docs
weight: 450
url: /de/net/insert-a-linked-picture-from-web-address/
---

{{% alert color="primary" %}}

Manchmal müssen Sie ein Bild von der Webseite (http://) in ein Arbeitsblatt einfügen. Geben Sie dazu die URL des Bildes an, und das Bild wird jedes Mal heruntergeladen, wenn die Tabelle in Microsoft Excel geöffnet wird. Das Bild ist nicht physisch in das Excel-Dokument eingebettet, sondern verweist auf eine Webressource.

{{% /alert %}}

## **Verwendung von Microsoft Excel**

In Microsoft Excel (zum Beispiel 2007):

1. Klicken Sie auf das **Einfügen** Menü und wählen Sie **Bild** aus.
1. Geben Sie die Webadresse für das Bild im Dialogfeld Bild einfügen an.

## **Verwendung von Aspose.Cells for .NET**

Aspose.Cells for .NET unterstützt das Hinzufügen eines verknüpften Bildes mit Hilfe des [**ShapeCollection.AddLinkedPicture(int upperLeftRow, int upperLeftColumn, int heightPixels, int widthPixels, string sourceFullName)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addlinkedpicture). Die Methode gibt ein [**Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture) Objekt zurück.

Das folgende Beispiel zeigt, wie ein verknüpftes Bild von einer Webadresse in ein Arbeitsblatt eingefügt wird.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-InsertLinkedPicture-1.cs" >}}
