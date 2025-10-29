---
title: 保留单引号前缀的单元格值或范围
type: docs
weight: 310
url: /zh/javascript-cpp/preserve-single-quote-prefix-of-cell-value-or-range/
description: 了解如何通过Aspose.Cells for Java脚本在C++ API中保持单引号前缀的单元格值或范围。
keywords: 使用JavaScript via C++保持单元格值或范围的单引号前缀，隐藏前导撇号或单引号，显示前导撇号或单引号JavaScript via C++
---

## **可能的使用场景**

当您在单元格中放入具有前导撇号或单引号标记的值时，Microsoft Excel会隐藏它，但当您选择单元格时，它会在公式栏中显示前导撇号或单引号，如下面的屏幕截图所示。

![todo:image_alt_text](preserve-single-quote-prefix-of-cell-value-or-range_1.png)

Aspose.Cells for Java脚本通过C++也会像Microsoft Excel一样隐藏前导撇号或单引号，但会将[**Style.quotePrefix**](https://reference.aspose.com/cells/javascript-cpp/style/#quotePrefix-boolean-)设为该单元格的**true**。如果将单元格的样式设为空，则[**Style.quotePrefix**](https://reference.aspose.com/cells/javascript-cpp/style/#quotePrefix--)变为**false**。为处理此问题，Aspose.Cells for Java脚本通过C++提供了[**Style.quotePrefix**](https://reference.aspose.com/cells/javascript-cpp/style/#quotePrefix-boolean-)属性。当设置为**false**时，[**Style.quotePrefix**](https://reference.aspose.com/cells/javascript-cpp/style/#quotePrefix--)不会被更新，旧值会被保留。这意味着如果旧值是**true**，仍为**true**；如果旧值是**false**，仍为**false**。

## **保留单引号前缀的单元格值或范围**

以下示例代码演示了前述[**Style.quotePrefix**](https://reference.aspose.com/cells/javascript-cpp/style/#quotePrefix-boolean-)的用法。请阅读代码中的注释，并查看下方给出的控制台输出以获得更多帮助。

## **示例代码**

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



## **控制台输出**

{{< highlight java >}}

Quote Prefix of Cell A1: False

Quote Prefix of Cell A1: True

When StyleFlag.quotePrefix is False, it means, do not update the value of Cell.Style.quotePrefix.

Similarly, when StyleFlag.quotePrefix is True, it means, update the value of Cell.Style.quotePrefix.

Quote Prefix of Cell A1: True

Quote Prefix of Cell A1: False

{{< /highlight >}}
