---
title: JavaScript ve C++ kullanarak Çalışma Sayfası içindeki Şekil ile Metin Döndürme
linktitle: Çalışma Sayfası İçindeki Şekil ile Metni Döndürme
type: docs
weight: 1300
url: /tr/javascript-cpp/rotate-text-with-shape-inside-the-worksheet/
description: C++ kullanarak Aspose.Cells for JavaScript ile bir Excel çalışma sayfasında şekil ile metni nasıl döndüreceğinizi öğrenin.
---

## **Olası Kullanım Senaryoları**

Microsoft Excel kullanarak herhangi bir şekle metin ekleyebilirsiniz. Çok eski Microsoft Excel 2003 kullanılarak eklenen şekillerde, metin şekille birlikte döndürülmez. Ama yeni sürümler kullanılarak, örneğin 2007, 2010, 2013 veya 2016 gibi, şekil ile birlikte metin döner. Metnin şekil ile döndürülüp döndürülmeyeceğini [**ShapeTextAlignment.rotateTextWithShape**](https://reference.aspose.com/cells/javascript-cpp/shapetextalignment/#rotateTextWithShape--) özelliği ile kontrol edebilirsiniz. Varsayılan değeri **true**’dur, bu da metnin şekille birlikte döneceği anlamına gelir. Eğer **false** olarak ayarlanırsa, metin şekille birlikte dönmez.

## **Çalışma Sayfası İçindeki Şekil ile Metni Döndürme**

Aşağıdaki örnek kod, üçgen şekli içeren ve metni şekille birlikte dönen [örnek Excel dosyasını](64716896.xlsx) yükler. Eğer örnek Excel dosyasını Microsoft Excel'de açarsanız ve üçgen şekli döndürürseniz, metin de onunla birlikte döner. Kod daha sonra [**ShapeTextAlignment.rotateTextWithShape**](https://reference.aspose.com/cells/javascript-cpp/shapetextalignment/#rotateTextWithShape--) özelliğini **false** yapar ve [çıktı Excel dosyasına](64716897.xlsx) kaydeder. Şimdi çıktı dosyasını Microsoft Excel'de açıp üçgen şekli döndürürseniz, metin onunla birlikte dönmez. Aşağıdaki ekran görüntüsü, kodun örnek Excel dosyasına etkisini gösterir.

![todo:image_alt_text](rotate-text-with-shape-inside-the-worksheet_1.png)

## **Örnek Kod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Rotate Text With Shape</title>
    </head>
    <body>
        <h1>Rotate Text With Shape Example</h1>
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

            // Instantiating a Workbook object by loading the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet.
            const worksheet = workbook.worksheets.get(0);

            // Access cell B4 and add message inside it.
            const cellB4 = worksheet.cells.get("B4");
            cellB4.value = "Text is not rotating with shape because RotateTextWithShape is false.";

            // Access first shape.
            const shape = worksheet.shapes.get(0);

            // Access shape text alignment.
            const shapeTextAlignment = shape.textBody.textAlignment;

            // Do not rotate text with shape by setting RotateTextWithShape as false.
            shapeTextAlignment.rotateTextWithShape = false;

            // Saving the modified Excel file and providing download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputRotateTextWithShapeInsideWorksheet.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
