---
title: PdfBookmarkEntry für Diagrammblatt erstellen
type: docs
weight: 50
url: /de/net/create-pdfbookmarkentry-for-chart-sheet/
---
## **Mögliche Nutzungsszenarien**

Früher würde Aspose.Cells anlegen[**PdfLesezeichenEintrag**](https://reference.aspose.com/cells/net/aspose.cells.rendering/pdfbookmarkentry) für ein normales Blatt. Aber jetzt kann Aspose.Cells auch anlegen[**PdfLesezeichenEintrag**](https://reference.aspose.com/cells/net/aspose.cells.rendering/pdfbookmarkentry) für Diagrammblatt. Da das Diagrammblatt keine andere Zelle außer Zelle A1 hat, wird es erstellt[**PdfLesezeichenEintrag**](https://reference.aspose.com/cells/net/aspose.cells.rendering/pdfbookmarkentry) nur für Zelle A1.

## **PdfBookmarkEntry für Diagrammblatt erstellen**

 Der folgende Beispielcode lädt die[Beispiel-Excel-Datei](61767756.xlsx) die vier Blätter hat. Zwei davon sind normale Blätter und die anderen zwei sind Diagrammblätter. Es erstellt vier Lesezeicheneinträge wie folgt

- Lesezeichen-I
- Lesezeichen-II-Chart1
- Lesezeichen-III
- Lesezeichen-IV-Chart2

Der folgende Screenshot zeigt die[PDF ausgeben](61767757.pdf) generiert durch den Beispielcode für eine Referenz.

![todo: Bild_alt_Text](create-pdfbookmarkentry-for-chart-sheet_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Rendering-CreatePdfBookmarkEntryForChartSheet.cs" >}}
