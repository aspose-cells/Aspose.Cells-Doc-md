---
title: تحميل صورة ويب من عنوان URL إلى ورقة إكسل باستخدام JavaScript عبر C++
linktitle: تحميل صورة ويب من عنوان URL إلى ورقة عمل إكسل
type: docs
weight: 30
url: /ar/javascript-cpp/load-a-web-image-from-a-url-into-an-excel-worksheet/
description: كيفية تحويل صورة من URL إلى صورة فعلية في إكسل باستخدام Aspose.Cells for JavaScript عبر C++.
keywords: إظهار الصورة من رابط URL، إظهار الصورة في إكسل من الرابط، إدراج الصورة من الرابط في إكسل، تحويل الرابط إلى صورة في إكسل، صورة من الرابط في إكسل، تحميل الصورة من URL في إكسل، JavaScript، إكسل
---

## تحميل صورة من عنوان URL إلى ورقة عمل إكسل

 يوفر Aspose.Cells for JavaScript عبر C++ طريقة بسيطة وسهلة لتحميل الصور من روابط URL إلى أوراق عمل إكسل. يشرح هذا المقال كيفية تنزيل بيانات الصورة إلى تيار ثم إدراجها في ورقة العمل باستخدام API الخاص بـ Aspose.Cells. باستخدام هذه الطريقة، تصبح الصور جزءًا من ملف إكسل ولا يتم تحميلها في كل مرة تُفتح فيها ورقة العمل.

## كود عينة

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Insert Web Image</title>
    </head>
    <body>
        <h1>Insert Web Image into Excel</h1>
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
                // If no file provided, create a new workbook
                document.getElementById('result').innerHTML = '<p style="color: orange;">No input workbook selected. A new workbook will be created.</p>';
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

            // Ensure at least one worksheet exists
            if (workbook.worksheets.count === 0) {
                workbook.worksheets.add("Sheet1");
            }
            const worksheet = workbook.worksheets.get(0);

            // Download the image from the web
            const url = "https://www.aspose.com/Images/aspose-logo.jpg";
            const response = await fetch(url);
            if (!response.ok) {
                document.getElementById('result').innerHTML = `<p style="color: red;">Failed to download image: ${response.status} ${response.statusText}</p>`;
                return;
            }
            const imgArrayBuffer = await response.arrayBuffer();
            const imgBytes = new Uint8Array(imgArrayBuffer);

            // Insert the image into the worksheet at row 0, column 0
            worksheet.pictures.add(0, 0, imgBytes);

            // Save the modified workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'webimagebook.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Image inserted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}
 قد تكون هناك حالات تريد فيها دائمًا الحصول على الصورة المحدّثة من URL. لتحقيق ذلك، يمكنك اتباع التعليمات الموجودة في مقال [إدراج صورة مرتبطة من عنوان ويب](/cells/ar/javascript-cpp/insert-a-linked-picture-from-web-address/). باتباع هذه الطريقة، يتم تحميل الصورة من URL في كل مرة تُفتح فيها ورقة العمل.
{{% /alert %}}
