---
title: تنفيذ حجم ورق مخصص لورقة العمل للعرض باستخدام جافا سكريبت عبر C++
linktitle: تنفيذ حجم ورق مخصص لورقة العمل للتقديم
type: docs
weight: 70
url: /ar/javascript-cpp/implement-custom-paper-size-of-worksheet-for-rendering/
description: تشرح هذه المقالة كيفية استخدام API جافا سكريبت عبر C++ لضبط حجم ورق مخصص لأوراق العمل المطلوبة عند تصدير ملف إكسل إلى تنسيق PDF برمجيًا.
keywords: تعيين حجم الورق المخصص أثناء تصدير إكسل إلى PDF باستخدام JavaScript عبر C++
---

## **سيناريوهات الاستخدام المحتملة**  

لا توجد خيار مباشر لإنشاء أحجام ورق مخصصة في MS Excel، ومع ذلك، يمكنك تعيين حجم ورق مخصص لأوراق العمل الخاصة بك عند تصدير ملف Excel إلى صيغة PDF. يوضح هذا المستند كيفية تعيين حجم ورق مخصص لأوراق العمل باستخدام واجهات Aspose.Cells.  

## **تنفيذ حجم ورق مخصص لورقة العمل للتقديم**  

تسمح Aspose.Cells بتنفيذ حجم ورق مخصص للورقة العمل. يمكنك استخدام طريقة [**PageSetup.customPaperSize(number, number)**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/#customPaperSize-number-number-) من فئة [**PageSetup**](https://reference.aspose.com/cells/javascript-cpp/pagesetup/) لتحديد حجم صفحة مخصص. يوضح الكود النموذجي التالي كيفية تحديد حجم ورق مخصص لورقة العمل الأولى في دفتر العمل. يرجى أيضًا مراجعة [الإخراج PDF](45056028.pdf) الذي تم توليده باستخدام الكود التالي للمراجعة.  

## **لقطة شاشة**  

![todo:image_alt_text](implement-custom-paper-size-of-worksheet-for-rendering_1.png)  

## **الكود المثالي**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Custom PDF Paper Size Example</h1>
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
                // If no file provided, create a new workbook as in the original JavaScript example
                const wb = new Workbook();

                // Access first worksheet
                const ws = wb.worksheets.get(0);

                // Set custom paper size in unit of inches
                ws.pageSetup.customPaperSize(6, 4);

                // Access cell B4
                const b4 = ws.cells.get("B4");

                // Add the message in cell B4
                b4.value = "Pdf Page Dimensions: 6.00 x 4.00 in";

                // Save the workbook in pdf format
                const outputData = wb.save(SaveFormat.Pdf);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = 'outputCustomPaperSize.pdf';
                downloadLink.style.display = 'block';
                downloadLink.textContent = 'Download PDF File';

                document.getElementById('result').innerHTML = '<p style="color: green;">PDF created successfully! Click the download link to get the file.</p>';
                return;
            }

            // If a file is provided, open it and apply the same operations
            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate workbook from uploaded file
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const ws = wb.worksheets.get(0);

            // Set custom paper size in unit of inches
            ws.pageSetup.customPaperSize(6, 4);

            // Access cell B4
            const b4 = ws.cells.get("B4");

            // Add the message in cell B4
            b4.value = "Pdf Page Dimensions: 6.00 x 4.00 in";

            // Save the workbook in pdf format
            const outputData = wb.save(SaveFormat.Pdf);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputCustomPaperSize.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
