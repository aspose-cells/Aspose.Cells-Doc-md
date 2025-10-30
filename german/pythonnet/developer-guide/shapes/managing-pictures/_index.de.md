---
title: Bilder verwalten
type: docs
weight: 10
url: /de/python-net/managing-pictures/
---

Aspose.Cells für Python via .NET ermöglicht es Entwicklern, Bilder zur Laufzeit in Tabellen einzufügen. Außerdem kann die Positionierung dieser Bilder zur Laufzeit kontrolliert werden, was in den kommenden Abschnitten näher erläutert wird.

Dieser Artikel erklärt, wie man Bilder hinzufügt und wie man ein Bild einfügt, das den Inhalt bestimmter Zellen zeigt.

## **Bilder hinzufügen**

Das Hinzufügen von Bildern zu einer Tabelle ist sehr einfach. Es dauert nur wenige Zeilen Code:
Rufen Sie einfach die [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picturecollection/add)-Methode der [**pictures**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picturecollection)-Sammlung (die im [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)-Objekt verkapselt ist) auf. Die [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picturecollection/add)-Methode akzeptiert die folgenden Parameter:

- **Index der oberen linken Zeile**, der Index der oberen linken Zeile.
- **Index der oberen linken Spalte**, der Index der oberen linken Spalte.
- **Bilddateiname**, der Name der Bilddatei inklusive des Pfads.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Pictures-AddingPictures-1.py" >}}

## **Bilder positionieren**

Es gibt zwei mögliche Wege, die Positionierung von Bildern mit Aspose.Cells für Python via .NET zu steuern:

- Proportionale Positionierung: Definieren Sie eine Position proportional zur Zeilenhöhe und -breite.
- Absolute Positionierung: Definieren Sie die genaue Position auf der Seite, an der das Bild eingefügt werden soll, z.B. 40 Pixel links und 20 Pixel unterhalb des Zellrandes.

### **Proportionale Positionierung**

Entwickler können die Bilder proportional zur Zeilenhöhe und Spaltenbreite mithilfe der [**upper_delta_x**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/upper_delta_x)- und [**upper_delta_y**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/upper_delta_y)-Eigenschaften des [**Aspose.Cells.Drawing.Picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture)-Objekts positionieren. Ein [**Picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture)-Objekt kann aus der [**pictures**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picturecollection)-Sammlung erhalten werden, indem sein Bildindex übergeben wird. Dieses Beispiel platziert ein Bild in der Zelle F6.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Pictures-PositioningPictures-ProportionalPositioning-1.py" >}}

### **Absolute Positionierung**

Entwickler können auch die Bilder absolut positionieren, indem sie die Eigenschaften [**left**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/left) und [**top**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/top) des [**Picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture)-Objekts verwenden. Dieses Beispiel platziert ein Bild in der Zelle F6, 60 Pixel von links und 10 Pixel von oben der Zelle entfernt.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Pictures-PositioningPictures-AbsolutePositioning-1.py" >}}

## **Einfügen eines Bildes basierend auf Zellverweis**

Aspose.Cells für Python via .NET ermöglicht es Ihnen, den Inhalt einer Tabellenzelle in eine Bildform zu rendern. Sie können das Bild mit der Zelle verlinken, die die Daten enthält, die Sie anzeigen möchten. Da die Zelle oder der Zellbereich mit dem Grafikobjekt verknüpft ist, werden Änderungen an den Daten in dieser Zelle oder diesem Zellbereich automatisch im Grafikobjekt angezeigt.

Fügen Sie ein Bild zum Arbeitsblatt hinzu, indem Sie die [**add_picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_picture)-Methode der [**ShapeCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection)-Sammlung aufrufen (die im [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet)-Objekt verkapselt ist). Geben Sie den Zellenbereich mit dem [**formula**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture/formula)-Attribut des [**Picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture)-Objekts an.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-Pictures-PictureCellReference-1.py" >}}

## **Erweiterte Themen**
- [Hinzufügen eines bedingten Symbolsets mit dem Zelltext](/cells/de/python-net/add-conditional-icons-set-with-the-cell-text/)
- [Verknüpftes Bild aus Webadresse einfügen](/cells/de/python-net/insert-a-linked-picture-from-web-address/)
- [Bild anhand von Zellenverweis einfügen](/cells/de/python-net/insert-a-picture-based-on-cell-reference/)
- [Laden Sie ein Web-Bild von einer URL in eine Excel-Arbeitsmappe](/cells/de/python-net/load-a-web-image-from-a-url-into-an-excel-worksheet/)

{{< app/cells/assistant language="python-net" >}}
