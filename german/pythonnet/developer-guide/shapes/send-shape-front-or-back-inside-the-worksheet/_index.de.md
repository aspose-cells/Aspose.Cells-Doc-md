---
title: Form vorwärts oder rückwärts innerhalb des Arbeitsblatts senden
type: docs
weight: 3400
url: /de/python-net/send-shape-front-or-back-inside-the-worksheet/
---

## **Mögliche Verwendungsszenarien**

Wenn mehrere Formen am selben Ort vorhanden sind, entscheidet die Z-Reihenfolge, wie sie sichtbar sind. Aspose.Cells für Python via .NET bietet die [**Shape.to_front_or_back()**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/to_front_or_back) Methode, mit der die Z-Order-Position der Form geändert werden kann. Möchten Sie eine Form nach hinten schicken, verwenden Sie eine negative Zahl wie -1, -2, -3 usw., und um sie nach vorne zu bringen, verwenden Sie eine positive Zahl wie 1, 2, 3 usw.

## **Form nach vorn oder hinten im Arbeitsblatt senden**

Der folgende Beispielcode erläutert die Verwendung der [**Shape.to_front_or_back()**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/to_front_or_back)-Methode. Bitte sehen Sie die [Beispiel-Excel-Datei](50528330.xlsx), die innerhalb des Codes verwendet wird, und die von ihr generierte [Ausgabedatei im Excel-Format](50528331.xlsx). Das Bild zeigt die Auswirkung des Codes auf die Beispiel-Excel-Datei bei der Ausführung.

![todo:image_alt_text](send-shape-front-or-back-inside-the-worksheet_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-SendShapeFrontOrBackInWorksheet.py" >}}
