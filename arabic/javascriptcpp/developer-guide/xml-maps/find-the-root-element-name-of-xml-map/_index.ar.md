---
title: اعثر على اسم العنصر الجذري لخريطة XML باستخدام JavaScript عبر C++
linktitle: العثور على اسم العنصر الجذري لخريطة XML
type: docs
weight: 30
url: /ar/javascript-cpp/find-the-root-element-name-of-xml-map/
description: تعلم كيفية العثور على اسم العنصر الجذري لخريطة XML في Excel باستخدام Aspose.Cells for JavaScript عبر C++.
---

## **سيناريوهات الاستخدام المحتملة**

يمكنك العثور على *اسم العنصر الجذري لخريطة XML* باستخدام Aspose.Cells for JavaScript عبر C++ مع الخاصية [**XmlMap.rootElementName**](https://reference.aspose.com/cells/javascript-cpp/xmlmap/#rootElementName--). تظهر لقطة الشاشة التالية اسم العنصر الجذري لخريطة XML في Microsoft Excel.

![todo:image_alt_text](find-the-root-element-name-of-xml-map_1.png)

## **الكود المثالي**

تحميل الكود النموذجي التالي لملف Excel التجريبي الخاص بك والوصول إلى خريطة XML الأولى وطباعة خاصية [**XmlMap.rootElementName**](https://reference.aspose.com/cells/javascript-cpp/xmlmap/#rootElementName--). يُرجى مراجعة مخرجات وحدة التحكم للكود النموذجي أدناه.

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

## **مخرجات الوحدة**

{{< highlight java >}}

Root Element Name Of Xml Map: MiscData

{{< /highlight >}}
