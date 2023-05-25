---
title: Finden Sie heraus, ob es sich bei dem Arbeitsblatt um ein Dialogblatt handelt
type: docs
weight: 90
url: /de/net/find-if-the-worksheet-is-dialog-sheet/
description: Dialog Sheet ist ein altes Blattformat. Dieser Artikel enthält Anweisungen und Beispielcode zum programmgesteuerten Bestimmen, ob ein Excel-Arbeitsblatt ein Dialogblatt ist, mithilfe der Bibliothek C#, API oder .NET.
keywords: find excel worksheet dialog type c#, worksheet dialog c#
---
##  **Mögliche Nutzungsszenarien**

Dialogblatt ist ein altes Blattformat, das ein Dialogfeld enthält. Ein solches Blatt könnte mit einer älteren Version von Microsoft Excel, z. B. 2003, eingefügt werden, wie in diesem Screenshot gezeigt. Es kann auch mit VBA in neuere Versionen eingefügt werden, z. B. Microsoft Excel 2016.

![todo:image_alt_text](find-if-the-worksheet-is-dialog-sheet_1.png)

Sie können herausfinden, ob es sich bei dem Blatt um ein Dialogblatt oder einen anderen Blatttyp handelt[**Arbeitsblatt.Typ**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/type)Eigenschaft, die von Aspose.Cells bereitgestellt wird. Wenn sie einen Aufzählungswert zurückgibt[**SheetType.Dialog**](https://reference.aspose.com/cells/net/aspose.cells/sheettype), dann bedeutet es, dass Sie es mit einem Dialogblatt zu tun haben.

##  **Finden Sie heraus, ob es sich bei dem Arbeitsblatt um ein Dialogblatt handelt**

 Der folgende Beispielcode lädt die[Beispiel-Excel-Datei](64716820.xlsx) das ein Dialogblatt enthält. Es überprüft die[**Arbeitsblatt.Typ**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/type)Eigenschaft vergleicht es mit[**SheetType.Dialog**](https://reference.aspose.com/cells/net/aspose.cells/sheettype) und druckt dann die Nachricht. Weitere Hilfe finden Sie in der Konsolenausgabe des unten angegebenen Beispielcodes.

##  **Beispielcode**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-FindIfWorksheetIsDialogSheet.cs" >}}

##  **Konsolenausgabe**

{{< highlight "java" >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
