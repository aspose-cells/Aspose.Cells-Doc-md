---
title: Нахождение или Поиск Данных
type: docs
weight: 50
url: /ru/javascript-cpp/find-or-search-data/
description: Узнайте, как находить или искать ячейки в листе, содержащие указанные данные, через Aspose.Cells for JavaScript через C++ API.
keywords: Найти данные JavaScript через C++, Искать данные JavaScript через C++, Найти ячейки содержащие формулу JavaScript через C++, Искать ячейки содержащие формулу JavaScript через C++, Найти данные или формулы используя FindOptions JavaScript через C++, Искать данные или формулы используя FindOptions JavaScript через C++, Найти или Обыскать ячейки содержащие заданную строку или число JavaScript через C++, Найти или Обыскать ячейки содержащие заданные данные
---

{{% alert color="primary" %}}  
Microsoft Excel позволяет пользователям находить ячейки в листе, содержащие указанные данные.  
{{% /alert %}}  

## **Поиск ячеек, содержащих указанные данные**  

### **Использование Microsoft Excel**  

Microsoft Excel позволяет пользователям находить ячейки в листе, содержащие указанные данные. Если выбрать **Редактировать** в меню **Найти** Microsoft Excel, появится диалоговое окно, в котором можно указать значение поиска.  

Здесь мы ищем значение "Апельсины". Aspose.Cells также позволяет разработчикам находить ячейки в листе с указанными значениями.  

### **Использование Aspose.Cells for JavaScript через C++**  

Aspose.Cells предоставляет класс [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), который представляет файл Microsoft Excel. Класс [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) содержит коллекцию [**Workbook.worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--), позволяющую получить доступ к каждому листу в файле Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). Класс [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) предоставляет коллекцию [**cells**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#cells--), которая отображает все ячейки листа. Коллекция [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) содержит несколько методов для поиска ячеек, содержащих пользовательские данные. Некоторые из этих методов подробно рассматриваются ниже.  

{{% alert color="primary" %}}  
Все методы поиска возвращают ссылки на ячейки, содержащие указанные искомые данные.  
{{% /alert %}}  

## **Поиск ячеек, содержащих формулу**  

Разработчики могут найти заданную формулу в листе, вызвав метод [**find**](https://reference.aspose.com/cells/javascript-cpp/cells/#find-object-cell-findoptions-) коллекции [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells). Обычно метод [**find**](https://reference.aspose.com/cells/javascript-cpp/cells/#find-object-cell-findoptions-) принимает три параметра:  

-  Объект для поиска. Тип должен быть int, double, DateTime, string, bool.  
-  Предыдущая ячейка с этим объектом. Этот параметр можно установить в null, если поиск идет с начала.  
-  Опции для поиска нужного объекта.  

Ниже приведены примеры использования данных листа для тренировки методов поиска:  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Find Cell Containing Formula</title>
    </head>
    <body>
        <h1>Find Cell Containing Formula</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, FindOptions, LookInType } = AsposeCells;

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

            // Instantiating a Workbook object by opening the Excel file from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Instantiate FindOptions Object and set to look in formulas
            const findOptions = new FindOptions();
            findOptions.lookInType = LookInType.Formulas;

            // Finding the cell containing the specified formula
            const cell = worksheet.cells.find("=SUM(A5:A10)", null, findOptions);

            // Displaying the name of the cell found after searching worksheet
            document.getElementById('result').innerHTML = `<p style="color: green;">Name of the cell containing formula: ${cell.name}</p>`;
        });
    </script>
</html>
```  


## **Поиск данных или формул с использованием FindOptions**  

Возможно найти указанные значения, используя метод [**Cells.find(object, Cell)**](https://reference.aspose.com/cells/javascript-cpp/cells/#find-object-cell-) коллекции [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) с различными [**FindOptions**](https://reference.aspose.com/cells/javascript-cpp/findoptions). Обычно метод [**find**](https://reference.aspose.com/cells/javascript-cpp/cells/#find-object-cell-findoptions-) принимает следующие параметры:  

- **Значение поиска**, данные или значение для поиска.  
- **Предыдущая ячейка**, последняя ячейка, содержавшая то же значение. Этот параметр может быть установлен в null при поиске с начала.  
- **Параметры поиска**, параметры поиска.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Find Using FindOptions</title>
    </head>
    <body>
        <h1>Find Using FindOptions Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, FindOptions, CellArea, LookInType, LookAtType } = AsposeCells;

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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Calculate formulas in workbook
            workbook.calculateFormula();

            // Get Cells collection from first worksheet
            const cells = workbook.worksheets.get(0).cells;

            // Instantiate FindOptions Object
            const findOptions = new FindOptions();

            // Create a Cells Area
            const ca = new CellArea();
            ca.startRow = 8;
            ca.startColumn = 2;
            ca.endRow = 17;
            ca.endColumn = 13;

            // Set cells area for find options
            findOptions.range = ca;

            // Set searching properties
            findOptions.searchBackward = false;
            findOptions.searchOrderByRows = true;

            // Set the lookintype, you may specify, values, formulas, comments etc.
            findOptions.lookInType = LookInType.Values;

            // Set the lookattype, you may specify Match entire content, endswith, startswith etc.
            findOptions.lookAtType = LookAtType.EntireContent;

            // Find the cell with value
            const cell = cells.find(341, null, findOptions);

            if (cell !== null) {
                document.getElementById('result').innerHTML = `<p>Name of the cell containing the value: ${cell.name}</p>`;
            } else {
                document.getElementById('result').innerHTML = '<p>Record not found</p>';
            }
        });
    </script>
</html>
```  


## **Поиск ячеек, содержащих указанное строковое значение или число**  

Можно найти указанные строковые значения, вызвав тот же метод [**find**](https://reference.aspose.com/cells/javascript-cpp/cells/#find-object-cell-findoptions-) коллекции [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells) с различными [**FindOptions**](https://reference.aspose.com/cells/javascript-cpp/findoptions).  

Укажите свойства [**FindOptions.lookInType**](https://reference.aspose.com/cells/javascript-cpp/findoptions/#lookInType-lookintype-) и [**FindOptions.lookAtType**](https://reference.aspose.com/cells/javascript-cpp/findoptions/#lookAtType-lookattype-). Следующий пример показывает, как использовать эти свойства для поиска ячеек с различным количеством строк в **начале**, **посередине** или **в конце** строки ячейки.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Find Examples</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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

            // Instantiate the workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get Cells collection
            const cells = workbook.worksheets.get(0).cells;

            const opts = new AsposeCells.FindOptions();
            opts.lookInType = AsposeCells.LookInType.Values;
            opts.lookAtType = AsposeCells.LookAtType.EntireContent;

            let messages = '';

            // Find the cell with the input integer or double
            let cell1 = cells.find(205, null, opts);

            if (cell1 !== null) {
                messages += '<p>Name of the cell containing the value: ' + cell1.name + '</p>';
            } else {
                messages += '<p>Record not found</p>';
            }

            // Find the cell with the input string
            let cell2 = cells.find("Items A", null, opts);

            if (cell2 !== null) {
                messages += '<p>Name of the cell containing the value: ' + cell2.name + '</p>';
            } else {
                messages += '<p>Record not found</p>';
            }

            // Find the cell containing the input string (partial match)
            opts.lookAtType = AsposeCells.LookAtType.Contains;
            let cell3 = cells.find("Data", null, opts);

            if (cell3 !== null) {
                messages += '<p>Name of the cell containing the value: ' + cell3.name + '</p>';
            } else {
                messages += '<p>Record not found</p>';
            }

            document.getElementById('result').innerHTML = messages;
        });
    </script>
</html>
``` 



## **Продвинутые темы**  
- [Нахождение ячеек с определенным стилем](/cells/ru/javascript-cpp/find-cells-with-specific-style/)  
- [Определите, начинается ли значение ячейки с одинарной кавычки](/cells/ru/javascript-cpp/find-if-the-cell-value-starts-with-single-quote-mark/)  
- [Поиск данных с использованием исходных значений](/cells/ru/javascript-cpp/search-data-using-original-values/)
