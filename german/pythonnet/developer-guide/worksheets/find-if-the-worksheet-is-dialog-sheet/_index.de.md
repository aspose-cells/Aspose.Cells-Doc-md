---
title: Feststellen, ob das Arbeitsblatt ein Dialogblatt ist
type: docs
weight: 90
url: /de/python-net/find-if-the-worksheet-is-dialog-sheet/
description: Dialogblatt ist ein altes Format. Dieser Artikel bietet Anweisungen und Beispielcode, um programmgesteuert zu bestimmen, ob ein Excel Arbeitsblatt ein Dialogblatt ist, unter Verwendung der Aspose.Cells für Python via .NET Bibliothek.
keywords: Python Excel Bibliothek, Python Dialogtyp für Excel Arbeitsblatt Suchdialog, Arbeitsblatt Dialog in Python.
---

## **Mögliche Verwendungsszenarien**

Ein Dialogblatt ist ein altes Format eines Arbeitsblatts mit einem Dialogfeld. Ein solches Blatt könnte von einer älteren Version von Microsoft Excel, z. B. 2003, wie in diesem Screenshot gezeigt, eingefügt werden. Es kann auch mit VBA in neueren Versionen wie Microsoft Excel 2016 eingefügt werden.

![todo:image_alt_text](find-if-the-worksheet-is-dialog-sheet_1.png)

Sie können feststellen, ob das Blatt ein Dialogblatt oder ein anderer Blatttyp ist, mit der Eigenschaft [**Worksheet.type**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/type/), die von Aspose.Cells für Python via .NET bereitgestellt wird. Wenn sie den Enumerationswert [**SheetType.DIALOG**](https://reference.aspose.com/cells/python-net/aspose.cells/sheettype/) zurückgibt, bedeutet dies, dass Sie es mit einem Dialogblatt zu tun haben.

## **Feststellen, ob das Arbeitsblatt ein Dialogblatt ist**

Der folgende Beispielcode lädt die [Beispieldatei Excel](64716820.xlsx), die ein Dialogblatt enthält. Es überprüft die  [**Worksheet.type**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/type/)-Eigenschaft, vergleicht sie mit  [**SheetType.DIALOG**](https://reference.aspose.com/cells/python-net/aspose.cells/sheettype/) und druckt dann die Meldung. Bitte sehen Sie die Konsolenausgabe des untenstehenden Beispielcodes für mehr Hilfe.

## **Beispielcode**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-FindIfWorksheetIsDialogSheet.py" >}}

## **Konsolenausgabe**

{{< highlight java >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
