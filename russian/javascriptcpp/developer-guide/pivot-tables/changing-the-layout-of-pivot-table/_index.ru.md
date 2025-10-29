---
title: Изменение макета сводной таблицы
type: docs
weight: 10
url: /ru/javascript-cpp/changing-the-layout-of-pivot-table/
description: Как изменить макет сводной таблицы с помощью Aspose.Cells for JavaScript на C++.
keywords: Aspose.Cells for JavaScript для Excel на C++, библиотека Excel JavaScript, изменение макета сводной таблицы с помощью Aspose.Cells for JavaScript для Excel на C++.
---

## **Как изменить макет сводной таблицы в MS-Excel**
Microsoft Excel позволяет изменять компоновку сводной таблицы с помощью команд меню *Инструменты сводной таблицы > Оформление > Оформление отчета*. Вы можете изменить компоновку в следующих формах:

- Показать в компактной форме
- Показать в контурной форме
- Показать в табличной форме

## **Как изменить макет сводной таблицы с помощью Aspose.Cells for JavaScript на C++**
Библиотека Aspose.Cells for JavaScript на C++ также предоставляет методы [**PivotTable.showInCompactForm()**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#showInCompactForm--), [**PivotTable.showInOutlineForm()**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#showInOutlineForm--) и [**PivotTable.showInTabularForm()**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#showInTabularForm--) для изменения макета сводной таблицы в трех форматах.

## **Образец кода**
В следующем образце кода сначала показывается сводная таблица в **Компактной форме**, затем она показывается в **Контурной форме**, и в конце концов, она показывается в **Табличной форме**.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Pivot Table Display Forms Example</title>
    </head>
    <body>
        <h1>Pivot Table Display Forms Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <div>
            <a id="downloadLink1" style="display: none; margin-right: 10px;"></a>
            <a id="downloadLink2" style="display: none; margin-right: 10px;"></a>
            <a id="downloadLink3" style="display: none;"></a>
        </div>
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

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access first pivot table
            const pivotTable = worksheet.pivotTables.get(0);

            // 1 - Show the pivot table in compact form
            pivotTable.showInCompactForm();
            pivotTable.refreshData();
            pivotTable.calculateData();

            // Save the Compact form output
            const outputData1 = workbook.save(SaveFormat.Xlsx);
            const blob1 = new Blob([outputData1]);
            const downloadLink1 = document.getElementById('downloadLink1');
            downloadLink1.href = URL.createObjectURL(blob1);
            downloadLink1.download = 'CompactForm_out.xlsx';
            downloadLink1.style.display = 'inline-block';
            downloadLink1.textContent = 'Download CompactForm_out.xlsx';

            // 2 - Show the pivot table in outline form
            pivotTable.showInOutlineForm();
            pivotTable.refreshData();
            pivotTable.calculateData();

            // Save the Outline form output
            const outputData2 = workbook.save(SaveFormat.Xlsx);
            const blob2 = new Blob([outputData2]);
            const downloadLink2 = document.getElementById('downloadLink2');
            downloadLink2.href = URL.createObjectURL(blob2);
            downloadLink2.download = 'OutlineForm_out.xlsx';
            downloadLink2.style.display = 'inline-block';
            downloadLink2.textContent = 'Download OutlineForm_out.xlsx';

            // 3 - Show the pivot table in tabular form
            pivotTable.showInTabularForm();
            pivotTable.refreshData();
            pivotTable.calculateData();

            // Save the Tabular form output
            const outputData3 = workbook.save(SaveFormat.Xlsx);
            const blob3 = new Blob([outputData3]);
            const downloadLink3 = document.getElementById('downloadLink3');
            downloadLink3.href = URL.createObjectURL(blob3);
            downloadLink3.download = 'TabularForm_out.xlsx';
            downloadLink3.style.display = 'inline-block';
            downloadLink3.textContent = 'Download TabularForm_out.xlsx';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operations completed. Use the links above to download the modified files.</p>';
        });
    </script>
</html>
```
