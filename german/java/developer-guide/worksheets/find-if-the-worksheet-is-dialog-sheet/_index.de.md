---
title: Feststellen, ob das Arbeitsblatt ein Dialogblatt ist
type: docs
weight: 100
url: /de/java/find-if-the-worksheet-is-dialog-sheet/
---

## **Mögliche Verwendungsszenarien**

Dialogblatt ist ein altes Format des Blatts, das eine Dialogbox enthält. Ein solches Blatt könnte von einer älteren Version von Microsoft Excel, z.B. 2003, wie in diesem Screenshot gezeigt, eingefügt werden. Es kann auch mit VBA in neueren Versionen, z.B. Microsoft Excel 2016, eingefügt werden.

![todo:image_alt_text](find-if-the-worksheet-is-dialog-sheet_1.png)

Sie können feststellen, ob das Blatt ein Dialogblatt oder eine andere Art von Blatt ist, indem Sie die Eigenschaft [**Worksheet.Type**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Type) verwenden, die von Aspose.Cells bereitgestellt wird. Wenn sie den Enumerationwert [**SheetType.DIALOG**](https://reference.aspose.com/cells/java/com.aspose.cells/sheettype#DIALOG) zurückgibt, bedeutet dies, dass es sich um ein Dialogblatt handelt.

## **Feststellen, ob das Arbeitsblatt ein Dialogblatt ist**

Der folgende Beispielcode lädt die [Beispieldatei](64716841.xlsx), die ein Dialogblatt enthält. Er überprüft die Eigenschaft {0, vergleicht sie mit {1} und gibt dann die Meldung aus. Bitte sehen Sie unten die Konsolenausgabe des Beispielcodes für weitere Hilfe.

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Worksheets-FindIfWorksheetIsDialogSheet.java" >}}

## **Konsolenausgabe**

{{< highlight java >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
