---
title: JavaScript kullanarak Birleşim Aralığı Oluşturma C++ ile
linktitle: Birleşik Aralık Oluştur
type: docs
weight: 360
url: /tr/javascript-cpp/create-union-range/
description: Aspose.Cells for JavaScript kullanarak birleşim aralığı nasıl oluşturulur öğrenin.
keywords: Birleşim Aralığı Oluşturma JavaScript ile C++, Aspose.Cells JavaScript ile Birleşim Aralığı, Çalışma Sayfası Koleksiyonu ile JavaScript kullanarak Birleşim Aralığı oluşturma
---

## **Birleşik Aralık Oluştur**
Aspose.Cells, [WorksheetCollection.createUnionRange](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#createUnionRange-string-number-) yöntemini kullanarak Birleşim Aralığı oluşturma yeteneği sağlar. [WorksheetCollection.createUnionRange](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#createUnionRange-string-number-) yöntemi, birleşim aralığını oluşturmak için adres ve çalışma sayfası dizini olmak üzere iki parametre alır. [WorksheetCollection.createUnionRange](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#createUnionRange-string-number-) yöntemi bir [UnionRange](https://reference.aspose.com/cells/javascript-cpp/unionrange) nesnesi döner.  

Aşağıdaki kod örneği [WorksheetCollection.createUnionRange](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#createUnionRange-string-number-) yöntemini kullanarak bir Birleşim Aralığı oluşturmayı göstermekte. Kod tarafından üretilen çıktı dosyası referans için eklenmiştir.  

- [Çıktı Dosyası](106364952.xlsx)  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Create Union Range Example</title>
    </head>
    <body>
        <h1>Create Union Range Example</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create union range
            const unionRange = workbook.worksheets.createUnionRange("sheet1!A1:A10,sheet1!C1:C10", 0);

            // Put value "ABCD" in the range (converted setter to property)
            unionRange.value = "ABCD";

            // Save the output workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'CreateUnionRange_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Union range created successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
