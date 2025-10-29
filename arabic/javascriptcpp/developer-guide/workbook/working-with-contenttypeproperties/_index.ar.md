---
title: العمل مع خصائص نوع المحتوى باستخدام جافا سكريبت عبر ++C
linktitle: العمل مع خصائص نوع الوسائط
type: docs
weight: 150
url: /ar/javascript-cpp/working-with-contenttypeproperties/
description: تعلم كيفية العمل مع خصائص نوع المحتوى المخصصة في ملفات Excel باستخدام Aspose.Cells for JavaScript عبر ++C
---

يوفر Aspose.Cells طريقة [**Workbook.contentTypeProperties**](https://reference.aspose.com/cells/javascript-cpp/workbook/#contentTypeProperties--) لإضافة ContentTypeProperties مخصصة إلى ملف إكسل. يمكنك أيضًا جعل الخاصية اختيارية عن طريق تعيين خاصية [**ContentTypeProperty.isNillable()**](https://reference.aspose.com/cells/javascript-cpp/contenttypeproperty/#isNillable--) إلى **true**. يوضح مقتطف الكود التالي كيف يتم إضافة Properties مخصصة اختيارية إلى ملف إكسل. تُظهر الصورة التالية كلا الخاصيتين اللتين تمت إضافتهما بواسطة الكود النموذجي.

![todo:image_alt_text](working-with-contenttypeproperties_1.jpg)

يتم إرفاق ملف الإخراج الذي تم إنشاؤه بواسطة مقتطف الكود للإشارة.

[ملف الإخراج](95584314.xlsx)

## **الكود المثالي**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Working With Content Type Properties</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample" disabled>Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, FileFormatType } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
            document.getElementById('runExample').disabled = false;
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const resultDiv = document.getElementById('result');

            // Creating a new Workbook with Xlsx format
            const workbook = new Workbook(FileFormatType.Xlsx);

            // Adding content type properties
            let index = workbook.contentTypeProperties.add("MK31", "Simple Data");
            workbook.contentTypeProperties.get(index).isNillable = false;

            index = workbook.contentTypeProperties.add("MK32", new Date().toISOString(), "DateTime");
            workbook.contentTypeProperties.get(index).isNillable = true;

            // Saving the workbook and preparing download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'WorkingWithContentTypeProperties_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
