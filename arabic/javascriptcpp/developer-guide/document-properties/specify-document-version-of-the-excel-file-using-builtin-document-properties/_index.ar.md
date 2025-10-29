---
title: حدد إصدار المستند لملف Excel باستخدام خصائص المستند المدمجة مع جافا سكريبت عبر C++
linktitle: تحديد إصدار المستند لملف الإكسل باستخدام خصائص المستند المضمنة
type: docs
weight: 20
url: /ar/javascript-cpp/specify-document-version-of-the-excel-file-using-builtin-document-properties/
description: تعلم كيفية تحديد إصدار مستند ملف Excel برمجياً باستخدام خصائص المستند المدمجة مع جافا سكريبت عبر C++.
---

## **سيناريوهات الاستخدام المحتملة**  

 يمكنك تغيير **رقم الإصدار** لملف إكسل بالنقر بزر الماوس الأيمن على الملف ثم اختيار خصائص > تفاصيل ثم تحرير حقل **رقم الإصدار**. يرجى استخدام الخاصية [**BuiltInDocumentPropertyCollection.documentVersion**](https://reference.aspose.com/cells/javascript-cpp/builtindocumentpropertycollection/#documentVersion--) لتغييره برمجيًا باستخدام واجهات برمجة تطبيقات Aspose.Cells.  

## **تحديد إصدار المستند لملف الإكسل باستخدام خصائص المستند المضمنة**  

 يخلق رمز النموذج التالي دفتر عمل ويغير خصائص المستند المدمجة التي تشمل العنوان، المؤلفين، ورقم الإصدار. يرجى الاطلاع على ملف إكسل الناتج (64716811.xlsx) المولد بواسطة الكود وصورة الشاشة التي تظهر رقم الإصدار المعدل بواسطة الخاصية [**BuiltInDocumentPropertyCollection.documentVersion**](https://reference.aspose.com/cells/javascript-cpp/builtindocumentpropertycollection/#documentVersion--).  

![todo:image_alt_text](specify-document-version-of-the-excel-file-using-builtin-document-properties_1.png)  

## **الكود المثالي**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Specify Document Version Example</h1>
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
            // Create workbook object
            const wb = new Workbook();

            // Access built-in document property collection
            const bdpc = wb.builtInDocumentProperties;

            // Set the title
            bdpc.title = "Aspose File Format APIs";

            // Set the author
            bdpc.author = "Aspose APIs Developers";

            // Set the document version
            bdpc.documentVersion = "Aspose.Cells Version - 18.3";

            // Save the workbook in xlsx format
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSpecifyDocumentVersionOfExcelFile.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and prepared for download. Click the download link to get the file.</p>';
        });
    </script>
</html>
```
