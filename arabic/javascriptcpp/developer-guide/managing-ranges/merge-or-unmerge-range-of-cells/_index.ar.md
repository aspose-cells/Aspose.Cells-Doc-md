---
title: دمج أو إلغاء دمج نطاق من الخلايا باستخدام JavaScript عبر C++
linktitle: دمج أو إلغاء دمج مجموعة من الخلايا
type: docs
weight: 190
url: /ar/javascript-cpp/merge-or-unmerge-range-of-cells/
description: دمج وفك دمج الخلايا في نطاق في إكسل باستخدام جافا سكريبت عبر ك++.
keywords: دمج وفك دمج الخلايا في جافا سكريبت في النطاق، دمج وفك دمج الخلايا في النطاق بجافا سكريبت، دمج وفك دمج الخلايا في النطاق باستخدام جافا سكريبت، دمج وفك دمج الخلايا في النطاق باستخدام جافا سكريبت، دمج وفك دمج الخلايا في إكسل باستخدام جافا سكريبت، دمج وفك دمج الخلايا في إكسل بجافا سكريبت، جافا سكريبت لدمج وفك دمج الخلايا في إكسل، دمج الخلايا في إكسل بجافا سكريبت، فك دمج الخلايا في إكسل بجافا سكريبت، دمج الخلايا في النطاق باستخدام جافا سكريبت
---

{{% alert color="primary" %}}

يمكنك استخدام Aspose.Cells لدمج أو تقسيم مجموعة من الخلايا. يوفر Aspose.Cells الأساليب [**Range.merge()**](https://reference.aspose.com/cells/javascript-cpp/range/#merge--) و [**Range.unMerge()**](https://reference.aspose.com/cells/javascript-cpp/range/#unMerge--) لهذا الغرض. يشرح هذا المقال كيفية دمج مجموعة من الخلايا في خلية واحدة.

{{% /alert %}}

## **مثال**

يعرض الكود النموذجي التالي أولاً إنشاء نطاق - A1:D4 - ثم دمج الخلايا في النطاق إلى خلية واحدة باستخدام الطريقة [**Range.merge()**](https://reference.aspose.com/cells/javascript-cpp/range/#merge--). بالمثل، يمكنك تقسيم الخلايا عن طريق إنشاء نطاق واستدعاء الطريقة [**Range.unMerge()**](https://reference.aspose.com/cells/javascript-cpp/range/#unMerge--).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Create and Merge Range Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

        let asposeInitialized = false;
        const runButton = document.getElementById('runExample');
        runButton.disabled = true;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
            asposeInitialized = true;
            runButton.disabled = false;
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            if (!asposeInitialized) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Aspose.Cells is not initialized yet. Please wait.</p>';
                return;
            }

            // Creating a workbook
            const workbook = new Workbook();

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Create a range
            const range = worksheet.cells.createRange("A1:D4");

            // Merge range into a single cell
            range.merge();

            // Saving the workbook
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and range merged successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
