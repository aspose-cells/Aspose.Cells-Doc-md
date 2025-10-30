---
title: Excel Datei in PDF Format konvertieren, das mit PDF/A 1a kompatibel ist, mit JavaScript via C++
linktitle: Excel Datei in ein PDF Format konvertieren, das mit PDF/A 1a kompatibel ist
type: docs
weight: 130
url: /de/javascript-cpp/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/
description: Lernen Sie, wie man Excel Dateien in PDF/A konforme PDF Dateien mit Aspose.Cells for JavaScript via C++ konvertiert.
---

## **Mögliche Verwendungsszenarien**  

PDF/A ist eine einzigartige Version des PDFs, die für die langfristige Archivierung von Dokumenten entwickelt wurde. PDF/A ist eine vom ISO standardisierte Version des Portable Document Format (PDF), das alle im Dokument verwendeten Schriftarten in die PDF-Datei eingebettet. PDF/A unterscheidet sich von PDF durch das Verbot von Funktionen wie Schriftartenverknüpfung (im Gegensatz zum Schriftarten-Einbetten) und Verschlüsselung. Aspose.Cells for JavaScript via C++ ermöglicht das Speichern der Excel-Dateien in PDF/A-konforme PDF-Dateien (PDF/A-1a, PDF/A-1b, PDF/A-2a, PDF/A-2b, PDF/A-2u, PDF/A-3a, PDF/A-2ab und PDF/A-3u werden unterstützt). Dieser Abschnitt beschreibt, wie das Excel-Arbeitsbuch in eine PDF/A-konforme PDF-Datei gespeichert wird.  

## **Excel-Datei in das mit PDF/A-1a kompatible PDF-Format konvertieren**  

Entwickler können die Klasse [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions) verwenden, um verschiedene Attribute für die Konvertierung festzulegen. Das Ändern verschiedener Eigenschaften der Klasse [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions) ermöglicht die Kontrolle über die Druck-, Schriftarten-, Sicherheits- und Komprimierungseinstellungen für das Ausgabepdf. Die wichtigste Eigenschaft ist [**PdfSaveOptions.compliance**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#compliance--), die das Speichern von Excel-Dateien als PDF/A-konforme PDFs ermöglicht.  

Der folgende Beispielcode erklärt, wie eine Excel-Datei in das PDF-Format konvertiert wird, das mit PDF/A-1a kompatibel ist. Sehen Sie sich das [Ausgabepdf](outputCompliancePdfA1a.pdf) sowie den Screenshot zur Referenz an.  

## **Screenshot**  

![todo:image_alt_text](convert-excel-file-to-pdf-format-compatible-with-pdfa-1a_1.png)  

## **Beispielcode**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Export to PDF (PDFA-1a) Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            // Create workbook object
            const wb = new Workbook();

            // Access first worksheet
            const ws = wb.worksheets.get(0);

            // Access cell B5 and add some message inside it
            const cell = ws.cells.get("B5");
            cell.value = "This PDF format is compatible with PDFA-1a.";

            // Create pdf save options and set its compliance to PDFA-1a
            const opts = new AsposeCells.PdfSaveOptions();
            opts.compliance = AsposeCells.PdfCompliance.PdfA1a;

            // Save the output pdf
            const outputData = wb.save(SaveFormat.Pdf, opts);
            const blob = new Blob([outputData], { type: "application/pdf" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputCompliancePdfA1a.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
