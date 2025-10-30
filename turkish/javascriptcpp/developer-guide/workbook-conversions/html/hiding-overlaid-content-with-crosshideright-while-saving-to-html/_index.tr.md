---
title: HTML ye kaydederken Çakışmayı Gizle ve Çapraz Gizleyanıt ContentOverlay i gizlerken kullanılır
linktitle: HTML ye Kaydederken CrossHideRight ile Örtüşmeyen İçeriği Gizleme
type: docs
weight: 100
url: /tr/javascript-cpp/hiding-overlaid-content-with-crosshideright-while-saving-to/
---

## **Olası Kullanım Senaryoları**

Excel dosyanızı HTML'ye kaydederken hücre dizileri için farklı çapraz türleri belirtebilirsiniz. Varsayılan olarak, Aspose.Cells Microsoft Excel'e göre HTML oluşturur, ancak çapraz türünü [**CrossHideRight**](https://reference.aspose.com/cells/javascript-cpp/htmlcrosstype) olarak değiştirirseniz, hücreyle örtüşen veya üst üste binen tüm dizileri gizler.

## **HTML'ye Kaydederken CrossHideRight ile Örtüşmeyen İçeriği Gizleme**

Aşağıdaki örnek kod, [örnek Excel dosyasını](64716894.xlsx) yükler ve [**HtmlSaveOptions.htmlCrossStringType**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#htmlCrossStringType--) değerini [**CrossHideRight**](https://reference.aspose.com/cells/javascript-cpp/htmlcrosstype) yapar, ardından [çıktı HTML'sine](64716893.zip) kaydeder. Ekran görüntüsü, [**CrossHideRight**](https://reference.aspose.com/cells/javascript-cpp/htmlcrosstype)'nin varsayılan çıktı üzerindeki etkisini açıklar.

![todo:image_alt_text](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **Örnek Kod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Hiding Overlaid Content With CrossHideRight While Saving To Html</title>
    </head>
    <body>
        <h1>Hiding Overlaid Content With CrossHideRight While Saving To Html</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the Excel file from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Specify HtmlSaveOptions - Hide Overlaid Content with CrossHideRight while saving to Html
            const opts = new AsposeCells.HtmlSaveOptions();
            opts.htmlCrossStringType = AsposeCells.HtmlCrossType.CrossHideRight;

            // Save to HTML with HtmlSaveOptions
            const outputData = workbook.save(SaveFormat.Html, opts);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputHidingOverlaidContentWithCrossHideRightWhileSavingToHtml.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">HTML file created successfully! Click the download link to get the result.</p>';
        });
    </script>
</html>
```
