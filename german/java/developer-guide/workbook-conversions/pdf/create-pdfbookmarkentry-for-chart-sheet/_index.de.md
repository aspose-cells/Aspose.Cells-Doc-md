---
title: PdfBookmarkEntry für Diagrammblatt erstellen
type: docs
weight: 50
url: /de/java/create-pdfbookmarkentry-for-chart-sheet/
---

## **Mögliche Verwendungsszenarien**

Früher würde Aspose.Cells für ein normales Blatt [**PdfBookmarkEntry**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfBookmarkEntry) erstellen. Aber jetzt kann Aspose.Cells auch [**PdfBookmarkEntry**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfBookmarkEntry) für Diagrammblätter erstellen. Da Diagrammblätter außer Zelle A1 keine anderen Zellen haben, wird es [**PdfBookmarkEntry**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfBookmarkEntry) nur für Zelle A1 erstellen.

## **Erstellen Sie PdfBookmarkEntry für Diagrammblatt**

Der folgende Beispielcode lädt die [Beispiel-Excel-Datei](61767772.xlsx), die vier Blätter hat. Zwei davon sind normale Blätter und die anderen beiden sind Diagrammblätter. Es erstellt vier Lesezeichen-Einträge wie folgt

- Lesezeichen-I
- Lesezeichen-II-Diagramm1
- Lesezeichen-III
- Lesezeichen-IV-Diagramm2

Der folgende Screenshot zeigt das [Ausgabe-PDF](61767771.pdf), das vom Beispielcode erstellt wurde.

![todo:image_alt_text](create-pdfbookmarkentry-for-chart-sheet_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Rendering-CreatePdfBookmarkEntryForChartSheet.java" >}}
{{< app/cells/assistant language="java" >}}
