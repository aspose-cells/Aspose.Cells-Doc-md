---
title: Hücreye Uygulanan Doğrulamayı Al
type: docs
weight: 200
url: /tr/javascript-cpp/get-validation-applied-on-a-cell/
description: Bu makale, C++ aracılığıyla JavaScript kullanarak Hücrede doğrulama nasıl uygulanır gösterir.
keywords: excel de hücre doğrulamasını JavaScript aracılığıyla C++ kullanarak uygula, excel de bir hücreye doğrulama uygula JavaScript aracılığıyla C++, excel de doğrulama yap JavaScript aracılığıyla C++, excel de hücre doğrulaması JavaScript aracılığıyla C++, excel de JavaScript ile hücre doğrulama aracılığıyla C++, JavaScript aracılığıyla C++ ile excel de hücre doğrulama, JavaScript aracılığıyla C++ ile excel de hücre üzerinde doğrulama uygula, JavaScript aracılığıyla C++ ile excel de hücre doğrulama
---

{{% alert color="primary" %}}

Aspose.Cells for JavaScript aracılığıyla C++ kullanarak hücreye uygulanan doğrulamayı alabilirsiniz. Aspose.Cells bunun için [**Cell.validation**](https://reference.aspose.com/cells/javascript-cpp/cell/#validation--) metodunu sağlar. Eğer hücreye doğrulama uygulanmamışsa, null döner.

Benzer şekilde, [**Worksheet.validations.validationInCell(number, number)**](https://reference.aspose.com/cells/javascript-cpp/validationcollection/#validationInCell-number-number-) yöntemini kullanarak bir hücreye uygulanan doğrulamayı alabilirsiniz. Bu yöntem, satır ve sütun indislerini sağlayarak çalışmaktadır.

{{% /alert %}}

## Hücreye Uygulanan Doğrulamayı Almak İçin JavaScript Kodu

Aşağıdaki kod örneği, hücreye uygulanan doğrulamayı nasıl alacağınızı gösterir.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Read Validation Properties Example</h1>
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

            // Instantiate the workbook from the selected Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access its first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Cell C1 has the Decimal Validation applied on it.
            const cell = worksheet.cells.get("C1");

            // Access the validation applied on this cell
            const validation = cell.validation;

            // Read various properties of the validation
            let output = '';
            output += '<p>Reading Properties of Validation</p>';
            output += '<hr />';
            output += `<p>Type: ${validation.type}</p>`;
            output += `<p>Operator: ${validation.operator}</p>`;
            output += `<p>Formula1: ${validation.formula1}</p>`;
            output += `<p>Formula2: ${validation.formula2}</p>`;
            output += `<p>Ignore blank: ${validation.ignoreBlank}</p>`;

            document.getElementById('result').innerHTML = output;
        });
    </script>
</html>
```


## İlgili Makaleler

- [Veri Doğrulama](/cells/tr/javascript-cpp/data-validation/)
