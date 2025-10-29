---
title: Comment convertir HTML en PDF avec JavaScript via C++
linktitle: Comment convertir du HTML en PDF
type: docs
weight: 80
url: /fr/javascript-cpp/convert-html-to-pdf/
description: Ce sujet explique comment convertir HTML en PDF et MHTML en PDF en utilisant Aspose.Cells for JavaScript via C++.
keywords: Conversion de HTML en PDF avec JavaScript via C++. 
---

## **Vue d'ensemble**
<b>Aspose.Cells</b> is a professional solution that allows you to generate PDF files from web pages and raw HTML code in your applications. 

This article explains how to <b>convertir du HTML en PDF</b>. It covers the following topics.

<ul>
<li><a href="#js-convert-html-to-pdf">JavaScript HTML vers PDF</a></li>
<li><a href="#js-convert-html-to-pdf">JavaScript Convertir HTML en PDF</a></li>
<li><a href="#js-convert-html-to-pdf">JavaScript Comment convertir HTML en PDF</a></li>
</ul>

## **Conversion HTML en PDF en JavaScript**
Comment convertir HTML en PDF ? Avec la bibliothèque [Aspose.Cells for JavaScript via C++](https://releases.aspose.com/cells/javascript-cpp/), vous pouvez facilement convertir HTML en PDF de manière programmatique en quelques lignes de code. Aspose.Cells for JavaScript via C++ est capable de créer des applications multiplateformes avec la capacité de générer, modifier, convertir, rendre et imprimer tous les fichiers Excel.

## **JavaScript Convertir HTML en PDF**
L'exemple de code JavaScript suivant montre comment convertir un document HTML en PDF en utilisant [Aspose.Cells for JavaScript via C++](https://releases.aspose.com/cells/javascript-cpp/).

1. Créez une instance de la classe [HtmlLoadOptions](https://reference.aspose.com/cells/javascript-cpp/htmlloadoptions/).
1. Initialiser l'objet [Workbook](https://reference.aspose.com/cells/javascript-cpp/workbook/) .
1. Enregistrer le document PDF de sortie en appelant la méthode Workbook.save().

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

## **Essayez de convertir du HTML en PDF en ligne**

[Aspose.Cells for JavaScript via C++](https://releases.aspose.com/cells/javascript-cpp/) presents you online free application <a href="https://products.aspose.app/cells/en/conversion/html-to-pdf">“HTML en PDF”</a>, where you may try to investigate the functionality and quality it works.
<br>
<a href="https://products.aspose.app/cells/en/conversion/html-to-pdf"><img src="htmltopdf.png" width=80%></a>
