---
title: Finden Sie heraus, ob das Arbeitsblatt ein Dialogblatt ist
type: docs
weight: 100
url: /de/java/find-if-the-worksheet-is-dialog-sheet/
---
## **Mögliche Nutzungsszenarien**

Dialogblatt ist ein altes Blattformat, das ein Dialogfeld enthält. Ein solches Blatt könnte von einer älteren Version von Microsoft Excel zB 2003 eingefügt werden, wie in diesem Screenshot gezeigt. In neueren Versionen zB Microsoft Excel 2016 kann es auch mit VBA eingefügt werden.

![todo: Bild_alt_Text](find-if-the-worksheet-is-dialog-sheet_1.png)

Sie können feststellen, ob das Blatt ein Dialogblatt oder ein anderer Blatttyp ist[**Arbeitsblatt.Typ**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Type)Eigenschaft, die von Aspose.Cells bereitgestellt wird. Wenn sie den Aufzählungswert zurückgibt[**SheetType.DIALOG**](https://reference.aspose.com/cells/java/com.aspose.cells/sheettype#DIALOG), dann handelt es sich um ein Dialogblatt.

## **Finden Sie heraus, ob das Arbeitsblatt ein Dialogblatt ist**

Der folgende Beispielcode lädt die[Beispiel-Excel-Datei](64716841.xlsx)die ein Dialogblatt enthält. Es prüft die[**Arbeitsblatt.Typ**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#Type)Eigenschaft vergleicht es mit[**SheetType.DIALOG**](https://reference.aspose.com/cells/java/com.aspose.cells/sheettype#DIALOG)und druckt dann die Nachricht. Weitere Hilfe finden Sie in der Konsolenausgabe des unten angegebenen Beispielcodes.

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Worksheets-FindIfWorksheetIsDialogSheet.java" >}}

## **Konsolenausgabe**

{{< highlight "java" >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
