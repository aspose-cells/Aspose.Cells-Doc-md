---
title: Как отформатировать число как валюту
type: docs
weight: 10
url: /ru/javascript-cpp/format-number-to-currency/
description: В этой статье рассказывается, как форматировать число в валюту с помощью Aspose.Cells for JavaScript через C++ API.
keywords: форматировать число как валюту, настройки чисел ячейки, форматировать число в валюту, настройки валюты, формат валюты.
---

## **Возможные сценарии использования**
Форматирование чисел в валюту в Excel важно по нескольким причинам, особенно при работе с финансовыми данными. Вот почему формат валюты полезен:

1. Уточнение финансовых значений: форматирование числа как валюты делает ясным, что значение представляет деньги. Например, вместо 1000, что может означать что угодно, $1,000 ясно указывает, что сумма денежная.
1. Включает символы валют: при работе с международными или несколькими валютами форматирование чисел с соответствующим символом (например, $, €, £) помогает понять тип используемой валюты, уменьшая путаницу в многонациональных отчетах или сделках.
1. Повышает профессиональный вид: хорошо отформатированные валютные значения выглядят аккуратно и профессионально, что особенно важно для отчетов, презентаций и деловых документов. $10 000,00 выглядит более надежным и организованным, чем просто 10000.
1. Улучшает читаемость: форматирование валюты добавляет запятые в качестве разделителей тысяч и десятичных знаков, что облегчает чтение больших чисел. Например, 1000000 становится $1,000,000.00, что намного удобнее для восприятия.
1. Обеспечивает последовательность: применяя согласованное форматирование валюты, вы гарантируете, что все денежные значения в наборе данных отображаются в одинаковом формате. Эта согласованность важна для финансовой точности и профессиональной коммуникации, особенно в больших таблицах с множеством чисел.
1. Показывает точность: форматирование валюты обычно включает две десятичные дроби, что облегчает просмотр точных денежных сумм. Например, $100.50 явно отличается от $100.00, что важно в финансовых отчетах, где важна точность.
1. Упрощает финансовые вычисления: при выполнении финансовых расчетов (например, сложение итогов или вычисление средних затрат) форматирование валюты помогает Excel и пользователям понять, что данные представлены в денежном выражении. Это помогает Excel правильно применять формат в формулах и функциях, обеспечивая согласованность результатов.
1. Снижение неправильного понимания: без форматирования валюты числа могут восприниматься как обычные числовые значения, а не как суммы денег. Например, 500 могут быть ошибочно восприняты как количество предметов или единиц, в то время как $500,00 явно представляет финансовую сумму.
1. Работает с бухгалтерскими функциями: форматирование валюты хорошо сочетается с бухгалтерскими функциями в Excel, такими как балансовые отчеты или отчеты о движении денежных средств. Оно облегчает использование значений в финансовых отчетах, где основное внимание уделяется деньгам.
<br>
В итоге, форматирование чисел в валюту помогает отличить денежные значения от других типов чисел, повышает ясность и делает данные более понятными для интерпретации, особенно в финансовом контексте.

## **Как форматировать число в валюту в Excel**
Чтобы отформатировать числа как валюту в Excel, выполните следующие шаги:

### **Использование опции Формат валюты**
1. Выберите ячейки, которые хотите отформатировать как валюту.
1. Перейдите на вкладку Главная на ленте.
1. В группе Число кликните по стрелке вниз рядом с полем формата числа (по умолчанию может отображаться "Общий").
<br>
<img src="1.png" width=60% />
1. Выберите из списка Валюта.

### **Использование диалогового окна Формат ячеек**
1. Выберите ячейки, которые хотите отформатировать.
1. Щелкните правой кнопкой мыши по выбранным ячейкам и выберите Формат ячеек, чтобы открыть диалоговое окно Формат ячеек.
1. Во вкладке Число выберите Валюта из списка слева.
<br>
<img src="2.png" width=60% />
1. Вы можете настроить следующее: число знаков после запятой, символ, отрицательные числа.
1. Нажмите ОК, чтобы применить форматирование.

## **Как форматировать число как валюту в Aspose.Cells**

Чтобы форматировать числа как валюту в Aspose.Cells for JavaScript через C++ библиотеку для работы с файлами Excel, вы можете программно применить форматирование валюты к ячейкам. Вот как это сделать, используя Aspose.Cells for JavaScript через C++:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Currency Formatting Example</h1>
        <p>Optionally select an Excel file to modify. If no file is selected, a new workbook will be created.</p>
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
            let workbook;

            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access the cell you want to format
            const a1 = worksheet.cells.get("A1");

            // Set a numeric value to the cell
            a1.value = 1234.56;

            // Create a style object to apply the currency format
            const a1Style = a1.style;
            // "7" is the currency format in Excel
            a1Style.number = 7;

            // Apply the style to the cell
            a1.style = a1Style;

            // Access the cell where you want to apply the currency format
            const a2 = worksheet.cells.get("A2");

            // Set a numeric value to the cell
            a2.value = 3456.78;

            // Create a style object to apply the currency format
            const a2Style = a2.style;
            // Custom format for dollar currency
            a2Style.custom = "$#,##0.00";

            // Apply the style to the cell
            a2.style = a2Style;

            // Saving the workbook and providing download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'CurrencyFormatted.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download CurrencyFormatted.xlsx';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook formatted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
