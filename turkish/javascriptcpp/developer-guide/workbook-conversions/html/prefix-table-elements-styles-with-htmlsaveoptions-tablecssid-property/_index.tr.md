---
title: HtmlSaveOptions.tableCssId özelliği ile Tablo Öğesi Stillerini önekleyin JavaScript ve C++ aracılığıyla
linktitle: HtmlSaveOptions.tableCssId özelliği ile Tablo Öğesi Stillerini önekleyin
type: docs
weight: 110
url: /tr/javascript-cpp/prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property/
description: HTML de tablo öğesi stillerinin öneki nasıl eklenir öğrenmek için Aspose.Cells for JavaScript kullanarak C++ üzerinden.
---

## **Olası Kullanım Senaryoları**

Aspose.Cells, tablo öğeleri stillerini [**HtmlSaveOptions.tableCssId**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#tableCssId--) özelliği ile önekleyebilir. Diyelim ki, bu özelliğe **MyTest_TableCssId** gibi bir değer atadınız, o zaman tablo öğeleri stilleri aşağıdaki gibi görünecektir:

{{< highlight javascript >}}
 table#MyTest_TableCssId

#MyTest_TableCssId tr

#MyTest_TableCssId col

#MyTest_TableCssId br

etc.
{{< /highlight >}}

Aşağıdaki ekran görüntüsü, [**HtmlSaveOptions.tableCssId**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#tableCssId--) özelliğinin çıkış HTML'si üzerindeki etkisini göstermektedir.

![todo:image_alt_text](prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property_1.png)

## **HtmlSaveOptions.tableCssId özelliği ile Tablo Öğeleri Stillere Önek Ekleme**

Aşağıdaki örnek kod, [**HtmlSaveOptions.tableCssId**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#tableCssId--) özelliğinin nasıl kullanılacağını gösterir. Lütfen referans için kod tarafından oluşturulan [çıktı HTML](60489790.zip) dosyasını kontrol edin.

## **Örnek Kod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Set Cell Style and Save as HTML with Table CSS ID</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlSaveOptions, Color } = AsposeCells;

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
            if (fileInput.files.length === 0) {
                // No file selected - create a new workbook as in original JavaScript sample
                const wb = new Workbook();

                // Access first worksheet
                const ws = wb.worksheets.get(0);

                // Access cell B5 and put value inside it
                const cell = ws.cells.get("B5");
                cell.value = "This is some text.";

                // Set the style of the cell - font color is Red
                const st = cell.style;
                st.font.color = Color.Red;
                cell.style = st;

                // Specify html save options - specify table css id
                const opts = new HtmlSaveOptions();
                opts.tableCssId = "MyTest_TableCssId";

                // Save the workbook in html
                const outputData = wb.save(SaveFormat.Html, opts);
                const blob = new Blob([outputData], { type: 'text/html' });
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = 'outputTableCssId.html';
                downloadLink.style.display = 'block';
                downloadLink.textContent = 'Download HTML File';

                document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the HTML file.</p>';
                return;
            }

            // If a file is provided, open it and apply the same changes
            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const ws = wb.worksheets.get(0);

            // Access cell B5 and put value inside it
            const cell = ws.cells.get("B5");
            cell.value = "This is some text.";

            // Set the style of the cell - font color is Red
            const st = cell.style;
            st.font.color = Color.Red;
            cell.style = st;

            // Specify html save options - specify table css id
            const opts = new HtmlSaveOptions();
            opts.tableCssId = "MyTest_TableCssId";

            // Save the workbook in html
            const outputData = wb.save(SaveFormat.Html, opts);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputTableCssId.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the HTML file.</p>';
        });
    </script>
</html>
```
