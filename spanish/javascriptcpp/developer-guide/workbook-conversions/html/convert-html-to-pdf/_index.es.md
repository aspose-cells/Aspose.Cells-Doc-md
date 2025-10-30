---
title: Cómo convertir HTML a PDF con JavaScript vía C++
linktitle: Cómo convertir HTML a PDF
type: docs
weight: 80
url: /es/javascript-cpp/convert-html-to-pdf/
description: Este tema te muestra cómo convertir HTML a PDF y MHTML a PDF usando Aspose.Cells for JavaScript vía C++.
keywords: Convertir HTML a PDF y MHTML a PDF con JavaScript vía C++. 
---

## **Visión general**
<b>Aspose.Cells</b> is a professional solution that allows you to generate PDF files from web pages and raw HTML code in your applications. 

This article explains how to <b>convertir HTML a PDF</b>. It covers the following topics.

<ul>
<li><a href="#js-convert-html-to-pdf">HTML JavaScript a PDF</a></li>
<li><a href="#js-convert-html-to-pdf">JavaScript Convierte HTML a PDF</a></li>
<li><a href="#js-convert-html-to-pdf">JavaScript Cómo convertir HTML a PDF</a></li>
</ul>

## **Conversión de HTML a PDF en JavaScript**
¿Cómo convertir HTML a PDF? Con la biblioteca [Aspose.Cells for JavaScript vía C++](https://releases.aspose.com/cells/javascript-cpp/), puedes convertir fácilmente HTML a PDF programáticamente con unas pocas líneas de código. Aspose.Cells for JavaScript vía C++ es capaz de construir aplicaciones multiplataforma con la capacidad de generar, modificar, convertir, renderizar e imprimir todos los archivos de Excel.

## **JavaScript Convierte HTML a PDF**
El siguiente ejemplo de código en JavaScript muestra cómo convertir un documento HTML a PDF usando [Aspose.Cells for JavaScript vía C++](https://releases.aspose.com/cells/javascript-cpp/).

1. Crear una instancia de la clase [HtmlLoadOptions](https://reference.aspose.com/cells/javascript-cpp/htmlloadoptions/).
1. Inicializar objeto [Workbook](https://reference.aspose.com/cells/javascript-cpp/workbook/).
1. Guarde el documento PDF de salida llamando al método Workbook.save().

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

## **Intenta convertir HTML a PDF en línea**

[Aspose.Cells for JavaScript via C++](https://releases.aspose.com/cells/javascript-cpp/) presents you online free application <a href="https://products.aspose.app/cells/en/conversion/html-to-pdf">“HTML a PDF”</a>, where you may try to investigate the functionality and quality it works.
<br>
<a href="https://products.aspose.app/cells/en/conversion/html-to-pdf"><img src="htmltopdf.png" width=80%></a>
