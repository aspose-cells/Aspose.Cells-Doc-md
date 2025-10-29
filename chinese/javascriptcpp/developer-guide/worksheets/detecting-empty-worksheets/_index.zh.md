---
title: 用 JavaScript 通过 C++ 侦测空白工作表
linktitle: 检测空工作表
type: docs
weight: 410
url: /zh/javascript-cpp/detecting-empty-worksheets/
description: 本文展示了如何使用 C++ 的 JavaScript API，通过代码检测 Excel 工作簿中空白工作表。
keywords: 用 C++ 通过 JavaScript 侦测空白工作表，寻找空的 Excel 工作表，JavaScript 通过 C++
---

## **检查已填充的单元格**

工作表可能包含一个或多个已填充值的单元格，这些值可以是简单（文本、数字、日期/时间）或基于公式的值或公式。这样，检测某个工作表是否为空就变得容易。只需检查[**Cells.maxDataRow**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxDataRow--)或[**Cells.maxDataColumn**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxDataColumn--)属性，如果这些属性返回零或正数，表示已填充一个或多个单元格；如果任何一个属性返回-1，则表示该工作表中没有已填充的单元格。

{{% alert color="primary" %}}

行和列集合索引从零开始；因此，位于第0行第0列的单元格即为工作表中的第一个单元格（A1）。

{{% /alert %}}

## **检测空初始化单元格**

所有具有值的单元格会自动初始化；但工作表中也可能只有格式应用的单元格。在这种情况下，[**Cells.maxDataRow**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxDataRow--)或[**Cells.maxDataColumn**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxDataColumn--)属性返回-1，表示没有已填充的值，但不能通过此方法检测仅格式化的已初始化单元格。为了检查工作表是否有空的已初始化单元格，建议使用从[**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells)集合获取的枚举器上的`Enumerator.MoveNext`方法。如果返回**true**，说明工作表中有一个或多个已初始化的单元格。

## **检查形状**

工作表可能没有任何已填充的单元格，但可能包含形状和对象，如控件、图表、图片等。如果需要检查工作表中是否包含任何形状，可以通过检查[**ShapeCollection.count**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#count--)属性。任何正值都表示工作表中存在形状。

## **编程示例**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Check Non-Empty Worksheets Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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

            // Instantiating a Workbook object from the uploaded file
            const book = new Workbook(new Uint8Array(arrayBuffer));

            const messages = [];

            // Loop over all worksheets in the workbook
            for (let i = 0; i < book.worksheets.count; i++) {
                const sheet = book.worksheets.get(i);
                // Check if worksheet has populated cells
                if (sheet.cells.maxDataRow !== -1) {
                    messages.push(`${sheet.name} is not empty because one or more cells are populated`);
                }
                // Check if worksheet has shapes
                else if (sheet.shapes.count > 0) {
                    messages.push(`${sheet.name} is not empty because there are one or more shapes`);
                }
                // Check if worksheet has empty initialized cells
                else {
                    const range = sheet.cells.maxDisplayRange;
                    const rangeIterator = range.getEnumerator();
                    if (rangeIterator.moveNext()) {
                        messages.push(`${sheet.name} is not empty because one or more cells are initialized`);
                    }
                }
            }

            if (messages.length) {
                resultDiv.innerHTML = '<ul>' + messages.map(m => `<li>${m}</li>`).join('') + '</ul>';
            } else {
                resultDiv.innerHTML = '<p style="color: green;">No non-empty worksheets found.</p>';
            }
        });
    </script>
</html>
```
