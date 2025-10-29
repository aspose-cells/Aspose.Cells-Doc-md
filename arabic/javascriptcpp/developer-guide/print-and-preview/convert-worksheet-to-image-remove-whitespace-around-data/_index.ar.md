---
title: تحويل ورقة العمل إلى صورة  إزالة المساحات الفارغة حول البيانات باستخدام JavaScript عبر C++
linktitle: تحويل ورقة عمل إلى صورة  إزالة الفراغات حول البيانات
type: docs
weight: 40
url: /ar/javascript-cpp/convert-worksheet-to-image-remove-whitespace-around-data/
description: تعرف على كيفية تحويل أوراق عمل Microsoft Excel إلى صور وإزالة الفراغات البيضاء حول البيانات باستخدام Aspose.Cells for JavaScript عبر C++. 
---

{{% alert color="primary" %}}

أحيانًا، قد تحتاج إلى عرض صور ورق العمل في التطبيقات أو صفحات الويب. على سبيل المثال، قد تحتاج إلى إدراج صور في مستند Word، ملف PDF، عرض PowerPoint، أو مستند آخر. بشكل أساسي، ترغب في عرض ورقة العمل كصورة بحيث يمكن لصقها في تطبيقات أخرى. تُسمح لك Aspose.Cells بتحويل جداول بيانات Microsoft Excel إلى صور.

{{% /alert %}}

## **إزالة الفراغات حول البيانات**

[**SheetRender**](https://reference.aspose.com/cells/javascript-cpp/sheetrender) API يحول ورقة عمل إلى ملف صورة مع أي سمات محددة، على سبيل المثال، تنسيق الصورة، الصفحات المقسمة، وما إلى ذلك. تدعم عدة صيغ للصور، بما في ذلك BMP، GIF، JPG، TIFF، و EMF.

عند استخدام ميزة الورقة إلى الصورة، يكون للصورة الناتجة فراغ حولها تلقائياً. يمكنك إزالة ذلك عن طريق تعيين الهوامش العلوية، السفلية، اليسرى واليمنى لتوجيه صفحة ورقة المصدر إلى 0 وتحديد [**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions) بشكل مناسب.

الكود التالي يزيل الفراغات حول البيانات في الصورة الناتجة.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Convert Sheet to EMF</title>
    </head>
    <body>
        <h1>Convert Worksheet to EMF Image</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to EMF</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, LoadOptions, LoadFilter, LoadDataFilterOptions, ImageOrPrintOptions, ImageType, PrintingPageType, SheetRender, Utils } = AsposeCells;

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

            // Prepare load options and filters
            const loadOptions = new LoadOptions();
            loadOptions.loadFilter = new LoadFilter(LoadDataFilterOptions.All);

            // Instantiate workbook with load options
            const workbook = new Workbook(new Uint8Array(arrayBuffer), loadOptions);

            // Get the first worksheet
            const sheet = workbook.worksheets.get(0);

            // To remove the white border around the image.
            sheet.pageSetup.leftMargin = 0;
            sheet.pageSetup.rightMargin = 0;
            sheet.pageSetup.bottomMargin = 0;
            sheet.pageSetup.topMargin = 0;

            // Define ImageOrPrintOptions
            const imgOptions = new ImageOrPrintOptions();
            imgOptions.imageType = ImageType.Emf;

            // Set only one page would be rendered for the image
            imgOptions.onePagePerSheet = true;
            imgOptions.printingPage = PrintingPageType.IgnoreBlank;

            // Create the SheetRender object based on the sheet with its ImageOrPrintOptions attributes
            const sr = new SheetRender(sheet, imgOptions);

            // Convert the image (returns image data in browser environment)
            const imageData = sr.toImage(0);

            // Create a blob and provide download link
            const blob = new Blob([imageData], { type: 'image/emf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputRemoveWhitespaceAroundData.emf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download EMF Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Image conversion completed successfully! Click the download link to get the EMF file.</p>';
        });
    </script>
</html>
```
