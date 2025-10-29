---
title: 使用JavaScript通过C++监控运行中的程序
linktitle: 监控运行中的程序
type: docs
weight: 20
url: /zh/javascript-cpp/monitor-running-programs/
---

## **如何监控运行中的程序**

 以下示例代码演示如何监控一个运行中的程序。此代码可用于监控[Workbook](https://reference.aspose.com/cells/javascript-cpp/workbook/)相关代码。只需使用[SystemTimeInterruptMonitor](https://reference.aspose.com/cells/javascript-cpp/systemtimeinterruptmonitor/)类创建监控对象，使用[LoadOptions.interruptMonitor(AbstractInterruptMonitor)](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#interruptMonitor-abstractinterruptmonitor-)方法添加到[LoadOptions](https://reference.aspose.com/cells/javascript-cpp/loadoptions/)参数中，然后用[startMonitor](https://reference.aspose.com/cells/javascript-cpp/systemtimeinterruptmonitor/#startMonitor-number-)函数设置预期中断时间（毫秒）。如果监控代码的运行时间超出预期，程序将中断并抛出异常。

## **示例代码**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Interrupt Monitor Example</title>
    </head>
    <body>
        <h1>Interrupt Monitor Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, LoadOptions, SystemTimeInterruptMonitor, SaveFormat, Utils } = AsposeCells;

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

            // Create interrupt monitor and load options
            const monitor = new SystemTimeInterruptMonitor(false);
            const lopts = new LoadOptions();
            lopts.interruptMonitor = monitor;
            monitor.startMonitor(1000); // time limit is 1 second

            // Load the workbook with the specified load options
            const wb = new Workbook(new Uint8Array(arrayBuffer), lopts);

            // If loading completed within time, start monitoring save
            monitor.startMonitor(1500); // time limit is 1.5 seconds
            const outputData = wb.save(SaveFormat.Xlsx);

            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'result.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Result.xlsx';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the resulting file.</p>';
        });
    </script>
</html>
```
