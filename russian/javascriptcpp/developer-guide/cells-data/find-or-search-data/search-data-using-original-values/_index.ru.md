---
title: Поиск данных с использованием исходных значений
type: docs
weight: 380
url: /ru/javascript-cpp/search-data-using-original-values/
description: Узнайте, как искать данные с использованием исходных значений через API Aspose.Cells for JavaScript через C++.
keywords: Поиск данных с использованием исходных значений JavaScript через C++, Поиск данных с использованием исходных значений JavaScript через C++, Поиск данных по исходным значениям JavaScript через C++, Поиск данных по исходным значениям JavaScript через C++
---

{{% alert color="primary" %}}  

Иногда значение данных скрыто, потому что оно отформатировано каким-то образом. Например, предположим, что ячейка D4 имеет формулу =Сумма(A1:A2) и ее значение равно 20, но оно отформатировано как ---, то значение 20 скрыто и не может быть найдено с помощью функции поиска в Microsoft Excel. Однако вы можете найти его с помощью Aspose.Cells, используя [**LookInType.OriginalValues**](https://reference.aspose.com/cells/javascript-cpp/lookintype)  

{{% /alert %}}  

Приведенный ниже образец кода иллюстрирует вышеупомянутый момент. Он находит ячейку D4, которую нельзя найти с помощью опций поиска Microsoft Excel, но Aspose.Cells может найти ее с помощью [**LookInType.OriginalValues**](https://reference.aspose.com/cells/javascript-cpp/lookintype). Пожалуйста, прочтите комментарии внутри кода для получения дополнительной информации.  

## JavaScript-код для поиска данных с использованием исходных значений  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Find Formatted Value</title>
    </head>
    <body>
        <h1>Find Formatted Value Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, FindOptions, Worksheet, Cell, Utils } = AsposeCells;

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
                workbook = new Workbook();
            }

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Add 10 in cell A1 and A2
            worksheet.cells.get("A1").value = 10;
            worksheet.cells.get("A2").value = 10;

            // Add Sum formula in cell D4 but customize it as ---
            const cell = worksheet.cells.get("D4");

            let style = cell.style;
            style.custom = "---";
            cell.style = style;

            // The result of formula will be 20 but 20 will not be visible because the cell is formatted as ---
            cell.formula = "=Sum(A1:A2)";

            // Calculate the workbook
            workbook.calculateFormula();

            // Create find options, we will search 20 using original values otherwise 20 will never be found because it is formatted as ---
            const options = new FindOptions();
            options.lookInType = AsposeCells.LookInType.OriginalValues;
            options.lookAtType = AsposeCells.LookAtType.EntireContent;

            let foundCell = null;
            const obj = 20;

            // Find 20 which is Sum(A1:A2) and formatted as ---
            foundCell = worksheet.cells.find(obj, foundCell, options);

            // Print the found cell to the page
            const resultDiv = document.getElementById('result');
            if (foundCell) {
                resultDiv.innerHTML = `<p style="color: green;">Found cell: ${foundCell.name}, value: ${foundCell.value}</p>`;
            } else {
                resultDiv.innerHTML = `<p style="color: red;">Cell not found.</p>`;
            }

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Resulting Excel File';
        });
    </script>
</html>
```


## Консольный вывод, сгенерированный образцовым кодом  



{{< highlight java >}}  

Aspose.Cells.Cell [ D4; ValueType : IsNumeric; Value : ---; Formula:=SUM(A1:A2)]  

{{< /highlight >}}
