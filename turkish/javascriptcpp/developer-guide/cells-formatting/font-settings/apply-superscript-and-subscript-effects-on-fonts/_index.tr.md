---
title: Fontlarda Üstsimge ve Altsimge Efektleri Uygulama
linktitle: Fontlarda Üstsimge ve Altsimge Efektleri Uygulama
type: docs
weight: 80
url: /tr/javascript-cpp/apply-superscript-and-subscript-effects-on-fonts/
description: C++ ile Aspose.Cells for JavaScript kullanarak Excel de üst simge ve alt simge efektleri uygulayan JavaScript kodu.
keywords: C++ ile Excel üst simge JavaScript, C++ ile Excel alt simge JavaScript, C++ ile Excel üst ve alt simge JavaScript, C++ ile Excel e alt ve üst simge ekleme, C++ ile excel de üst ve alt simge ekleme, C++ ile excel üst ve alt simge ekleme, C++ ile excel üst ve alt simge ekleme
---

{{% alert color="primary" %}}

Aspose.Cells, metne üstsimge (metnin taban çizgisinin üstünde) ve altsimge (metnin taban çizgisinin altında) efektlerini uygulama işlevselliği sağlar.

{{% /alert %}}

## **Üstsimge ve Altsimge ile Çalışma**

[**Font**](https://reference.aspose.com/cells/javascript-cpp/font) nesnesinin [**isSuperscript**](https://reference.aspose.com/cells/javascript-cpp/font/#isSuperscript-boolean-) özelliğini **true** olarak ayarlayarak üst simge efektini uygulayın. Alt simge uygulamak için, [**Font**](https://reference.aspose.com/cells/javascript-cpp/font) nesnesinin [**isSubscript**](https://reference.aspose.com/cells/javascript-cpp/font/#isSubscript-boolean-) özelliğini **true** yapın.

Aşağıdaki kod örnekleri, metne üst simge ve altsimge uygulamanın nasıl yapılacağını göstermektedir.

### Metinde Üst Simge Efekti Uygulamak İçin JavaScript Kodu

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Superscript Example</title>
    </head>
    <body>
        <h1>Superscript Example</h1>
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
            // Instantiating a Workbook object
            const workbook = new Workbook();

            // Adding a new worksheet to the Excel object
            workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(0);

            // Accessing the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.value = "Hello";

            // Setting the font Superscript
            const style = cell.style;
            style.font.isSuperscript = true;
            cell.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Auto);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Superscript.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```


### Metinde Alt Simge Efekti Uygulamak İçin JavaScript Kodu

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Subscript Example</h1>
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
            // Instantiate a Workbook object
            const workbook = new Workbook();

            // Add a new worksheet to the Excel object
            workbook.worksheets.add();

            // Obtain the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(0);

            // Access the "A1" cell from the worksheet
            const cell = worksheet.cells.get("A1");

            // Adding some value to the "A1" cell
            cell.value = "Hello";

            // Setting the font Subscript
            const style = cell.style;
            style.font.isSubscript = true;
            cell.style = style;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Auto);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Subscript.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created with subscript formatting. Click the download link to get the file.</p>';
        });
    </script>
</html>
```
