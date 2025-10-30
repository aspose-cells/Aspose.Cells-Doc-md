---
title: C++ kullanarak JavaScript ile Aralıkta Veri Arama ve Değiştirme
linktitle: Excel de Bir Aralıktaki Verileri Arama ve Değiştirme
type: docs
weight: 170
url: /tr/javascript-cpp/search-and-replace-data-in-a-range/
description: Bu makale, C++ kullanarak Excel de bir aralıkta veri arama ve değiştirme nasıl yapılır gösterir.
keywords: Javascript ile Excel de veri arama ve değiştirme, Javascript ile Excel de veri arama, Javascript ile bir aralıkta veri arama ve değiştirme, Javascript ile aralıkta veri arama, Javascript ile aralıkta veri arama, Javascript ile aralıkta veri arama, Javascript ile Excel de veri arama, Javascript ile aralıkta veri arama, Javascript ile Excel de veri arama ve değiştir, Javascript ile aralıkta veri arama ve değiştirme, Javascript ile aralıkta veri arama ve değiştirme
---

{{% alert color="primary" %}}

Bazen, belirli bir aralıkta arama ve değiştirme yapmak gerekir, istenmeyen hücre değerlerini dikkate almadan. C++ kullanarak JavaScript ile belirli bir aralığa arama sınırlandırması yapılabilir. Bu makalede açıklanmıştır.

{{% /alert %}}

C++ kullanarak JavaScript ile [**FindOptions.range(CellArea)**](https://reference.aspose.com/cells/javascript-cpp/findoptions/#range-cellarea-) yöntemi, bir veri ararken aralık belirtmek için kullanılır. Aşağıdaki örnek, bir aralıkta veri arama ve değiştirme işlemi yapmaktadır.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Find and Replace Example</title>
    </head>
    <body>
        <h1>Find and Replace Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellArea, FindOptions, LookInType, LookAtType } = AsposeCells;

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

            // Instantiating a Workbook object by loading the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Define the search range (E9:H15)
            const area = CellArea.createCellArea("E9", "H15");

            // Configure find options
            const opts = new FindOptions();
            opts.lookInType = LookInType.Values;
            opts.lookAtType = LookAtType.EntireContent;
            opts.range = area;

            let cell = null;

            do {
                cell = worksheet.cells.find("search", cell, opts);
                if (cell === null || cell.isNull()) {
                    break;
                }
                // Replace found cell's value
                cell.value = "replace";
            } while (true);

            // Saving the modified Excel file and providing a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Find and replace completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
