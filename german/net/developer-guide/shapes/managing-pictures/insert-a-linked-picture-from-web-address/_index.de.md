---
title: Fügen Sie ein verknüpftes Bild von der Webadresse ein
type: docs
weight: 450
url: /de/net/insert-a-linked-picture-from-web-address/
---
{{% alert color="primary" %}}

Manchmal müssen Sie ein Bild aus dem Internet (http://) in ein Arbeitsblatt einfügen. Geben Sie dazu die URL des Bildes an und das Bild wird jedes Mal heruntergeladen, wenn die Tabelle in Microsoft Excel geöffnet wird. Das Bild ist nicht physisch in das Excel-Dokument eingebettet, sondern verweist auf eine Webressource.

{{% /alert %}}

## **Mit Microsoft Excel**

In Microsoft Excel (z. B. 2007):

1.  Drücke den**Einfügung** Menü und auswählen**Bild**.
1. Geben Sie die Webadresse für das Bild im Dialogfeld Bild einfügen an.

## **Mit Aspose.Cells for .NET**

 Aspose.Cells for .NET unterstützt das Hinzufügen eines verknüpften Bildes mithilfe von[**ShapeCollection.AddLinkedPicture(int upperLeftRow, int upperLeftColumn, int heightPixels, int widthPixels, string sourceFullName)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addlinkedpicture) . Die Methode gibt a zurück[**Bild**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture)Objekt.

Das folgende Beispiel zeigt, wie Sie ein verknüpftes Bild von einer Webadresse zu einem Arbeitsblatt hinzufügen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-InsertLinkedPicture-1.cs" >}}
