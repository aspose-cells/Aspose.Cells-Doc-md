---
title: Bilder verwalten
type: docs
weight: 10
url: /de/java/managing-pictures/
---
{{% alert color="primary" %}}

Aspose.Cells ermöglicht es Entwicklern, Bilder zur Laufzeit zu Tabellenkalkulationen hinzuzufügen. Darüber hinaus kann die Positionierung dieser Bilder zur Laufzeit gesteuert werden, was in den nächsten Abschnitten näher erläutert wird.

Aspose.Cells for Java unterstützt nur Bildformate: BMP, JPEG, PNG, GIF.

In Beispielen verwendete Indizes beginnen bei 0.

{{% /alert %}}

## **Bilder hinzufügen**

Das Hinzufügen von Bildern zu einer Tabelle ist sehr einfach. Es dauert nur ein paar Zeilen Code.

 Einfach anrufen[**addieren**](https://reference.aspose.com/cells/java/com.aspose.cells/picturecollection#add(int,%20int,%20java.lang.String) ) Methode der[**Bilder**](https://reference.aspose.com/cells/java/com.aspose.cells/PictureCollection) Sammlung (eingekapselt in der[**Arbeitsblatt**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) Objekt). Das[**addieren**](https://reference.aspose.com/cells/java/com.aspose.cells/picturecollection#add(int,%20int,%20java.lang.String))-Methode nimmt die folgenden Parameter an:

- **Zeilenindex oben links**, der Index der oberen linken Zeile.
- **Spaltenindex oben links**, der Index der oberen linken Spalte.
- **Name der Bilddatei**, der Name der Bilddatei, komplett mit Pfad.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-pictures-AddingPictures-1.java" >}}

## **Positionierung von Bildern**

Bilder können mit Aspose.Cells wie folgt positioniert werden:

- [Absolute Positionierung](/cells/de/java/managing-pictures/#absolute-positioning).

### **Absolute Positionierung**

 Entwickler können die Bilder absolut positionieren, indem sie die verwenden[**setUpperDeltaX**](https://reference.aspose.com/cells/java/com.aspose.cells/picture#UpperDeltaX) und[**setUpperDeltaY**](https://reference.aspose.com/cells/java/com.aspose.cells/picture#UpperDeltaY) Methoden der[**Bild**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture)Objekt.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-pictures-PositioningPictures-AbsolutePositioning-1.java" >}}

## **Themen vorantreiben**
- [Fügen Sie ein verknüpftes Bild von der Webadresse ein](/cells/de/java/insert-a-linked-picture-from-web-address/)
- [Fügen Sie ein Bild ein, das auf der Referenz Cell basiert](/cells/de/java/insert-a-picture-based-on-cell-reference/)
- [Fügen Sie ein Webbild von einer URL in ein Excel-Arbeitsblatt ein](/cells/de/java/insert-web-image-from-a-url-into-an-excel-worksheet/)
