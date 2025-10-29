---
title: 获取应用于单元格的验证
type: docs
weight: 200
url: /zh/javascript-cpp/get-validation-applied-on-a-cell/
description: 本文介绍了如何通过C++中的JavaScript对单元格应用验证。
keywords: 用JavaScript通过C++在Excel中应用单元格验证，使用C++在Excel中对单元格应用验证，在Excel中使用JavaScript进行验证，通过C++实现单元格验证，JavaScript通过C++在Excel中应用单元格验证，JavaScript通过C++实现对Excel单元格的验证
---

{{% alert color="primary" %}}

你可以使用C++中的Aspose.Cells for JavaScript获取应用于某个单元格的验证，Aspose.Cells提供了[**Cell.validation**](https://reference.aspose.com/cells/javascript-cpp/cell/#validation--)方法用于此目的。如果单元格没有应用验证，则返回null。

同样，您可以使用 [**Worksheet.validations.validationInCell(number, number)**](https://reference.aspose.com/cells/javascript-cpp/validationcollection/#validationInCell-number-number-) 方法通过提供它的行和列索引来获取应用于单元格的验证。

{{% /alert %}}

## 获取单元格验证的JavaScript代码

下面的代码示例演示了如何获取应用到单元格的验证。

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


## 相关文章

- [数据有效性](/cells/zh/javascript-cpp/data-validation/)
