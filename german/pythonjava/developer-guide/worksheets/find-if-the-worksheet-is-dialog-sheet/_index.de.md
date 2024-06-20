---
title: Feststellen, ob das Arbeitsblatt ein Dialogblatt ist
type: docs
weight: 70
url: /de/python-java/find-if-the-worksheet-is-dialog-sheet/
---

## **Mögliche Verwendungsszenarien**
Dialogblatt ist ein altes Format des Blatts, das eine Dialogbox enthält. Ein solches Blatt könnte von einer älteren Version von Microsoft Excel, z.B. 2003, wie in diesem Screenshot gezeigt, eingefügt werden. Es kann auch mit VBA in neueren Versionen, z.B. Microsoft Excel 2016, eingefügt werden.

![todo:image_alt_text](DialogSheet.png)
## **Feststellen, ob das Arbeitsblatt ein Dialogblatt ist**
Aspose.Cells für Python via Java bietet Ihnen die Möglichkeit zu überprüfen, ob das Arbeitsblatt ein Dialogblatt ist. Hierfür bietet es die [Worksheet.Type](https://reference.aspose.com/cells/python/asposecells.api/worksheet#Type) Eigenschaft. Wenn [Worksheet.Type](https://reference.aspose.com/cells/python/asposecells.api/worksheet#Type) einen Enumerationswert [SheetType.DIALOG](https://reference.aspose.com/cells/python/asposecells.api/sheettype#DIALOG) zurückgibt, bedeutet dies, dass Sie es mit einem Dialogblatt zu tun haben.

Der folgende Codeausschnitt zeigt, wie nach einem Dialogblatt gesucht wird. Die von dem Code erzeugte Konsolenausgabe dient als Referenz.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Worksheets-FindIfWorksheetIsDialogSheet.py" >}}
## **Konsolenausgabe**
{{< highlight java >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
