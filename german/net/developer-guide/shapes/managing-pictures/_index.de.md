---
title: Bilder verwalten
type: docs
weight: 10
url: /de/net/managing-pictures/
---
Aspose.Cells ermöglicht es Entwicklern, Bilder zur Laufzeit zu Tabellenkalkulationen hinzuzufügen. Darüber hinaus kann die Positionierung dieser Bilder zur Laufzeit gesteuert werden, was in den nächsten Abschnitten näher erläutert wird.

In diesem Artikel wird erläutert, wie Sie Bilder hinzufügen und wie Sie ein Bild einfügen, das den Inhalt bestimmter Zellen zeigt.

## **Bilder hinzufügen**

Das Hinzufügen von Bildern zu einer Tabelle ist sehr einfach. Es dauert nur ein paar Zeilen Code:
 Einfach anrufen[**Hinzufügen**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index) Methode der[**Bilder**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection) Sammlung (eingekapselt in der[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Objekt). Das[**Hinzufügen**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index)Die Methode nimmt die folgenden Parameter an:

- **Zeilenindex oben links**, der Index der oberen linken Zeile.
- **Spaltenindex oben links**, der Index der oberen linken Spalte.
- **Name der Bilddatei**, der Name der Bilddatei, komplett mit Pfad.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-AddingPictures-1.cs" >}}

## **Bilder positionieren**

Es gibt zwei Möglichkeiten, die Positionierung von Bildern mit Aspose.Cells zu steuern:

- Proportionale Positionierung: Definieren Sie eine Position proportional zur Zeilenhöhe und -breite.
- Absolute Positionierung: Definieren Sie die genaue Position auf der Seite, an der das Bild eingefügt wird, z. B. 40 Pixel links und 20 Pixel unterhalb des Rands der Zelle.

### **Proportionale Positionierung**

 Entwickler können die Bilder mithilfe von proportional zur Zeilenhöhe und Spaltenbreite positionieren[**UpperDeltaX**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/upperdeltax) und[**UpperDeltaY**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/upperdeltay) Eigenschaften der[**Aspose.Cells.Drawing.Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture) Objekt. EIN[**Bild**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture) Objekt kann von der bezogen werden[**Bilder**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection)Sammlung durch Übergabe ihres Bildindexes. Dieses Beispiel platziert ein Bild in der Zelle F6.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-PositioningPictures-ProportionalPositioning-1.cs" >}}

### **Absolute Positionierung**

 Entwickler können die Bilder auch absolut positionieren, indem sie die verwenden[**Links**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/left) und[**oben**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/top) Eigenschaften der[**Bild**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture)Objekt. Dieses Beispiel platziert ein Bild in Zelle F6, 60 Pixel vom linken und 10 Pixel vom oberen Rand der Zelle.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-PositioningPictures-AbsolutePositioning-1.cs" >}}

## **Einfügen eines Bildes basierend auf der Referenz Cell**

Mit Aspose.Cells können Sie den Inhalt einer Arbeitsblattzelle in einer Bildform anzeigen. Sie können das Bild mit der Zelle verknüpfen, die die Daten enthält, die Sie anzeigen möchten. Da die Zelle oder der Zellbereich mit dem Grafikobjekt verknüpft ist, werden Änderungen, die Sie an den Daten in dieser Zelle oder diesem Zellbereich vornehmen, automatisch im Grafikobjekt angezeigt.

 Fügen Sie dem Arbeitsblatt ein Bild hinzu, indem Sie die aufrufen[**Bild hinzufügen**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addpicture/index) Methode der[**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection) Sammlung (eingekapselt in der[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) Objekt). Geben Sie den Zellbereich mithilfe von an[**Formel**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture/properties/formula) Attribut der[**Bild**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture)Objekt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-PictureCellReference-1.cs" >}}

## **Themen vorantreiben**
- [Fügen Sie bedingte Symbole mit dem Text Cell hinzu](/cells/de/net/add-conditional-icons-set-with-the-cell-text/)
- [Fügen Sie ein verknüpftes Bild von der Webadresse ein](/cells/de/net/insert-a-linked-picture-from-web-address/)
- [Fügen Sie ein Bild basierend auf der Referenz Cell ein](/cells/de/net/insert-a-picture-based-on-cell-reference/)
- [Laden Sie ein Webbild von einer URL in ein Excel-Arbeitsblatt](/cells/de/net/load-a-web-image-from-a-url-into-an-excel-worksheet/)

