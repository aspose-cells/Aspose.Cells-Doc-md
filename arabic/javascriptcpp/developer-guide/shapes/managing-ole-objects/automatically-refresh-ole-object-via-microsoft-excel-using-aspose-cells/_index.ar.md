---
title: تحديث تلقائي لكائن OLE عبر Microsoft Excel باستخدام Aspose.Cells for JavaScript عبر C++
linktitle: تحديث كائن Ole تلقائيًا عبر Microsoft Excel باستخدام Aspose.Cells
type: docs
weight: 270
url: /ar/javascript-cpp/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/
description: تعلم كيفية تحديث أوتوماتيكي لكائنات OLE في Excel باستخدام Aspose.Cells for JavaScript عبر C++،.
---

{{% alert color="primary" %}}  
يوفر Aspose.Cells خاصية [**OleObject.autoLoad**](https://reference.aspose.com/cells/javascript-cpp/oleobject/#autoLoad--) لتحديث كائن OLE عند فتح ملف الإكسل في Microsoft Excel. نتيجة لهذه الخاصية، سيعرض الكائن OLE الصورة الصحيحة المُولدة بواسطة Microsoft Excel.  
{{% /alert %}}  

يقوم الكود العينة التالي بتحميل [ملف الإكسل العينة](5115231.xlsx) الذي يحتوي على صورة OLE غير حقيقية. الكائن OLE هو في الواقع مستند Microsoft Word ولكن ملف الإكسل العينة يعرض صورة الحيوان بدلاً من صورة Microsoft Word. ولكن إذا فتحت [ملف الإكسل الناتج](5115225.xlsx)، سترى Microsoft Excel عرض الصورة الصحيحة لـ OLE.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Refresh OLE Objects Example</title>
    </head>
    <body>
        <h1>Refresh OLE Objects Example</h1>
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

            // Access first worksheet
            const sheet = workbook.worksheets.get(0);

            // Set auto load property of first ole object to true
            sheet.oleObjects.get(0).autoLoad = true;

            // Save the workbook in xlsx format and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'RefreshOLEObjects_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">OLE object autoLoad set to true. Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
