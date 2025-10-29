---
title: إضافة روابط فائقة النص للصور
type: docs
weight: 140
url: /ar/javascript-cpp/add-image-hyperlinks/
description: تعلم كيفية إضافة روابط الصور من خلال Aspose.Cells for JavaScript عبر واجهة برمجة التطبيقات C++.
keywords: إضافة روابط صور JavaScript عبر C++، إدراج روابط صور JavaScript عبر C++
---

{{% alert color="primary" %}} 

الروابط التشعبية مفيدة للوصول إلى معلومات على أوراق عمل أخرى أو على مواقع إلكترونية. يتيح Microsoft Excel للمستخدمين إضافة روابط على النصوص داخل الخلايا وعلى الصور. يمكن أن تجعل روابط الصور التنقل في ورقة العمل أسهل، على سبيل المثال، أزرار التالي والسابق، أو الشعارات التي ترتبط بمواقع معينة. يشرح هذا المستند كيفية إدراج روابط صور في ورقة عمل باستخدام Aspose.Cells for JavaScript عبر C++.

{{% /alert %}} 

 يتيح Aspose.Cells for JavaScript عبر C++ إضافة روابط تشعبية للصور في جداول البيانات في وقت التشغيل. من الممكن تعيين وتعديل نص التلميح الخاص بالارتباط وعنوانه. يوضح رمز المثال التالي كيفية إضافة ارتباط صورة إلى ورقة عمل.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Image Hyperlink Example</h1>
        <p>Select an optional Excel file to modify, or leave blank to create a new workbook.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <p>Select an image to insert as a picture with a hyperlink:</p>
        <input type="file" id="imageInput" accept="image/*" />
        <br /><br />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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
            const imageInput = document.getElementById('imageInput');
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '';

            if (!imageInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an image file to add as a picture.</p>';
                return;
            }

            // Create or load workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Get the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Insert a string value to a cell
            const cell = worksheet.cells.get("C2");
            cell.value = "Image Hyperlink";

            // Set the 4th row height (row index 3)
            const row = worksheet.cells.rows.get(3);
            row.height = 100;

            // Set the C column width (column index 2)
            const column = worksheet.cells.columns.get(2);
            column.width = 21;

            // Read the image file bytes
            const imgFile = imageInput.files[0];
            const imgArrayBuffer = await imgFile.arrayBuffer();
            const imgBytes = new Uint8Array(imgArrayBuffer);

            // Add a picture to the C4 cell (using coordinates similar to Node example)
            const picIndex = worksheet.pictures.add(3, 2, 4, 3, imgBytes);

            // Get the picture object
            const pic = worksheet.pictures.get(picIndex);

            // Set the placement type (converted from setPlacement)
            pic.placement = AsposeCells.Drawing.PlacementType.FreeFloating;

            // Add an image hyperlink
            const hlink = pic.addHyperlink("http://www.aspose.com/");

            // Specify the screen tip (converted from setScreenTip)
            hlink.screenTip = "Click to go to Aspose site";

            // Save the Excel file (using Excel97To2003 for .xls output)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'ImageHyperlink.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Image with hyperlink added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
