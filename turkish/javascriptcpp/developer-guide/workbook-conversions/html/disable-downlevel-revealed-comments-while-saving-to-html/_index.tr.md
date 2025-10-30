---
title: JavaScript ile C++ kullanarak HTML ye kaydederken Downlevel Reveal Comments ı devre dışı bırakın
linktitle: HTML ye kaydederken Downlevel Açıklanan Yorumları Devre Dışı Bırak
type: docs
weight: 20
url: /tr/javascript-cpp/disable-downlevel-revealed-comments-while-saving-to/
description: C++ ile Aspose.Cells for JavaScript kullanarak Excel dosyasını HTML ye kaydederken downlevel revealed comments ı nasıl devre dışı bırakacağınızı öğrenin.
---

## **Olası Kullanım Senaryoları**

Excel dosyanızı HTML'ye kaydettiğinizde, Aspose.Cells Downlevel Conditional Comments'ı gösterir. Bu koşullu yorumlar çoğunlukla eski Internet Explorer sürümleriyle ilgilidir ve modern web tarayıcılar için anlamlı değildir. Ayrıntılı bilgi için aşağıdaki bağlantıya bakabilirsiniz.

- [Koşullu yorum - Downlevel-açıklanan koşullu yorum](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

 C++ ile Aspose.Cells for JavaScript kullanarak bu Downlevel Revealed Comments'ı [**HtmlSaveOptions.disableDownlevelRevealedComments**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#disableDownlevelRevealedComments--) özelliğini **true** olarak ayarlayarak kaldırabilirsiniz.

## **HTML'ye kaydederken Downlevel Açıklanan Yorumları Devre Dışı Bırak**

Aşağıdaki örnek kod, [**HtmlSaveOptions.disableDownlevelRevealedComments**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#disableDownlevelRevealedComments--) özelliğinin kullanımını gösterir. Bu özelliğin **true** olarak ayarlanmadığında etkisini ekran görüntüsü ile görebilirsiniz. Bu kodda kullanılan örnek Excel dosyasını ([software.xlsx](50528257.xlsx)) ve üretilen [çıktı HTML'sini](50528258.zip) indirerek referans alabilirsiniz.

![todo:image_alt_text](disable-downlevel-revealed-comments-while-saving-to-html_1.png)

## **Örnek Kod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Disable Downlevel Revealed Comments Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlSaveOptions, Utils } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Load sample workbook
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Disable DisableDownlevelRevealedComments
            const opts = new HtmlSaveOptions();
            opts.disableDownlevelRevealedComments = true;

            // Save the workbook in html
            const outputData = workbook.save(SaveFormat.Html, opts);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputDisableDownlevelRevealedComments_true.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook saved as HTML with DisableDownlevelRevealedComments = true. Click the download link to get the result.</p>';
        });
    </script>
</html>
```
