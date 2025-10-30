---
title: Come Convertire HTML in PDF con JavaScript tramite C++
linktitle: Come convertire HTML in PDF
type: docs
weight: 80
url: /it/javascript-cpp/convert-html-to-pdf/
description: Questo argomento mostra come convertire HTML in PDF e MHTML in PDF usando Aspose.Cells for JavaScript tramite C++.
keywords: Converti HTML in PDF e MHTML in PDF con JavaScript tramite C++. 
---

## **Panoramica**
<b>Aspose.Cells</b> is a professional solution that allows you to generate PDF files from web pages and raw HTML code in your applications. 

This article explains how to <b>converti HTML in PDF</b>. It covers the following topics.

<ul>
<li><a href="#js-convert-html-to-pdf">JavaScript HTML in PDF</a></li>
<li><a href="#js-convert-html-to-pdf">JavaScript Converti HTML in PDF</a></li>
<li><a href="#js-convert-html-to-pdf">JavaScript Come convertire HTML in PDF</a></li>
</ul>

## **Conversione da HTML a PDF in JavaScript**
Come convertire HTML in PDF? Con la libreria [Aspose.Cells for JavaScript tramite C++](https://releases.aspose.com/cells/javascript-cpp/), puoi facilmente convertire HTML in PDF programmaticamente con poche righe di codice. Aspose.Cells for JavaScript tramite C++ è in grado di creare applicazioni multipiattaforma con la capacità di generare, modificare, convertire, renderizzare e stampare tutti i file Excel.

## **JavaScript Converti HTML in PDF**
Il seguente esempio di codice JavaScript mostra come convertire un documento HTML in PDF utilizzando [Aspose.Cells for JavaScript tramite C++](https://releases.aspose.com/cells/javascript-cpp/).

1. Crea un'istanza della classe [HtmlLoadOptions](https://reference.aspose.com/cells/javascript-cpp/htmlloadoptions/).
1. Inizializza l'oggetto [Workbook](https://reference.aspose.com/cells/javascript-cpp/workbook/).
1. Salvare il documento PDF di output chiamando il metodo Workbook.save().

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells HTML to PDF Example</title>
    </head>
    <body>
        <h1>Convert HTML to PDF using Aspose.Cells</h1>
        <input type="file" id="fileInput" accept=".html,.htm" />
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
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an HTML file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Loads the workbook which contains hidden external links
            const options = new AsposeCells.HtmlLoadOptions(AsposeCells.LoadFormat.Html);
            const workbook = new Workbook(new Uint8Array(arrayBuffer), options);

            // Save as PDF
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **Prova a convertire HTML in PDF online**

[Aspose.Cells for JavaScript via C++](https://releases.aspose.com/cells/javascript-cpp/) presents you online free application <a href="https://products.aspose.app/cells/en/conversion/html-to-pdf">“HTML to PDF”</a>, where you may try to investigate the functionality and quality it works.
<br>
<a href="https://products.aspose.app/cells/en/conversion/html-to-pdf"><img src="htmltopdf.png" width=80%></a>
