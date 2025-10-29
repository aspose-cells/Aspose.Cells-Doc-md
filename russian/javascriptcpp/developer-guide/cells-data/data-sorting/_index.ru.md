---
title: Сортировка данных
type: docs
weight: 130
url: /ru/javascript-cpp/sort-data-of-excel/
description: Узнайте, как сортировать данные с помощью Aspose.Cells for JavaScript через API C++.
keywords: Сортировка данных в порядке возрастания или убывания, сортировка данных на основе цвета фона
---

{{% alert color="primary" %}}

Сортировка данных — одна из многих полезных функций Microsoft Excel. Она позволяет пользователям упорядочивать данные для облегчения просмотра. Aspose.Cells for JavaScript через C++ позволяет разработчикам сортировать листовые данные alphabetically или numerically аналогично тому, как это делает Microsoft Excel.

{{% /alert %}}

## **Сортировка данных в Microsoft Excel**

Чтобы отсортировать данные в Microsoft Excel:

1. Выберите **Данные** в меню **Сортировка**. В диалоговом окне сортировки будет отображаться.
1. Выберите вариант сортировки.

Обычно сортировка выполняется в списке - это непрерывная группа данных, отображаемых в столбцах.

## **Сортировка данных с помощью Aspose.Cells**

Aspose.Cells for JavaScript через C++ предоставляет класс [**DataSorter**](https://reference.aspose.com/cells/javascript-cpp/datasorter), используемый для сортировки данных по возрастанию или убыванию. У класса есть важные члены, например свойства Key1 ... Key3 и Order1 ... Order3. Эти члены используются для определения отсортированных ключей и указания порядка сортировки ключей.

Перед реализацией сортировки данных необходимо определить ключи и установить порядок сортировки. В классе предоставляется метод [**DataSorter.sort**](https://reference.aspose.com/cells/javascript-cpp/datasorter/#sort-cells-cellarea-), используемый для выполнения сортировки данных на основе данных ячейки на листе таблицы.

Метод [**DataSorter.sort**](https://reference.aspose.com/cells/javascript-cpp/datasorter/#sort-cells-cellarea-) принимает следующие параметры:

- [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells), ячейки для основного листа таблицы.
- [**CellArea**](https://reference.aspose.com/cells/javascript-cpp/cellarea), диапазон ячеек. Определите область ячеек перед применением сортировки данных.

В этом примере используется шаблонный файл "Book1.xls", созданный в Microsoft Excel. После выполнения приведенного ниже кода данные сортируются правильно.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>DataSorter Example</title>
    </head>
    <body>
        <h1>DataSorter Example</h1>
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

            // Instantiate a Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the workbook datasorter object.
            const sorter = workbook.dataSorter;

            // Set the first order for datasorter object.
            sorter.order1 = AsposeCells.SortOrder.Descending;
            // Define the first key.
            sorter.key1 = 0;
            // Set the second order for datasorter object.
            sorter.order2 = AsposeCells.SortOrder.Ascending;
            // Define the second key.
            sorter.key2 = 1;

            // Create a cells area (range).
            const ca = new AsposeCells.CellArea();
            // Specify the start row index.
            ca.startRow = 0;
            // Specify the start column index.
            ca.startColumn = 0;
            // Specify the last row index.
            ca.endRow = 13;
            // Specify the last column index.
            ca.endColumn = 1;

            // Sort data in the specified data range (A1:B14)
            sorter.sort(workbook.worksheets.get(0).cells, ca);

            // Save the excel file.
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Sorting completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

Если вы хотите выполнить сортировку *СлеваНаправо*, используйте атрибут [**DataSorter.sortLeftToRight**](https://reference.aspose.com/cells/javascript-cpp/datasorter/#sortLeftToRight-boolean-).

{{% /alert %}}

### **Сортировка данных с цветом фона**

Excel предоставляет функции сортировки данных по цвету фона. Аналогичная функция реализуется с помощью Aspose.Cells for JavaScript через C++, используя DataSorter, где [**SortOnType**](https://reference.aspose.com/cells/javascript-cpp/sortontype/).CellColor может применяться в [**DataSorter.addKey**](https://reference.aspose.com/cells/javascript-cpp/datasorter/#addColorKey-number-sortontype-sortorder-color-) для сортировки данных по цвету фона. Все ячейки с указанным цветом в функции размещаются вверху или внизу согласно настройке SortOrder, при этом порядок остальных ячеек не изменяется.

Ниже приведены образцовые файлы, которые можно загрузить для тестирования этой функции:

[sampleBackGroundFile.xlsx](81920906.xlsx)

[outputsampleBackGroundFile.xlsx](81920907.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Custom Sort by Cell Color</title>
    </head>
    <body>
        <h1>Custom Sort by Cell Color Example</h1>
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

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the data sorter (converted from getDataSorter())
            const sorter = workbook.dataSorter;

            // Add key for second column for red color
            sorter.addKey(1, AsposeCells.SortOnType.CellColor, AsposeCells.SortOrder.Descending, AsposeCells.Color.Red);

            // Perform the sort on the first worksheet cells (converted from getWorksheets().get(0).getCells())
            sorter.sort(workbook.worksheets.get(0).cells, AsposeCells.CellArea.createCellArea("A2", "C6"));

            // Save the modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSortData_CustomSortList.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Sorted Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Sorting completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Продвинутые темы**
- [Сортировка данных в столбце с пользовательским списком](/cells/ru/javascript-cpp/sort-data-in-column-with-custom-sort-list/)
- [Указание предупреждения при сортировке данных](/cells/ru/javascript-cpp/specifying-sort-warning-while-sorting-data/)
