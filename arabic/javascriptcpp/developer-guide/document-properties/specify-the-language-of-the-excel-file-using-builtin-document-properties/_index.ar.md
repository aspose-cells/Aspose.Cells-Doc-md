---
title: حدد لغة ملف Excel باستخدام خصائص المستند المدمجة مع جافا سكريبت عبر C++
linktitle: تحديد لغة ملف إكسل باستخدام الخصائص المدمجة للمستند
type: docs
weight: 30
url: /ar/javascript-cpp/specify-the-language-of-the-excel-file-using-builtin-document-properties/
---

## **سيناريوهات الاستخدام المحتملة**

يمكنك تغيير لغة ملف Excel عن طريق النقر بزر الفأرة الأيمن على الملف ثم اختيار خصائص > التفاصيل ثم تحرير حقل اللغة. يرجى استخدام الخاصية [**BuiltInDocumentPropertyCollection.language**](https://reference.aspose.com/cells/javascript-cpp/builtindocumentpropertycollection/#language--) لتغييرها برمجياً باستخدام Aspose.Cells for JavaScript عبر واجهات برمجة التطبيقات C++.

## **تحديد لغة ملف إكسل باستخدام الخصائص المدمجة للمستند**

 يخلق رمز النموذج التالي دفتر عمل ويغير الخاصية المدمجة لاسم اللغة. يرجى الاطلاع على ملف إكسل الناتج (64716891.xlsx) المولد بواسطة الكود وصورة الشاشة التي تظهر حقل اللغة المعدل بواسطة الخاصية [**BuiltInDocumentPropertyCollection.language**](https://reference.aspose.com/cells/javascript-cpp/builtindocumentpropertycollection/#language--).

![todo:image_alt_text](specify-the-language-of-the-excel-file-using-builtin-document-properties_1.png)

## **الكود المثالي**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Specify Language Using BuiltInDocumentProperties</h1>
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

        document.getElementById('runExample').addEventListener('click', () => {
            // Create workbook object.
            const wb = new Workbook();

            // Access built-in document property collection.
            const bdpc = wb.builtInDocumentProperties;

            // Set the language of the Excel file.
            bdpc.language = "German, French";

            // Save the workbook in xlsx format.
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSpecifyLanguageOfExcelFileUsingBuiltInDocumentProperties.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Language set successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
