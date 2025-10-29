---
title: 用 JavaScript 通过 C++ 查找工作表是否为对话框表
linktitle: 查找工作表是否为对话框工作表
type: docs
weight: 90
url: /zh/javascript-cpp/find-if-the-worksheet-is-dialog-sheet/
description: 本文提供用 Aspose.Cells for JavaScript 通过 C++ 判断 Excel 工作表是否为对话框表的指令和示例代码。
keywords: 用 C++ 通过 JavaScript 查找 Excel 工作表对话框类型，工作表对话框 JavaScript 通过 C++
---

## **可能的使用场景**

对话框工作表是包含对话框的旧格式工作表。此类工作表可以由老版本的Excel（如2003）插入，如截图所示，也可以通过VBA在较新版本（如Excel 2016）中插入。

![todo:image_alt_text](find-if-the-worksheet-is-dialog-sheet_1.png)

你可以使用 Aspose.Cells for JavaScript 通过 C++ 提供的 [**Worksheet.type**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#type--) 属性判断工作表是否为对话框表。如果返回枚举值 [**SheetType.Dialog**](https://reference.aspose.com/cells/javascript-cpp/sheettype)，则代表你面对的是对话框表。

## **查找工作表是否为对话框工作表**

以下示例代码加载了包含对话框工作表的示例Excel文件（64716820.xlsx）。它检查[**Worksheet.type**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#type--)属性，将其与[**SheetType.Dialog**](https://reference.aspose.com/cells/javascript-cpp/sheettype)比较，然后输出信息。请参阅下面的控制台输出以获取更多帮助。

## **示例代码**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Detect Dialog Sheet</title>
    </head>
    <body>
        <h1>Detect if Worksheet Is a Dialog Sheet</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const ws = workbook.worksheets.get(0);

            // Find if the sheet type is dialog and print the message
            if (ws.type === AsposeCells.SheetType.Dialog) {
                document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet is a Dialog Sheet.</p>';
            } else {
                document.getElementById('result').innerHTML = '<p>Worksheet is NOT a Dialog Sheet.</p>';
            }
        });
    </script>
</html>
```

## **控制台输出**

{{< highlight js >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
