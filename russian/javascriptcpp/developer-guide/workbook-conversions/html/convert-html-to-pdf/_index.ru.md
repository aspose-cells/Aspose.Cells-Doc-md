---
title: Как преобразовать HTML в PDF с помощью JavaScript через C++
linktitle: Как конвертировать HTML в PDF
type: docs
weight: 80
url: /ru/javascript-cpp/convert-html-to-pdf/
description: Этот раздел показывает, как преобразовать HTML в PDF и MHTML в PDF с помощью Aspose.Cells for JavaScript через C++.
keywords: Преобразование HTML в PDF и MHTML в PDF с помощью JavaScript через C++. 
---

## **Обзор**
<b>Aspose.Cells</b> is a professional solution that allows you to generate PDF files from web pages and raw HTML code in your applications. 

This article explains how to <b>конвертировать HTML в PDF</b>. It covers the following topics.

<ul>
<li><a href="#js-convert-html-to-pdf">JavaScript HTML в PDF</a></li>
<li><a href="#js-convert-html-to-pdf">JavaScript Конвертация HTML в PDF</a></li>
<li><a href="#js-convert-html-to-pdf">JavaScript Как конвертировать HTML в PDF</a></li>
</ul>

## **Преобразование HTML в PDF на JavaScript**
Как преобразовать HTML в PDF? С помощью библиотеки [Aspose.Cells for JavaScript через C++](https://releases.aspose.com/cells/javascript-cpp/) вы можете легко преобразовывать HTML в PDF программным способом за несколько строк кода. Aspose.Cells for JavaScript через C++ способен создавать кроссплатформенные приложения с возможностью генерации, изменения, преобразования, рендеринга и печати всех файлов Excel.

## **JavaScript Конвертация HTML в PDF**
Следующий пример кода JavaScript показывает, как преобразовать HTML-документ в PDF с помощью [Aspose.Cells for JavaScript через C++](https://releases.aspose.com/cells/javascript-cpp/).

1. Создайте экземпляр класса [HtmlLoadOptions](https://reference.aspose.com/cells/javascript-cpp/htmlloadoptions/).
1. Инициализация объекта [Workbook](https://reference.aspose.com/cells/javascript-cpp/workbook/).
1. Сохранить выходной PDF-документ, вызвав метод Workbook.save().

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

## **Попробуйте конвертировать HTML в PDF онлайн**

[Aspose.Cells for JavaScript via C++](https://releases.aspose.com/cells/javascript-cpp/) presents you online free application <a href="https://products.aspose.app/cells/en/conversion/html-to-pdf">«HTML в PDF»</a>, where you may try to investigate the functionality and quality it works.
<br>
<a href="https://products.aspose.app/cells/en/conversion/html-to-pdf"><img src="htmltopdf.png" width=80%></a>
