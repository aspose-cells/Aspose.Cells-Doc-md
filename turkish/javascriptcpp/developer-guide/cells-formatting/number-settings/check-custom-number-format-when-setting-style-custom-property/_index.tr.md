---
title: Stil.Custom Özelliğini Ayarlarken Özel Sayı Biçimini Kontrol Edin
linktitle: Stil.Custom Özelliğini Ayarlarken Özel Sayı Biçimini Kontrol Edin
description: Aspose.Cells, stillendirme sırasında özel sayı biçimlerini kontrol etmeyi destekleyen çalışma sayfası dosyalarıyla çalışmaya yönelik bir JavaScript kütüphanesidir. Bu makale, stilin doğru olup olmadığını sağlamak için Aspose.Cells kütüphanesini kullanarak özel sayı biçimlerini nasıl kontrol edeceğinizi gösterecektir.
keywords: Aspose.Cells, JavaScript kütüphaneleri, çalışma sayfaları, stil, özel sayı biçimlendirme, kontrol, doğrulama
type: docs
weight: 170
url: /tr/javascript-cpp/check-custom-number-format-when-setting-style-custom-property/
---

## **Olası Kullanım Senaryoları**

Geçersiz bir özel sayı biçimi [**Style.custom**](https://reference.aspose.com/cells/javascript-cpp/style/#custom-string-) özelliğine atanırsa, Aspose.Cells for JavaScript C++ üzerinden herhangi bir istisna fırlatmaz. Ancak, Aspose.Cells'in atanmış olan özel sayı biçiminin geçerli olup olmadığını kontrol etmesini istiyorsanız, lütfen [**Workbook.settings.checkCustomNumberFormat**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#checkCustomNumberFormat-boolean-) özelliğini **true** olarak ayarlayın.

## **Style.custom özelliği ayarlanırken Özel Sayı Biçimini Kontrol Et**

Aşağıdaki örnek kod, [**Style.custom**](https://reference.aspose.com/cells/javascript-cpp/style/#custom-string-) özelliğine geçersiz bir özel sayı biçimi atar. Zaten [**Workbook.settings.checkCustomNumberFormat**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#checkCustomNumberFormat-boolean-) özelliğini **true** olarak ayarladığımız için, örneğin Geçersiz sayı biçimi gibi bir istisna fırlatır. Daha fazla yardım için kod içindeki açıklamaları okuyunuz.

## **Örnek Kod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Check Custom Number Format</h1>
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
            let workbook;

            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                // Create a new empty workbook if no file is provided
                workbook = new Workbook();
            }

            // Setting this property to true will make Aspose.Cells throw an exception
            // when invalid custom number format is assigned to Style.custom property
            workbook.settings.checkCustomNumberFormat = true;

            // Access first worksheet
            const sheet = workbook.worksheets.get(0);

            // Access cell A1 and put some number to it
            const cell = sheet.cells.get("A1");
            cell.value = 2347;

            // Access cell's style and set its Style.custom property
            const style = cell.style;

            // This line will throw exception if workbook.settings.checkCustomNumberFormat is set to true
            style.custom = "ggg @ fff"; // Invalid custom number format

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed. Click the download link to get the file.</p>';
        });
    </script>
</html>
```
