---
title: إنشاء دفتر عمل مشترك باستخدام Aspose.Cells for JavaScript عبر C++
linktitle: إنشاء دفتر عمل مشترك باستخدام Aspose.Cells
type: docs
weight: 40
url: /ar/javascript-cpp/create-shared-workbook-with-aspose-cells/
description: تعلم كيفية إنشاء دفتر عمل مشترك باستخدام Aspose.Cells for JavaScript عبر C++.
---

## **سيناريوهات الاستخدام المحتملة**  

يسمح Microsoft Excel بمشاركة دفتر العمل كما هو موضح في الصورة التالية. عندما تقوم بمشاركة دفتر العمل، يمكن لأكثر من مستخدم تحرير دفتر العمل على الشبكة. يتيح لك Aspose.Cells for JavaScript عبر C++ إنشاء دفتر عمل مشترك باستخدام الخاصية [**WorkbookSettings.shared**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#shared--).  

![todo:image_alt_text](create-shared-workbook-with-aspose-cells_1.png)  

## **إنشاء دفتر عمل مشترك باستخدام Aspose.Cells**  

يخلق الكود النموذجي التالي دفتر عمل مشترك عن طريق تعيين الخاصية [**WorkbookSettings.shared**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#shared--) كـ **true**. عندما تفتح ملف Excel المخرج ([ملف الإخراج](55541786.xlsx)) في Microsoft Excel، سترى **مشترك** مع اسم دفتر العمل كما هو موضح في لقطة الشاشة هذه.  

![todo:image_alt_text](create-shared-workbook-with-aspose-cells_2.png)  

## **الكود المثالي**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Create Shared Workbook Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="createShared" disabled>Create Shared Workbook</button>
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
            document.getElementById('createShared').disabled = false;
        });

        document.getElementById('createShared').addEventListener('click', async () => {
            const wb = new Workbook();

            // Share the Workbook (converted getter/setter to property)
            wb.settings.shared = true;

            // Save the Shared Workbook
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSharedWorkbook.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Shared Workbook';

            document.getElementById('result').innerHTML = '<p style="color: green;">Shared workbook created successfully! Click the download link to save the file.</p>';
        });
    </script>
</html>
```
