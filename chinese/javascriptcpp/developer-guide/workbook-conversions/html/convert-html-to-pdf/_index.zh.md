---
title: 如何使用JavaScript通过C++将HTML转换为PDF
linktitle: 如何将 HTML 转换为 PDF
type: docs
weight: 80
url: /zh/javascript-cpp/convert-html-to-pdf/
description: 本主题演示如何使用Aspose.Cells for JavaScript通过C++将HTML转换为PDF和将MHTML转换为PDF。
keywords: 通过C++将JavaScript转换为HTML到PDF和MHTML到PDF。 
---

## **概述**
<b>Aspose.Cells</b> is a professional solution that allows you to generate PDF files from web pages and raw HTML code in your applications. 

This article explains how to <b>将 HTML 转换为 PDF</b>. It covers the following topics.

<ul>
<li><a href="#js-convert-html-to-pdf">JavaScript HTML转PDF</a></li>
<li><a href="#js-convert-html-to-pdf">JavaScript 转换 HTML 为 PDF</a></li>
<li><a href="#js-convert-html-to-pdf">JavaScript 如何将 HTML 转换为 PDF</a></li>
</ul>

## **JavaScript中的HTML到PDF转换**
如何转换HTML为PDF？借助[Aspose.Cells for JavaScript via C++](https://releases.aspose.com/cells/javascript-cpp/)库，您可以轻松地通过几行代码以编程方式将HTML转换为PDF。Aspose.Cells for JavaScript via C++能够构建跨平台应用，具备生成、修改、转换、渲染和打印所有Excel文件的能力。

## **JavaScript 转换 HTML 为 PDF**
以下JavaScript示例展示如何使用[Aspose.Cells for JavaScript via C++](https://releases.aspose.com/cells/javascript-cpp/)将HTML文档转换为PDF。

1. 创建一个[HtmlLoadOptions](https://reference.aspose.com/cells/javascript-cpp/htmlloadoptions/)类的实例。
1. 初始化[Workbook](https://reference.aspose.com/cells/javascript-cpp/workbook/)对象。
1. 通过调用Workbook.save()方法保存输出PDF文档。

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

## **尝试在线将HTML转换为PDF**

[Aspose.Cells for JavaScript via C++](https://releases.aspose.com/cells/javascript-cpp/) presents you online free application <a href="https://products.aspose.app/cells/en/conversion/html-to-pdf">“HTML转PDF”</a>, where you may try to investigate the functionality and quality it works.
<br>
<a href="https://products.aspose.app/cells/en/conversion/html-to-pdf"><img src="htmltopdf.png" width=80%></a>
