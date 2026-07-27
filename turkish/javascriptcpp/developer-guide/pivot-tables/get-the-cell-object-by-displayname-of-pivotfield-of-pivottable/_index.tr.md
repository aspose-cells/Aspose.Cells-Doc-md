---
title: PivotTablo alanının GörünenAdı ile Hücre nesnesini alın
type: docs
weight: 70
url: /tr/javascript-cpp/get-the-cell-object-by-displayname-of-pivotfield-of-pivottable/
description: PivotTable un DisplayName özelliği ile hücre nesnesi nasıl alınır Aspose.Cells for JavaScript ile C++ kullanarak
keywords: Aspose.Cells for JavaScript ile C++ Excel, Excel JavaScript kütüphanesi kullanarak, PivotTable daki PivotField un DisplayName özelliği ile Hücre nesnesi nasıl alınır
---

{{% alert color="primary" %}}

Aspose.Cells for JavaScript ile C++, pivot alanının display name'ine göre hücre nesnesine erişmek için kullanılabilecek [**PivotTable.cellByDisplayName(string)**](https://reference.aspose.com/cells/javascript-cpp/pivottable/#cellByDisplayName-string-) yöntemi sağlar. Bu yöntem, pivot alan başlığını vurgulamak veya biçimlendirmek istediğinizde faydalıdır. Bu makale, data alanının display name'ine göre hücre nesnesini nasıl alacağınızı ve ardından biçimlendirmeyi nasıl uygulayacağınızı açıklar.

{{% /alert %}}

## **PivotTablosunun PivotAlanı'nın DisplayName'ine göre Hücre nesnesini alma yöntemi**

Aşağıdaki kod, çalışma kitabının ilk pivot tablosuna erişir ve ardından pivot tablosunun ikinci veri alanının görüntü adıyla hücreyi alır. Daha sonra hücrenin dolum rengini açık mavi, yazı tipi rengini ise siyah olarak değiştirir. Aşağıdaki ekran görüntüleri, kodun yürütülmeden önce ve sonra pivot tablosunun nasıl göründüğünü göstermektedir.

|**Pivot Tablosu - Önce**|
| :- |
|![todo:image_alt_text](get-the-cell-object-by-displayname-of-pivotfield-of-pivottable_1.png)|

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Pivot Table Cell Styling Example</h1>
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
            const resultDiv = document.getElementById('result');
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access first pivot table inside the worksheet
            const pivotTable = worksheet.pivotTables.get(0);

            // Access cell by display name of 2nd data field of the pivot table
            const dataFieldDisplayName = pivotTable.dataFields.get(1).displayName;
            const cell = pivotTable.cellByDisplayName(dataFieldDisplayName);

            // Access cell style and set its fill color and font color
            const style = cell.style;
            style.foregroundColor = AsposeCells.Color.LightBlue;
            style.font.color = AsposeCells.Color.Black;

            // Set the style of the cell
            pivotTable.format(cell.row, cell.column, style);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

|**Pivot Tablosu - Sonra**|
| :- |
|![todo:image_alt_text](get-the-cell-object-by-displayname-of-pivotfield-of-pivottable_2.png)|
