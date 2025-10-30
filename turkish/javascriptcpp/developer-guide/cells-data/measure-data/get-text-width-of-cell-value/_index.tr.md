---
title: Hücre Değeri Metnin Genişliğini Alma
type: docs
weight: 50
url: /tr/javascript-cpp/get-text-width-of-cell-value/
description: C++ API aracılığıyla Aspose.Cells for JavaScript kullanarak Hücre Değeri Metin Genişliğini Nasıl Alırsınız öğrenin.
keywords: C++ aracılığıyla JavaScript ile Hücre Değeri Metin Genişliğini Alın, JavaScript ile Hücre Değeri Metin Genişliğini Edinin
---

## **Hücre Değeri Metnin Genişliğini Alma**

Bazen, geliştiriciler verileri düzenlemek için hücrenin değer genişliğini hesaplamaları gerekebilir. Aspose.Cells for JavaScript aracılığıyla C++, geliştiricilerin hücre değeri metin genişliğini almalarını sağlayan [**CellsHelper.textWidth(string, Font, number)**](https://reference.aspose.com/cells/javascript-cpp/cellshelper/#textWidth-string-font-number-) yöntemini sunar. Aşağıdaki örnek kod, [**CellsHelper.textWidth(string, Font, number)**](https://reference.aspose.com/cells/javascript-cpp/cellshelper/#textWidth-string-font-number-)'nin kullanılmasıyla hücre değeri metin genişliğine nasıl erişileceğini gösterir.

Aşağıdaki kod parçasında kullanılan Kaynak dosyası, referansınız için ekte bulunmaktadır.

[Kaynak Dosya](96928090.xlsx)

## Örnek Kod

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Text Width Example</title>
    </head>
    <body>
        <h1>Get Text Width Example</h1>
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet and A1 cell
            const worksheet = workbook.worksheets.get(0);
            const cell = worksheet.cells.get("A1");

            // Accessing default font style
            const font = workbook.defaultStyle.font;

            // Calculating text width using CellsHelper (converted getter name to property)
            const textWidth = AsposeCells.CellsHelper.textWidth(cell.stringValue, font, 1);

            resultDiv.innerHTML = `<p style="color: green;">Text width: ${textWidth}</p>`;
        });
    </script>
</html>
```
