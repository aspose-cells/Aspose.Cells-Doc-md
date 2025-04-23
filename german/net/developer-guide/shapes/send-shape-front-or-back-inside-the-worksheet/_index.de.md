---
title: Form vorwärts oder rückwärts innerhalb des Arbeitsblatts senden
type: docs
weight: 3400
url: /de/net/send-shape-front-or-back-inside-the-worksheet/
---

## **Mögliche Verwendungsszenarien**

Wenn sich mehrere Formen am selben Ort befinden, wird entschieden, wie sie sichtbar sein sollen, anhand ihrer Z-Order-Positionen. Aspose.Cells bietet die Methode [**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/methods/tofrontorback), mit der die Z-Order-Position der Form geändert wird. Wenn Sie die Form nach hinten senden möchten, verwenden Sie eine negative Zahl wie -1, -2, -3 usw. Wenn Sie die Form nach vorne senden möchten, verwenden Sie eine positive Zahl wie 1, 2, 3 usw.

## **Form nach vorn oder hinten im Arbeitsblatt senden**

Der folgende Beispielcode erläutert die Verwendung der [**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/methods/tofrontorback)-Methode. Bitte sehen Sie die [Beispiel-Excel-Datei](50528330.xlsx), die innerhalb des Codes verwendet wird, und die von ihr generierte [Ausgabedatei im Excel-Format](50528331.xlsx). Das Bild zeigt die Auswirkung des Codes auf die Beispiel-Excel-Datei bei der Ausführung.

![todo:image_alt_text](send-shape-front-or-back-inside-the-worksheet_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-SendShapeFrontOrBackInWorksheet.cs" >}}
{{< app/cells/assistant language="csharp" >}}
