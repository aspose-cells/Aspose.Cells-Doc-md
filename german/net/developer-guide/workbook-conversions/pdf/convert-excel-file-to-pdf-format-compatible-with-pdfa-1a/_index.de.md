---
title: Konvertieren Sie Excel Datei in das PDF Format, das mit PDFA 1a kompatibel ist
type: docs
weight: 130
url: /de/net/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/
---

## **Mögliche Verwendungsszenarien**

PDF/A ist eine einzigartige Variante von PDF, die für die langfristige Archivierung von Dokumenten konzipiert ist. PDF/A ist eine ISO-standardisierte Version des Portable Document Format (PDF), das eine archivarische Formatierung von PDF darstellt und alle im Dokument verwendeten Schriftarten in der PDF-Datei einbettet. PDF/A unterscheidet sich von PDF, indem es bestimmte Funktionen wie die Schriftartverknüpfung (im Gegensatz zur Schriftarteinbettung) und Verschlüsselung verbietet. Aspose.Cells ermöglicht es Ihnen, Excel-Dateien als PDF/A-konforme PDF-Dateien zu speichern (PDF/A-1a, PDF/A-1b, PDF/A-2a, PDF/A-2b, PDF/A-2u, PDF/A-3a, PDF/A-2ab und PDF/A-3u werden unterstützt). Dieses Thema beschreibt, wie Sie das Excel-Arbeitsbuch als PDF/A-konforme (PDF/A-1a) PDF-Datei speichern können.

## **Excel-Datei in das mit PDF/A-1a kompatible PDF-Format konvertieren**

Entwickler können die [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)-Klasse verwenden, um verschiedene Attribute für die Konvertierung festzulegen. Durch das Festlegen verschiedener Eigenschaften der [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)-Klasse haben Sie Kontrolle über die Druck-, Schrift-, Sicherheits- und Kompressionseinstellungen für die Ausgabe-PDF. Die wichtigste Eigenschaft ist [**PdfSaveOptions.Compliance**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/compliance), die es Ihnen ermöglicht, die Excel-Dateien in PDF/A-konforme PDF-Dateien zu speichern.

Der folgende Beispielcode erläutert, wie man eine Excel-Datei in das mit PDF/A-1a kompatible PDF-Format konvertiert. Bitte sehen Sie sich die [Ausgabe-PDF](outputCompliancePdfA1a.pdf) sowie den Screenshot zur Referenz an.

## **Screenshot**

![todo:image_alt_text](convert-excel-file-to-pdf-format-compatible-with-pdfa-1a_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-ConvertExcelFileToPDFA_1a.cs" >}}
{{< app/cells/assistant language="csharp" >}}
