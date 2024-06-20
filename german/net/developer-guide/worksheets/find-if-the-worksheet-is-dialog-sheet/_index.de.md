---
title: Feststellen, ob das Arbeitsblatt ein Dialogblatt ist
type: docs
weight: 90
url: /de/net/find-if-the-worksheet-is-dialog-sheet/
description: Ein Dialogblatt ist ein älteres Format eines Arbeitsblatts. Dieser Artikel enthält Anweisungen und Beispielcode zum programmgesteuerten Bestimmen, ob ein Excel Arbeitsblatt ein Dialogblatt mithilfe der C# API oder .NET Bibliothek ist.
keywords: Excel Arbeitsblattdialogtyp in c# finden, Arbeitsblattdialog in c#
---

## **Mögliche Verwendungsszenarien**

Ein Dialogblatt ist ein altes Format eines Arbeitsblatts mit einem Dialogfeld. Ein solches Blatt könnte von einer älteren Version von Microsoft Excel, z. B. 2003, wie in diesem Screenshot gezeigt, eingefügt werden. Es kann auch mit VBA in neueren Versionen wie Microsoft Excel 2016 eingefügt werden.

![todo:image_alt_text](find-if-the-worksheet-is-dialog-sheet_1.png)

Sie können mithilfe der [**Worksheet.Type**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/type)-Eigenschaft von Aspose.Cells feststellen, ob das Blatt ein Dialogblatt oder ein anderes Blatt ist. Wenn sie einen Enumerationswert [**SheetType.Dialog**](https://reference.aspose.com/cells/net/aspose.cells/sheettype) zurückgibt, bedeutet dies, dass Sie es mit einem Dialogblatt zu tun haben.

## **Feststellen, ob das Arbeitsblatt ein Dialogblatt ist**

Der folgende Beispielcode lädt die [Beispieldatei Excel](64716820.xlsx), die ein Dialogblatt enthält. Es überprüft die  [**Worksheet.Type**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/type)-Eigenschaft, vergleicht sie mit  [**SheetType.Dialog**](https://reference.aspose.com/cells/net/aspose.cells/sheettype) und druckt dann die Meldung. Bitte sehen Sie die Konsolenausgabe des untenstehenden Beispielcodes für mehr Hilfe.

## **Beispielcode**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-FindIfWorksheetIsDialogSheet.cs" >}}

## **Konsolenausgabe**

{{< highlight java >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
