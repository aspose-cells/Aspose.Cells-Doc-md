---
title: تصفية نوع البيانات أثناء تحميل دفتر العمل من ملف القالب باستخدام JavaScript عبر C++
linktitle: تصفية نوع البيانات أثناء تحميل ورق العمل من ملف النموذج
type: docs
weight: 400
url: /ar/javascript-cpp/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/
---

{{% alert color="primary" %}}
أحيانًا، ترغب في تحديد نوع البيانات التي يجب تحميلها عند بناء دفتر العمل من ملف القالب. يمكن أن يحسن تصفية البيانات المحملة الأداء لغرضك الخاص، خاصة عند استخدام [LightCells APIs](/cells/ar/javascript-cpp/using-lightcells-api/). يرجى استخدام خاصية [**LoadOptions.loadFilter**](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#loadFilter--) لهذا الغرض.
{{% /alert %}}

يقوم الكود النموذجي التالي بتحميل كائنات الشكل فقط أثناء تحميل دفتر العمل من [ملف القالب](5115552.xlsx) والذي يمكنك تنزيله من الرابط المعطى. توضح الصورة التالية محتويات [ملف القالب](5115552.xlsx) كما تشرح أن البيانات باللون الأحمر والخلفية الصفراء لن يتم تحميلها لأن الخاصية [**LoadOptions.loadFilter**](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#loadFilter--) تم تعيينها إلى [**Shape**](https://reference.aspose.com/cells/javascript-cpp/shape/)

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)

تُظهر اللقطة الشاشية التالية ال [PDF الناتج](5115555.pdf) الذي يمكنك تحميله من الرابط المقدم. هنا يمكنك أن ترى، البيانات ذات اللون الأحمر والخلفية الصفراء غير موجودة لكن جميع الأشكال موجودة.

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_2.png)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, LoadFormat, LoadFilter, LoadDataFilterOptions, Utils } = AsposeCells;

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

            // Set the load options, we only want to load shapes and do not want to load data
            const loadOptions = new LoadOptions(LoadFormat.Xlsx);
            loadOptions.loadFilter = new LoadFilter(LoadDataFilterOptions.All & ~LoadDataFilterOptions.Chart);

            // Create workbook object from uploaded excel file using load options
            const workbook = new Workbook(new Uint8Array(arrayBuffer), loadOptions);

            // Save the output in pdf format
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sampleFilterChars_out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Result PDF';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```
