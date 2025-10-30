---
title: Hücre Değeri Genişliğini ve Yüksekliğini Piksel Biriminde Ölçün
linktitle: Boyutu Ölçün
type: docs
weight: 260
url: /tr/javascript-cpp/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/
description: Hücre Değeri Genişliğini ve Yüksekliğini Piksel Birimiyle Ölçmeyi öğrenin, C++ ile Aspose.Cells for JavaScript kullanarak.
keywords: Hücre Değeri Genişliğini Piksel Birimiyle Ölçmek, JavaScript ile C++ kullanarak, Hücre Değeri Yüksekliğini Piksel Birimiyle Ölçmek, JavaScript ile C++ kullanarak, Hücrenin Genişliğini ve Yüksekliğini Piksel Birimiyle Almak, JavaScript ile C++ kullanarak
---

{{% alert color="primary" %}}  

Bazen hücre değerinin genişliğini ve yüksekliğini, hücre içine hücre değerini sığdırmak için hesaplamanız gerekir. Aspose.Cells bu amaçla [**Cell.widthOfValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#widthOfValue--) ve [**Cell.heightOfValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#heightOfValue--) yöntemlerini sağlar. Bu yöntemleri kullanarak hücre değerinin genişliğini ve yüksekliğini hesaplayabilir, ardından o hücrenin sütun genişliğini ve satır yüksekliğini ayarlayabilirsiniz ve bu, hücre değerini hücrenin içine otomatik olarak ayarlar veya sığdırır.  

Alternatif olarak, Aspose.Cells API'lerini kullanarak hücrelerinizi veya hücre aralıklarınızı [otomatik uyacak şekilde ayarlayabilirsiniz](/cells/tr/javascript-cpp/autofit-rows-and-columns/)  

{{% /alert %}}  

Aşağıdaki kod, [**Cell.widthOfValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#widthOfValue--) ve [**Cell.heightOfValue**](https://reference.aspose.com/cells/javascript-cpp/cell/#heightOfValue--) metodlarının kullanımını açıklar.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Get Cell Size Example</h1>
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

            // Create or load workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access cell B2 and add some value inside it
            const cell = worksheet.cells.get("B2");
            cell.value = "Welcome to Aspose!";

            // Enlarge its font to size 16
            const style = cell.style;
            style.font.size = 16;
            cell.style = style;

            // Calculate the width and height of the cell value in unit of pixels
            const widthOfValue = cell.widthOfValue;
            const heightOfValue = cell.heightOfValue;

            // Print both values to the page
            document.getElementById('result').innerHTML = `<p>Width of Cell Value: ${widthOfValue}</p><p>Height of Cell Value: ${heightOfValue}</p>`;

            // Set the row height and column width to adjust/fit the cell value inside cell
            worksheet.cells.setColumnWidthPixel(1, widthOfValue);
            worksheet.cells.setRowHeightPixel(1, heightOfValue);

            // Save the output excel file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';
        });
    </script>
</html>
```


## **Gelişmiş Konular**  
- [Hücre Değeri Metnin Genişliğini Alma](/cells/tr/javascript-cpp/get-text-width-of-cell-value/)
