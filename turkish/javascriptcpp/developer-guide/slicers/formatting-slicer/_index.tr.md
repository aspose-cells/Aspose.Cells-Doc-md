---
title: JavaScript ile Slicer biçimlendirme C++ kullanılarak
linktitle: Dilimleyici Biçimlendirme
type: docs
weight: 20
url: /tr/javascript-cpp/formatting-slicer/
---

## **Olası Kullanım Senaryoları**

Microsoft Excel'de Slicer'ı hücre sayısını veya stilini ayarlayarak biçimlendirebilirsiniz. Aspose.Cells for JavaScript ile C++ ayrıca bunu [**Slicer.numberOfColumns**](https://reference.aspose.com/cells/javascript-cpp/slicer/#numberOfColumns--) ve [**Slicer.styleType**](https://reference.aspose.com/cells/javascript-cpp/slicer/#styleType--) özelliklerini kullanarak yapmanıza olanak tanır.

## **Dilimleyici Biçimlendirme**

Lütfen aşağıdaki kodu inceleyin. Bu kod, bir slicer içeren [örnek Excel dosyasını](67338473.xlsx) yükler. Slicer'a erişir ve hücre sayısını ve stil tipini ayarlar ve ardından [çıktı Excel dosyasına](67338474.xlsx) kaydeder. Ekran görüntüsü, örnek kod çalıştırıldıktan sonra slicer'ın nasıl göründüğünü gösterir.

![todo:image_alt_text](formatting-slicer_1.png)

## **Örnek Kod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Slicer Formatting Example</title>
    </head>
    <body>
        <h1>Slicer Formatting Example</h1>
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

            // Instantiate Workbook from uploaded file
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const ws = wb.worksheets.get(0);

            // Access the first slicer inside the slicer collection
            const slicer = ws.slicers.get(0);

            // Set the number of columns of the slicer
            slicer.numberOfColumns = 2;

            // Set the type of slicer style
            slicer.styleType = AsposeCells.SlicerStyleType.SlicerStyleLight6;

            // Save the workbook in output XLSX format
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputFormattingSlicer.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Slicer formatting updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
