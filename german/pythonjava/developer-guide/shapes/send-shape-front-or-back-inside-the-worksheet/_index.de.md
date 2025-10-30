---
title: Formen in einem Arbeitsblatt nach vorne oder nach hinten bringen
type: docs
weight: 3400
url: /de/python-java/send-shape-front-or-back-inside-the-worksheet/
---

## **Mögliche Verwendungsszenarien**

Wenn sich mehrere Formen am selben Ort befinden, wird entschieden, wie sie sichtbar sein sollen, anhand ihrer Z-Order-Positionen. Aspose.Cells bietet die Methode [**Shape.toFrontOrBack()**](https://reference.aspose.com/cells/python-java/asposecells.api/shape#toFrontOrBack(int)), mit der die Z-Order-Position der Form geändert wird. Wenn Sie die Form nach hinten senden möchten, verwenden Sie eine negative Zahl wie -1, -2, -3 usw. Wenn Sie die Form nach vorne senden möchten, verwenden Sie eine positive Zahl wie 1, 2, 3 usw.

## **Formform vorne oder hinten in das Arbeitsblatt bringen**

Der folgende Beispielcode erklärt die Verwendung der [**Shape.toFrontOrBack()**](https://reference.aspose.com/cells/python-java/asposecells.api/shape#toFrontOrBack(int))-Methode. Bitte sehen Sie sich die [Beispiel-Excel-Datei](sampleToFrontOrBack.xlsx) an, die im Code verwendet wird, sowie die durch ihn erzeugte [Ausgabe-Excel-Datei](50528331.xlsx). Der Screenshot zeigt die Wirkung des Codes auf die Beispiel-Excel-Datei bei Ausführung.

![todo:image_alt_text](send-shape-front-or-back-inside-the-worksheet_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Examples-pythonjava-Shapes-BringShapeFrontOrBackInWorksheet.py" >}}
{{< app/cells/assistant language="csharp" >}}
