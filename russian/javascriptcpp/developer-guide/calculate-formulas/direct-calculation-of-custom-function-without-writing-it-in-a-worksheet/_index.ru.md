---
title: Прямой расчет пользовательской функции без её записи в лист с помощью JavaScript через C++
linktitle: Прямой расчет пользовательской функции без записи ее в рабочий лист
description: В этой статье рассказывается, как использовать библиотеку Aspose.Cells для прямого расчета пользовательских функций в Microsoft Excel без их записи в лист, с помощью JavaScript через C++. Загрузите существующий файл Excel или создайте новый, вычислите пользовательскую функцию и сохраните измененный файл.
keywords: Aspose.Cells, Excel, пользовательские функции, прямые вычисления, JavaScript через C++, без необходимости писать, листы
type: docs
weight: 90
url: /ru/javascript-cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
---

## **Прямой расчет пользовательской функции без записи ее на лист**

Эта тема объясняет, как напрямую вычислить ваши пользовательские функции, не записывая их предварительно в лист. Пожалуйста, используйте метод [**Worksheet.calculateFormula(formula, opts)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#calculateFormula-string-CalculationOptions-) для этой цели.

Пожалуйста, ознакомьтесь с приведенным ниже образцом кода, иллюстрирующим использование этого метода. Мы использовали пользовательскую функцию MyCompany.CustomFunction() и рассчитываем ее значение как "Aspose.Cells." сами, после чего это значение автоматически конкатенируется со значением ячейки A1, которая равна "Добро пожаловать в " движком расчета, и окончательное рассчитанное значение возвращается как "Добро пожаловать в Aspose.Cells.". Как видно из кода, мы не писали нашу пользовательскую функцию где-либо на рабочем листе, и она рассчитывается напрямую нашей собственной пользовательской логикой.

### **Пример программирования**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Custom Function Example</title>
    </head>
    <body>
        <h1>Implement Direct Calculation Of Custom Function</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, AbstractCalculationEngine, CalculationOptions } = AsposeCells;

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

        class CustomEngine extends AbstractCalculationEngine {
            // Override the calculate method with custom logic
            calculate(data) {
                // Check the formula name and calculate it yourself
                if (data.functionName === "MyCompany.CustomFunction") {
                    // This is our calculated value
                    data.calculatedValue = "Aspose.Cells.";
                }
            }
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                // Create a new workbook if no file is provided
                workbook = new Workbook();
            }

            // Access first worksheet
            const ws = workbook.worksheets.get(0);

            // Add some text in cell A1
            ws.cells.get("A1").putValue("Welcome to ");

            // Create a calculation options with custom engine
            const opts = new CalculationOptions();
            opts.customEngine = new CustomEngine();

            // This line shows how you can call your own custom function without
            // a need to write it in any worksheet cell
            // After the execution of this line, it will return
            // Welcome to Aspose.Cells.
            const ret = ws.calculateFormula("=A1 & MyCompany.CustomFunction()", opts);

            // Write the returned value into B1 for demonstration
            ws.cells.get("B1").putValue(ret);

            // Prepare download of the modified workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Calculated Value: ' + ret + '</p>';
        });
    </script>
</html>
```

### **Вывод в консоль**

Ниже приведен вывод консоли приведенного выше образца кода.

{{< highlight javascript >}}

Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}

### **Связанная статья**

{{% alert color="primary" %}}

[Реализовать движок пользовательских расчетов для расширения стандартного движка расчетов Aspose.Cells](/cells/ru/javascript-cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}}
