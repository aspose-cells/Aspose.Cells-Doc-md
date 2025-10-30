---
title: Excel Çalışma Sayfasında Satır Eklemek veya Silmek İçin JavaScript ve C++ ile
linktitle: Bir Excel Çalışma Sayfasına Satır Ekle veya Sil
type: docs
weight: 20
url: /tr/javascript-cpp/insert-or-delete-rows-in-an-excel-worksheet/
description: Bu makale, C++ kullanarak Excel çalışma sayfasında satır ekleme ve silme için JavaScript kodu sağlar.
keywords: Javascript ile Excel çalışma sayfasında satır ekleme veya silme, JavaScript ile excel de satır ekleme veya silme, javascript kullanarak Excel de satır ekle, javascript ile excel de satır sil, javascript ile satır ve sütun ekleme veya silme, javascript ile excel de satır ve sütun ekle veya sil, javascript ile excel e satır ekle, javascript ile excel de satır sil
---

{{% alert color="primary" %}}  

Yeni bir çalışma sayfası oluştururken veya mevcut bir çalışma sayfasıyla çalışırken, verileri sığdırmak için ek satırlar veya sütunlar eklemeniz gerekebilir. Ayrıca, bazen belirli pozisyonlardan satır veya sütun silmeniz gerekebilir.  

{{% /alert %}}  

C++ aracılığıyla Aspose.Cells for JavaScript, satır ekleme ve silme için [**Cells.insertRows(number, number, boolean)**](https://reference.aspose.com/cells/javascript-cpp/cells/#insertRows-number-number-boolean-) ve [**Cells.deleteRows(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#deleteRows-number-number-) olmak üzere iki yöntem sunar. Bu yöntemler performans için optimize edilmiştir ve işlemi oldukça hızlı yapar.  

Satır ekleme veya kaldırma işlemi sırasında, hazırladığımız veya hazırlayacağımız her durumda, her zaman [**Cells.insertRows(number, number, boolean)**](https://reference.aspose.com/cells/javascript-cpp/cells/#insertRows-number-number-boolean-) ve [**Cells.deleteRows(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#deleteRows-number-number-) metodlarını kullanmanızı öneririz, çünkü [**Cells.insertRow(number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#insertRow-number-) veya [**Cells.deleteRow(number)**](https://reference.aspose.com/cells/javascript-cpp/cells/#deleteRow-number-) metodlarını döngü içinde kullanmak yerine.  

Aspose.Cells, Microsoft Excel'in çalışma şekliyle aynı şekilde çalışır. Satırlar veya sütunlar eklenirse, çalışma sayfası içeriği aşağıya ve sağa kaydırılır. Satırlar veya sütunlar kaldırıldığında, çalışma sayfası içeriği yukarı veya sola kaydırılır. Satırlar eklenip kaldırıldığında diğer çalışma sayfaları ve hücrelerdeki referanslar güncellenir.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Insert and Delete Rows</title>
    </head>
    <body>
        <h1>Insert and Delete Rows Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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

            // Instantiate a Workbook object and load the selected file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet in the book
            const sheet = workbook.worksheets.get(0);

            // Insert 10 rows at row index 2 (insertion starts at 3rd row)
            sheet.cells.insertRows(2, 10);

            // Delete 5 rows now. (8th row - 12th row)
            sheet.cells.deleteRows(7, 5);

            // Save the excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out_book1.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Rows modified successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
