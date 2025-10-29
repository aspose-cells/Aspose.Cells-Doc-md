---
title: ربط الخلايا بعناصر خريطة XML باستخدام JavaScript عبر C++
linktitle: ربط الخلايا بعناصر خريطة XML
type: docs
weight: 50
url: /ar/javascript-cpp/link-cells-to-xml-map-elements/
---

## **سيناريوهات الاستخدام المحتملة**

 يمكنك ربط خلاياك بعناصر خريطة XML باستخدام Aspose.Cells for JavaScript عبر C++. يرجى استخدام طريقة [**Cells.linkToXmlMap(string, number, number, string)**](https://reference.aspose.com/cells/javascript-cpp/cells/#linkToXmlMap-string-number-number-string-) لهذا الغرض.

## **ربط الخلايا بعناصر خريطة XML**

يقوم الكود العيني التالي بتحميل [ملف إكسل المصدري](5115471.xlsx) الذي يحتوي على خريطة XML ومن ثم يربط الخلايا A1، B2، C3، D4، E5، و F6 بعناصر خريطة XML FIELD1، FIELD2، FIELD4، FIELD5، FIELD7، و FIELD8 على التوالي ومن ثم يحفظ سجل العمل في [ملف إكسل المخرجات](5115467.xlsx).

إذا قمت بفتح [ملف إكسل المخرجات](5115467.xlsx) ونقرت على زر المطور > مصدر، سترى الخلايا مرتبطة بعناصر خريطة XML وسيتم إظهارها أيضًا من قبل Microsoft Excel كما هو موضح في هذه الصورة.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Map XML to Cells Example</h1>
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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the Xml Map inside it
            const map = workbook.worksheets.xmlMaps.get(0);

            // Access first worksheet
            const ws = workbook.worksheets.get(0);

            // Map FIELD1 and FIELD2 to cell A1 and B2
            ws.cells.linkToXmlMap(map.name, 0, 0, "/root/row/FIELD1");
            ws.cells.linkToXmlMap(map.name, 1, 1, "/root/row/FIELD2");

            // Map FIELD4 and FIELD5 to cell C3 and D4
            ws.cells.linkToXmlMap(map.name, 2, 2, "/root/row/FIELD4");
            ws.cells.linkToXmlMap(map.name, 3, 3, "/root/row/FIELD5");

            // Map FIELD7 and FIELD8 to cell E5 and F6
            ws.cells.linkToXmlMap(map.name, 4, 4, "/root/row/FIELD7");
            ws.cells.linkToXmlMap(map.name, 5, 5, "/root/row/FIELD8");

            // Save the workbook in xlsx format
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">XML mapped to cells successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
