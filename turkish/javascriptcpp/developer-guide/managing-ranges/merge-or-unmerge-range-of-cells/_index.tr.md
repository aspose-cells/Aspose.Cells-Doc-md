---
title: JavaScript ile C++ kullanarak Hücre Aralığını Birleştir veya Birleştirmeyi Kaldır
linktitle: Hücre Aralığını Birleştirin veya Ayırın
type: docs
weight: 190
url: /tr/javascript-cpp/merge-or-unmerge-range-of-cells/
description: JavaScript ile C++ kodu kullanarak Excel de hücreleri Birleştir ve Ayırma.
keywords: JavaScript ile aralıkta hücreleri birleştir ve ayır, JavaScript ile aralıkta hücreleri birleştir ve ayır, JavaScript kullanarak aralıkta hücreleri birleştir ve ayır, JavaScript kullanarak hücreleri aralıkta birleştir ve ayır, JavaScript ile Excel de hücreleri birleştir ve ayır, JavaScript ile Excel de hücreleri birleştir ve ayır, JavaScript ile Excel de hücreleri birleştir ve ayır, JavaScript ile Excel de hücreleri birleştir, JavaScript ile Excel de hücreleri ayır, JavaScript ile aralıktaki hücreleri birleştir
---

{{% alert color="primary" %}}

Aspose.Cells'i kullanarak hücre aralığını birleştirmek veya bölmek için [**Range.merge()**](https://reference.aspose.com/cells/javascript-cpp/range/#merge--) ve [**Range.unMerge()**](https://reference.aspose.com/cells/javascript-cpp/range/#unMerge--) yöntemlerini kullanabilirsiniz. Bu makale, bir hücre aralığını tek bir hücreye birleştirmenin nasıl gerçekleştirileceğini açıklar.

{{% /alert %}}

## **Örnek**

Aşağıdaki örnek kod ilk olarak A1:D4 aralığını oluşturur, ardından [**Range.merge()**](https://reference.aspose.com/cells/javascript-cpp/range/#merge--) metodunu kullanarak aralıktaki hücreleri tek bir hücreye birleştirir. Benzer şekilde, hücreleri bölmek için bir aralık oluşturup [**Range.unMerge()**](https://reference.aspose.com/cells/javascript-cpp/range/#unMerge--) metodunu çağırabilirsiniz.

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
