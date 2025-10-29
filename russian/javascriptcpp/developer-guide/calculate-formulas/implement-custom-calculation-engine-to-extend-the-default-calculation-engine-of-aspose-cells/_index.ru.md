---
title: Реализуйте пользовательский движок расчетов для расширения стандартного движка расчетов Aspose.Cells с помощью JavaScript через C++
linktitle: Реализация собственного расчетного механизма для расширения стандартного расчетного механизма Aspose.Cells
description: В этой статье описывается, как расширить стандартный движок расчетов с помощью реализации пользовательского движка с помощью библиотеки Aspose.Cells для JavaScript via C++. Загрузите существующий файл Excel или создайте новый, используйте предоставленные методы и сохраните измененный файл.
keywords: Aspose.Cells, Excel, пользовательский движок расчетов, JavaScript через C++
type: docs
weight: 80
url: /ru/javascript-cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---

## **Реализация пользовательского расчетного движка**

Aspose.Cells имеет мощный расчетный механизм, который может рассчитывать практически все формулы Microsoft Excel. Тем не менее, он также позволяет вам расширять стандартный расчетный механизм для обеспечения вам большей мощности и гибкости.

Следующие свойства и классы используются при реализации этой функции.

- [**CalculationOptions.customEngine**](https://reference.aspose.com/cells/javascript-cpp/calculationoptions/#customEngine--)
- [**AbstractCalculationEngine**](https://reference.aspose.com/cells/javascript-cpp/abstractcalculationengine)
- [**CalculationData**](https://reference.aspose.com/cells/javascript-cpp/calculationdata)

Следующий код реализует пользовательский движок расчетов. Он реализует интерфейс [**AbstractCalculationEngine**](https://reference.aspose.com/cells/javascript-cpp/abstractcalculationengine), который содержит метод [**calculate(CalculationData data)**](https://reference.aspose.com/cells/javascript-cpp/abstractcalculationengine/#calculate-calculationdata-). Этот метод вызывается для всех ваших формул. Внутри этого метода мы захватываем функцию **TODAY** и добавляем один день к системной дате. Таким образом, если текущая дата 27/07/2023, то пользовательский движок будет вычислять TODAY() как 28/07/2023.

### **Пример программирования**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Custom Calculation Engine Example</title>
    </head>
    <body>
        <h1>Custom Calculation Engine Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample" disabled>Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CalculationOptions, CellsHelper } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
            document.getElementById('runExample').disabled = false;
        });

        // Create a new class derived from AbstractCalculationEngine
        class CustomEngine extends AsposeCells.AbstractCalculationEngine {
            constructor() {
                super();
                // Indicate processing built-in functions
                this.processBuiltInFunctions = true;
            }

            // Override the Calculate method with custom logic
            calculate(data) {
                // Check the formula name and change the implementation
                if (data.functionName.toUpperCase() === "TODAY") {
                    // Assign the CalculationData.CalculatedValue: add one day offset for the date
                    data.calculatedValue = CellsHelper.getDoubleFromDateTime(new Date(), false) + 1.0;
                }
            }
        }

        class ImplementCustomCalculationEngine {
            static run() {
                // Create an instance of Workbook
                const workbook = new Workbook();

                // Access first Worksheet from the collection
                const sheet = workbook.worksheets.get(0);

                // Access Cell A1 and put a formula to sum values of B1 to B2
                const a1 = sheet.cells.get("A1");
                const style = a1.style;
                style.number = 14;
                a1.style = style;

                a1.formula = "=TODAY()";

                // Calculate all formulas in the Workbook 
                workbook.calculateFormula();

                // The result of A1 with default calculation engine
                console.log("The value of A1 with default calculation engine: " + a1.stringValue);

                // Create an instance of CustomEngine
                const engine = new CustomEngine();

                // Create an instance of CalculationOptions
                const opts = new CalculationOptions();

                // Assign the CalculationOptions.CustomEngine property to the instance of CustomEngine
                opts.customEngine = engine;

                // Recalculate all formulas in Workbook using the custom calculation engine
                workbook.calculateFormula(opts);

                // The result of A1 with custom calculation engine
                console.log("The value of A1 with custom calculation engine: " + a1.stringValue);

                console.log("Press any key to continue...");

                document.getElementById('result').innerHTML = '<p style="color: green;">Calculation completed. Check console for output.</p>';
            }
        }

        document.getElementById('runExample').addEventListener('click', () => {
            ImplementCustomCalculationEngine.run();
        });
    </script>
</html>
```

### **Результат**

Пожалуйста, проверьте вывод консоли приведенного выше примера кода; значение (дата и время) A1 с пользовательским движком должно быть на один день позже результата без него.

### **Связанная статья**

{{% alert color="primary" %}}

[Прямой расчет пользовательской функции без её записи в лист](/cells/ru/javascript-cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}
