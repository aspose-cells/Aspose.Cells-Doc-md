---
title: Akıllı Sanatı Grup Şekline Dönüştür JavaScript kullanarak C++ ile
linktitle: Akıllı Sanatı Grup Şekline Dönüştür
type: docs
weight: 200
url: /tr/javascript-cpp/convert-the-smart-art-to-group-shape/
---

## **Olası Kullanım Senaryoları**

[**Shape.resultOfSmartArt**](https://reference.aspose.com/cells/javascript-cpp/shape/#resultOfSmartArt--) yöntemi kullanılarak Akıllı Sanat Şekli Grup Şekline dönüştürülebilir. Bu, akıllı sanat şekliyle bir grup şekli gibi ilgilenmenizi sağlar. Sonuç olarak, grup şeklinin bireysel parçalarına veya şekillerine erişebilirsiniz.

## **Akıllı Sanatı Grup Şekline Dönüştür**

Aşağıdaki örnek kod, bu ekran görüntüsünde gösterildiği gibi bir akıllı sanat şekli içeren [örnek Excel dosyasını](55541793.xlsx) yükler. Ardından, akıllı sanat şeklini grup şekline dönüştürür ve Shape.isGroup özelliğini yazdırır. Lütfen aşağıda verilen örnek kodun çıktılarını konsolda inceleyiniz.

![todo:image_alt_text](convert-the-smart-art-to-group-shape_1.png)

## **Örnek Kod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Get Result Of SmartArt</title>
    </head>
    <body>
        <h1>Get Result Of SmartArt Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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

            // Instantiating a Workbook object using the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Accessing the first shape
            const shape = worksheet.shapes.get(0);

            // Determine if shape is smart art (property access, not method)
            const isSmartArt = shape.isSmartArt;

            // Determine if shape is group shape (property access)
            const isGroup = shape.isGroup;

            // Convert smart art shape into group shape result and check if group (getResultOfSmartArt -> resultOfSmartArt property)
            const resultOfSmartArtIsGroup = shape.resultOfSmartArt.isGroup;

            const html = [
                `<p>Is Smart Art Shape: ${isSmartArt}</p>`,
                `<p>Is Group Shape: ${isGroup}</p>`,
                `<p>Result of SmartArt is Group: ${resultOfSmartArtIsGroup}</p>`
            ].join('');

            resultDiv.innerHTML = html;
        });
    </script>
</html>
```

## **Konsol Çıktısı**

{{< highlight javascript >}}

Is Smart Art Shape: True

Is Group Shape: False

Is Group Shape: True

{{< /highlight >}}
