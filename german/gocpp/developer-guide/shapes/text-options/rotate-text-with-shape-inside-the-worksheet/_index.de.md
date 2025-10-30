---
title: Text mit Shape im Arbeitsblatt rotieren mit Golang via C++
linktitle: Text mit Shape drehen
type: docs
weight: 1300
url: /de/go-cpp/rotate-text-with-shape-inside-the-worksheet/
description: Lernen Sie, wie Sie die Textrotation mit Shapes in Excel Tabellen mit Aspose.Cells for C++ steuern.
---

## **Mögliche Verwendungsszenarien**

Sie können Text in jeder Form mit Microsoft Excel hinzufügen. Wenn Sie eine Form mit der sehr alten Microsoft Excel 2003-Version hinzufügen, dreht sich der Text nicht mit der Form. Wenn Sie jedoch eine Form mit neueren Versionen von Microsoft Excel hinzufügen, wie 2007, 2010, 2013 oder 2016, dreht sich der Text mit der Form. Sie können steuern, ob der Text mit der Form drehen soll oder nicht, mit der [**ShapeTextAlignment.GetRotateTextWithShape()**](https://reference.aspose.com/cells/go-cpp/shapetextalignment/getrotatetextwithshape/)-Eigenschaft. Der Standardwert dieser Eigenschaft ist **true**, was bedeutet, dass sich der Text mit der Form dreht. Wenn Sie ihn auf **false** setzen, dreht sich der Text nicht mit der Form.

## **Text mit Form im Arbeitsblatt drehen**

Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](64716896.xlsx), die eine Dreieckform enthält und deren Text sich mit der Form dreht. Wenn Sie die Beispiel-Excel-Datei in Microsoft Excel öffnen und das Dreieck drehen, dreht sich auch der Text mit. Der Code setzt dann die [**ShapeTextAlignment.GetRotateTextWithShape()**](https://reference.aspose.com/cells/go-cpp/shapetextalignment/getrotatetextwithshape/)-Eigenschaft auf **false** und speichert sie als [Ausgabedatei](64716897.xlsx). Wenn Sie die Ausgabedatei in Microsoft Excel öffnen und das Dreieck drehen, dreht sich der Text nicht mit. Bitte sehen Sie sich den folgenden Screenshot an, der die Wirkung des Codes auf die Beispiel-Excel-Datei zeigt.

![todo:image_alt_text](rotate-text-with-shape-inside-the-worksheet_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RotateTextWithShapeInsideTheWorksheet.go" >}}
