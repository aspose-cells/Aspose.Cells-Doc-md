---
title: So konvertieren Sie HTML mit JavaScript über C++ in PDF
linktitle: Wie konvertiere ich HTML in PDF
type: docs
weight: 80
url: /de/javascript-cpp/convert-html-to-pdf/
description: Dieses Thema zeigt Ihnen, wie Sie HTML in PDF und MHTML in PDF mit Aspose.Cells for JavaScript via C++ konvertieren.
keywords: JavaScript wandelt HTML in PDF und MHTML in PDF über C++ um. 
---

## **Übersicht**
<b>Aspose.Cells</b> is a professional solution that allows you to generate PDF files from web pages and raw HTML code in your applications. 

This article explains how to <b>konvertieren Sie HTML in das PDF-Saveformat</b>. It covers the following topics.

<ul>
<li><a href="#js-convert-html-to-pdf">JavaScript HTML zu PDF</a></li>
<li><a href="#js-convert-html-to-pdf">JavaScript HTML in PDF konvertieren</a></li>
<li><a href="#js-convert-html-to-pdf">JavaScript Wie konvertiert man HTML in PDF</a></li>
</ul>

## **HTML zu PDF-Konvertierung in JavaScript**
Wie konvertiert man HTML in PDF? Mit der [Aspose.Cells for JavaScript via C++](https://releases.aspose.com/cells/javascript-cpp/) Bibliothek können Sie HTML einfach programmatisch in PDF umwandeln, mit nur wenigen Codezeilen. Aspose.Cells for JavaScript via C++ ist in der Lage, plattformübergreifende Anwendungen zu erstellen, die alle Excel-Dateien generieren, modifizieren, konvertieren, rendern und drucken können.

## **JavaScript HTML in PDF konvertieren**
Das folgende JavaScript-Codebeispiel zeigt, wie man ein HTML-Dokument mit [Aspose.Cells for JavaScript via C++](https://releases.aspose.com/cells/javascript-cpp/) in PDF umwandelt.

1. Erstellen Sie eine Instanz der Klasse [HtmlLoadOptions](https://reference.aspose.com/cells/javascript-cpp/htmlloadoptions/).
1. Initialisieren Sie das [Workbook](https://reference.aspose.com/cells/javascript-cpp/workbook/) Objekt.
1. Speichern Sie das Ausgabedokument als PDF, indem Sie die Methode Workbook.save() aufrufen.

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

## **Versuchen Sie, HTML online in PDF zu konvertieren**

[Aspose.Cells for JavaScript via C++](https://releases.aspose.com/cells/javascript-cpp/) presents you online free application <a href="https://products.aspose.app/cells/en/conversion/html-to-pdf">„HTML in PDF“</a>, where you may try to investigate the functionality and quality it works.
<br>
<a href="https://products.aspose.app/cells/en/conversion/html-to-pdf"><img src="htmltopdf.png" width=80%></a>
