---
title: Verknüpftes Bild aus Webadresse einfügen
type: docs
weight: 50
url: /de/java/insert-a-linked-picture-from-web-address/
---

{{% alert color="primary" %}}

Manchmal müssen Sie ein Bild von der Webseite (http://) in ein Arbeitsblatt einfügen. Geben Sie dazu die URL des Bildes an, und das Bild wird jedes Mal heruntergeladen, wenn die Tabelle in Microsoft Excel geöffnet wird. Das Bild ist nicht physisch in das Excel-Dokument eingebettet, sondern verweist auf eine Webressource.

{{% /alert %}}

## **Einfügen eines verknüpften Bildes von Webadresse**

### **Verwendung von Microsoft Excel**

In Microsoft Excel (zum Beispiel 2007):

1. Klicken Sie auf das **Einfügen** Menü und wählen Sie **Bild** aus.

![todo:image_alt_text](insert-a-linked-picture-from-web-address_1.png)

1. Geben Sie die Webadresse für das Bild im Dialogfeld Bild einfügen an. 

![todo:image_alt_text](insert-a-linked-picture-from-web-address_2.png)

Das Bild wird eingefügt.

![todo:image_alt_text](insert-a-linked-picture-from-web-address_3.png)

### **Verwendung von Aspose.Cells for Java**

Aspose.Cells for Java unterstützt das Hinzufügen eines verknüpften Bildes mit der Methode [**ShapeCollection.addLinkedPicture(int upperLeftRow, int upperLeftColumn, int height, int width, java.lang.String sourceFullName)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addLinkedPicture-int-int-int-int-java.lang.String-).

Die Methode gibt ein [**Picture**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture)-Objekt zurück.

Das folgende Beispiel zeigt, wie ein verknüpftes Bild von einer Webadresse in ein Arbeitsblatt eingefügt wird.

Nach Ausführen des Codes enthält die generierte Excel-Datei ein verknüpftes Bild auf dem ersten Arbeitsblatt.

**Die Ausgabedatei** 

![todo:image_alt_text](insert-a-linked-picture-from-web-address_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-InsertLinkedPicturefromWebAddress-InsertLinkedPicturefromWebAddress.java" >}}
{{< app/cells/assistant language="java" >}}
