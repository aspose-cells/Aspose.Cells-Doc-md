---
title: HtmlCrossType kullanarak çıktı HTML sinde dizgeleri nasıl çapraz göstereceğinizi belirtin
linktitle: Çıkış HTML sinde dizeyi nasıl geçeceğini HtmlCrossType kullanarak belirtin
type: docs
weight: 140
url: /tr/javascript-cpp/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
description: Aspose.Cells for JavaScript kullanarak HTML çıktısında dize taşmasına nasıl kontrol edileceğini öğrenin, HtmlCrossType belirterek.
---

## **Olası Kullanım Senaryoları**

Bir hücre metin veya dizi içeriyorsa ve hücrenin genişliğinden büyükse, dizi taşar; eğer bir sonraki hücre boş veya null ise. Excel dosyanızı HTML'ye kaydederken, [**HtmlCrossType**](https://reference.aspose.com/cells/javascript-cpp/htmlcrosstype) sıralaması kullanılarak çaprazlama türü belirleyerek bu taşmayı kontrol edebilirsiniz. Aşağıdaki değerlere sahiptirler:

- **HtmlCrossType.Default**: MS Excel gibi gösterir; bir sonraki hücreye bağlıdır. Eğer bir sonraki hücre null ise, dizi çaprazlar veya kısaltılır.

- **HtmlCrossType.MSExport**: Diziyi MS Excel'in HTML olarak dışa aktarması gibi görüntüle.

- **HtmlCrossType.Cross**: HTML çapraz dizisini gösterir; büyük HTML dosyaları oluşturma performansı, Default veya FitToCell ayarlarından on kat daha hızlıdır.

- **HtmlCrossType.FitToCell**: Dizeyi yalnızca hücre genişliği içinde gösterir.

## **Çıkış HTML'sinde dizeyi nasıl geçeceğini HtmlCrossType kullanarak belirtin**

 Aşağıdaki örnek kod, [örnek Excel dosyasını](51740732.xlsx) yükler ve farklı [**HtmlCrossType**](https://reference.aspose.com/cells/javascript-cpp/htmlcrosstype) değerleri belirterek HTML formatında kaydeder. Lütfen bu kod ile üretilen [çıktı HTML'leri](51740734.zip) indirin. Örnek Excel dosyası, bu ekran görüntüsünde gösterildiği gibi kırmızı renkli çerçeve ile sınırlanmış bir resmi içerir ve bu ekran görüntüsü, [**HtmlCrossType**](https://reference.aspose.com/cells/javascript-cpp/htmlcrosstype) değerlerinin çıktı HTML'sine etkisini gösterir.

![todo:image_alt_text](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **Örnek Kod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Export HTML Cross String Type Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlSaveOptions, HtmlCrossType, Utils } = AsposeCells;

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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Specify HTML Cross Type via HtmlSaveOptions
            const opts = new HtmlSaveOptions();
            // Applying the sequence of assignments as in the original JavaScript code
            opts.htmlCrossStringType = HtmlCrossType.Default;
            opts.htmlCrossStringType = HtmlCrossType.MSExport;
            opts.htmlCrossStringType = HtmlCrossType.Cross;
            opts.htmlCrossStringType = HtmlCrossType.FitToCell;

            // Save workbook to HTML using the specified options
            const outputData = workbook.save(SaveFormat.Html, opts);
            const blob = new Blob([outputData], { type: "text/html" });
            const downloadLink = document.getElementById('downloadLink');
            const fileName = 'out' + opts.htmlCrossStringType + '.htm';
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = fileName;
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">HTML exported successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
