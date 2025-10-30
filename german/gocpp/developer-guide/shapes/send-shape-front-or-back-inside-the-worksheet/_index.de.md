---
title: Formen im Arbeitsblatt mit Golang über C++ nach vorne oder hinten schicken
linktitle: Form vorwärts oder rückwärts innerhalb des Arbeitsblatts senden
type: docs
weight: 3400
url: /de/go-cpp/send-shape-front-or-back-inside-the-worksheet/
description: Lernen Sie, wie Sie die Z Order Position von Formen in einem Arbeitsblatt mit Aspose.Cells for C++ ändern.
---

## **Mögliche Verwendungsszenarien**

Wenn mehrere Formen am selben Ort vorhanden sind, wird ihre Sichtbarkeit durch ihre Z-Reihenfolge-Positionen bestimmt. Aspose.Cells bietet die [**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/go-cpp/shape/tofrontorback/) Methode, die die Z-Orders-Position der Form ändert. Wenn Sie eine Form nach hinten schicken möchten, verwenden Sie eine negative Zahl wie -1, -2, -3 usw. Wenn Sie eine Form nach vorne bringen möchten, verwenden Sie eine positive Zahl wie 1, 2, 3 usw.

## **Form nach vorn oder hinten im Arbeitsblatt senden**

Der folgende Beispielcode zeigt die Verwendung der [**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/go-cpp/shape/tofrontorback/) Methode. Bitte sehen Sie sich die [Beispiel-Excel-Datei](50528330.xlsx) an, die im Code verwendet wird, sowie die [Ausgabe-Excel-Datei](50528331.xlsx), die daraus erzeugt wurde. Der Screenshot zeigt die Wirkung des Codes auf die Beispiel-Excel-Datei nach der Ausführung.

![todo:image_alt_text](send-shape-front-or-back-inside-the-worksheet_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SendShapeFrontOrBackInsideTheWorksheet.go" >}}
