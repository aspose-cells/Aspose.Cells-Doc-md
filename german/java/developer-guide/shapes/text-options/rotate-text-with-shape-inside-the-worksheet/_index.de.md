---
title: Text mit Shape innerhalb des Arbeitsblatts drehen
type: docs
weight: 110
url: /de/java/rotate-text-with-shape-inside-the-worksheet/
---

## **Mögliche Verwendungsszenarien**

Sie können Text in jeder Form in Microsoft Excel hinzufügen. Wenn Sie eine Form in dem sehr alten Microsoft Excel 2003 hinzufügen, wird der Text nicht mit der Form gedreht. Wenn Sie jedoch Formen in neueren Versionen von Microsoft Excel z. B. 2007, 2010, 2013 oder 2016, usw. hinzufügen, wird der Text mit der Form gedreht. Sie können steuern, ob der Text mit der Form gedreht werden soll oder nicht, indem Sie die Eigenschaft [**ShapeTextAlignment.RotateTextWithShape**](https://reference.aspose.com/cells/java/com.aspose.cells/shapetextalignment#RotateTextWithShape) verwenden. Der Standardwert davon ist **true**, was bedeutet, dass der Text mit der Form gedreht wird, aber wenn Sie es als **false** festlegen, dann wird der Text nicht mit der Form gedreht.

## **Text mit Form im Arbeitsblatt drehen**

Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](64716919.xlsx), die eine Dreiecksform enthält und deren Text sich mit der Form dreht. Wenn Sie die Beispiel-Excel-Datei in Microsoft Excel öffnen und die Dreiecksform drehen, wird auch der Text mitgedreht. Der Code setzt dann die Eigenschaft [**ShapeTextAlignment.RotateTextWithShape**](https://reference.aspose.com/cells/java/com.aspose.cells/shapetextalignment#RotateTextWithShape) auf **falsch** und speichert sie als [Ausgabe-Excel-Datei](64716917.xlsx). Wenn Sie die Ausgabe-Excel-Datei jetzt in Microsoft Excel öffnen und die Dreiecksform drehen, wird der Text nicht mitgedreht. Bitte beachten Sie den folgenden Screenshot, der die Auswirkung des Codes auf die Beispiel-Excel-Datei zeigt.

![todo:image_alt_text](rotate-text-with-shape-inside-the-worksheet_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "DrawingObjects-RotateTextWithShapeInsideWorksheet.java" >}}
