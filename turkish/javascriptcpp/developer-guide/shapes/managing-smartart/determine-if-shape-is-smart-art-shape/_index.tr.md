---
title: Shape’in Akıllı Sanat Şekli olup olmadığını JavaScript ile C++ kullanarak belirle
linktitle: Şekil Akıllı Sanat Şekli mi Belirle
type: docs
weight: 400
url: /tr/javascript-cpp/determine-if-shape-is-smart-art-shape/
description: Excel de bir şeklin Akıllı Sanat şekli olup olmadığını nasıl belirleyeceğinizi öğrenin Aspose.Cells for JavaScript kullanarak C++ ile.
---

## **Olası Kullanım Senaryoları**  

Smart Art Şekilleri, Microsoft Excel'de otomatik olarak karmaşık diyagramlar oluşturmanıza olanak tanıyan özel şekillerdir. Bir şeklin smart art şekli olup olmadığını veya normal şekil olduğunu [**Shape.isSmartArt()**](https://reference.aspose.com/cells/javascript-cpp/shape/#isSmartArt--) özelliği kullanarak bulabilirsiniz.  

## **Şekil Akıllı Sanat Şekli mi Belirle**  

Aşağıdaki örnek kod, bu ekran görüntüsünde gösterildiği gibi bir smart art şekli içeren [örnek Excel dosyasını](55541792.xlsx) yükler. Ardından, ilk şeklin [**Shape.isSmartArt()**](https://reference.aspose.com/cells/javascript-cpp/shape/#isSmartArt--) özelliğinin değerini yazdırır. Lütfen aşağıda verilen örnek kodun çıktılarını konsolda inceleyiniz.  

![todo:image_alt_text](determine-if-shape-is-smart-art-shape_1.png)  

## **Örnek Kod**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Example Title</h1>
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
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Accessing the first shape
            const shape = worksheet.shapes.get(0);

            // Determine if shape is smart art (converted to property access)
            const isSmartArt = shape.isSmartArt;

            document.getElementById('result').innerHTML = `<p>Is Smart Art Shape: ${isSmartArt}</p>`;
        });
    </script>
</html>
```  

## **Konsol Çıktısı**  

{{< highlight java >}}  

Is Smart Art Shape: True  

{{< /highlight >}}
