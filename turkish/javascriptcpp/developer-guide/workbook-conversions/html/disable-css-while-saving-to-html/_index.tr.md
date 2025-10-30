---
title: JavaScript ile C++ kullanarak HTML kaydederken CSS yi devre dışı bırak
linktitle: HTML yi kaydederken CSS yi devre dışı bırak
type: docs
weight: 320
url: /tr/javascript-cpp/disable-css-while-saving-to-html/
description: C++ ile Aspose.Cells for JavaScript kullanarak Excel dosyalarını HTML ye kaydederken CSS yi nasıl devre dışı bırakacağınızı öğrenin. 
---

## **Olası Kullanım Senaryoları**

Excel dosyanızı tek sayfa HTML'ye kaydettiğinizde, genellikle CSS öğeleri HTML dosyasına gömülü olur ve HEAD bölümünde bulunur. Bu dosyayı e-posta içeriği/gövdesi olarak eklediğinizde, CSS öğeleri çoğu e-posta istemcisi tarafından kaldırılır ve düzgün görüntüleme sağlanmaz. Aspose.Cells'in 24.12 sürümü, CSS'yi isteğe bağlı olarak devre dışı bırakmanıza olanak tanıyan bir seçenek sunar, böylece stiller doğrudan HTML öğeleri içinde uygulanabilir. E-posta içeriği/gövdesi olarak HTML ayarlamak istiyorsanız, lütfen [**HtmlSaveOptions.disableCss**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#disableCss--) özelliğini kullanın ve **true** olarak ayarlayın.

## **CSS'yi devre dışı bırakırken HTML'ye kaydetme**

 Aşağıdaki örnek kod, [**HtmlSaveOptions.disableCss**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#disableCss--) özelliğinin kullanımını gösterir. 

## **Örnek Kod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Disable CSS Example</title>
    </head>
    <body>
        <h1>Disable CSS Save Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlSaveOptions } = AsposeCells;

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
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const opts = new HtmlSaveOptions();
            opts.disableCss = true;

            const outputData = workbook.save(SaveFormat.Html, opts);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputDisable.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">HTML file generated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
