---
title: JavaScript ile Çalışan Programları İzleme C++ kullanarak
linktitle: Çalışan Programları İzleme
type: docs
weight: 20
url: /tr/javascript-cpp/monitor-running-programs/
---

## ** Bir çalışan programı nasıl izlenir**

Aşağıdaki örnek kod, bir çalışmakta olan programı nasıl izleneceğini gösterir. Bu kod, [Workbook](https://reference.aspose.com/cells/javascript-cpp/workbook/) ile ilgili kodların izlenmesi için kullanılabilir. Sadece bir izleme nesnesi oluşturmak için [SystemTimeInterruptMonitor](https://reference.aspose.com/cells/javascript-cpp/systemtimeinterruptmonitor/) sınıfını kullanın, bunu [LoadOptions.interruptMonitor(AbstractInterruptMonitor)] fonksiyonu ile [LoadOptions](https://reference.aspose.com/cells/javascript-cpp/loadoptions/) çalışma parametrelerine ekleyin ve ardından beklenen kesme süresini (milisaniye cinsinden) ayarlamak için [startMonitor](https://reference.aspose.com/cells/javascript-cpp/systemtimeinterruptmonitor/#startMonitor-number-) fonksiyonunu kullanın. İzlenen kodun çalışma süresi beklenen zamanı aşarsa, program kesilir ve bir istisna fırlatılır.

## **Örnek Kod**

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
