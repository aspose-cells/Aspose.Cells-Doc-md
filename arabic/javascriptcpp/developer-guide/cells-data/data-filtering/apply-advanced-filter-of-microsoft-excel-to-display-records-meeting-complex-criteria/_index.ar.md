---
title: تطبيق مرشح Microsoft Excel المتقدم لعرض السجلات التي تلبي معايير معقدة
type: docs
weight: 280
url: /ar/javascript-cpp/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/
description: تعلم كيفية تطبيق فلتر متقدم على إكسل لعرض السجلات التي تلبي معايير معقدة باستخدام Aspose.Cells for JavaScript عبر API C++.
keywords: تطبيق الفلتر المتقدم جافا سكريبت عبر C++، تحديد الفلتر المتقدم جافا سكريبت عبر C++، إضافة فلتر متقدم جافا سكريبت عبر C++، إنشاء فلتر متقدم جافا سكريبت عبر C++، كيف تضيف فلتر متقدم إلى نطاق جافا سكريبت عبر C++
---

## **سيناريوهات الاستخدام المحتملة**  

يسمح لك Microsoft Excel بتطبيق *التصفية المتقدمة* على بيانات ورقة العمل لعرض السجلات التي تلبي معايير معقدة. يمكنك تطبيق التصفية المتقدمة باستخدام أمر *البيانات > متقدمة* كما هو موضح في لقطة الشاشة هذه.  

![todo:image_alt_text](1.png)  

 يتيح لك Aspose.Cells for JavaScript عبر C++ أيضًا تطبيق الفلتر المتقدم باستخدام طريقة [**Worksheet.advanced_Filter()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#advanced_Filter-boolean-string-string-string-boolean-). تمامًا كما في Microsoft Excel، فإنه يقبل المعلمات التالية.  

**isFilter**  

يشير ما إذا كان يتم تصفية القائمة في المكان.  

**listRange**  

نطاق القائمة.  

**criteriaRange**  

نطاق المعيار.  

**copyTo**  

نطاق نسخ البيانات إليه.  

**uniqueRecordOnly**  

عرض أو نسخ الصفوف الفريدة فقط.  

## **تطبيق مرشح Microsoft Excel المتقدم لعرض السجلات التي تلبي معايير معقدة**  

الكود النموذجي التالي يطبق التصفية المتقدمة على ملف Excel [ملف Excel النموذجي](48496692.xlsx) ويولد ملف [ملف إخراج Excel](48496691.xlsx). تُظهر لقطة الشاشة كلا الملفين للمقارنة. كما ترى في لقطة الشاشة، تم تصفية البيانات داخل ملف الإخراج وفقًا لمعايير معقدة.  

![todo:image_alt_text](2.png)  

## **الكود المثالي**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Advanced Filter Example</title>
    </head>
    <body>
        <h1>Advanced Filter Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Advanced Filter</button>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file (sampleAdvancedFilter.xlsx).</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            const wb = new Workbook(new Uint8Array(arrayBuffer));

            const ws = wb.worksheets.get(0);

            // Apply advanced filter on range A5:D19 with criteria A1:D2, filter in place, include all records (not unique)
            ws.advanced_Filter(true, "A5:D19", "A1:D2", "", false);

            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputAdvancedFilter.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Filtered Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Advanced filter applied successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
