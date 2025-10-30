---
title: JavaScript ve C++ ile Tablolar ve Aralıklar
linktitle: Tablolar ve Aralıklar
type: docs
weight: 50
url: /tr/javascript-cpp/tables-and-ranges/
---

## **Giriş**  

Bazen Microsoft Excel'de bir tablo oluşturursunuz ve onunla gelen tablo işlevleriyle çalışmak istemezsiniz. Bunun yerine, bir tablo gibi görünen bir şey istersiniz. Biçimlendirmeyi kaybetmeden bir tabloda veri tutmak için tabloyu normal bir veri aralığına dönüştürün.  
Aspose.Cells, Microsoft Excel'in tablo ve liste nesneleri için bu özelliği destekler.  

## **Microsoft Excel Kullanımı**  

**Dönüştürülecek Aralığı Belirt** özelliğini kullanarak bir tabloyu biçimlendirmeyi kaybetmeden hızlıca bir aralığa dönüştürmek için aşağıdaki adımları izleyin. Microsoft Excel 2007/2010'da:  

1. Tablonun herhangi bir yerine tıklayın ve etkin hücrenin bir tablo sütununda olduğundan emin olun.  
1. **Tasarım** sekmesinde, **Araçlar** grubunda, **Dönüştür**'ü tıklayın.  

## **Aspose.Cells Kullanımı**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Convert Table to Range</title>
    </head>
    <body>
        <h1>Convert Table to Range Example</h1>
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

            // Access the first worksheet and convert the first table/list object to a normal range
            const worksheet = workbook.worksheets.get(0);
            const listObject = worksheet.listObjects.get(0);
            listObject.convertToRange();

            // Save the modified workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Table converted to range successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

{{% alert color="primary" %}}  

Tablo özellikleri, tablo bir aralığa dönüştürüldükten sonra artık kullanılamaz. Örneğin, satır başlıkları artık sıralama ve filtre oklarını içermez ve formüllerde kullanılan yapılandırılmış referanslar (tablo adlarını kullanan referanslar), normal hücre referanslarına dönüşür.  

{{% /alert %}}  

## **Tablo, Aralığı Seçenekleri ile Aralığı Dönüştürme**  

Aspose.Cells, [**TableToRangeOptions**](https://reference.aspose.com/cells/javascript-cpp/tabletorangeoptions/) sınıfı aracılığıyla Tablo'yu Aralığa dönüştürürken ek seçenekler sağlar. [**TableToRangeOptions**](https://reference.aspose.com/cells/javascript-cpp/tabletorangeoptions/) sınıfı, belirtilen satır dizinine kadar tablo biçimlendirmesini korumanızı ve geri kalan biçimlendirmeyi kaldırmanızı sağlayan [**lastRow**](https://reference.aspose.com/cells/javascript-cpp/tabletorangeoptions/#lastRow--) özelliğini sağlar.  

Aşağıda verilen örnek kod, [**TableToRangeOptions**](https://reference.aspose.com/cells/javascript-cpp/tabletorangeoptions/) sınıfının kullanımını göstermektedir.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Table to Range Example</title>
    </head>
    <body>
        <h1>Convert Table to Range Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, TableToRangeOptions, Utils } = AsposeCells;

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
            const downloadLink = document.getElementById('downloadLink');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create TableToRangeOptions and set lastRow property
            const options = new TableToRangeOptions();
            options.lastRow = 5;

            // Convert the first table/list object (from the first worksheet) to normal range
            workbook.worksheets.get(0).listObjects.get(0).convertToRange(options);

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Table converted to range successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
