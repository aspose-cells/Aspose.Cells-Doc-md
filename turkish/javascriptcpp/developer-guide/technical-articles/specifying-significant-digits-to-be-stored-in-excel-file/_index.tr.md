---
title: Excel Dosyasına JavaScript ile C++ üzerinden Önemli Rakamlar Belirtmek
linktitle: Excel Dosyasında Saklanacak Anlamlı Basamakları Belirtme
type: docs
weight: 30
url: /tr/javascript-cpp/specifying-significant-digits-to-be-stored-in-excel-file/
description: JavaScript ile C++ kullanarak bir Excel dosyasına kaydedilecek önemli rakamları nasıl belirleyeceğinizi öğrenin.
---

## **Olası Kullanım Senaryoları**  

Varsayılan olarak, JavaScript ile C++ kullanarak, Aspose.Cells 17 önemli rakamı içeren double değerleri Excel dosyasına kaydeder, MS-Excel ise yalnızca 15 önemli rakam kaydeder. Aspose.Cells'un varsayılan davranışını 17 önemli rakamdan 15 önemli rakama değiştirebilirsiniz, [**CellsHelper.significantDigits**](https://reference.aspose.com/cells/javascript-cpp/cellshelper/#significantDigits--) özelliğini kullanarak.  

## **Excel dosyasında saklanacak anlamlı basamakları belirtme**  

Aşağıdaki örnek kod, Aspose.Cells'in düzeltilmiş değerleri saklarken 15 önemli rakam kullanmasını sağlar. Lütfen [çıktı excel dosyasını](22774105.xlsx) kontrol edin. Uzantısını .zip yapıp açın, ve içinde sadece 15 önemli rakam saklandığını göreceksiniz. Aşağıdaki ekran görüntüsü, [**CellsHelper.significantDigits**](https://reference.aspose.com/cells/javascript-cpp/cellshelper/#significantDigits--) özelliğinin çıktı Excel dosyasına etkisini açıklar.  

![todo:image_alt_text](specifying-significant-digits-to-be-stored-in-excel-file_1.png)  

## **Örnek Kod**  

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>Aspose.Cells Example - Significant Digits</title>
    </head>
    <body>
        <h1>Significant Digits Example</h1>
        <p>This example sets CellsHelper.significantDigits to 15 and writes a double to cell A1.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellsHelper } = AsposeCells;

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

            // If a file is provided, open it; otherwise create a new workbook (matches original Node behavior)
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // By default, Aspose.Cells stores 17 significant digits unlike MS-Excel which stores only 15 significant digits
            CellsHelper.significantDigits = 15;

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access cell A1
            const c = worksheet.cells.get("A1");

            // Put double value, only 15 significant digits as specified by CellsHelper.significantDigits above will be stored
            c.value = 1234567890.123451711;

            // Saving the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out_SignificantDigits.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created/modified successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
