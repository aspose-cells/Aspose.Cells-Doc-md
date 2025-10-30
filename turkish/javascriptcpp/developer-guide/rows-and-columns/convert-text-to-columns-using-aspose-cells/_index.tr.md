---
title: Text i Columns a Dönüştürmek için Aspose.Cells for JavaScript kullanma C++ ile
linktitle: Metni Sütunlara Dönüştürme
type: docs
weight: 30
url: /tr/javascript-cpp/convert-text-to-columns-using-aspose-cells/
description: Excel de Text i Columns a dönüştürmenin nasıl yapılacağını Aspose.Cells for JavaScript ile C++ kullanarak öğrenin.
---

## **Olası Kullanım Senaryoları**  

Metninizi Columns'a çevirebilirsiniz. Bu özellik, *Data Tools* altında *Data* sekmesinde kullanılabilir. Bir sütunun içeriğini birden çok sütuna bölmek için, verilerin belirli bir ayıraç içermesi gerekir, örneğin virgül veya başka bir karakter, böylece Microsoft Excel hücrenin içeriğini birden fazla hücreye böler. C++ ile Aspose.Cells for JavaScript bu özelliği [**Cells.textToColumns(number, number, number, TxtLoadOptions)**](https://reference.aspose.com/cells/javascript-cpp/cells/#textToColumns-number-number-number-txtloadoptions-) aracılığıyla sağlar.  

## **C++ ile Text'i Columns'a Dönüştürmek için Aspose.Cells for JavaScript kullanma**  

Aşağıdaki örnek kod, [**Cells.textToColumns(number, number, number, TxtLoadOptions)**](https://reference.aspose.com/cells/javascript-cpp/cells/#textToColumns-number-number-number-txtloadoptions-) metodunun kullanımını açıklar. Kod önce ilk çalışma sayfasındaki A sütununa bazı kişilerin isimlerini ekler. İsimler boşluk karakteriyle ayrılmıştır. Sonra [**Cells.textToColumns(number, number, number, TxtLoadOptions)**](https://reference.aspose.com/cells/javascript-cpp/cells/#textToColumns-number-number-number-txtloadoptions-) metodunu A sütununda uygular ve sonucu bir Excel dosyası olarak kaydeder. Eğer [çıktı Excel dosyasını](25395213.xlsx) açarsanız, ilk isimlerin A sütununda, soy isimlerin B sütununda olduğunu göreceksiniz.  

![todo:image_alt_text](convert-text-to-columns-using-aspose-cells_1.png)  

## **Örnek Kod**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Text to Columns Example</h1>
        <p>Select an optional Excel file to start from, or leave empty to create a new workbook.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, TxtLoadOptions, Utils } = AsposeCells;

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

            // Basic validation only: file is optional
            let workbook;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                // Create a new workbook if no file is provided
                workbook = new Workbook();
            }

            // Access first worksheet.
            const ws = workbook.worksheets.get(0);

            // Add people name in column A. First name and last name are separated by space.
            ws.cells.get("A1").value = "John Teal";
            ws.cells.get("A2").value = "Peter Graham";
            ws.cells.get("A3").value = "Brady Cortez";
            ws.cells.get("A4").value = "Mack Nick";
            ws.cells.get("A5").value = "Hsu Lee";

            // Create text load options with space as separator.
            const opts = new TxtLoadOptions();
            opts.separator = ' ';

            // Split the column A into two columns using TextToColumns() method.
            // Now column A will have first name and column B will have second name.
            ws.cells.textToColumns(0, 0, 5, opts);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputTextToColumns.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
