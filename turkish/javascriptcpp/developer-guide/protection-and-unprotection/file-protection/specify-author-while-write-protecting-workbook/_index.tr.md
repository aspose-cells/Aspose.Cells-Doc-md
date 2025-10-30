---
title: JavaScript kullanarak C++ ile Çalışma Kitabını Yazma Koruma sırasında Yazar belirtmek
linktitle: Çalışma Kitabını Korumaya Alırken Yazarı Belirtme
type: docs
weight: 40
url: /tr/javascript-cpp/specify-author-while-write-protecting-workbook/
description: C++ ile Aspose.Cells for JavaScript kullanarak çalışma kitabını yazma koruması sırasında yazar adı belirtin.
---

## **Olası Kullanım Senaryoları**

Aspose.Cells API kullanarak çalışma kitabınızı yazarken yazar adını belirtebilirsiniz. Bu amaçla [**Workbook.author**](https://reference.aspose.com/cells/javascript-cpp/writeprotection/#author--) özelliğini kullanın.

## **Çalışma Kitabını Yazma Koruması Sırasında Yazar Belirtme**

Aşağıdaki örnek kod, [**Workbook.author**](https://reference.aspose.com/cells/javascript-cpp/writeprotection/#author--) özelliğinin kullanımını açıklar. Kod, boş bir çalışma kitabı oluşturur, şifre ile korur, yazar adını belirtir ve [çıktı Excel dosyası](67338582.xlsx) olarak kaydeder. Aşağıdaki ekran görüntüsü, örnek kodun çıktı Excel dosyasına etkisini gösterir.

![todo:image_alt_text](specify-author-while-write-protecting-workbook_1.png)

## **Örnek Kod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Specify Author While Write Protecting Workbook</h1>
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
            // Create empty workbook.
            const workbook = new Workbook();

            // Write protect workbook with password.
            workbook.settings.writeProtection.password = "1234";

            // Specify author while write protecting workbook.
            workbook.settings.writeProtection.author = "SimonAspose";

            // Save the workbook in XLSX format.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSpecifyAuthorWhileWriteProtectingWorkbook.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and write-protected successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
