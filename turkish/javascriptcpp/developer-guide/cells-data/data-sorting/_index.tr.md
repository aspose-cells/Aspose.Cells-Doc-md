---
title: Veri Sıralama
type: docs
weight: 130
url: /tr/javascript-cpp/sort-data-of-excel/
description: C++ API kullanarak veriyi sıralamayı öğrenin.
keywords: Verileri artan veya azalan sırada, arka plan rengine göre sıralama
---

{{% alert color="primary" %}}

Veri sıralama, Microsoft Excel'in birçok kullanışlı özelliklerinden biridir. Kullanıcıların verileri taramayı kolaylaştırmak için sıralamasına izin verir. C++ ile Aspose.Cells for JavaScript, sayfa içi verileri alfabetik veya sayısal olarak sıralamanıza olanak tanır; bu, Microsoft Excel'in veri sıralama işlemiyle aynıdır.

{{% /alert %}}

## **Microsoft Excel'de Veri Sıralama**

Microsoft Excel'de veri sıralamak için:

1. **Veri**'yi **Sırala** menüsünden seçin. Sırala iletişim kutusu görüntülenecektir.
1. Sıralama seçeneğini seçin.

Genellikle, sıralama bir liste üzerinde yapılır - verilerin sütunlarda gösterildiği, verilerin bağlantılı bir grup olduğu.

## **Aspose.Cells ile Veri Sıralama**

C++ ile Aspose.Cells for JavaScript, veriyi artan veya azalan sırayla sıralamak için kullanılan [**DataSorter**](https://reference.aspose.com/cells/javascript-cpp/datasorter) sınıfını sağlar. Bu sınıfın bazı önemli üyeleri vardır; örneğin, Key1 ... Key3 ve Order1 ... Order3 gibi özellikler. Bu üyeler, sıralanmış anahtarları tanımlar ve anahtar sıralama düzenini belirler.

Veri sıralaması gerçekleştirmeden önce anahtarları tanımlamalı ve sıralama düzenini belirlemelisiniz. Sınıf, çalışsayadaki hücre verilerine dayalı veri sıralamasını gerçekleştirmek için kullanılan [**DataSorter.sort**](https://reference.aspose.com/cells/javascript-cpp/datasorter/#sort-cells-cellarea-) yöntemini sağlar.

[**DataSorter.sort**](https://reference.aspose.com/cells/javascript-cpp/datasorter/#sort-cells-cellarea-) yöntemi aşağıdaki parametreleri kabul eder:

- [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells), altındaki çalışsayadaki hücreler.
- [**CellArea**](https://reference.aspose.com/cells/javascript-cpp/cellarea), hücre aralığı. Veri sıralaması uygulamadan önce hücre alanını tanımlayın.

Bu örnek, Microsoft Excel'de oluşturulmuş "Book1.xls" şablon dosyasını kullanır. Aşağıdaki kodu çalıştırdıktan sonra, veri uygun bir şekilde sıralanır.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>DataSorter Example</title>
    </head>
    <body>
        <h1>DataSorter Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the workbook datasorter object.
            const sorter = workbook.dataSorter;

            // Set the first order for datasorter object.
            sorter.order1 = AsposeCells.SortOrder.Descending;
            // Define the first key.
            sorter.key1 = 0;
            // Set the second order for datasorter object.
            sorter.order2 = AsposeCells.SortOrder.Ascending;
            // Define the second key.
            sorter.key2 = 1;

            // Create a cells area (range).
            const ca = new AsposeCells.CellArea();
            // Specify the start row index.
            ca.startRow = 0;
            // Specify the start column index.
            ca.startColumn = 0;
            // Specify the last row index.
            ca.endRow = 13;
            // Specify the last column index.
            ca.endColumn = 1;

            // Sort data in the specified data range (A1:B14)
            sorter.sort(workbook.worksheets.get(0).cells, ca);

            // Save the excel file.
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Sorting completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

*Soldan Sağa* sıralamak istiyorsanız, [**DataSorter.sortLeftToRight**](https://reference.aspose.com/cells/javascript-cpp/datasorter/#sortLeftToRight-boolean-) özniteliğini kullanın.

{{% /alert %}}

### **Arka plan rengine göre veri sıralama**

Excel, arka plan rengine göre veriyi sıralama özellikleri sağlar. Aynı özellik, Aspose.Cells for JavaScript kullanılarak DataSorter aracılığıyla, [**SortOnType**](https://reference.aspose.com/cells/javascript-cpp/sortontype/).CellColor kullanılarak [**DataSorter.addKey**](https://reference.aspose.com/cells/javascript-cpp/datasorter/#addColorKey-number-sortontype-sortorder-color-) içinde veriyi arka plan rengine göre sıralamak için kullanılır. [**DataSorter.addKey**](https://reference.aspose.com/cells/javascript-cpp/datasorter/#addColorKey-number-sortontype-sortorder-color-) içindeki belirtilen renkleri içeren tüm hücreler, SortOrder ayarına göre yukarı veya aşağı yerleştirilir ve kalan hücrelerin sırası değiştirilmez.

Bu özelliği test etmek için indirilebilecek örnek dosyalar aşağıda sunulmuştur:

[sampleBackGroundFile.xlsx](81920906.xlsx)

[outputsampleBackGroundFile.xlsx](81920907.xlsx)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Custom Sort by Cell Color</title>
    </head>
    <body>
        <h1>Custom Sort by Cell Color Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the data sorter (converted from getDataSorter())
            const sorter = workbook.dataSorter;

            // Add key for second column for red color
            sorter.addKey(1, AsposeCells.SortOnType.CellColor, AsposeCells.SortOrder.Descending, AsposeCells.Color.Red);

            // Perform the sort on the first worksheet cells (converted from getWorksheets().get(0).getCells())
            sorter.sort(workbook.worksheets.get(0).cells, AsposeCells.CellArea.createCellArea("A2", "C6"));

            // Save the modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSortData_CustomSortList.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Sorted Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Sorting completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **Gelişmiş Konular**
- [Özel Sıralama Listesi ile Sütunda Verileri Sıralama](/cells/tr/javascript-cpp/sort-data-in-column-with-custom-sort-list/)
- [Veri Sıralama Sırasında Uyarıyı Belirtme](/cells/tr/javascript-cpp/specifying-sort-warning-while-sorting-data/)
