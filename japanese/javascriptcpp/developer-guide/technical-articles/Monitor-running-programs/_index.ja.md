---
title: JavaScript経由のC++で実行中のプログラムを監視
linktitle: 実行中のプログラムの監視
type: docs
weight: 20
url: /ja/javascript-cpp/monitor-running-programs/
---

## **実行中のプログラムの監視方法**

 以下のサンプルコードは、実行中のプログラムを監視する方法を示しています。このコードは[Workbook](https://reference.aspose.com/cells/javascript-cpp/workbook/)関連のコードの監視に使用できます。単に[SystemTimeInterruptMonitor](https://reference.aspose.com/cells/javascript-cpp/systemtimeinterruptmonitor/)クラスを使用して監視オブジェクトを作成し、[LoadOptions.interruptMonitor(AbstractInterruptMonitor)](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#interruptMonitor-abstractinterruptmonitor-)関数を使ってこれを[LoadOptions](https://reference.aspose.com/cells/javascript-cpp/loadoptions/)の実行パラメータに追加し、次に[startMonitor](https://reference.aspose.com/cells/javascript-cpp/systemtimeinterruptmonitor/#startMonitor-number-)関数を使って期待される停止時間（ミリ秒）を設定します。監視中のコードの実行時間が予想時間を超えた場合、プログラムは中断され、例外がスローされます。

## **サンプルコード**

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
