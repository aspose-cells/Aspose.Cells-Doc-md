---
title: Veri Sıralaması Yaparken Özel Sıralama Uyarısını Belirtme
type: docs
weight: 140
url: /tr/javascript-cpp/specifying-sort-warning-while-sorting-data/
description: Verileri sıralarken uyarı bildirimini nasıl belirleyeceğinizi öğrenin, Aspose.Cells for JavaScript ile C++ API kullanarak.
keywords: Veri sıralama işlemi yaparken sıralama uyarısı eklemek, veri sıralama sırasında sıralama uyarısı ayarlamak, veri sıralama sırasında sıralama uyarısı seçmek.
---

## **Olası Kullanım Senaryoları**

Lütfen bu metinsel veriyi dikkate alın, yani {11, 111, 22}. Bu metinsel veri sıralandı çünkü metin açısından 111, 22’den önce gelir. Ancak, bu verileri metin olarak değil sayısal olarak sıralamak istiyorsanız, o zaman {11, 22, 111} olur çünkü sayısal olarak 111, 22’den sonra gelir. Aspose.Cells for JavaScript C++ ile bu sorunu çözmek için {0} özelliği sağlar. Lütfen bu özelliği **true** olarak ayarlayın ve metinsel veriniz sayısal olarak sıralanacaktır. Aşağıdaki ekran görüntüsü, sayısal veri gibi görünen metinsel veriler sıralandığında Microsoft Excel tarafından gösterilen sıralama uyarısını göstermektedir.

![todo:image_alt_text](specifying-sort-warning-while-sorting-data_1.png)

## **Örnek Kod**

Aşağıdaki örnek kod, daha önce açıklandığı gibi [**DataSorter.sortAsNumber**](https://reference.aspose.com/cells/javascript-cpp/datasorter/#sortAsNumber-boolean-) özelliğinin kullanımını açıklar. Daha fazla yardım için lütfen [örnek Excel dosyasını](43352075.xlsx) ve [çıktı Excel dosyasını](43352076.xlsx) kontrol edin.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Sort As Number Example</title>
    </head>
    <body>
        <h1>Sort As Number Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellsHelper, CellArea, SortOrder } = AsposeCells;

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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Create your cell area.
            const ca = AsposeCells.CellArea.createCellArea("A1", "A20");

            // Create your sorter.
            const sorter = workbook.dataSorter;

            // Find the index for column A.
            const idx = CellsHelper.columnNameToIndex("A");

            // Add key in sorter, it will sort in Ascending order.
            sorter.addKey(idx, SortOrder.Ascending);

            // Set sort as number
            sorter.sortAsNumber = true;

            // Perform sort.
            sorter.sort(worksheet.cells, ca);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSortAsNumber.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Sort completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
