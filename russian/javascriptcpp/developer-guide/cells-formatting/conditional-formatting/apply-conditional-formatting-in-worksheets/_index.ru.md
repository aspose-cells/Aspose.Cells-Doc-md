---
title: Применение условного форматирования в рабочих листах
linktitle: Применение условного форматирования в рабочих листах
description: Как использовать библиотеку Aspose.Cells в JavaScript через C++ для применения условного форматирования в рабочих листах для более точного контроля внешнего вида ячеек.
keywords: Aspose.Cells, Условное форматирование, JavaScript через C++, рабочий лист, форматирование
type: docs
weight: 130
url: /ru/javascript-cpp/apply-conditional-formatting-in-worksheets/
---

{{% alert color="primary" %}}

Эта статья предназначена для подробного понимания того, как добавить условное форматирование к диапазону ячеек на рабочем листе.

Условное форматирование - это расширенная функция в Microsoft Excel, которая позволяет применять форматы к диапазону ячеек и менять этот формат в зависимости от значения ячейки или значения формулы. Например, фон ячейки может быть красным, чтобы выделить отрицательное значение, или цвет текста может быть зеленым для положительного значения. Когда значение ячейки соответствует условию форматирования, формат применяется. Если значение ячейки не соответствует условию форматирования, используется форматирование по умолчанию для ячейки.

Возможно применить условное форматирование с помощью автоматизации Microsoft Office, но это имеет свои недостатки. В этом участвует несколько причин и проблем: например, безопасность, стабильность, масштабируемость и скорость. Основной причиной поиска другого решения является то, что сама Microsoft настоятельно рекомендует не использовать автоматизацию Office для программных решений.

В этой статье показано, как создать веб-приложение, добавлять условное форматирование ячеек с помощью нескольких простых строк кода, используя API Aspose.Cells.

{{% /alert %}}

## **Использование Aspose.Cells для применения условного форматирования на основе значения ячейки**

1. **Загрузите и установите Aspose.Cells**.
   1. Загрузите скрипт Aspose.Cells for JavaScript через C++.
1. Установите его на вашем компьютере для разработки.
   Все компоненты Aspose, установленные, работают в режиме оценки. Режим оценки не имеет ограничения по времени и только внедряет водные знаки в созданные документы.
1. **Создайте проект**.
   Начните свой проект на JavaScript, инициализировав его. Этот пример демонстрирует использование в веб-приложении на базе браузера.
1. **Добавьте ссылки**.
   Добавьте ссылку на Aspose.Cells в ваш проект, например, включив библиотеку следующим образом:
   ```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Conditional Formatting Example</title>
    </head>
    <body>
        <h1>Apply Conditional Formatting Based on Cell Value</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, FormatConditionType, OperatorType, CellArea, Color } = AsposeCells;

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

            // Add conditional formatting collection
            const cfCollection = worksheet.conditionalFormattings;
            const idx = cfCollection.add();
            const formatConditionCollection = cfCollection.get(idx);

            // Define the cell area to apply conditional formatting (A1)
            const area = CellArea.createCellArea(0, 0, 0, 0); // fromRow, fromCol, toRow, toCol
            formatConditionCollection.addArea(area);

            // Add a condition: Cell Value > 100
            const conditionIndex = formatConditionCollection.addCondition(
                FormatConditionType.CellValue,
                OperatorType.Greater,
                "100",
                null
            );

            const formatCondition = formatConditionCollection.get(conditionIndex);

            // Modify the style for the condition: bold and red font
            const style = formatCondition.style;
            if (!style.font) {
                style.font = {};
            }
            style.font.bold = true;
            style.font.color = Color.fromArgb(255, 255, 0, 0); // ARGB red

            // Assign modified style back (property assignment pattern)
            formatCondition.style = style;

            // Save the modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'conditional_formatting_result.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conditional formatting applied to cell A1 (value &gt; 100). Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

При выполнении приведенного выше кода условное форматирование применяется к ячейке «A1» в первом рабочем листе выходного файла (output.xls). В зависимости от значения ячейки A1, фон ячейки становится красным, если значение находится между 50 и 100, из-за примененного условного форматирования.

## **Использование Aspose.Cells для применения условного форматирования на основе формулы**

1. Применение условного форматирования в зависимости от формулы (Фрагмент кода)
   Ниже приведен код для выполнения задачи. Он применяет условное форматирование к B3.
