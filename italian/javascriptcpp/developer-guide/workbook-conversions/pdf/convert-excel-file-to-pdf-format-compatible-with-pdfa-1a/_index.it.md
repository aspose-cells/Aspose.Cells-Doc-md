---
title: Convertire il file Excel in formato PDF compatibile con PDF/A 1a usando JavaScript via C++
linktitle: Converti file Excel in formato PDF compatibile con PDF/A 1a
type: docs
weight: 130
url: /it/javascript-cpp/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/
description: Scopri come convertire i file Excel in PDF compatibili con PDF/A usando Aspose.Cells for JavaScript via C++.
---

## **Possibili Scenari di Utilizzo**  

 PDF/A è una variante unica di PDF progettata per la conservazione a lungo termine dei documenti. PDF/A è una versione standardizzata ISO del formato di documento portatile (PDF), che è un formato di archiviazione di PDF che incorpora tutti i font usati nel documento all’interno del file PDF. PDF/A si differenzia da PDF proibendo funzionalità come il collegamento di font (a favore dell’incorporamento dei font) e la crittografia. Aspose.Cells for JavaScript via C++ consente di salvare i file Excel in PDF conformi a PDF/A (PDF/A-1a, PDF/A-1b, PDF/A-2a, PDF/A-2b, PDF/A-2u, PDF/A-3a, PDF/A-2ab e PDF/A-3u sono supportati). Questo argomento descrive come salvare il workbook Excel in un file PDF conforme a PDF/A (PDF/A-1a).  

## **Convertire file Excel nel formato PDF compatibile con PDF/A-1a**  

Gli sviluppatori possono usare la classe [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions) per impostare attributi diversi per la conversione. Impostare proprietà diverse della classe [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions) ti dà il controllo su impostazioni di stampa, font, sicurezza e compressione per il PDF di output. La proprietà più importante è [**PdfSaveOptions.compliance**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#compliance--) che permette di salvare i file Excel come file PDF conformi a PDF/A.  

Il codice di esempio seguente spiega come convertire un file Excel in formato PDF compatibile con PDF/A-1a. Per favore, consulta il [PDF di output](outputCompliancePdfA1a.pdf) e lo screenshot come riferimento.  

## **Screenshot**  

![todo:image_alt_text](convert-excel-file-to-pdf-format-compatible-with-pdfa-1a_1.png)  

## **Codice di Esempio**  

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
