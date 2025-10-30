---  
title: Excel Datei in ein PDF Format konvertieren, das mit PDF/A 1a kompatibel ist, mit Node.js via C++  
linktitle: Excel Datei in ein PDF Format konvertieren, das mit PDF/A 1a kompatibel ist  
type: docs  
weight: 130  
url: /de/nodejs-cpp/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/  
description: Lernen Sie, wie Sie Excel Dateien in PDF/A konforme PDF Dateien mit Aspose.Cells for Node.js via C++ umwandeln.  
---  

## **Mögliche Verwendungsszenarien**  

PDF/A ist eine spezielle Variante des PDF, die für die Langzeiterhaltung von Dokumenten entwickelt wurde. PDF/A ist eine ISO-standardisierte Version des Portable Document Format (PDF), die ein Archivformat ist und alle in dem Dokument verwendeten Schriftarten im PDF-Datei integriert. PDF/A unterscheidet sich von PDF durch das Verbot bestimmter Funktionen wie Schriftartverlinkung (im Gegensatz zum Einbetten der Schriftart) und Verschlüsselung. Aspose.Cells for Node.js via C++ ermöglicht das Speichern von Excel-Dateien als PDF/A-konforme PDFs (PDF/A-1a, PDF/A-1b, PDF/A-2a, PDF/A-2b, PDF/A-2u, PDF/A-3a, PDF/A-2ab und PDF/A-3u werden unterstützt). Dieses Thema beschreibt, wie man die Arbeitsmappe in eine PDF/A-konforme PDF-Datei (PDF/A-1a) speichert.  

## **Excel-Datei in das mit PDF/A-1a kompatible PDF-Format konvertieren**  

Entwickler können die Klasse [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions) verwenden, um verschiedene Attribute für die Konvertierung festzulegen. Das Ändern verschiedener Eigenschaften der Klasse [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions) ermöglicht die Kontrolle über die Druck-, Schriftarten-, Sicherheits- und Komprimierungseinstellungen für das Ausgabepdf. Die wichtigste Eigenschaft ist [**PdfSaveOptions.getCompliance()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getCompliance--), die das Speichern von Excel-Dateien als PDF/A-konforme PDFs ermöglicht.  

Der folgende Beispielcode erklärt, wie eine Excel-Datei in das PDF-Format konvertiert wird, das mit PDF/A-1a kompatibel ist. Sehen Sie sich das [Ausgabepdf](outputCompliancePdfA1a.pdf) sowie den Screenshot zur Referenz an.  

## **Screenshot**  

![todo:image_alt_text](convert-excel-file-to-pdf-format-compatible-with-pdfa-1a_1.png)  

## **Beispielcode**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Create workbook object
const wb = new AsposeCells.Workbook();

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Access cell B5 and add some message inside it
const cell = ws.getCells().get("B5");
cell.putValue("This PDF format is compatible with PDFA-1a.");

// Create pdf save options and set its compliance to PDFA-1a
const opts = new AsposeCells.PdfSaveOptions();
opts.setCompliance(AsposeCells.PdfCompliance.PdfA1a);

// Save the output pdf
wb.save(path.join(outputDir, "outputCompliancePdfA1a.pdf"), opts);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
