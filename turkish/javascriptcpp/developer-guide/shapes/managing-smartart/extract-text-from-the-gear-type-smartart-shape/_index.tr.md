---
title: JavaScript üzerinden C++ kullanarak Gear Type SmartArt Şekli nden Metin Çıkar
linktitle: Dişli Türü Akıllı Sanat Şeklinden Metin Ayıklama
type: docs
weight: 500
url: /tr/javascript-cpp/extract-text-from-the-gear-type-smartart-shape/
description: C++ kullanarak Aspose.Cells for JavaScript ile Gear Type SmartArt Şekli nden metin çıkarma yöntemlerini öğrenin.
---

## **Olası Kullanım Senaryoları**

Aspose.Cells, Gear Type Smart Art Şekli'nden metin çıkarabilir. Bunu yapmak için ilk olarak Smart Art Şekli'ni [**Shape.resultOfSmartArt**](https://reference.aspose.com/cells/javascript-cpp/shape/#resultOfSmartArt--) özelliği ile Grup Şekli'ne dönüştürmelisiniz. Daha sonra, [**GroupShape.groupedShapes**](https://reference.aspose.com/cells/javascript-cpp/groupshape/#groupedShapes--) özelliği kullanarak Grup Şekli'ni oluşturan Tüm Bireysel Şekiller dizisini almalısınız. Son olarak, tüm Bireysel Şekilleri döngü içinde tek tek gezip [**Shape.text**](https://reference.aspose.com/cells/javascript-cpp/shape/#text--) özelliği ile metinlerini çıkarabilirsiniz.

## **Dişli Türü Akıllı Sanat Şeklinden Metin Ayıklama**

Aşağıdaki örnek kod, Dişli Türü Akıllı Sanat Şeklini içeren [örnek Excel dosyasını](67338483.xlsx) yükler. Daha sonra yukarıda tartışıldığı gibi, bireysel şekillerinden metin çıkarır. Lütfen aşağıdaki kodun konsol çıktısına bakınız.

## **Örnek Kod**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Extract Gear SmartArt Text Example</h1>
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
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet.
            const worksheet = workbook.worksheets.get(0);

            // Access first shape.
            const shape = worksheet.shapes.get(0);

            // Get the result of gear type smart art shape in the form of group shape.
            const groupShape = shape.resultOfSmartArt;

            // Get the list of individual shapes consisting of group shape.
            const shapes = groupShape.groupedShapes;

            // Extract the text of gear type shapes and display them.
            const results = [];
            for (let i = 0; i < shapes.count; i++) {
                const s = shapes.get(i);

                if (s.type === AsposeCells.AutoShapeType.Gear9 || s.type === AsposeCells.AutoShapeType.Gear6) {
                    const text = s.text;
                    results.push(text);
                    console.log("Gear Type Shape Text: " + text);
                }
            }

            if (results.length) {
                document.getElementById('result').innerHTML = '<p style="color: green;">Found gear shape texts:</p><ul>' + results.map(t => '<li>' + t + '</li>').join('') + '</ul>';
            } else {
                document.getElementById('result').innerHTML = '<p style="color: orange;">No gear type SmartArt shapes found in the first shape.</p>';
            }
        });
    </script>
</html>
```

## **Konsol Çıktısı**

{{< highlight javascript >}}

Gear Type Shape Text: Nice

Gear Type Shape Text: Good

Gear Type Shape Text: Excellent

{{< /highlight >}}
