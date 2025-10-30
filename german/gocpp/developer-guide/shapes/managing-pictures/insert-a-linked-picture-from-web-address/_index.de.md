---
title: Webadresse Verknüpfen Sie ein Bild mit Golang via C++
linktitle: Verknüpftes Bild aus Webadresse einfügen
type: docs
weight: 450
url: /de/go-cpp/insert-a-linked-picture-from-web-address/
description: Erfahren Sie, wie Sie ein verknüpftes Bild von einer Webadresse in ein Arbeitsblatt mit Aspose.Cells for C++ einfügen.
---

{{% alert color="primary" %}}

Manchmal müssen Sie ein Bild von der Webseite (http://) in ein Arbeitsblatt einfügen. Geben Sie dazu die URL des Bildes an, und das Bild wird jedes Mal heruntergeladen, wenn die Tabelle in Microsoft Excel geöffnet wird. Das Bild ist nicht physisch in das Excel-Dokument eingebettet, sondern verweist auf eine Webressource.

{{% /alert %}}

## **Verwendung von Microsoft Excel**

In Microsoft Excel (zum Beispiel 2007):

1. Klicken Sie auf das **Einfügen** Menü und wählen Sie **Bild** aus.
1. Geben Sie die Webadresse für das Bild im Dialogfeld Bild einfügen an.

## **Mit Aspose.Cells for C++ verwenden**

Aspose.Cells for C++ unterstützt das Hinzufügen eines verknüpften Bildes mit der Methode [**ShapeCollection::AddLinkedPicture(int upperLeftRow, int upperLeftColumn, int heightPixels, int widthPixels, System::String sourceFullName)**](https://reference.aspose.com/cells/go-cpp/shapecollection/addlinkedpicture/). Die Methode gibt ein [**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/)-Objekt zurück.

Das folgende Beispiel zeigt, wie man ein verknüpftes Bild von einer Webadresse in ein Arbeitsblatt einfügt.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-InsertALinkedPictureFromWebAddress.go" >}}
