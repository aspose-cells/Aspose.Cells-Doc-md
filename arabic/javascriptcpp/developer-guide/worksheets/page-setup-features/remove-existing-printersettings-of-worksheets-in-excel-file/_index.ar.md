---
title: إزالة إعدادات الطابعة الحالية لأوراق العمل في ملف إكسل باستخدام JavaScript عبر C++
linktitle: إزالة إعدادات الطابعة الحالية لورقة العمل في ملف Excel
type: docs
weight: 60
url: /ar/javascript-cpp/remove-existing-printersettings-of-worksheets-in-excel-file/
description: في هذا المقال، ستتعلم كيفية إزالة إعدادات الطابعة الموجودة لأوراق العمل داخل ملف إكسل برمجياً باستخدام Aspose.Cells for JavaScript عبر C++.
keywords: إزالة إعدادات الطابعة لورقة العمل JavaScript عبر C++، إزالة إعدادات الطابعة لورقة إكسل JavaScript عبر C++
---

## **سيناريوهات الاستخدام المحتملة**
في بعض الأحيان، يرغب المطورون في منع Excel من تضمين ملفات *.bin* لإعدادات الطابعة في ملفات XLSX المحفوظة. تقع ملفات إعدادات الطابعة تحت *“[file "root"]\xl\printerSettings”.* يوضح هذا المستند كيفية إزالة إعدادات الطابعة الحالية باستخدام واجهة برمجة التطبيقات Aspose.Cells.

## **إزالة إعدادات الطابعة الحالية لورقات العمل في ملف Excel**
تتيح Aspose.Cells إزالة إعدادات الطابعة الحالية المحددة لورقات العمل المختلفة في ملف Excel. يوضح الكود العينات التالية كيفية إزالة إعدادات الطابعة الحالية لجميع ورقات العمل في الدفتر. يرجى الاطلاع على [ملف Excel عينة](45056020.xlsx)، [ملف Excel الناتج](45056021.xlsx)، الإخراج على وحدة التحكم، فضلاً عن اللقطة للإشارة.

## **لقطة شاشة**
![todo:image_alt_text](remove-existing-printersettings-of-worksheets-in-excel-file_1.png)

## **الكود المثالي**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Remove Printer Settings</title>
        <meta charset="utf-8" />
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            #result { margin-top: 15px; white-space: pre-wrap; }
            input, button { margin-top: 10px; display: block; }
        </style>
    </head>
    <body>
        <h1>Remove Existing Printer Settings Of Worksheets</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>

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
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Get the sheet counts of the workbook
            const sheetCount = wb.worksheets.count;

            const messages = [];
            // Iterate all sheets
            for (let i = 0; i < sheetCount; i++) {
                // Access the i-th worksheet
                const ws = wb.worksheets.get(i);

                // Access worksheet page setup
                const ps = ws.pageSetup;

                // Check if printer settings for this worksheet exist
                if (ps.printerSettings != null) {
                    // Print the following message
                    console.log("PrinterSettings of this worksheet exist.");
                    messages.push("PrinterSettings of this worksheet exist.");

                    // Print sheet name and its paper size
                    console.log("Sheet Name: " + ws.name);
                    console.log("Paper Size: " + ps.paperSize);
                    messages.push("Sheet Name: " + ws.name);
                    messages.push("Paper Size: " + ps.paperSize);

                    // Remove the printer settings by setting them null
                    ps.printerSettings = null;
                    console.log("Printer settings of this worksheet are now removed by setting it null.");
                    messages.push("Printer settings of this worksheet are now removed by setting it null.");
                    messages.push("");
                }
            }

            // Save the workbook
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputRemoveExistingPrinterSettingsOfWorksheets.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p><pre>' + messages.join('\n') + '</pre>';
        });
    </script>
    </body>
</html>
```

## **مخرجات الوحدة**
{{< highlight javascript >}}

 PrinterSettings of this worksheet exist.

Sheet Name: Sheet1

Paper Size: PaperLegal

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet2

Paper Size: PaperEnvelopeB5

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet3

Paper Size: PaperA6

Printer settings of this worksheet are now removed by setting it null.

PrinterSettings of this worksheet exist.

Sheet Name: Sheet4

Paper Size: PaperA3

Printer settings of this worksheet are now removed by setting it null.

{{< /highlight >}}
