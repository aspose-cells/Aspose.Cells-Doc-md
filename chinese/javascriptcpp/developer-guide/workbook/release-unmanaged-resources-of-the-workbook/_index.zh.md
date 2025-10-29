---
title: 释放工作簿的未托管资源（JavaScript通过C++）
linktitle: 释放工作簿的非托管资源
type: docs
weight: 310
url: /zh/javascript-cpp/release-unmanaged-resources-of-the-workbook/
description: 学习如何使用Aspose.Cells for JavaScript通过C++释放Workbook对象的未托管资源。 
---

{{% alert color="primary" %}}

Aspose.Cells 提供 [**Workbook.dispose()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#dispose--) 方法以释放 [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) 对象的非托管资源。Dispose 模式仅用于访问非托管资源的对象，例如文件和管道句柄、注册表句柄、等待句柄或指向非托管内存块的指针。这是因为垃圾收集器在回收未使用的托管对象方面非常高效，但无法回收非托管对象。

{{% /alert %}}

[**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) 对象现在实现了 *System.IDisposable* 接口，该接口包含唯一的方法 [**Workbook.dispose()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#dispose--)。你可以直接调用 [**Workbook.dispose()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#dispose--) 方法，或者使用 *Using* 语句自动调用此方法。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Dispose Example</h1>
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

            // Loads the workbook which contains hidden external links
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create workbook object
            const wb1 = new Workbook();

            // Call Dispose method
            wb1.dispose();

            // Call Dispose method via a scoped approach
            (async () => {
                const wb2 = new Workbook();
                // Any other code goes here
                wb2.dispose();
            })();

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully!</p>';
        });
    </script>
</html>
```
