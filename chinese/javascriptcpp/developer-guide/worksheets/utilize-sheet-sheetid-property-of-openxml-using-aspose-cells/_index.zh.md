---
title: 利用C++的Aspose.Cells for JavaScript使用OpenXml的Sheet.SheetId属性
linktitle: 使用 Aspose.Cells 利用 OpenXml 的 Sheet.SheetId 属性
type: docs
weight: 200
url: /zh/javascript-cpp/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/
description: 本文演示了如何利用C++的Aspose.Cells for JavaScript编程方式使用OpenXml的Sheet.SheetId属性进行Excel操作。
keywords: OpenXml的工作表id属性通过C++的JavaScript，Excel工作表的sheet id通过C++的JavaScript
---

## **可能的使用场景**

*Sheet.SheetId* 属性在 *DocumentFormat.OpenXml.Spreadsheet* 模块中可用，是 OpenXml 的一部分。你可以在 *workbook.xml* 中看到此属性及其值，如下图所示。Aspose.Cells 提供了等效的属性 [**Worksheet.tabId**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#tabId--)。

![todo:image_alt_text](utilize-sheet-sheetid-property-of-openxml-using-aspose-cells_1.png)

## **使用C++通过Aspose.Cells for JavaScript利用OpenXml的Sheet.SheetId属性**

以下示例代码加载了[示例Excel文件](51740716.xlsx)，读取其表格或标签ID，然后将其分配为新的标签ID并保存为[输出Excel文件](51740717.xlsx)。还请参见下方给出的代码的控制台输出作为参考。

## **示例代码**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Sheet Id Example</h1>
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

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const ws = workbook.worksheets.get(0);

            // Print its Sheet or Tab Id on console and show in page
            console.log("Sheet or Tab Id: " + ws.tabId);
            resultDiv.innerHTML = `<p>Original Sheet or Tab Id: ${ws.tabId}</p>`;

            // Change Sheet or Tab Id
            ws.tabId = 358;

            // Save the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSheetId.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML += `<p style="color: green;">Sheet Id changed to ${ws.tabId}. Click the download link to get the modified file.</p>`;
        });
    </script>
</html>
```

## **控制台输出**

{{< highlight text >}}

Sheet or Tab Id: 1297

{{< /highlight >}}
