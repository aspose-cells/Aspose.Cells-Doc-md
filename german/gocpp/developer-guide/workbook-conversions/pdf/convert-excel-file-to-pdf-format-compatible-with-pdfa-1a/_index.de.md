---
title: Excel Datei in PDF Format konvertieren, das mit PDFA 1a kompatibel ist, mit Golang über C++
linktitle: Konvertieren Sie Excel Datei in das PDF Format, das mit PDFA 1a kompatibel ist
type: docs
weight: 130
url: /de/go-cpp/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/
description: Lernen Sie, wie man Excel Dateien in ein PDF/A 1a konformes PDF Format mit Aspose.Cells unter Golang via C++ konvertiert.
---

## **Mögliche Verwendungsszenarien**

PDF/A ist eine spezielle Version des PDF, die für die langfristige Archivierung von Dokumenten entwickelt wurde. PDF/A ist eine ISO-standardisierte Version des Portable Document Format (PDF), die alle in einem Dokument verwendeten Schriftarten innerhalb der PDF-Datei embeddingiert. PDF/A unterscheidet sich von PDF durch das Verbot von Funktionen wie Schriftartenverlinkung (im Gegensatz zum Schriftart-Embedding) und Verschlüsselung. Aspose.Cells ermöglicht das Speichern von Excel-Dateien in PDF/A-konforme PDF-Dateien (PDF/A-1a, PDF/A-1b, PDF/A-2a, PDF/A-2b, PDF/A-2u, PDF/A-3a, PDF/A-2ab und PDF/A-3u werden unterstützt). Dieses Thema beschreibt, wie man die Excel-Arbeitsmappe in eine PDF/A-konforme (PDF/A-1a) PDF-Datei speichert.

## **Excel-Datei in das mit PDF/A-1a kompatible PDF-Format konvertieren**

Entwickler können die Klasse [**PdfSaveOptions**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/) verwenden, um verschiedene Attribute für die Konvertierung festzulegen. Das Ändern verschiedener Eigenschaften der Klasse [**PdfSaveOptions**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/) ermöglicht die Kontrolle über die Druck-, Schriftarten-, Sicherheits- und Komprimierungseinstellungen für das Ausgabepdf. Die wichtigste Eigenschaft ist [**PdfSaveOptions.GetCompliance()**](https://reference.aspose.com/cells/go-cpp/pdfsaveoptions/getcompliance/), die das Speichern von Excel-Dateien als PDF/A-konforme PDFs ermöglicht.

Der folgende Beispielcode erläutert, wie man eine Excel-Datei in das mit PDF/A-1a kompatible PDF-Format konvertiert. Bitte sehen Sie sich die [Ausgabe-PDF](outputCompliancePdfA1a.pdf) sowie den Screenshot zur Referenz an.

## **Screenshot**

![todo:image_alt_text](convert-excel-file-to-pdf-format-compatible-with-pdfa-1a_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertExcelFileToPdfFormatCompatibleWithPdfa1a.go" >}}
