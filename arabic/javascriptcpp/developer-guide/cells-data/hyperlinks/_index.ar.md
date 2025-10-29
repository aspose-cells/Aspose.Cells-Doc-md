---
title: إدراج الروابط التشعبية في إكسل أو أوبن أوفيس
linktitle: إدارة الروابط التشعبية
type: docs
weight: 45
url: /ar/javascript-cpp/insert-hyperlinks-to-excel/
description: كيفية إدراج روابط تشعبية في ملف إكسل باستخدام مكتبة Aspose.Cells بدون MS Excel عبر جافا سكريبت عبر C++.
keywords: إدراج روابط تشعبية في إكسل جافا سكريبت عبر C++، إضافة أو إدراج روابط تشعبية جافا سكريبت عبر C++، إضافة أو إدراج رابط إلى عنوان URL جافا سكريبت عبر C++، إضافة أو إدراج رابط إلى خلية جافا سكريبت عبر C++، إضافة رابط إلى ملف خارجي جافا سكريبت عبر C++
---

{{% alert color="primary" %}} 

يتم استخدام الارتباط التشعبي لإنشاء ارتباط بين كيانين. الجميع على دراية باستخدام الارتباطات التشعبية، خاصة على المواقع الإلكترونية.
باستخدام Aspose.Cells، يمكن للمطورين إنشاء أنواع مختلفة من الارتباطات التشعبية في ملفات Microsoft Excel. يناقش هذا الموضوع أنواع الارتباطات التشعبية الدعمها Aspose.Cells وكيف يمكن استخدامها في ملفات Excel الخاصة بنا.

{{% /alert %}} 

## **إضافة الروابط المختصرة**
 تسمح Aspose.Cells للمطورين بإضافة روابط تشعبية إلى ملفات Excel إما باستخدام واجهة برمجة التطبيقات أو جداول البيانات المصممة (جداول البيانات التي يتم إنشاؤها يدويًا وتستخدم Aspose.Cells لاستيرادها إلى جداول بيانات أخرى).

توفر Aspose.Cells فصل، [Workbook](https://reference.aspose.com/cells/javascript-cpp/workbook) الذي يمثل ملف إكسل من مايكروسوفت. يحتوي [Workbook](https://reference.aspose.com/cells/javascript-cpp/workbook) على [WorksheetCollection](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection) التي تتيح الوصول إلى كل ورقة عمل في ملف الإكسل. تمثل ورقة العمل بواسطة فئة [Worksheet](https://reference.aspose.com/cells/javascript-cpp/worksheet). توفر فئة [Worksheet](https://reference.aspose.com/cells/javascript-cpp/worksheet) طرقًا مختلفة لإضافة روابط تشعبية مختلفة إلى ملفات إكسل.
## **إضافة رابط إلى عنوان URL**
 تحتوي فئة [Worksheet](https://reference.aspose.com/cells/javascript-cpp/worksheet) على مجموعة [hyperlinks](https://reference.aspose.com/cells/javascript-cpp/worksheet/#hyperlinks--). كل عنصر في مجموعة [hyperlinks](https://reference.aspose.com/cells/javascript-cpp/worksheet/#hyperlinks--) يمثل [Hyperlink](https://reference.aspose.com/cells/javascript-cpp/hyperlink). أضف روابط تشعبية لروابط URL عن طريق استدعاء طريقة [add](https://reference.aspose.com/cells/javascript-cpp/hyperlinkcollection/#add-string-number-number-string-) لمجموعة [Hyperlinks](https://reference.aspose.com/cells/javascript-cpp/hyperlinkcollection). تأخذ طريقة [add](https://reference.aspose.com/cells/javascript-cpp/hyperlinkcollection/#add-string-number-number-string-) المعلمات التالية:

- اسم الخلية، اسم الخلية التي سيتم إضافة الرابط التشعبي إليها.
- عدد الصفوف، عدد الصفوف في نطاق الارتباط الفائق.
- عدد الأعمدة، عدد الأعمدة في نطاق الارتباط الفائق.
- عنوان URL, عنوان عنوان URL.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Add Hyperlink Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example (Create Workbook & Add Hyperlink)</button>
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
            // Instantiate a new Workbook
            const workbook = new Workbook();

            // Obtain the reference of the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Add a hyperlink to a URL at "A1" cell
            worksheet.hyperlinks.add("A1", 1, 1, "http://www.aspose.com");

            // Save the Excel file and provide a download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and hyperlink added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```


{{% alert color="primary" %}} 

في المثال أعلاه، يتم إضافة رابط تشعبي إلى عنوان URL في خلية فارغة، **A1**. في مثل هذه الحالات، إذا كانت الخلية فارغة فإن عنوان عنوان URL يتم أيضًا إضافته إلى تلك الخلية الفارغة كقيمتها. إذا لم تكن الخلية فارغة وتمت إضافة رابط تشعبي، فإن قيمة الخلية تبدو كنص عادي. لجعلها تبدو كرابط تشعبي، ضع إعدادات التنسيق المناسبة على تلك الخلية.

{{% /alert %}} 
## **إضافة رابط إلى خلية في نفس الملف**
من الممكن إضافة روابط تشعبية إلى خلايا في نفس ملف إكسل عن طريق استدعاء طريقة [add](https://reference.aspose.com/cells/javascript-cpp/hyperlinkcollection/#add-string-number-number-string-) لمجموعة [Hyperlinks](https://reference.aspose.com/cells/javascript-cpp/hyperlinkcollection). تعمل طريقة [add](https://reference.aspose.com/cells/javascript-cpp/hyperlinkcollection/#add-string-number-number-string-) لكل من الروابط الداخلية والخارجية. نسخة المفرغة من الطريقة تتطلب المعلمات التالية:

- اسم الخلية، اسم الخلية التي سيتم إضافة الرابط التشعبي إليها.
- عدد الصفوف، عدد الصفوف في نطاق الارتباط الفائق.
- عدد الأعمدة، عدد الأعمدة في نطاق الارتباط الفائق.
- URL، عنوان الخلية المستهدفة.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Add Internal Hyperlink Example</h1>
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
            // Create a new Workbook
            const workbook = new Workbook();

            // Adding a new worksheet to the Workbook object
            workbook.worksheets.add();

            // Obtaining the reference of the first (default) worksheet
            const worksheet = workbook.worksheets.get(0);

            // Adding an internal hyperlink to the "B3" cell of the other worksheet "Sheet2" in the same Excel file
            worksheet.hyperlinks.add("B3", 1, 1, "Sheet2!B9");

            // Saving the Excel file and providing a download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Excel file created successfully. Click the download link to save it.</p>';
        });
    </script>
</html>
```


## **إضافة رابط إلى ملف خارجي**
من الممكن إضافة روابط تشعبية إلى ملفات إكسل خارجية عند استدعاء طريقة [add](https://reference.aspose.com/cells/javascript-cpp/hyperlinkcollection/#add-string-number-number-string-) لمجموعة [Hyperlinks](https://reference.aspose.com/cells/javascript-cpp/hyperlinkcollection). تأخذ طريقة [add](https://reference.aspose.com/cells/javascript-cpp/hyperlinkcollection/#add-string-number-number-string-) المعلمات التالية:

- اسم الخلية، اسم الخلية التي سيتم إضافة الرابط التشعبي إليها.
- عدد الصفوف، عدد الصفوف في نطاق الارتباط الفائق.
- عدد الأعمدة، عدد الأعمدة في نطاق الارتباط الفائق.
- عنوان الويب (URL)، عنوان الهدف، ملف Excel الخارجي.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <p>Select an optional Excel file to use its filename as the hyperlink target (or leave empty to use "book1.xls"):</p>
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
            const fileInput = document.getElementById('fileInput');
            let targetFileName = 'book1.xls';
            if (fileInput.files.length) {
                targetFileName = fileInput.files[0].name;
            }

            // Instantiating a Workbook object
            const workbook = new Workbook();

            // Adding a new worksheet to the Excel object
            const i = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(i);

            // Adding an internal hyperlink to the "A5" cell of the other worksheet "Sheet2" in the same Excel file
            worksheet.hyperlinks.add("A5", 1, 1, targetFileName);

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Hyperlink added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```



## **مواضيع متقدمة**
- [إضافة روابط تشعبية للصور](/cells/ar/javascript-cpp/add-image-hyperlinks/)
- [كشف نوع الروابط التشعبية](/cells/ar/javascript-cpp/detect-hyperlink-type/)
- [تحرير الارتباطات التشعبية لورقة العمل](/cells/ar/javascript-cpp/editing-hyperlinks-of-worksheet/)
- [الحصول على الارتباطات التشعبية في النطاق](/cells/ar/javascript-cpp/get-hyperlinks-in-range/)
