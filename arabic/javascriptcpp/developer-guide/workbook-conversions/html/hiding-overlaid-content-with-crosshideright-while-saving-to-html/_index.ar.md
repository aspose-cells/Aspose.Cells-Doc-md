---
title: إخفاء المحتوى المتراكب باستخدام CrossHideRight عند الحفظ إلى HTML باستخدام JavaScript عبر C++
linktitle: إخفاء المحتوى المتراكب باستخدام CrossHideRight أثناء الحفظ إلى HTML
type: docs
weight: 100
url: /ar/javascript-cpp/hiding-overlaid-content-with-crosshideright-while-saving-to/
---

## **سيناريوهات الاستخدام المحتملة**

عند حفظ ملف إكسل إلى HTML، يمكنك تحديد أنواع تقاطع مختلفة لسلاسل الخلايا. بشكل افتراضي، يولد Aspose.Cells HTML وفقًا لـ Microsoft Excel، ولكنه عند تغيير نوع التقاطع إلى [**CrossHideRight**](https://reference.aspose.com/cells/javascript-cpp/htmlcrosstype)، فإنه يخفي جميع النصوص على الجانب الأيمن من الخلية التي تتراكب أو تتداخل مع نص الخلية.

## **إخفاء المحتوى المتراكب باستخدام CrossHideRight أثناء الحفظ إلى Html**

يحمِّل الكود النموذجي التالي [ملف إكسل النموذجي](64716894.xlsx) ويحفظه إلى [ملف HTML الإخراجي](64716893.zip) بعد ضبط [**HtmlSaveOptions.htmlCrossStringType**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#htmlCrossStringType--) كـ [**CrossHideRight**](https://reference.aspose.com/cells/javascript-cpp/htmlcrosstype). يشرح لقطة الشاشة كيف يؤثر [**CrossHideRight**](https://reference.aspose.com/cells/javascript-cpp/htmlcrosstype) على ملف HTML الناتج من الوضع الافتراضي.

![todo:image_alt_text](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **الكود المثالي**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Hiding Overlaid Content With CrossHideRight While Saving To Html</title>
    </head>
    <body>
        <h1>Hiding Overlaid Content With CrossHideRight While Saving To Html</h1>
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

            // Instantiating a Workbook object by opening the Excel file from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Specify HtmlSaveOptions - Hide Overlaid Content with CrossHideRight while saving to Html
            const opts = new AsposeCells.HtmlSaveOptions();
            opts.htmlCrossStringType = AsposeCells.HtmlCrossType.CrossHideRight;

            // Save to HTML with HtmlSaveOptions
            const outputData = workbook.save(SaveFormat.Html, opts);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputHidingOverlaidContentWithCrossHideRightWhileSavingToHtml.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">HTML file created successfully! Click the download link to get the result.</p>';
        });
    </script>
</html>
```
