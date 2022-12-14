---
title: Finden Sie heraus, ob das Arbeitsblatt ein Dialogblatt ist
type: docs
weight: 90
url: /de/net/find-if-the-worksheet-is-dialog-sheet/
---
## **Mögliche Nutzungsszenarien**

Dialogblatt ist ein altes Blattformat, das ein Dialogfeld enthält. Ein solches Blatt könnte von einer älteren Version von Microsoft Excel zB 2003 eingefügt werden, wie in diesem Screenshot gezeigt. In neueren Versionen zB Microsoft Excel 2016 kann es auch mit VBA eingefügt werden.

![todo: Bild_alt_Text](find-if-the-worksheet-is-dialog-sheet_1.png)

Sie können feststellen, ob das Blatt ein Dialogblatt oder ein anderer Blatttyp ist[**Arbeitsblatt.Typ**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/type)Eigenschaft, die von Aspose.Cells bereitgestellt wird. Wenn sie den Aufzählungswert zurückgibt[**SheetType.Dialog**](https://reference.aspose.com/cells/net/aspose.cells/sheettype), dann bedeutet es, dass Sie es mit einem Dialogblatt zu tun haben.

## **Finden Sie heraus, ob das Arbeitsblatt ein Dialogblatt ist**

 Der folgende Beispielcode lädt die[Beispiel-Excel-Datei](64716820.xlsx) die ein Dialogblatt enthält. Es prüft die[**Arbeitsblatt.Typ**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/type)Eigenschaft vergleicht es mit[**SheetType.Dialog**](https://reference.aspose.com/cells/net/aspose.cells/sheettype) und druckt dann die Nachricht. Weitere Hilfe finden Sie in der Konsolenausgabe des unten angegebenen Beispielcodes.

## **Beispielcode**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-FindIfWorksheetIsDialogSheet.cs" >}}

## **Konsolenausgabe**

{{< highlight "java" >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
