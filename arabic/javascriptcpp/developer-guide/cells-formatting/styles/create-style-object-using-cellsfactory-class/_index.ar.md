---
title: انشاء كائن نمط باستخدام فئة CellsFactory
linktitle: انشاء كائن نمط باستخدام فئة CellsFactory
description: تعلّم كيف تنشئ كائن نمط خلية باستخدام فئة CellsFactory في Aspose.Cells for JavaScript عبر C++. قم بتخصيص مظهر خلايا الجدول حسب الحاجة.
keywords: Aspose.Cells، جافا سكريبت عبر C++، جدول بيانات إلكتروني، كائن نمط، نمط خلية، تخصيص
type: docs
weight: 70
url: /ar/javascript-cpp/create-style-object-using-cellsfactory-class/
---

## **انشاء كائن نمط باستخدام فئة CellsFactory**
النص التالي يوضح كيف يتم إنشاء كائن [نمط](https://reference.aspose.com/cells/javascript-cpp/style) باستخدام فئة [CellsFactory](https://reference.aspose.com/cells/javascript-cpp/cellsfactory) ثم تعيين النمط الافتراضي لمصنف العمل. يرجى تنزيل [ملف إكسل الناتج](5115153.xlsx) لمعاينة نتائج هذا الرمز.


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Create Workbook with Default Style</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellsFactory, BackgroundType, Color, Utils } = AsposeCells;

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
            // Create a Style object using CellsFactory class
            const cf = new CellsFactory();
            const st = cf.createStyle();

            // Set the Style fill color to Yellow
            st.pattern = BackgroundType.Solid;
            st.foregroundColor = Color.Yellow;

            // Create a workbook and set its default style using the created Style object
            const wb = new Workbook();
            wb.defaultStyle = st;

            // Save the workbook
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully. Click the download link to save the file.</p>';
        });
    </script>
</html>
```
