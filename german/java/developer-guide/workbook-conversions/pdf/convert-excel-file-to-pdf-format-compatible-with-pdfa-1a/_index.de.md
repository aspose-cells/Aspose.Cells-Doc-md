---
title: Konvertieren Sie Excel-Dateien in das mit PDFA-1a kompatible PDF-Format
type: docs
weight: 80
url: /de/java/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/
---
## **Mögliche Nutzungsszenarien**

PDF/A ist eine einzigartige Variante von PDF, die für die langfristige Aufbewahrung von Dokumenten entwickelt wurde. PDF/A ist eine ISO-standardisierte Version des Portable Document Format (PDF), einem Archivierungsformat von PDF, das alle im Dokument verwendeten Schriftarten in die PDF-Datei einbettet. PDF/A unterscheidet sich von PDF durch das Verbot von Funktionen wie Schriftartverknüpfung (im Gegensatz zur Schriftarteinbettung) und Verschlüsselung. Aspose.Cells ermöglicht es Ihnen, die Excel-Dateien in PDF/A-kompatible PDF-Dateien zu speichern (sowohl PdfA1a als auch PdfA1b werden unterstützt). In diesem Thema wird beschrieben, wie Sie die Excel-Arbeitsmappe in einer PDF/A-kompatiblen (PdfA1a) PDF-Datei speichern.

## **Konvertieren Sie Excel-Dateien in das mit PDFA-1a kompatible PDF-Format**

Entwickler können die verwenden**[PdfSaveOptions](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)**-Klasse, um verschiedene Attribute für die Konvertierung festzulegen. Festlegen verschiedener Eigenschaften der**[PdfSaveOptions](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)**Klasse gibt Ihnen die Kontrolle über die Druck-, Schriftart-, Sicherheits- und Komprimierungseinstellungen für die Ausgabe-PDF. Die wichtigste Eigenschaft ist**[PdfSaveOptions.Compliance](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#Compliance)**mit dem Sie die Excel-Dateien in PDF/A-kompatible PDF-Dateien speichern können.

 Der folgende Beispielcode erläutert, wie Sie eine Excel-Datei in ein mit PDFA-1a kompatibles PDF-Format konvertieren. Bitte sehen Sie es sich an[PDF ausgeben](outputCompliancePdfA1a.pdf) sowie ein Screenshot als Referenz.

## **Bildschirmfoto**

![todo: Bild_alt_Text](convert-excel-file-to-pdf-format-compatible-with-pdfa-1a_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertExcelFileToPDFA_1a.java" >}}
