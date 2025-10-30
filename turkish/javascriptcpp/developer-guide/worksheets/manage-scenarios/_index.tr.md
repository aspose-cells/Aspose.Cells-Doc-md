---
title: Çalışma Sayfalarından Senaryolar Oluşturma, Manipüle Etme veya Kaldırma ile JavaScript kullanarak C++
linktitle: Senaryoları Yönetme
type: docs
weight: 190
url: /tr/javascript-cpp/create-manipulate-or-remove-scenarios-from-worksheets/
description: JavaScript ve C++ API kullanarak Excel Çalışma Sayfalarından senaryolar oluşturmayı, değiştirmeyi veya kaldırmayı öğrenin.
keywords: Çalışma sayfası senaryosu oluşturma JavaScript ile C++, senaryoyu kaldırma JavaScript ile C++, senaryo üzerinde manipülasyon JavaScript ile C++
---

{{% alert color="primary" %}}

Bazen Elektronik Tablolarda senaryolar oluşturmanızı, manipüle etmenizi veya silmenizi gerekebilir. Senaryo, bir veya daha fazla formülle bağlı değişken giriş hücrelerini içeren adlandırılmış 'ne olurdu?' modelidir. Bir senaryo oluşturmadan önce, farklı değerlerin eklenebileceği en az bir formül içeren çalışma sayfasını tasarlayın. Aşağıdaki örnek, Aspose.Cells API'leri aracılığıyla bir iş kitabındaki bir çalışma sayfasından senaryolar oluşturmayı ve kaldırmayı gösterir.

{{% /alert %}}

Aspose.Cells, bazı kullanışlı sınıflar sağlar, örneğin [**ScenarioCollection**](https://reference.aspose.com/cells/javascript-cpp/scenariocollection), [**Scenario**](https://reference.aspose.com/cells/javascript-cpp/scenario), [**ScenarioInputCellCollection**](https://reference.aspose.com/cells/javascript-cpp/scenarioinputcellcollection) ve [**ScenarioInputCell**](https://reference.aspose.com/cells/javascript-cpp/scenarioinputcell) sınıfları. Ayrıca [**Worksheet.scenarios**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#scenarios--) özelliği de mevcuttur. Aşağıdaki örnek kod, bazı senaryolar içeren bir XLSX Excel dosyasını açar ve mevcut bir senaryoyu kaldırır. Ayrıca, Excel dosyasını kaydetmeden önce çalışma sayfasına yeni bir senaryo ekler. Bu örnek, çok basit bir şablon dosyası kullanır ve içinde bir senaryo bulunur.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Scenarios Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Scenarios Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
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
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate the Workbook by loading the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            if (worksheet.scenarios.count > 0) {
                // Remove the existing first scenario from the sheet
                worksheet.scenarios.removeAt(0);
            }

            // Create a scenario
            const i = worksheet.scenarios.add("MyScenario");
            // Get the scenario
            const scenario = worksheet.scenarios.get(i);
            // Add comment to it
            scenario.comment = "Test scenario is created.";
            // Get the input cells for the scenario
            const sic = scenario.inputCells;
            // Add the scenario on B4 (as changing cell) with default value
            sic.add(3, 1, "1100000");

            // Save the Excel file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outBk_scenarios1.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Process completed successfully. File ready for download.</p>';
        });
    </script>
</html>
```
