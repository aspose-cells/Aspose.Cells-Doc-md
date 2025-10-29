---
title: تحويل مصنف Excel إلى Ods، Sxc و Fods (OpenOffice / LibreOffice Calc) باستخدام Script via Java
linktitle: Ods
type: docs
weight: 20
url: /ar/javascript-cpp/convert-excel-to-ods/
description: كيفية تحويل Excel إلى Ods (OpenOffice / LibreOffice Calc) أو تحويل Ods (OpenOffice / LibreOffice Calc) إلى Excel باستخدام Script Aspose.Cells for Java عبر C++.
---

## **حول OpenDocument**
[تنسيق OpenDocument (ODF)](https://en.wikipedia.org/wiki/OpenDocument) هو تنسيق ملف مجاني ومفتوح للوثائق المكتبية الإلكترونية الذي طوّره الأصل لـ OpenOffice suite. تنسيق الجدول الخلية OpenDocument (ODS) هو تنسيق الملفات لوثائق Excel. حاليًا يُعتبر OpenDocument معيارًا لـ OASIS و ISO.

## **تحويل Ods (OpenOffice / LibreOffice calc) إلى Excel**
يدعم Script عبر C++ Aspose.Cells for Java تحميل Ods، Sxc و Fods التي تدعمها OpenOffice / LibreOffice Calc، وتحويل [Ods](book1.ods)، [Sxc](book1.sxc) و [Fods](book1.fods) إلى ملفات Excel.

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>Aspose.Cells Example</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            .links a { display: inline-block; margin-right: 10px; margin-top: 10px; }
            #result p { margin: 10px 0; }
        </style>
    </head>
    <body>
        <h1>Convert Excel to ODS / SXC / FODS</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <div class="links">
            <a id="downloadLinkOds" style="display: none;">Download ODS</a>
            <a id="downloadLinkSxc" style="display: none;">Download SXC</a>
            <a id="downloadLinkFods" style="display: none;">Download FODS</a>
        </div>
        <div id="result"></div>

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
            const downloadOds = document.getElementById('downloadLinkOds');
            const downloadSxc = document.getElementById('downloadLinkSxc');
            const downloadFods = document.getElementById('downloadLinkFods');

            // Clear previous links/messages
            downloadOds.style.display = 'none';
            downloadSxc.style.display = 'none';
            downloadFods.style.display = 'none';
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save as ODS
            const outputOdsData = workbook.save(SaveFormat.Ods);
            const blobOds = new Blob([outputOdsData]);
            downloadOds.href = URL.createObjectURL(blobOds);
            downloadOds.download = 'ods_out.ods';
            downloadOds.style.display = 'inline-block';
            downloadOds.textContent = 'Download ods_out.ods';

            // Save as SXC
            const outputSxcData = workbook.save(SaveFormat.Sxc);
            const blobSxc = new Blob([outputSxcData]);
            downloadSxc.href = URL.createObjectURL(blobSxc);
            downloadSxc.download = 'sxc_out.sxc';
            downloadSxc.style.display = 'inline-block';
            downloadSxc.textContent = 'Download sxc_out.sxc';

            // Save as FODS
            const outputFodsData = workbook.save(SaveFormat.Fods);
            const blobFods = new Blob([outputFodsData]);
            downloadFods.href = URL.createObjectURL(blobFods);
            downloadFods.download = 'fods_out.fods';
            downloadFods.style.display = 'inline-block';
            downloadFods.textContent = 'Download fods_out.fods';

            resultDiv.innerHTML = '<p style="color: green;">Files generated successfully. Use the links above to download.</p>';
        });
    </script>
</html>
```

## **تحويل Excel إلى Ods (OpenOffice / LibreOffice Calc)**
يدعم Script عبر C++ Aspose.Cells for Java تحويل ملفات Excel إلى ملفات Ods، Sxc و Fods. يوضح مثال الكود أدناه كيفية تحويل [القالب](book1.xlsx) إلى ملفات Ods، Sxc و Fods.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Save Workbook to ODS / SXC / FODS</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <div>
            <a id="downloadLinkOds" style="display: none; margin-right: 8px;">Download Out.ods</a>
            <a id="downloadLinkSxc" style="display: none; margin-right: 8px;">Download Out.sxc</a>
            <a id="downloadLinkFods" style="display: none;">Download Out.fods</a>
        </div>
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

            // Load your source workbook
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Save as ods file 
            const odsData = workbook.save(SaveFormat.Ods);
            const blobOds = new Blob([odsData]);
            const downloadLinkOds = document.getElementById('downloadLinkOds');
            downloadLinkOds.href = URL.createObjectURL(blobOds);
            downloadLinkOds.download = 'Out.ods';
            downloadLinkOds.style.display = 'inline-block';
            downloadLinkOds.textContent = 'Download Out.ods';

            // Save as sxc file 
            const sxcData = workbook.save(SaveFormat.Sxc);
            const blobSxc = new Blob([sxcData]);
            const downloadLinkSxc = document.getElementById('downloadLinkSxc');
            downloadLinkSxc.href = URL.createObjectURL(blobSxc);
            downloadLinkSxc.download = 'Out.sxc';
            downloadLinkSxc.style.display = 'inline-block';
            downloadLinkSxc.textContent = 'Download Out.sxc';

            // Save as fods file 
            const fodsData = workbook.save(SaveFormat.Fods);
            const blobFods = new Blob([fodsData]);
            const downloadLinkFods = document.getElementById('downloadLinkFods');
            downloadLinkFods.href = URL.createObjectURL(blobFods);
            downloadLinkFods.download = 'Out.fods';
            downloadLinkFods.style.display = 'inline-block';
            downloadLinkFods.textContent = 'Download Out.fods';

            document.getElementById('result').innerHTML = '<p style="color: green;">Files generated. Click the download links to get the converted files.</p>';
        });
    </script>
</html>
```

## **مواضيع متقدمة**
- [حفظ ملف ODS بمواصفات ODF 1.1 و 1.2](/cells/ar/javascript-cpp/save-ods-file-in-odf-1-1-and-1-2-specifications/)
- [العمل مع الخلفية في ملفات ODS](/cells/ar/javascript-cpp/working-with-background-in-ods-files/)
