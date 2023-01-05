---
title: Fügen Sie ein verknüpftes Bild von der Webadresse ein
type: docs
weight: 50
url: /de/java/insert-a-linked-picture-from-web-address/
---
{{% alert color="primary" %}}

Manchmal müssen Sie ein Bild aus dem Internet (http://) in ein Arbeitsblatt einfügen. Geben Sie dazu die URL des Bildes an und das Bild wird jedes Mal heruntergeladen, wenn die Tabelle in Microsoft Excel geöffnet wird. Das Bild ist nicht physisch in das Excel-Dokument eingebettet, sondern verweist auf eine Webressource.

{{% /alert %}}

## **Einfügen eines verlinkten Bildes von einer Webadresse**

### **Mit Microsoft Excel**

In Microsoft Excel (z. B. 2007):

1.  Drücke den**Einfügung** Menü und auswählen**Bild**.

![todo: Bild_alt_Text](insert-a-linked-picture-from-web-address_1.png)

1.  Geben Sie die Webadresse für das Bild im Dialogfeld Bild einfügen an.

![todo: Bild_alt_Text](insert-a-linked-picture-from-web-address_2.png)

Das Bild wird eingefügt.

![todo: Bild_alt_Text](insert-a-linked-picture-from-web-address_3.png)

### **Mit Aspose.Cells for Java**

 Aspose.Cells for Java unterstützt das Hinzufügen eines verknüpften Bildes mit der Methode[**ShapeCollection.addLinkedPicture(int upperLeftRow, int upperLeftColumn, int height, int width, java.lang.String sourceFullName)**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#addLinkedPicture(int,%20int,%20int,%20int,%20java.lang.String)).

 Die Methode gibt a zurück[**Bild**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture)Objekt.

Das folgende Beispiel zeigt, wie Sie ein verknüpftes Bild von einer Webadresse zu einem Arbeitsblatt hinzufügen.

Nach dem Ausführen des Codes enthält die generierte Excel-Datei ein verknüpftes Bild auf dem ersten Arbeitsblatt.

**Die Ausgabedatei** 

![todo: Bild_alt_Text](insert-a-linked-picture-from-web-address_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-InsertLinkedPicturefromWebAddress-InsertLinkedPicturefromWebAddress.java" >}}
