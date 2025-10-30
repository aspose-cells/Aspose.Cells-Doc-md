---
title: Hücrenin Zengin Metin Kısımlarına Erişim ve Güncelleme
linktitle: Zengin Biçimlendirme Metni
type: docs
weight: 40
url: /tr/javascript-cpp/access-and-update-the-portions-of-rich-text-of-cell/
description: Hücrenin Zengin Metninin Bölümlerine Erişme ve Güncelleme konusunda Aspose.Cells for JavaScript C++ API sini kullanmayı öğrenin.
keywords: Hücrenin zengin metin bölümlerine erişme ve güncelleme, Hücrenin zengin metnini alma, Hücrenin zengin metnini düzenleme, Hücrenin zengin metnine erişme, Hücrenin zengin metnini güncelleme, Hücrenin zengin metnini değiştirme
---

{{% alert color="primary" %}}

Aspose.Cells for JavaScript C++ hücrenin zengin metninin bölümlerine erişmenize ve güncellemenize olanak tanır. Bunu yapmak için [**Cell.characters**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters--) ve [**Cell.characters**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters-fontsettingarray-) özelliklerini kullanabilirsiniz. Bu özellikler, font adı, renk, kalınlık gibi farklı özelliklere erişip güncellemenizi sağlayan [**FontSetting**](https://reference.aspose.com/cells/javascript-cpp/fontsetting) nesne dizisini döndürür ve kabul eder.

{{% /alert %}}

## **Zengin Metnin Kısımlarına Erişme ve Güncelleme**

Aşağıdaki kod, sağlanan bağlantıdan indirebileceğiniz [kaynak excel dosyası](5112369.xlsx) kullanılarak [**Cell.characters**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters--) ve [**Cell.characters**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters-fontsettingarray-) özelliklerinin kullanımını gösterir. Kaynak excel dosyasının A1 hücresinde zengin metin vardır. 3 bölüme ayrılmıştır ve her bölüm farklı fontlar içerir. Aşağıdaki kod bu bölümlere erişir ve ilk bölümü yeni bir font adıyla günceller. Son olarak, çalışma kitabını [ çıktı excel dosyası](5112366.xlsx) olarak kaydeder. Açtığınızda, ilk bölümdeki yazı fontunun **"Arial"** olarak değiştiğini göreceksiniz.

### Zengin Metnin Bölümlerine Erişmek ve Güncellemek İçin JavaScript Kodu

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Update Cell Character Font Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

        const readyPromise = AsposeCells.onReady({
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            // Ensure Aspose.Cells is initialized
            await readyPromise;

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet and its cells
            const cells = workbook.worksheets.get(0).cells;
            const cell = cells.get("A1");

            console.log("Before updating the font settings....");
            let fnts = cell.characters;
            const count = fnts.length;
            for (let i = 0; i < count; i++) {
                console.log(fnts[i].font.name);
            }

            // Modify the first FontSetting Font Name
            fnts[0].font.name = "Arial";

            // And update it using characters property
            cell.characters = fnts;

            console.log("After updating the font settings....");

            fnts = cell.characters;

            for (let i = 0; i < count; i++) {
                console.log(fnts[i].font.name);
            }

            // Save workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### Örnek kod tarafından oluşturulan konsol çıktısı



{{< highlight java >}}

Before updating the font settings....

Century

Courier New

Verdana

After updating the font settings....

Arial

Courier New

Verdana

{{< /highlight >}}
