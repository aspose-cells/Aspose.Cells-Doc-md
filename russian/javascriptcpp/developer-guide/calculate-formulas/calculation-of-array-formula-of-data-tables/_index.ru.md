---
title: Вычисление массивных формул таблиц данных с помощью JavaScript через C++
linktitle: Вычисление массивной формулы таблиц данных
description: Как использовать библиотеку Aspose.Cells для вычисления массивных формул для таблицы данных в Microsoft Excel с помощью JavaScript через C++. Загрузите или создайте файл Excel, вычислите массивную формулу и сохраните изменённый файл.
keywords: Aspose.Cells, Excel, таблицы данных, массивные формулы, вычисления JavaScript через C++
type: docs
weight: 70
url: /ru/javascript-cpp/calculation-of-array-formula-of-data-tables/
---

{{% alert color="primary" %}}

Вы можете создать Таблицу данных в Microsoft Excel, используя Data > What-If Analysis > Data Table.... Сейчас Aspose.Cells позволяет вычислять массивные формулы таблицы данных. Пожалуйста, используйте [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--) как обычно для вычисления любых типов формул.

{{% /alert %}}

В следующем образце кода мы использовали [исходный файл Excel](5115535.xlsx). Если вы измените значение ячейки B1 на 100, значения Таблицы данных, заполненные желтым цветом, станут равными 120, как показано на следующих изображениях. Образец кода генерирует [выходной PDF](5115538.pdf).

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_1.png)

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_2.png)



```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>DataTable Calculation Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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

            // Creating a Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // When you will put 100 in B1, then all Data Table values formatted as Yellow will become 120
            const cell = worksheet.cells.get("B1");
            cell.putValue(100);

            // Calculate formula, now it also calculates Data Table array formula
            workbook.calculateFormula();

            // Save the workbook in pdf format
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: "application/pdf" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```
