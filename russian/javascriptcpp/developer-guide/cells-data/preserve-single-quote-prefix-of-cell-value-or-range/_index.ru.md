---
title: Сохранить одинарное кавычку перед значением ячейки или диапазоном
type: docs
weight: 310
url: /ru/javascript-cpp/preserve-single-quote-prefix-of-cell-value-or-range/
description: Изучите, как сохранить префикс одинарной кавычки значения ячейки или диапазона через API Aspose.Cells for JavaScript через C++.
keywords: Сохранение префикса одинарной кавычки значения ячейки или диапазона через JavaScript с использованием C++, скрытие ведущей апострофа или кавычки через JavaScript с использованием C++, показ ведущей апострофа или кавычки через JavaScript с использованием C++
---

## **Возможные сценарии использования**

Когда вы вводите значение в ячейку, которое имеет ведущий апостроф или одинарный знак кавычки, Microsoft Excel скрывает его, но когда вы выбираете ячейку, он отображает ведущий апостроф или одинарный знак в строке формул, как показано на следующем скриншоте.

![todo:image_alt_text](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Aspose.Cells for JavaScript через C++ также скрывает ведущий апостроф или кавычку, как в Microsoft Excel, но при этом устанавливает [**Style.quotePrefix**](https://reference.aspose.com/cells/javascript-cpp/style/#quotePrefix-boolean-) в значение **true** для этой ячейки. Если задать ячейке пустой стиль, то [**Style.quotePrefix**](https://reference.aspose.com/cells/javascript-cpp/style/#quotePrefix--) снова станет **false**. Для решения этой проблемы Aspose.Cells for JavaScript через C++ предоставляет свойство [**Style.quotePrefix**](https://reference.aspose.com/cells/javascript-cpp/style/#quotePrefix-boolean-). Когда оно установлено в **false**, то [**Style.quotePrefix**](https://reference.aspose.com/cells/javascript-cpp/style/#quotePrefix--) не обновляется вообще и сохраняет своё старое значение. Это означает, что если старое значение [**Style.quotePrefix**](https://reference.aspose.com/cells/javascript-cpp/style/#quotePrefix--) было **true**, оно останется **true**, а если старое — **false**, то останется **false**.

## **Сохранить префикс одинарной кавычки значения ячейки или диапазона**

Следующий пример кода иллюстрирует использование [**Style.quotePrefix**](https://reference.aspose.com/cells/javascript-cpp/style/#quotePrefix-boolean-), как описано ранее. Пожалуйста, прочтите комментарии в коде и посмотрите вывод в консоли для получения дополнительной информации.

## **Образец кода**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells QuotePrefix Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>QuotePrefix Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;"></a>
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
            const resultDiv = document.getElementById('result');
            const outputLines = [];

            // Create workbook
            const wb = new Workbook();

            // Access first worksheet
            const ws = wb.worksheets.get(0);

            // Access cell A1
            const cell = ws.cells.get("A1");

            // Put some text in cell, it does not have Single Quote at the beginning
            cell.value = "Text";

            // Access style of cell A1
            let st = cell.style;

            // Print the value of Style.QuotePrefix of cell A1
            outputLines.push("Quote Prefix of Cell A1: " + st.quotePrefix);

            // Put some text in cell, it has Single Quote at the beginning
            cell.value = "'Text";

            // Access style of cell A1
            st = cell.style;

            // Print the value of Style.QuotePrefix of cell A1
            outputLines.push("Quote Prefix of Cell A1: " + st.quotePrefix);

            // Print information about StyleFlag.QuotePrefix property
            outputLines.push("");
            outputLines.push("When StyleFlag.QuotePrefix is False, it means, do not update the value of Cell.Style.QuotePrefix.");
            outputLines.push("Similarly, when StyleFlag.QuotePrefix is True, it means, update the value of Cell.Style.QuotePrefix.");
            outputLines.push("");

            // Create an empty style
            st = wb.createStyle();

            // Create style flag - set StyleFlag.QuotePrefix as false
            // It means, we do not want to update the Style.QuotePrefix property of cell A1's style.
            let flag = new AsposeCells.StyleFlag();
            flag.quotePrefix = false;

            // Create a range consisting of single cell A1
            const rng = ws.cells.createRange("A1");

            // Apply the style to the range
            rng.applyStyle(st, flag);

            // Access the style of cell A1
            st = cell.style;

            // Print the value of Style.QuotePrefix of cell A1
            // It will print True, because we have not updated the Style.QuotePrefix property of cell A1's style.
            outputLines.push("Quote Prefix of Cell A1: " + st.quotePrefix);

            // Create an empty style
            st = wb.createStyle();

            // Create style flag - set StyleFlag.QuotePrefix as true
            // It means, we want to update the Style.QuotePrefix property of cell A1's style.
            flag = new AsposeCells.StyleFlag();
            flag.quotePrefix = true;

            // Apply the style to the range
            rng.applyStyle(st, flag);

            // Access the style of cell A1
            st = cell.style;

            // Print the value of Style.QuotePrefix of cell A1
            // It will print False, because we have updated the Style.QuotePrefix property of cell A1's style.
            outputLines.push("Quote Prefix of Cell A1: " + st.quotePrefix);

            // Update result div
            resultDiv.innerHTML = "<pre>" + outputLines.join("\n") + "</pre>";

            // Save the modified workbook and provide download link
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Resulting Excel File';
        });
    </script>
</html>
```



## **Вывод в консоль**

{{< highlight java >}}

Quote Prefix of Cell A1: False

Quote Prefix of Cell A1: True

When StyleFlag.quotePrefix is False, it means, do not update the value of Cell.Style.quotePrefix.

Similarly, when StyleFlag.quotePrefix is True, it means, update the value of Cell.Style.quotePrefix.

Quote Prefix of Cell A1: True

Quote Prefix of Cell A1: False

{{< /highlight >}}
