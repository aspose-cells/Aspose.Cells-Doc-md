---
title: HTML yi PDF ye Dönüştürmek için JavaScript ile C++ kullanımı
linktitle: HTML i PDF e nasıl dönüştürülür
type: docs
weight: 80
url: /tr/javascript-cpp/convert-html-to-pdf/
description: Bu konu, Aspose.Cells for JavaScript i C++ kullanarak HTML ve MHTML yi PDF ye dönüştürmeyi gösterir.
keywords: JavaScript ile HTML yi PDF ye ve MHTML yi PDF ye dönüştürme 
---

## **Genel Bakış**
<b>Aspose.Cells</b> is a professional solution that allows you to generate PDF files from web pages and raw HTML code in your applications. 

This article explains how to <b>HTML'i PDF'e dönüştür</b>. It covers the following topics.

<ul>
<li><a href="#js-convert-html-to-pdf">JavaScript HTML'den PDF'ye</a></li>
<li><a href="#js-convert-html-to-pdf">JavaScript HTML'yi PDF'ye Dönüştür</a></li>
<li><a href="#js-convert-html-to-pdf">JavaScript HTML'yi PDF'ye nasıl dönüştürülür</a></li>
</ul>

## **JavaScript'te HTML'den PDF'ye Dönüşüm**
HTML'yi PDF'ye nasıl dönüştürürüm? [Aspose.Cells for JavaScript via C++](https://releases.aspose.com/cells/javascript-cpp/) kütüphanesi ile, HTML'yi birkaç satır kodla PDF'ye programlı olarak kolayca dönüştürebilirsiniz. Aspose.Cells for JavaScript'i C++ çapraz platform uygulamalar oluşturma, üretme, değiştirme, dönüştürme, render ve yazdırma yeteneğine sahiptir.

## **JavaScript HTML'yi PDF'ye Dönüştür**
Aşağıdaki JavaScript kod örneği, bir HTML belgesini [Aspose.Cells for JavaScript via C++](https://releases.aspose.com/cells/javascript-cpp/) kullanarak PDF'ye dönüştürmenin nasıl yapılacağını gösterir.

1. [HtmlLoadOptions](https://reference.aspose.com/cells/javascript-cpp/htmlloadoptions/) sınıfının bir örneğini oluşturun.
2. [Workbook](https://reference.aspose.com/cells/javascript-cpp/workbook/) nesnesini başlatın.
1. Workbook.save() yöntemini çağırarak çıktı PDF belgesini kaydedin.

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

## **HTML'i PDF'e çevirmeyi deneyin**

[Aspose.Cells for JavaScript via C++](https://releases.aspose.com/cells/javascript-cpp/) presents you online free application <a href="https://products.aspose.app/cells/en/conversion/html-to-pdf">“HTML'den PDF'e”</a>, where you may try to investigate the functionality and quality it works.
<br>
<a href="https://products.aspose.app/cells/en/conversion/html-to-pdf"><img src="htmltopdf.png" width=80%></a>
