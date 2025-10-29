---
title: إدارة التعليقات والملاحظات باستخدام JavaScript عبر C++
linktitle: التعليقات والملاحظات
type: docs
weight: 128
url: /ar/javascript-cpp/comments-and-notes/
description: إدراج وإدارة التعليقات أو الملاحظات باستخدام 8667720447سكربت عبر C++.
keywords: إدراج تعليقات، إدراج ملاحظات JavaScript عبر C++
---

## **مقدمة**

تُستخدم التعليقات لإضافة معلومات إضافية إلى الخلايا. توفر 8667720447سكربت عبر C++ طريقتين لإضافة التعليقات إلى الخلايا. الأولى هي إنشاء تعليقات في ملف المُصمم يدويًا، ثم يتم استيرادها باستخدام Aspose.Cells. الثانية هي إضافة التعليقات باستخدام API الخاص بـ Aspose.Cells في الوقت الفعلي. يناقش هذا الموضوع إضافة التعليقات إلى الخلايا باستخدام API الخاص بـ Aspose.Cells. كما سيتم شرح تنسيق التعليقات.

## **إضافة تعليق**

إضافة تعليق إلى خلية عن طريق استدعاء طريقة مجموعة [**Comments**](https://reference.aspose.com/cells/javascript-cpp/commentcollection) (الم encapsulated في كائن [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)). يمكن الوصول إلى كائن [**Comment**](https://reference.aspose.com/cells/javascript-cpp/comment) الجديد من مجموعة [**Comments**](https://reference.aspose.com/cells/javascript-cpp/commentcollection) عن طريق تمرير فهرس التعليق. بعد الوصول إلى كائن [**Comment**](https://reference.aspose.com/cells/javascript-cpp/comment)، قم بتخصيص ملاحظة التعليق باستخدام الخاصية [**note**](https://reference.aspose.com/cells/javascript-cpp/comment/#note--).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Add Comment Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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
            // Instantiating a Workbook object
            const workbook = new Workbook();

            // Adding a new worksheet to the Workbook object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding a comment to "F5" cell
            const commentIndex = worksheet.comments.add("F5");

            // Accessing the newly added comment
            const comment = worksheet.comments.get(commentIndex);

            // Setting the comment note
            comment.note = "Hello Aspose!";

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Comment added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **تنسيق التعليق**

من الممكن أيضًا تنسيق مظهر التعليقات عن طريق تكوين ارتفاعها، وعرضها وإعدادات الخط.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Comment</title>
    </head>
    <body>
        <h1>Add Comment Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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
            // Creating a new Workbook object
            const workbook = new Workbook();

            // Adding a new worksheet to the Workbook object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding a comment to "F5" cell
            const commentIndex = worksheet.comments.add("F5");

            // Accessing the newly added comment
            const comment = worksheet.comments.get(commentIndex);

            // Setting the comment note
            comment.note = "Hello Aspose!";

            // Setting the font size of a comment to 14
            comment.font.size = 14;

            // Setting the font of a comment to bold
            comment.font.isBold = true;

            // Setting the height of the font to 10
            comment.heightCM = 10;

            // Setting the width of the font to 2
            comment.widthCM = 2;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and saved. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **إضافة صورة إلى التعليق**

مع Microsoft Excel 2007، من الممكن أيضًا وضع صورة كخلفية لتعليق الخلية. في Excel 2007، يمكن القيام بذلك من خلال الخطوات التالية. (يلزم أن يكون قد تم بالفعل إضافة تعليق للخلية.)

1. انقر بزر الماوس الأيمن فوق الخلية التي تحتوي على التعليق.
1. حدد **إظهار/إخفاء التعليقات**، وامسح أي نص من التعليق.
1. انقر على الحد للتعليق لتحديده.
1. حدد **تنسيق**، ثم **تعليق**.
1. على علامة تبويب **الألوان والخطوط**، قم بتوسيع قائمة **اللون**.
1. انقر على **ملء الآثار**.
1. على علامة تبويب **الصورة**، انقر على **تحديد صورة**.
1. العثور على الصورة وتحديدها.
1. انقر على **موافق** حتى يتم إغلاق جميع الحوارات.

توفر Aspose.Cells أيضًا هذه الميزة. فيما يلي عينة من الشفرة التي تنشئ ملف XLSX من البداية، مع إضافة تعليق إلى الخلية "A1" وتعيين صورة كخلفية لها.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Comment with Image</title>
    </head>
    <body>
        <h1>Add Comment with Image Example</h1>
        <p>
            Select an existing Excel file to modify (optional). If no file is selected, a new workbook will be created.
        </p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <p>
            Select an image file to attach to the comment (required):
        </p>
        <input type="file" id="imageInput" accept="image/*" />
        <br/><br/>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
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
            const resultEl = document.getElementById('result');
            resultEl.innerHTML = '';

            const fileInput = document.getElementById('fileInput');
            const imageInput = document.getElementById('imageInput');

            if (!imageInput.files.length) {
                resultEl.innerHTML = '<p style="color: red;">Please select an image file for the comment.</p>';
                return;
            }

            // Load or create workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Get a reference of comments collection with the first sheet
            const comments = workbook.worksheets.get(0).comments;

            // Add a comment to cell A1
            const commentIndex = comments.add(0, 0);
            const comment = comments.get(commentIndex);

            // Set the comment note and font name (converted from set/get to properties)
            comment.note = "First note.";
            comment.font.name = "Times New Roman";

            // Load image file data
            const imgFile = imageInput.files[0];
            const imgArrayBuffer = await imgFile.arrayBuffer();
            const imgUint8 = new Uint8Array(imgArrayBuffer);

            // Set image data to the shape associated with the comment
            comment.commentShape.fill.imageData = imgUint8;

            // Save the workbook to browser-downloadable file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultEl.innerHTML = '<p style="color: green;">Comment added with image successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **مواضيع متقدمة**
- [تغيير اتجاه النص للتعليق](/cells/ar/javascript-cpp/change-text-direction-of-the-comment/)
- [كيفية تغيير لون خط التعليق](/cells/ar/javascript-cpp/how-to-change-the-comment-font-color/)
- [كيفية تعيين خلفية التعليق](/cells/ar/javascript-cpp/how-to-set-comment-background/)
- [تعليقات متداخلة](/cells/ar/javascript-cpp/threaded-comments/)
