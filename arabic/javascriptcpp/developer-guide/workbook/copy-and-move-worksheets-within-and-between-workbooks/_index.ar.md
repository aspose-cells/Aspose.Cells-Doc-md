---
title: نسخ ونقل أوراق العمل داخل وبين دفاتر العمل باستخدام جافا سكريبت عبر C++
linktitle: نسخ ونقل أوراق العمل داخل وبين أوراق العمل
type: docs
weight: 80
url: /ar/javascript-cpp/copy-and-move-worksheets-within-and-between-workbooks/
description: تعلم كيفية نسخ ونقل أوراق العمل داخل وبين دفاتر العمل باستخدام Aspose.Cells for JavaScript عبر C++. إدارة بنية دفتر العمل بكفاءة.
---

{{% alert color="primary" %}}

أحيانًا، تحتاج إلى عدد من أوراق العمل مع تنسيقات وإدخال بيانات مشتركة. على سبيل المثال، إذا كنت تعمل مع الميزانيات الربعية، قد ترغب في إنشاء دفتر عمل يحتوي على أوراق تحتوي على نفس عناوين الأعمدة وعناوين الصفوف والصيغ. هناك طريقة للقيام بذلك: عن طريق إنشاء ورقة واحدة ثم نسخها ثلاث مرات.

يدعم Aspose.Cells for JavaScript عبر C++نسخ أو نقل أوراق العمل داخل أو بين دفاتر العمل. يتم نسخ الأوراق بما في ذلك البيانات، التنسيقات، الجداول، المصفوفات، الرسوم البيانية، الصور، وغيرها من الكائنات بأعلى درجة من الدقة.

{{% /alert %}}

## **نسخ ونقل أوراق العمل**

### **نسخ ورقة عمل داخل دفتر عمل**

الخطوات الأولية هي نفسها لجميع الأمثلة.

1. أنشئ معينين بيانات في Microsoft Excel. لأغراض هذا المثال، قمنا بإنشاء معينين جديدين في Microsoft Excel وإدخال بعض البيانات إلى أوراق العمل.

- FirstWorkbook.xlsx (3 ورقات عمل).
- SecondWorkbook.xlsx (ورقة عمل واحدة).

1. قم بتنزيل وتثبيت Aspose.Cells:
   1. [تحميل Aspose.Cells for JavaScript عبر C++](https://downloads.aspose.com/cells/javascript-cpp).
   1. قم بتثبيته على كمبيوتر التطوير الخاص بك.
      جميع [مكونات Aspose](http://www.aspose.com/) ، عند التثبيت، تعمل في وضع التقييم. وضع التقييم ليس له حد زمني ولكنه يضيف علامات مائية فقط إلى المستندات المنتجة.
1. أنشئ مشروعًا:
   1.ابدأ بيئة تطويرك.
   1. أنشئ تطبيقًا جديدًا على الكونسول.
1. أضف مراجع:
   1. أضف مرجعًا إلى Aspose.Cells إلى المشروع.
      على سبيل المثال، أضف مرجع إلى ...\Program Files\Aspose\Aspose.Cells\Bin\NodeJs\Aspose.Cells.dll
1. نسخ ورقة العمل داخل دفتر العمل
   المثال الأول يقوم بنسخ الورقة الأولى (نسخ) داخل FirstWorkbook.xlsx.

عند تنفيذ الكود، يتم نسخ ورقة العمل التي تحمل اسم نسخ داخل FirstWorkbook.xlsx بإسم الورقة الأخيرة.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Copy Worksheet Example</title>
    </head>
    <body>
        <h1>Copy Worksheet Example</h1>
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Copy the first sheet of the first book within the workbook
            workbook.worksheets.get(2).copy(workbook.worksheets.get("Copy"));

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'FirstWorkbookCopied_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Worksheet copied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **نقل ورقة العمل داخل دفتر العمل**

يظهر الكود أدناه كيفية نقل ورقة العمل من موقع إلى آخر في دفتر العمل. عند تنفيذ الكود، يتم نقل ورقة العمل التي تسمى Move من المؤشر 1 إلى المؤشر 2 في FirstWorkbook.xlsx.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Move Worksheet Example</h1>
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

            // Move the first sheet to index 1
            const worksheets = workbook.worksheets;
            const worksheet = worksheets.get(0);
            worksheet.moveTo(1);

            // Saving the modified Excel file and offering it for download
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'FirstWorkbookMoved_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet moved successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **نسخ ورقة العمل بين دفاتر العمل**

ينفذ الرمز نسخة من ورقة العمل المسماة Copy إلى ملف SecondWorkbook.xlsx باسم Sheet2.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Copy Worksheets Between Workbooks</h1>
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
            // Create two workbooks
            const excelWorkbook3 = new Workbook();
            const excelWorkbook4 = new Workbook();

            // Create source worksheet
            excelWorkbook3.worksheets.add("Copy");

            // Add new worksheet into second Workbook
            excelWorkbook4.worksheets.add();

            // Copy the first sheet of the first book into second book.
            excelWorkbook4.worksheets.get(1).copy(excelWorkbook3.worksheets.get("Copy"));

            // Save the file.
            const outputData = excelWorkbook4.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'CopyWorksheetsBetweenWorkbooks_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheets copied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **نقل ورقة العمل بين دفاتر العمل**

عند تنفيذ الكود، يتم نقل ورقة العمل المسماة Move من FirstWorkbook.xlsx إلى SecondWorkbook.xlsx بإسم Sheet3.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Move Worksheets Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink1" style="display: none; margin-right: 10px;">Download First Workbook</a>
        <a id="downloadLink2" style="display: none;">Download Second Workbook</a>
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
            // Create new workbooks instead of opening existing files
            const excelWorkbook5 = new Workbook();
            const excelWorkbook6 = new Workbook();

            // Add New Worksheet
            excelWorkbook6.worksheets.add();

            // Copy the sheet from first book into second book.
            excelWorkbook6.worksheets.get(0).copy(excelWorkbook5.worksheets.get(0));

            // Remove the copied worksheet from first workbook
            excelWorkbook5.worksheets.removeAt(0);

            // Save the first workbook
            const outputData1 = excelWorkbook5.save(SaveFormat.Xlsx);
            const blob1 = new Blob([outputData1]);
            const downloadLink1 = document.getElementById('downloadLink1');
            downloadLink1.href = URL.createObjectURL(blob1);
            downloadLink1.download = 'FirstWorkbookWithMove_out.xlsx';
            downloadLink1.style.display = 'inline';
            downloadLink1.textContent = 'Download FirstWorkbookWithMove_out.xlsx';

            // Save the second workbook
            const outputData2 = excelWorkbook6.save(SaveFormat.Xlsx);
            const blob2 = new Blob([outputData2]);
            const downloadLink2 = document.getElementById('downloadLink2');
            downloadLink2.href = URL.createObjectURL(blob2);
            downloadLink2.download = 'SecondWorkbookWithMove_out.xlsx';
            downloadLink2.style.display = 'inline';
            downloadLink2.textContent = 'Download SecondWorkbookWithMove_out.xlsx';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbooks processed successfully. Click the download links to retrieve the files.</p>';
        });
    </script>
</html>
```
