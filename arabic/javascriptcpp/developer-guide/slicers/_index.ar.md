---
title: إدراج القُطار
linktitle: قاطعات
type: docs
weight: 170
url: /ar/javascript-cpp/create-slicer/
description: إدارة فلاتر مقسمات جداول ملفات إكسل بواسطة Aspose.Cells for JavaScript عبر C++.
---

## **سيناريوهات الاستخدام المحتملة**

يُستخدم المُقسم لتصفية البيانات بسرعة. يمكن استخدامه لتصفية البيانات سواء في جدول أو جدول محوري. يسمح لك Microsoft Excel بإنشاء مقسم عن طريق تحديد جدول أو جدول محوري ثم النقر على *إدراج > مقسم*. كما يتيح لك Aspose.Cells for JavaScript عبر C++ إنشاء مقسم باستخدام طريقة [**Worksheet.slicers.add()**](https://reference.aspose.com/cells/javascript-cpp/slicercollection/#add-pivottable-string-string-).

## **إنشاء مُقطَّع إلى جدول محوري**

يرجى الاطلاع على كود العينة التالي. يحمل ملف إكسل عياري يحتوي على جدول محوري. ثم ينشئ المقسم بناءً على أول حقل جدول محوري أساسي. أخيرًا، يحفظ المصنف بصيغة [XLSX المخرجة](67338470.xlsx) و [XLSB المخرجة](67338472.xlsb). يُظهر لقطة الشاشة التالية المقسم الذي أنشأه Aspose.Cells for JavaScript عبر C++ في ملف إكسل الناتج.

![todo:image_alt_text](create-slicer-to-a-pivot-table_1.png)

### **الكود المثالي**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Create Slicer to PivotTable</title>
    </head>
    <body>
        <h1>Create Slicer to PivotTable Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsb,.csv" />
        <button id="runExample">Run Example</button>
        <br/><br/>
        <a id="downloadXlsxLink" style="display: none;">Download XLSX Result</a>
        <br/>
        <a id="downloadXlsbLink" style="display: none;">Download XLSB Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file (e.g., sampleCreateSlicerToPivotTable.xlsx).</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet.
            const ws = wb.worksheets.get(0);

            // Access first pivot table inside the worksheet.
            const pt = ws.pivotTables.get(0);

            // Add slicer relating to pivot table with first base field at cell B22.
            const idx = ws.slicers.add(pt, "B22", pt.baseFields.get(0));

            // Access the newly added slicer from slicer collection.
            const slicer = ws.slicers.get(idx);

            // Save the workbook in output XLSX format.
            const outputDataXlsx = wb.save(SaveFormat.Xlsx);
            const blobXlsx = new Blob([outputDataXlsx]);
            const downloadXlsxLink = document.getElementById('downloadXlsxLink');
            downloadXlsxLink.href = URL.createObjectURL(blobXlsx);
            downloadXlsxLink.download = 'outputCreateSlicerToPivotTable.xlsx';
            downloadXlsxLink.style.display = 'inline';
            downloadXlsxLink.textContent = 'Download outputCreateSlicerToPivotTable.xlsx';

            // Save the workbook in output XLSB format.
            const outputDataXlsb = wb.save(SaveFormat.Xlsb);
            const blobXlsb = new Blob([outputDataXlsb]);
            const downloadXlsbLink = document.getElementById('downloadXlsbLink');
            downloadXlsbLink.href = URL.createObjectURL(blobXlsb);
            downloadXlsbLink.download = 'outputCreateSlicerToPivotTable.xlsb';
            downloadXlsbLink.style.display = 'inline';
            downloadXlsbLink.textContent = 'Download outputCreateSlicerToPivotTable.xlsb';

            document.getElementById('result').innerHTML = '<p style="color: green;">Slicer created and files are ready for download.</p>';
        });
    </script>
</html>
```

## **إنشاء مُقطَّع إلى جدول Excel**

يرجى الاطلاع على رمز العينة التالي. يقوم بتحميل ملف Excel العيني ([sampleCreateSlicerToExcelTable.xlsx](sampleCreateSlicerToExcelTable.xlsx)) الذي يحتوي على جدول. ثم يقوم بإنشاء المُقطَّع بناءً على العمود الأول. أخيرًا، يحفظ برنامج العمل بتنسيق [XLSX](outputCreateSlicerToExcelTable.xlsx).

### **الكود المثالي**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Create Slicer to Excel Table Example</title>
    </head>
    <body>
        <h1>Create Slicer to Excel Table Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

        let asposeReady = false;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
            asposeReady = true;
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            if (!asposeReady) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Aspose.Cells is not initialized yet. Please wait and try again.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet.
            const worksheet = workbook.worksheets.get(0);

            // Access first table inside the worksheet.
            const table = worksheet.listObjects.get(0);

            // Add slicer
            const idx = worksheet.slicers.add(table, 0, "H5");

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputCreateSlicerToExcelTable.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Slicer added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
