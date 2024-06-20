---
title: Konvertieren Sie Excel Datei in das PDF Format, das mit PDFA 1a kompatibel ist
type: docs
weight: 80
url: /de/java/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/
---

## **Mögliche Verwendungsszenarien**

PDF/A ist eine einzigartige Variante von PDF, die für die langfristige Archivierung von Dokumenten konzipiert ist. PDF/A ist eine ISO-standardisierte Version des Portable Document Format (PDF), das eine archivarische Formatierung von PDF darstellt und alle im Dokument verwendeten Schriftarten in der PDF-Datei einbettet. PDF/A unterscheidet sich von PDF, indem es bestimmte Funktionen wie die Schriftartverknüpfung (im Gegensatz zur Schriftarteinbettung) und Verschlüsselung verbietet. Aspose.Cells ermöglicht es Ihnen, Excel-Dateien als PDF/A-konforme PDF-Dateien zu speichern (PDF/A-1a, PDF/A-1b, PDF/A-2a, PDF/A-2b, PDF/A-2u, PDF/A-3a, PDF/A-2ab und PDF/A-3u werden unterstützt). Dieses Thema beschreibt, wie Sie das Excel-Arbeitsbuch als PDF/A-konforme (PDF/A-1a) PDF-Datei speichern können.

## **Excel-Datei in das mit PDF/A-1a kompatible PDF-Format konvertieren**

Entwickler können die [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)-Klasse verwenden, um verschiedene Attribute für die Konvertierung festzulegen. Durch das Setzen verschiedener Eigenschaften der [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)-Klasse haben Sie die Kontrolle über die Druck-, Schrift-, Sicherheits- und Kompressionseinstellungen für die Ausgabedatei PDF. Die wichtigste Eigenschaft ist [PdfSaveOptions.Compliance**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#Compliance), mit der Sie Excel-Dateien in PDF/A-konforme PDF-Dateien speichern können.

Der folgende Beispielcode erläutert, wie man eine Excel-Datei in das mit PDF/A-1a kompatible PDF-Format konvertiert. Bitte sehen Sie sich die [Ausgabe-PDF](outputCompliancePdfA1a.pdf) sowie einen Screenshot zur Referenz an.

## **Screenshot**

![todo:image_alt_text](convert-excel-file-to-pdf-format-compatible-with-pdfa-1a_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-ConvertExcelFileToPDFA_1a.java" >}}
