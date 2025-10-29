---
title: كيفية تحويل HTML إلى PDF باستخدام JavaScript عبر C++
linktitle: كيفية تحويل HTML إلى PDF
type: docs
weight: 80
url: /ar/javascript-cpp/convert-html-to-pdf/
description: يعرض لك هذا الموضوع كيفية تحويل HTML إلى PDF وMHTML إلى PDF باستخدام Aspose.Cells for JavaScript عبر C++.
keywords: JavaScript يحول HTML إلى PDF وMHTML إلى PDF عبر C++. 
---

## **نظرة عامة**
<b>Aspose.Cells</b> is a professional solution that allows you to generate PDF files from web pages and raw HTML code in your applications. 

This article explains how to <b>تحويل HTML إلى PDF</b>. It covers the following topics.

<ul>
<li><a href="#js-convert-html-to-pdf">HTML إلى PDF باستخدام جافا سكريبت</a></li>
<li><a href="#js-convert-html-to-pdf">تحويل HTML إلى PDF باستخدام جافا سكريبت</a></li>
<li><a href="#js-convert-html-to-pdf">كيفية تحويل HTML إلى PDF باستخدام جافا سكريبت</a></li>
</ul>

## **تحويل HTML إلى PDF في JavaScript**
كيفية تحويل HTML إلى PDF؟ مع مكتبة [Aspose.Cells for JavaScript عبر C++](https://releases.aspose.com/cells/javascript-cpp/) يمكنك بسهولة تحويل HTML إلى PDF برمجيًا ببضع أسطر من التعليمات البرمجية. يمكن لـ Aspose.Cells for JavaScript عبر C++ إنشاء تطبيقات متعددة المنصات مع القدرة على إنشاء وتعديل وتحويل وعرض وطباعة جميع ملفات إكسل.

## **تحويل HTML إلى PDF باستخدام جافا سكريبت**
يعرض المثال التالي لشفرة JavaScript كيفية تحويل مستند HTML إلى PDF باستخدام [Aspose.Cells for JavaScript عبر C++](https://releases.aspose.com/cells/javascript-cpp/).

1. إنشاء مثيل من فئة [HtmlLoadOptions](https://reference.aspose.com/cells/javascript-cpp/htmlloadoptions/).
1. تهيئة كائن [الكتاب](https://reference.aspose.com/cells/javascript-cpp/workbook/).
1. حفظ مستند PDF الناتج باستدعاء طريقة Workbook.save().

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

## **محاولة تحويل HTML إلى PDF عبر الإنترنت**

[Aspose.Cells for JavaScript via C++](https://releases.aspose.com/cells/javascript-cpp/) presents you online free application <a href="https://products.aspose.app/cells/en/conversion/html-to-pdf">“HTML إلى PDF”</a>, where you may try to investigate the functionality and quality it works.
<br>
<a href="https://products.aspose.app/cells/en/conversion/html-to-pdf"><img src="htmltopdf.png" width=80%></a>
