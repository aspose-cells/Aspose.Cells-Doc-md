---
title: 使用JavaScript和C++确定工作表的纸张大小是否为自动
linktitle: 确定工作表的纸张尺寸是否为自动
type: docs
weight: 90
url: /zh/javascript-cpp/determine-if-paper-size-of-worksheet-is-automatic/
description: 本文说明如何利用JavaScript API和C++插件以编程方式判断工作表的纸张大小是否设置为自动。
keywords: 使用JavaScript和C++判断工作表的纸张大小是否为自动
---

## **可能的使用场景**

大多时候，工作表的纸张大小是自动的。当设置为自动时，通常为*Letter*。有时用户会根据需求设置工作表的纸张大小。在这种情况下，纸张大小不是自动的。你可以利用 [**Worksheet.isAutomaticPaperSize()**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#isAutomaticPaperSize--) 属性判断工作表的纸张大小是否为自动。

## **确定工作表的纸张大小是否自动**

以下给出的示例代码加载以下两个Excel文件

- [samplePageSetupIsAutomaticPaperSize-False.xlsx](48496681.xlsx)
- [samplePageSetupIsAutomaticPaperSize-True.xlsx](48496682.xlsx)

并找到它们的第一个工作表的纸张尺寸是否为自动。在Microsoft Excel中，您可以通过页面设置窗口（如截图所示）检查纸张尺寸是否是自动的。

![todo:image_alt_text](determine-if-paper-size-of-worksheet-is-automatic_1.png)

## **示例代码**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - PageSetup IsAutomaticPaperSize</title>
    </head>
    <body>
        <h1>PageSetup IsAutomaticPaperSize Example</h1>
        <p>Select two Excel files to compare the PageSetup.isAutomaticPaperSize property:</p>
        <input type="file" id="fileInput1" accept=".xls,.xlsx,.csv" />
        <input type="file" id="fileInput2" accept=".xls,.xlsx,.csv" />
        <br/><br/>
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
            const fileInput1 = document.getElementById('fileInput1');
            const fileInput2 = document.getElementById('fileInput2');
            const resultDiv = document.getElementById('result');

            if (!fileInput1.files.length || !fileInput2.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select both Excel files.</p>';
                return;
            }

            const file1 = fileInput1.files[0];
            const file2 = fileInput2.files[0];

            const arrayBuffer1 = await file1.arrayBuffer();
            const arrayBuffer2 = await file2.arrayBuffer();

            // Instantiating Workbook objects from uploaded files
            const wb1 = new Workbook(new Uint8Array(arrayBuffer1));
            const wb2 = new Workbook(new Uint8Array(arrayBuffer2));

            // Access first worksheet of both workbooks
            const ws11 = wb1.worksheets.get(0);
            const ws12 = wb2.worksheets.get(0);

            // Read the PageSetup.isAutomaticPaperSize property of both worksheets
            const isAuto1 = ws11.pageSetup.isAutomaticPaperSize;
            const isAuto2 = ws12.pageSetup.isAutomaticPaperSize;

            // Display results
            resultDiv.innerHTML = `
                <p>First Worksheet of First Workbook - IsAutomaticPaperSize: ${isAuto1}</p>
                <p>First Worksheet of Second Workbook - IsAutomaticPaperSize: ${isAuto2}</p>
            `;
        });
    </script>
</html>
```

## **控制台输出**



{{< highlight java >}}

First Worksheet of First Workbook - IsAutomaticPaperSize: False

First Worksheet of Second Workbook - IsAutomaticPaperSize: True

{{< /highlight >}}
