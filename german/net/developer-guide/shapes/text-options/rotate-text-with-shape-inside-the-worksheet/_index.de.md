---
title: Drehen Sie Text mit Form innerhalb des Arbeitsblatts
type: docs
weight: 1300
url: /de/net/rotate-text-with-shape-inside-the-worksheet/
---
## **Mögliche Nutzungsszenarien**

Mit Microsoft Excel können Sie Text in jede beliebige Form einfügen. Wenn Sie eine Form mit dem sehr alten Microsoft Excel 2003 hinzufügen, dreht sich der Text nicht mit der Form. Wenn Sie jedoch eine Form mit neueren Versionen von Microsoft Excel hinzufügen, z. B. 2007, 2010, 2013 oder 2016 usw., dreht sich der Text mit der Form. Sie können steuern, ob sich der Text mit der Form drehen soll oder nicht[**ShapeTextAlignment.RotateTextWithShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing.texts/shapetextalignment/properties/rotatetextwithshape) Eigentum. Der Standardwert davon ist**wahr**was bedeutet, dass sich der Text mit der Form dreht, aber wenn Sie ihn so einstellen**FALSCH**, dann dreht sich der Text nicht mit der Form.

## **Drehen Sie Text mit Form innerhalb des Arbeitsblatts**

 Der folgende Beispielcode lädt die[Beispiel-Excel-Datei](64716896.xlsx) das eine Dreiecksform hat und dessen Text sich mit der Form dreht. Wenn Sie die Beispiel-Excel-Datei in Microsoft Excel öffnen und die Dreiecksform drehen, dreht sich auch der Text mit. Der Code setzt dann die[**ShapeTextAlignment.RotateTextWithShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing.texts/shapetextalignment/properties/rotatetextwithshape) Eigentum als**FALSCH** und speichert es als[Excel-Datei ausgeben](64716897.xlsx). Wenn Sie jetzt die Excel-Ausgabedatei in Microsoft Excel öffnen und die Dreiecksform drehen, dreht sich der Text nicht mit. Als Referenz sehen Sie sich bitte den folgenden Screenshot an, der die Auswirkung des Codes auf die Beispiel-Excel-Datei zeigt.

![todo: Bild_alt_Text](rotate-text-with-shape-inside-the-worksheet_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "DrawingObjects-RotateTextWithShapeInsideWorksheet.cs" >}}
