---
title: Применить засветку для альтернативных строк и столбцов с условным форматированием
linktitle: Применить засветку для альтернативных строк и столбцов с условным форматированием
description: Как использовать библиотеку Aspose.Cells в JavaScript через C++ для применения теней условного форматирования для чередующихся строк и столбцов. Настроив эти параметры, вы получите больший контроль над внешним видом и отображением ячеек.
keywords: Aspose.Cells, Условное форматирование, JavaScript через C++, Чередующиеся строки, Чередующиеся столбцы, Тени
type: docs
weight: 30
url: /ru/javascript-cpp/apply-shading-to-alternate-rows-and-columns-with-conditional-formatting/
---

{{% alert color="primary" %}}

APIs Aspose.Cells предоставляют возможности добавлять и управлять правилами условного форматирования для объекта [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). Эти правила можно настроить различными способами для достижения желаемого форматирования в соответствии с условиями или правилами. В этой статье продемонстрировано использование API Aspose.Cells for JavaScript через C++ для применения затенения к чередующимся строкам и столбцам с помощью правил условного форматирования и встроенных функций Excel.

{{% /alert %}}

В этой статье используются встроенные функции Excel, такие как ROW, COLUMN & MOD. Вот некоторые подробности об этих функциях для лучшего понимания предоставленного фрагмента кода.

- Функция **ROW()** возвращает номер строки ссылки. Если параметр reference пропущен, считается, что ссылка — это адрес ячейки, в которой вызвана функция.
- Функция **COLUMN()** возвращает номер столбца ссылки. Если параметр reference пропущен, считается, что ссылка — это адрес ячейки, в которой вызвана функция.
- **Функция MOD()** возвращает остаток после деления числа на делитель, где первый параметр функции - это числовое значение, для которого вы хотите найти остаток, и второй параметр - это число, используемое для деления числа. Если делитель равен 0, то она вернет ошибку #DIV/0!.

Давайте начнем писать код для достижения этой цели с помощью API Aspose.Cells for JavaScript через C++.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Conditional Formatting</title>
    </head>
    <body>
        <h1>Conditional Formatting Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellArea, Utils } = AsposeCells;

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
            // Create an instance of Workbook
            const book = new Workbook();

            // Access the first worksheet
            const sheet = book.worksheets.get(0);

            // Add FormatConditions to the instance of Worksheet
            let idx = sheet.conditionalFormattings.add();

            // Access the newly added FormatConditions via its index
            const conditionCollection = sheet.conditionalFormattings.get(idx);

            // Define a CellsArea on which conditional formatting will be applicable (A1 to I20)
            const area = CellArea.createCellArea("A1", "I20");

            // Add area to the instance of FormatConditions
            conditionCollection.addArea(area);

            // Add a condition to the instance of FormatConditions (Expression type)
            idx = conditionCollection.addCondition(AsposeCells.FormatConditionType.Expression);

            // Access the newly added FormatCondition via its index
            const formatCondition = conditionCollection.get(idx);

            // Set the formula for the FormatCondition
            formatCondition.formula1 = "=MOD(ROW(),2)=0";

            // Set the background color and pattern for the FormatCondition's Style
            formatCondition.style.backgroundColor = AsposeCells.Color.Blue;
            formatCondition.style.pattern = AsposeCells.BackgroundType.Solid;

            // Save the result and provide a download link
            const outputData = book.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conditional formatting applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


В следующем снимке экрана показан полученный электронный лист, загруженный в приложение Excel.

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_1.png)|
| :- |

Для применения засветки к альтернативным столбцам вам нужно изменить формулу **=MOD(ROW(),2)=0** на **=MOD(COLUMN(),2)=0**, то есть вместо получения индекса строки измените формулу для получения индекса столбца.  
Результирующая электронная таблица в этом случае будет выглядеть следующим образом.

|![todo:image_alt_text](apply-shading-to-alternate-rows-and-columns-with-conditional-formatting_2.png)|
| :- |
