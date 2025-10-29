---
title: Проверка того, что значение ячейки удовлетворяет правилам валидации данных
type: docs
weight: 210
url: /ru/javascript-cpp/verify-that-cell-value-satisfies-data-validation-rules/
description: Узнайте, как проверить, соответствует ли значение ячейки правилам проверки данных через API Aspose.Cells for JavaScript через C++.
keywords: Получить значение проверки ячейки JavaScript через C++, Получить значение проверки ячейки JavaScript через C++, Проверить, соответствует ли значение правилам проверки данных, примененным к ячейке, JavaScript через C++
---

{{% alert color="primary" %}} 

Microsoft Excel позволяет пользователям добавлять правила проверки данных к ячейкам. Например, правило дескриминативной проверки определяет, что могут вводиться только числа между 10 и 20. Если пользователь вводит другое число, Excel показывает сообщение об ошибке и предлагает ввести число в правильном диапазоне. Если вы копируете и вставляете число, например 3, в ячейку, проверка не запускается и сообщение об ошибке не показывается.

Иногда необходимо программно проверить, удовлетворяет ли значение правилам валидации данных, примененным к ячейке. В приведенном выше случае, например, ввод должен завершиться неудачей.

{{% /alert %}} 
## **Введение**
Aspose.Cells for JavaScript через C++ предоставляет свойство [Cell.validationValue](https://reference.aspose.com/cells/javascript-cpp/cell/#validationValue--) для программной проверки значений ячеек. Если значение в ячейке не удовлетворяет правилу проверки данных, примененному к этой ячейке, он возвращает **false**, иначе **true**.

Следующий пример кода иллюстрирует, как работает свойство [Cell.validationValue](https://reference.aspose.com/cells/javascript-cpp/cell/#validationValue--). Сначала вводится значение 3 в C1. Так как это не соответствует правилу проверки данных, свойство [Cell.validationValue](https://reference.aspose.com/cells/javascript-cpp/cell/#validationValue--) возвращает **false**. Затем вводится значение 15 в C1. Так как это значение соответствует правилу проверки данных, свойство [Cell.validationValue](https://reference.aspose.com/cells/javascript-cpp/cell/#validationValue--) возвращает **true**. Аналогично для значения 30, возвращает **false**.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Validation Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Validation Example</h1>
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
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access Cell C1
            // Cell C1 has the Decimal Validation applied on it.
            // It can take only the values Between 10 and 20
            const cell = worksheet.cells.get("C1");

            // Enter 3 inside this cell (not between 10 and 20)
            cell.value = 3;

            // Check if number 3 satisfies the Data Validation rule applied on this cell
            const valid3 = cell.validationValue;
            console.log("Is 3 a Valid Value for this Cell: " + valid3);
            resultDiv.innerHTML += `<p>Is 3 a Valid Value for this Cell: ${valid3}</p>`;

            // Enter 15 inside this cell (between 10 and 20)
            cell.value = 15;

            // Check if number 15 satisfies the Data Validation rule applied on this cell
            const valid15 = cell.validationValue;
            console.log("Is 15 a Valid Value for this Cell: " + valid15);
            resultDiv.innerHTML += `<p>Is 15 a Valid Value for this Cell: ${valid15}</p>`;

            // Enter 30 inside this cell (not between 10 and 20)
            cell.value = 30;

            // Check if number 30 satisfies the Data Validation rule applied on this cell
            const valid30 = cell.validationValue;
            console.log("Is 30 a Valid Value for this Cell: " + valid30);
            resultDiv.innerHTML += `<p>Is 30 a Valid Value for this Cell: ${valid30}</p>`;
        });
    </script>
</html>
```


### **Вывод**
{{< highlight javascript >}}

 Is 3 a Valid Value for this Cell: false

Is 15 a Valid Value for this Cell: true

Is 30 a Valid Value for this Cell: false

{{< /highlight >}}
