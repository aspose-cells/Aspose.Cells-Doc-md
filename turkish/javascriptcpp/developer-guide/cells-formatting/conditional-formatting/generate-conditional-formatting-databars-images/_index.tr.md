---
title: Koşullu Biçimlendirme DataBar Görüntüleri Oluşturma
linktitle: Koşullu Biçimlendirme DataBar Görüntüleri Oluşturma
description: Aspose.Cells, elektronik tablo dosyalarıyla çalışmak için bir JavaScript kitaplığıdır. Koşullu biçimlendirilmiş veri çubukları ve görüntülerin oluşturulmasını destekler, böylece kullanıcılar hücrelerin değerine göre tablonun görüntüsünü özelleştirebilir. Bu makale, Aspose.Cells kitaplığını kullanarak koşullu biçimlendirilmiş veri çubukları ve görüntülerin nasıl oluşturulacağını tanıtacaktır.
keywords: Aspose.Cells, Koşullu Biçimlendirme, Veri Çubukları, Görüntüler, Elektronik Tablolar, JavaScript C++ ile
type: docs
weight: 40
url: /tr/javascript-cpp/generate-conditional-formatting-databars-images/
---

{{% alert color="primary" %}}

Bazen Koşullu Biçimlendirme DataBar'ların görüntülerini oluşturmanız gerekebilir. Aspose.Cells [**DataBar.toImage(Cell, ImageOrPrintOptions)**](https://reference.aspose.com/cells/javascript-cpp/databar/#toImage-cell-imageorprintoptions-) yöntemini kullanarak bu görüntüleri oluşturabilirsiniz. Bu makale, Aspose.Cells kullanarak DataBar görüntüsünün nasıl oluşturulacağını gösterir.

{{% /alert %}}

Aşağıdaki örnek kod, C1 hücresinin Veri Çubuğu görüntüsünü üretir. İlk olarak, hücrenin biçim koşulu nesnesine erişir ve ardından bu nesneden, [**DataBar**](https://reference.aspose.com/cells/javascript-cpp/databar) nesnesine erişerek ve onun [**DataBar.toImage(Cell, ImageOrPrintOptions)**](https://reference.aspose.com/cells/javascript-cpp/databar/#toImage-cell-imageorprintoptions-) metodunu kullanarak hücrenin resmini oluşturur. Son olarak, resmi diske kaydeder.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Generate DataBar Image</title>
    </head>
    <body>
        <h1>Generate DataBar Image Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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

            // Creating a workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the cell which contains conditional formatting databar
            const cell = worksheet.cells.get("C1");

            // Create and get the conditional formatting of the worksheet
            const idx = worksheet.conditionalFormattings.add();
            const fcc = worksheet.conditionalFormattings.get(idx);
            fcc.addCondition(AsposeCells.FormatConditionType.DataBar);
            fcc.addArea(AsposeCells.CellArea.createCellArea("C1", "C4"));

            // Access the conditional formatting databar
            const dbar = fcc.get(0).dataBar;

            // Create image or print options
            const opts = new AsposeCells.ImageOrPrintOptions();
            opts.imageType = AsposeCells.ImageType.Png;

            // Get the image bytes of the databar
            const imgBytes = dbar.toImage(cell, opts);

            // Create a blob and provide download link
            const blob = new Blob([imgBytes], { type: "image/png" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputGenerateDatabarImage.png';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Generated DataBar Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Image generated successfully! Click the download link to save the PNG file.</p>';
        });
    </script>
</html>
```
