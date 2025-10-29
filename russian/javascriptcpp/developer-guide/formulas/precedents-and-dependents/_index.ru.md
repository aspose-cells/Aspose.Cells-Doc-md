---
title: Предпосылки и зависимые ячейки с помощью JavaScript через C++
linktitle: Прецеденты и зависимые
type: docs
weight: 230
url: /ru/javascript-cpp/precedents-and-dependents/
description: Узнайте, как отслеживать предпосылки и зависимые ячейки в таблицах с помощью Aspose.Cells for JavaScript через C++. Поймите, как определить связанные ячейки в сложных финансовых листах.
---

{{% alert color="primary" %}} 

Сложные финансовые рабочие листы, особенно те, которые разработаны в сотрудничестве, могут скрывать наиболее нелестные ошибки. Проверка формул на точность и поиск источника ошибки может быть сложной, когда формула использует предшествующие и зависимые ячейки.

{{% /alert %}} 
## **Введение**
- **Предшествующие ячейки** - это ячейки, на которые ссылается формула в другой ячейке. Например, если ячейка D10 содержит формулу =B5, то ячейка B5 является предшествующей по отношению к ячейке D10.
- **Зависимые ячейки** содержат формулы, ссылающиеся на другие ячейки. Например, если ячейка D10 содержит формулу =B5, то D10 зависит от B5.

Чтобы сделать таблицу удобной для чтения, вы можете явно показать, какие ячейки в таблице используются в формулах. Точно так же, вы можете извлечь зависимые ячейки других ячеек.

Aspose.Cells позволяет отслеживать ячейки и выяснять, какие из них связаны между собой.
## **Отслеживание предшествующих и зависимых ячеек: Microsoft Excel**
Формулы могут изменяться в зависимости от изменений, внесенных клиентом. Например, если ячейка C1 зависит от того, что в C3 и C4 содержится формула, и C1 изменяется (что приводит к перезаписи формулы), то C3 и C4 или другие ячейки должны измениться, чтобы сбалансировать таблицу согласно правилам бизнеса.

Точно так же, предположим, что C1 содержит формулу "=(B1*22)/(M2*N32)". Я хочу найти ячейки, от которых зависит C1, то есть предшественники B1, M2 и N32.

Вам может потребоваться определить зависимость конкретной ячейки от других ячеек. Если деловые правила закодированы в формулах, мы хотели бы узнать зависимость и выполнить некоторые правила на ее основе. Точно так же, если значение конкретной ячейки изменено, какие ячейки в листе электронной таблицы затронуты этим изменением?

Microsoft Excel позволяет пользователям отслеживать предшественников и зависимых.

1. На **Панели инструментов Вид** выберите **Аудит формул**. Будет отображено диалоговое окно Аудит формул.
1. Следить за предшественниками:
   1. Выберите ячейку, содержащую формулу, для которой вы хотите найти предшествующие ячейки.
   1. Чтобы отобразить стрелку маршрута к каждой ячейке, которая непосредственно предоставляет данные для активной ячейки, щелкните **Отслеживание предшественников** на **Панели инструментов Проверка формул**.
1. Отследить формулы, которые ссылается на конкретную ячейку (зависимости)
   1. Введите ячейку, для которой вы хотите найти зависимые ячейки.
   1. Чтобы отображать стрелку-трассировщик для каждой зависимой от активной ячейки, нажмите **Следить за зависимыми** на панели инструментов Формульного аудита.
## **Отслеживание предшественников и зависимых ячеек: Aspose.Cells**
### **Отслеживание предшественников**
Aspose.Cells позволяет легко получить предшествующие ячейки. Он может не только извлекать ячейки, которые предоставляют данные для простых предшественников формул, но и находить ячейки, которые предоставляют данные для сложных предшественников формул с именованными диапазонами.

В приведенном ниже примере используется шаблонный файл Excel, Book1.xls. На первом листе электронной таблицы содержатся данные и формулы.

Aspose.Cells предоставляет метод [Cell.precedents()](https://reference.aspose.com/cells/javascript-cpp/cell/#precedents--) класса [Cell](https://reference.aspose.com/cells/javascript-cpp/cell), используемый для отслеживания предпосылок ячейки. Он возвращает коллекцию указанных областей. Как видно выше, в Book1.xls ячейка B7 содержит формулу "=SUM(A1:A3)". Таким образом, ячейки A1:A3 являются предпосылками для ячейки B7. Следующий пример демонстрирует функцию отслеживания предпосылок с использованием шаблонного файла Book1.xls.


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Get Cell Precedents Example</h1>
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

            // Access first worksheet's cells
            const cells = workbook.worksheets.get(0).cells;

            // Get cell B4
            const cell = cells.get("B4");

            if (cell) {
                // Get precedents (converted from getPrecedents)
                const ret = cell.precedents;

                if (!ret.isNull() && ret.count > 0) {
                    const area = ret.get(0);

                    const sheetName = area.sheetName;
                    const startAddress = AsposeCells.CellsHelper.cellIndexToName(area.startRow, area.startColumn);
                    const endAddress = AsposeCells.CellsHelper.cellIndexToName(area.endRow, area.endColumn);

                    console.log(sheetName);
                    console.log(startAddress);
                    console.log(endAddress);

                    document.getElementById('result').innerHTML = `<pre>Sheet: ${sheetName}\nStart: ${startAddress}\nEnd: ${endAddress}</pre>`;
                } else {
                    document.getElementById('result').innerHTML = '<p style="color: red;">No precedents found for the cell.</p>';
                }
            } else {
                document.getElementById('result').innerHTML = '<p style="color: red;">Cell B4 is null.</p>';
            }
        });
    </script>
</html>
```
### **Отслеживание зависимых**
Aspose.Cells позволяет получать зависимые ячейки в электронных таблицах. Aspose.Cells может не только извлекать ячейки, содержащие данные о простой формуле, но и находить ячейки, предоставляющие данные для сложных формул с именованными диапазонами.

Aspose.Cells предоставляет метод [Cell.dependents(boolean)](https://reference.aspose.com/cells/javascript-cpp/cell/#dependents-boolean-) класса [Cell](https://reference.aspose.com/cells/javascript-cpp/cell), используемый для отслеживания зависимых ячеек. Например, в Book1.xlsx в ячейках B2 и C2 есть формулы "=A1+20" и "=A1+30" соответственно. Следующий пример показывает, как отслеживать зависимые для ячейки A1 с использованием шаблонного файла Book1.xlsx.


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Get Cell Dependents Example</h1>
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Loads the workbook which contains hidden external links
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            const cells = workbook.worksheets.get(0).cells;
            const cell = cells.get("B2");
            // Ensure dependents is accessed as a property (converted from getDependents)
            const dependents = cell.dependents;

            if (Array.isArray(dependents)) {
                let out = '<p>Dependents found:</p><ul>';
                for (const c of dependents) {
                    console.log(c.name);
                    out += `<li>${c.name}</li>`;
                }
                out += '</ul>';
                resultDiv.innerHTML = out;
            } else {
                console.error("Dependents is not an array");
                resultDiv.innerHTML = '<p style="color: red;">Dependents is not an array</p>';
            }
        });
    </script>
</html>
```
### **Отслеживание предшествующих и зависимых ячеек в соответствии с цепочкой вычислений**
Вышеуказанные API для отслеживания предпосылок и зависимых ячеек соответствуют самим формулам. Они просто предоставляют удобный способ для пользователей отслеживать взаимозависимости для нескольких формул. Если в рабочей книге много формул и пользователю нужно отслеживать предпосылки и зависимые для каждой ячейки, это скажется на производительности. В таком случае рекомендуется использовать методы [Cell.precedentsInCalculation()](https://reference.aspose.com/cells/javascript-cpp/cell/#precedentsInCalculation--) и [Cell.dependentsInCalculation(boolean)](https://reference.aspose.com/cells/javascript-cpp/cell/#dependentsInCalculation-boolean-). Эти два метода отслеживают зависимости согласно цепочке вычислений. Для их использования необходимо включить цепочку вычислений с помощью [FormulaSettings.enableCalculationChain()](https://reference.aspose.com/cells/javascript-cpp/formulasettings/#enableCalculationChain--). После этого нужно выполнить полное вычисление рабочей книги через [Workbook.calculateFormula()](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--). После этого вы можете отслеживать предпосылки или зависимые для всех нужных ячеек.

Для некоторых формул результат предпосылок может отличаться при использовании precedents и precedentsInCalculation, а зависимых — при использовании dependents и dependentsInCalculation. Например, если формула ячейки A1 — "=IF(TRUE,B2,C3)", то предпосылками будут B2 и C3. Соответственно, B2 и C3 оба имеют зависимость A1 при проверке dependents. Однако для вычисления этой формулы очевидно, что только B2 влияет на результат. Поэтому precedentsInCalculation не укажет C3 для A1, а dependentsInCalculation — A1 для C3. Иногда пользователи просто хотят отслеживать те взаимозависимости, которые действительно влияют на вычисленный результат формул на основе текущих данных рабочей книги, и в этом случае им нужно использовать dependentsInCalculation/precedentsInCalculation вместо dependents/precedents.

Следующий пример демонстрирует, как отслеживать предков и зависимых в соответствии с цепочкой вычислений для ячеек:


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '';
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet and its cells
            const cells = workbook.worksheets.get(0).cells;

            // Setting formulas
            cells.get("A1").formula = "=B1+SUM(B1:B10)+[Book1.xls]Sheet1!B2";
            cells.get("A2").formula = "=IF(TRUE,B2,B1)";

            // Enable calculation chain
            workbook.settings.formulaSettings.enableCalculationChain = true;

            // Calculate formulas
            workbook.calculateFormula();

            // Collect output
            let output = '';

            let en = cells.get("B1").dependentsInCalculation;
            output += "B1's calculation dependents:\n";
            if (en && en.length !== undefined) {
                for (var cell of en) {
                    output += (cell.name || '') + "\n";
                }
            } else if (en) {
                // If it's an iterable but doesn't have length
                for (var cell of en) {
                    output += (cell.name || '') + "\n";
                }
            }
            output += "\n";

            en = cells.get("B2").dependentsInCalculation;
            output += "B2's calculation dependents:\n";
            if (en && en.length !== undefined) {
                for (var cell of en) {
                    output += (cell.name || '') + "\n";
                }
            } else if (en) {
                for (var cell of en) {
                    output += (cell.name || '') + "\n";
                }
            }
            output += "\n";

            en = cells.get("A1").precedentsInCalculation;
            output += "A1's calculation precedents:\n";
            if (en && en.length !== undefined) {
                for (var area of en) {
                    output += area.toString() + "\n";
                }
            } else if (en) {
                for (var area of en) {
                    output += area.toString() + "\n";
                }
            }
            output += "\n";

            en = cells.get("A2").precedentsInCalculation;
            output += "A2's calculation precedents:\n";
            if (en && en.length !== undefined) {
                for (var area of en) {
                    output += area.toString() + "\n";
                }
            } else if (en) {
                for (var area of en) {
                    output += area.toString() + "\n";
                }
            }

            resultDiv.innerHTML = '<pre>' + output.replace(/</g, '&lt;') + '</pre>';

            // Save the modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';
        });
    </script>
</html>
```
