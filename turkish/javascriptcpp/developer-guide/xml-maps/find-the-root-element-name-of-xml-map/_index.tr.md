---
title: JavaScript kullanarak ve C++ ile XML Haritasının Kök Öğesi Adını bulun
linktitle: XML Haritasının Kök Öğe Adını Bul
type: docs
weight: 30
url: /tr/javascript-cpp/find-the-root-element-name-of-xml-map/
description: Excel de XML Haritasının kök öğe adını C++ kullanarak Aspose.Cells for JavaScript ile nasıl bulunacağını öğrenin.
---

## **Olası Kullanım Senaryoları**

 [**XmlMap.rootElementName**](https://reference.aspose.com/cells/javascript-cpp/xmlmap/#rootElementName--) özelliği ile C++ kullanarak Xml Map'in Kök Öğesi Adını bulabilirsiniz. Aşağıdaki ekran görüntüsü Microsoft Excel'deki XML Haritasının kök öğe adını gösterir.

![todo:image_alt_text](find-the-root-element-name-of-xml-map_1.png)

## **Örnek Kod**

Aşağıdaki örnek kod, [örnek Excel dosyasını](55541789.xlsx) yükler ve ilk XML Map'e erişir ve [**XmlMap.rootElementName**](https://reference.aspose.com/cells/javascript-cpp/xmlmap/#rootElementName--) özelliğini yazdırır. Lütfen aşağıdaki örnek kodun konsol çıktısına bakın.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Get Root Element Name Of Xml Map</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Get Root Element Name</button>
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object using the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first Xml Map inside the Workbook
            const xmap = workbook.worksheets.xmlMaps.get(0);

            // Get Root Element Name of Xml Map
            const rootName = xmap.rootElementName;

            // Display result
            resultDiv.innerHTML = `<p>Root Element Name Of Xml Map: ${rootName}</p>`;
            console.log("Root Element Name Of Xml Map: " + rootName);
        });
    </script>
</html>
```

## **Konsol Çıktısı**

{{< highlight java >}}

Root Element Name Of Xml Map: MiscData

{{< /highlight >}}
