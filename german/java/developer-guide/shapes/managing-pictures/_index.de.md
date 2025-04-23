---
title: Bilder verwalten
type: docs
weight: 10
url: /de/java/managing-pictures/
---

Aspose.Cells ermöglicht es Entwicklern, Bilder zur Laufzeit zu Tabellenkalkulationen hinzuzufügen. Darüber hinaus kann die Positionierung dieser Bilder zur Laufzeit kontrolliert werden, was in den folgenden Abschnitten detaillierter erläutert wird.

Dieser Artikel erklärt, wie man Bilder hinzufügt und wie man ein Bild einfügt, das den Inhalt bestimmter Zellen zeigt.

## **Bilder hinzufügen**

Das Hinzufügen von Bildern zu einer Tabelle ist sehr einfach. Es dauert nur wenige Zeilen Code.

Rufen Sie einfach die Methode [**add**](https://reference.aspose.com/cells/java/com.aspose.cells/picturecollection#add-int-int-java.lang.String-) der Sammlung [**Pictures**](https://reference.aspose.com/cells/java/com.aspose.cells/PictureCollection) (die im Objekt [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) gekapselt ist) auf. Die Methode [**add**](https://reference.aspose.com/cells/java/com.aspose.cells/picturecollection#add-int-int-java.lang.String-) nimmt die folgenden Parameter an:

- **Index der oberen linken Zeile**, der Index der oberen linken Zeile.
- **Index der oberen linken Spalte**, der Index der oberen linken Spalte.
- **Bilddateiname**, der Name der Bilddatei inklusive des Pfads.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-pictures-AddingPictures-1.java" >}}

## **Positionierung von Bildern**

Bilder können in Aspose.Cells wie folgt positioniert werden:

- [Absolute Positionierung](/cells/de/java/managing-pictures/#absolute-positioning).

### **Absolute Positionierung**

Entwickler können die Bilder absolut positionieren, indem sie die Methoden [**setUpperDeltaX**](https://reference.aspose.com/cells/java/com.aspose.cells/picture#UpperDeltaX) und [**setUpperDeltaY**](https://reference.aspose.com/cells/java/com.aspose.cells/picture#UpperDeltaY) des Objekts [**Picture**](https://reference.aspose.com/cells/java/com.aspose.cells/Picture) verwenden.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-DrawingObjects-pictures-PositioningPictures-AbsolutePositioning-1.java" >}}

## **Erweiterte Themen**
- [Verknüpftes Bild aus Webadresse einfügen](/cells/de/java/insert-a-linked-picture-from-web-address/)
- [Ein Bild basierend auf Zellverweis einfügen](/cells/de/java/insert-a-picture-based-on-cell-reference/)
- [Ein Webbild von einer URL in ein Excel-Arbeitsblatt einfügen](/cells/de/java/insert-web-image-from-a-url-into-an-excel-worksheet/)
{{< app/cells/assistant language="java" >}}
