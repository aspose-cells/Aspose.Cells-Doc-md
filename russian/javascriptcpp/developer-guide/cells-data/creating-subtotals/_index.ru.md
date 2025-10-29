---
title: Создание Промежуточных Итогов
type: docs
weight: 800
url: /ru/javascript-cpp/creating-subtotals/
description: Узнайте, как создавать промежуточные итоги для любых повторяющихся значений в электронной таблице с помощью API Aspose.Cells for JavaScript через C++.
keywords: Применение итогов, Установка итогов, Добавление итогов, Создание итогов, Как добавить итоги к рабочему листу 
---

{{% alert color="primary" %}}

Вы можете автоматически создавать промежуточные итоги для любых повторяющихся значений в электронной таблице. Aspose.Cells for JavaScript через C++ предоставляет возможности API, которые помогают добавлять промежуточные итоги в таблицы программным способом.

{{% /alert %}}

## **Использование Microsoft Excel**

Чтобы добавить промежуточные итоги в Microsoft Excel:

1. Создайте простой список данных на первом листе книги (как показано на рисунке ниже) и сохраните файл как Book1.xls.
1. Выберите любую ячейку в вашем списке.
1. В меню **Данные** выберите **Промежуточные итоги**. Будет отображен диалоговое окно Промежуточные итоги. Определите, какую функцию использовать и где разместить промежуточные итоги.

## **Использование API Aspose.Cells for JavaScript через C++**

Aspose.Cells for JavaScript через C++ предоставляет класс, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) содержит коллекцию [**worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--), которая позволяет получить доступ к каждому листу Excel.

Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). Класс предоставляет широкий спектр свойств и методов для управления листами и другими объектами. Каждый лист состоит из коллекции [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells). Чтобы добавить промежуточные итоги в лист, используйте метод [**subtotal**](https://reference.aspose.com/cells/javascript-cpp/cells/#subtotal-cellarea-number-consolidationfunction-numberarray-) класса [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells). Укажите параметры метода, чтобы определить, как должен рассчитываться и размещаться итог.

В приведённых ниже примерах мы добавили промежуточные итоги в первый лист файла [шаблона](book1.xlsx) с помощью API Aspose.Cells for JavaScript через C++. Когда код выполнен, создается лист с промежуточными итогами.

Следующие примеры показывают, как добавлять промежуточные итоги в лист с помощью Aspose.Cells for JavaScript через C++.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Apply Subtotal Example</h1>
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

            // Instantiate a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the Cells collection in the first worksheet
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;

            // Create a cellarea i.e., B3:C19
            const ca = new AsposeCells.CellArea();
            ca.startRow = 2;
            ca.startColumn = 1;
            ca.endRow = 18;
            ca.endColumn = 2;

            // Apply subtotal, the consolidation function is Sum and it will be applied to
            // Second column (C) in the list
            cells.subtotal(ca, 0, AsposeCells.ConsolidationFunction.Sum, [1]);

            // Save the excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Subtotal applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
