---
title: Form vorwärts oder rückwärts innerhalb des Arbeitsblatts senden
type: docs
weight: 600
url: /de/java/send-shape-front-or-back-inside-the-worksheet/
---

## **Mögliche Verwendungsszenarien**

Wenn sich mehrere Formen am selben Ort befinden, wird entschieden, wie sie sichtbar sind, durch ihre Z-Order-Positionen. Aspose.Cells bietet die Methode [**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#toFrontOrBack-int-), die die Z-Order-Position der Form ändert. Wenn Sie die Form nach hinten senden möchten, verwenden Sie eine negative Zahl wie -1, -2, -3 usw. und wenn Sie die Form nach vorne senden möchten, verwenden Sie eine positive Zahl wie 1, 2, 3 usw.

## **Form nach vorn oder hinten im Arbeitsblatt senden**

Der folgende Beispielcode erläutert die Verwendung der Methode [**Shape.ToFrontOrBack()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#toFrontOrBack-int-). Bitte sehen Sie die [Beispiel-Excel-Datei](50528362.xlsx) im Code und die [Ausgabe-Excel-Datei](50528361.xlsx), die durch sie generiert wird. Der Screenshot zeigt die Auswirkung des Codes auf die Beispiel-Excel-Datei bei seiner Ausführung.

![todo:image_alt_text](send-shape-front-or-back-inside-the-worksheet_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-DrawingObjects-SendShapeFrontOrBackInWorksheet.java" >}}
{{< app/cells/assistant language="java" >}}
