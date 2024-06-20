---
title: Bilder verwalten
type: docs
weight: 10
url: /de/net/managing-pictures/
---

Aspose.Cells ermöglicht es Entwicklern, Bilder zur Laufzeit zu Tabellenkalkulationen hinzuzufügen. Darüber hinaus kann die Positionierung dieser Bilder zur Laufzeit kontrolliert werden, was in den folgenden Abschnitten detaillierter erläutert wird.

Dieser Artikel erklärt, wie man Bilder hinzufügt und wie man ein Bild einfügt, das den Inhalt bestimmter Zellen zeigt.

## **Bilder hinzufügen**

Das Hinzufügen von Bildern zu einer Tabelle ist sehr einfach. Es dauert nur wenige Zeilen Code:
Rufen Sie einfach die [**Add**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index)-Methode der [**Pictures**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection)-Sammlung (die im [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)-Objekt verkapselt ist) auf. Die [**Add**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection/methods/add/index)-Methode akzeptiert die folgenden Parameter:

- **Index der oberen linken Zeile**, der Index der oberen linken Zeile.
- **Index der oberen linken Spalte**, der Index der oberen linken Spalte.
- **Bilddateiname**, der Name der Bilddatei inklusive des Pfads.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-AddingPictures-1.cs" >}}

## **Bilder positionieren**

Es gibt zwei mögliche Methoden, um die Positionierung von Bildern mithilfe von Aspose.Cells zu kontrollieren:

- Proportionale Positionierung: Definieren Sie eine Position proportional zur Zeilenhöhe und -breite.
- Absolute Positionierung: Definieren Sie die genaue Position auf der Seite, an der das Bild eingefügt werden soll, z.B. 40 Pixel links und 20 Pixel unterhalb des Zellrandes.

### **Proportionale Positionierung**

Entwickler können die Bilder proportional zur Zeilenhöhe und Spaltenbreite mithilfe der [**UpperDeltaX**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/upperdeltax)- und [**UpperDeltaY**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/upperdeltay)-Eigenschaften des [**Aspose.Cells.Drawing.Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture)-Objekts positionieren. Ein [**Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture)-Objekt kann aus der [**Pictures**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picturecollection)-Sammlung erhalten werden, indem sein Bildindex übergeben wird. Dieses Beispiel platziert ein Bild in der Zelle F6.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-PositioningPictures-ProportionalPositioning-1.cs" >}}

### **Absolute Positionierung**

Entwickler können auch die Bilder absolut positionieren, indem sie die Eigenschaften [**Left**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/left) und [**Top**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/top) des [**Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture)-Objekts verwenden. Dieses Beispiel platziert ein Bild in der Zelle F6, 60 Pixel von links und 10 Pixel von oben der Zelle entfernt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-PositioningPictures-AbsolutePositioning-1.cs" >}}

## **Einfügen eines Bildes basierend auf Zellverweis**

Mit Aspose.Cells können Sie den Inhalt einer Arbeitsblattzelle in eine Bildform darstellen. Sie können das Bild mit der Zelle verknüpfen, die die Daten enthält, die Sie anzeigen möchten. Da die Zelle oder Zellenbereich mit dem Grafikobjekt verknüpft ist, erscheinen Änderungen, die Sie an den Daten in dieser Zelle oder dem Zellenbereich vornehmen, automatisch im Grafikobjekt.

Fügen Sie ein Bild zum Arbeitsblatt hinzu, indem Sie die [**AddPicture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addpicture/index)-Methode der [**ShapeCollection**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection)-Sammlung aufrufen (die im [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)-Objekt verkapselt ist). Geben Sie den Zellenbereich mit dem [**Formula**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture/properties/formula)-Attribut des [**Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture)-Objekts an.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-Pictures-PictureCellReference-1.cs" >}}

## **Erweiterte Themen**
- [Hinzufügen eines bedingten Symbolsets mit dem Zelltext](/cells/de/net/add-conditional-icons-set-with-the-cell-text/)
- [Verknüpftes Bild aus Webadresse einfügen](/cells/de/net/insert-a-linked-picture-from-web-address/)
- [Bild anhand von Zellenverweis einfügen](/cells/de/net/insert-a-picture-based-on-cell-reference/)
- [Laden Sie ein Web-Bild von einer URL in eine Excel-Arbeitsmappe](/cells/de/net/load-a-web-image-from-a-url-into-an-excel-worksheet/)

