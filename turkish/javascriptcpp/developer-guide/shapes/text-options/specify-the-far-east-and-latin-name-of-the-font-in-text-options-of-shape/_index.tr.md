---
title: JavaScript ve C++ kullanarak Şekil in Metin Seçeneklerinde Uzak Doğu ve Latin Font adını belirtin
linktitle: Şekil Metin Seçenekleri nde Uzak Doğu ve Latin Yazı Tipi Adını Belirtin
type: docs
weight: 1600
url: /tr/javascript-cpp/specify-the-far-east-and-latin-name-of-the-font-in-text-options-of-shape/
description: Uzak Doğu ve Latin font isimlerini şekil içi metin seçeneklerinde nasıl belirteceğinizi Aspose.Cells for JavaScript kullanarak öğrenin.
---

## **Olası Kullanım Senaryoları**  

Bazen Uzak Doğu dil fontlarında metin görüntülemek istersiniz, örneğin Japonca, Çin, Tayca vb. Aspose.Cells for JavaScript, C++ kullanılarak Uzak Doğu dilinin font adını belirtmek için [**TextOptions.farEastName**](https://reference.aspose.com/cells/javascript-cpp/textoptions/#farEastName--) özelliği sağlar. Ayrıca Latin font adını [**TextOptions.latinName**](https://reference.aspose.com/cells/javascript-cpp/textoptions/#latinName--) özelliğiyle belirtebilirsiniz.  

## **Şekil Metin Seçenekleri'nde Uzak Doğu ve Latin Yazı Tipi Adını Belirtin**  

Aşağıdaki örnek kod, bir metin kutusu oluşturur ve içine bazı Japonca metinler ekler. Daha sonra, metnin Latin ve Doğu (Far East) yazı tipi adlarını belirler ve çalışma kitabını [çıktı Excel dosyası](67338274.xlsx) olarak kaydeder. Aşağıdaki ekran görüntüsü, Microsoft Excel'de çıktı metin kutusunun Latin ve Doğu yazı tipi adlarını gösterir.  

![todo:image_alt_text](specify-the-far-east-and-latin-name-of-the-font-in-text-options-of-shape_1.png)  

## **Örnek Kod**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Specify Far East and Latin Name of Font in TextOptions of Shape</h1>
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
            // Create empty workbook.
            const wb = new Workbook();

            // Access first worksheet.
            const ws = wb.worksheets.get(0);

            // Add textbox inside the worksheet.
            const idx = ws.textBoxes.add(5, 5, 50, 200);
            const tb = ws.textBoxes.get(idx);

            // Set the text of the textbox.
            tb.text = "こんにちは世界";

            // Specify the Far East and Latin name of the font.
            tb.textOptions.latinName = "Comic Sans MS";
            tb.textOptions.farEastName = "KaiTi";

            // Save the output Excel file.
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSpecifyFarEastAndLatinNameOfFontInTextOptionsOfShape.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
