---
title: Tablo veya Liste Nesnesinde Formülü Otomatik Olarak Yayınlayın ve JavaScript ile C++ kullanarak Yeni Satırlara Veri Girerken
linktitle: Tablo Formülünü Ayarlar
type: docs
weight: 260
url: /tr/javascript-cpp/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/
description: Aspose.Cells for JavaScript kullanarak C++ ile yeni satırlara veri girerken tablolar veya liste nesnelerinde formülleri otomatik olarak yaymayı öğrenin.
---

## **Olası Kullanım Senaryoları**
Bazen, Tablo veya Liste Nesnenizdeki formülün yeni veriler girilirken otomatik olarak yeni satırlara yayılmasını istersiniz. Bu, Microsoft Excel'in varsayılan davranışıdır. Aynı işlevselliği Aspose.Cells for JavaScript kullanarak C++ ile elde etmek için lütfen [ListColumn.formula](https://reference.aspose.com/cells/javascript-cpp/listcolumn/#formula--) özelliğini kullanın.

## **Formülü Otomatik Yayma - Yeni Satırlara Veri Girerken Tablo veya Liste Nesnesinde Otomatik Yayılım**
Aşağıdaki örnek kod, B sütunundaki formülün yeni veriler girildiğinde otomatik olarak yeni satırlara yayılacak şekilde bir Tablo veya Liste Nesnesi oluşturur. Bu kodla üretilen [çıktı excel dosyasını](5115469.xlsx) kontrol edin. A3 hücresine herhangi bir sayı girerseniz, B2 hücresindeki formülün otomatik olarak B3 hücresine yayıldığını göreceksiniz.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells ListObject Example</h1>
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
            // Create workbook object
            const book = new Workbook();

            // Access first worksheet
            const sheet = book.worksheets.get(0);

            // Add column headings in cell A1 and B1
            sheet.cells.get(0, 0).value = "Column A";
            sheet.cells.get(0, 1).value = "Column B";

            // Add list object, set its name and style
            const listObject = sheet.listObjects.get(
                sheet.listObjects.add(0, 0, 1, sheet.cells.maxColumn, true)
            );
            listObject.tableStyleType = AsposeCells.TableStyleType.TableStyleMedium2;
            listObject.displayName = "Table";

            // Set the formula of second column so that it propagates to new rows automatically while entering data
            listObject.listColumns.get(1).formula = "=[Column A] + 1";

            // Save the workbook in xlsx format
            const outputData = book.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
