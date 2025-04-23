---
title: Text mit Shape innerhalb des Arbeitsblatts drehen
type: docs
weight: 1300
url: /de/python-net/rotate-text-with-shape-inside-the-worksheet/
---

## **Mögliche Verwendungsszenarien**

Sie können Text in jede Form innerhalb von Microsoft Excel einfügen. Wenn Sie eine Form mithilfe des sehr alten Microsoft Excel 2003 hinzufügen, wird der Text nicht mit der Form gedreht. Wenn Sie jedoch eine Form mit neueren Versionen von Microsoft Excel, z. B. 2007, 2010, 2013 oder 2016, usw., hinzufügen, wird der Text mit der Form gedreht. Sie können steuern, ob der Text mit der Form gedreht werden soll oder nicht, indem Sie die Eigenschaft [**ShapeTextAlignment.rotate_text_with_shape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.texts/shapetextalignment/rotate_text_with_shape) verwenden. Der Standardwert dafür ist **true**, was bedeutet, dass der Text mit der Form gedreht wird. Wenn Sie ihn jedoch auf **false** setzen, wird der Text nicht mit der Form gedreht.

## **Text mit Form im Arbeitsblatt drehen**

Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](64716896.xlsx) mit einer Dreiecksform und deren Text dreht sich mit der Form. Wenn Sie die Beispiel-Excel-Datei in Microsoft Excel öffnen und die Dreiecksform drehen, dreht sich auch der Text mit. Der Code stellt dann die [**ShapeTextAlignment.rotate_text_with_shape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.texts/shapetextalignment/rotate_text_with_shape) Eigenschaft als **false** ein und speichert sie als [Ausgabedatei](64716897.xlsx). Wenn Sie nun die Ausgabedatei in Microsoft Excel öffnen und die Dreiecksform drehen, wird sich der Text nicht mit ihr drehen. Bitte beachten Sie den folgenden Screenshot, der die Wirkung des Codes auf die Beispiel-Excel-Datei zur Veranschaulichung zeigt.

![todo:image_alt_text](rotate-text-with-shape-inside-the-worksheet_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Text-Options-RotateTextWithShapeInsideWorksheet.py" >}}
