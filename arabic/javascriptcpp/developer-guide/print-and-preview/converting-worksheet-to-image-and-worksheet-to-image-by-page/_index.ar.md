---
title: تحويل ورقة العمل إلى صورة وتحويل صفحة من ورقة العمل إلى صورة باستخدام JavaScript عبر C++
linktitle: تحويل ورقة العمل إلى صورة وورقة العمل إلى صورة بواسطة الصفحة
type: docs
weight: 80
url: /ar/javascript-cpp/converting-worksheet-to-image-and-worksheet-to-image-by-page/
---

{{% alert color="primary" %}}
تم تصميم هذا المستند لتوفير فهم مفصل للمطورين حول كيفية تحويل ورقة العمل إلى ملف صورة وورقة عمل متعددة الصفحات إلى ملفات صور لكل صفحة.

في بعض الأحيان قد تحتاج إلى تقديم ورقات العمل على شكل صور، على سبيل المثال، لاستخدامها في التطبيقات أو صفحات الويب. قد تحتاج إلى إدراج الصور في مستند Word أو ملف PDF أو عرض PowerPoint، أو استخدامها في سيناريو آخر. ببساطة، ترغب في عرض ورقة العمل على شكل صورة. تدعم Aspose.Cells تحويل ورقات العمل في ملفات Microsoft Excel إلى صور. بالإضافة إلى ذلك، تدعم Aspose.Cells تحويل دفتر العمل إلى عدة ملفات صور، واحدة لكل صفحة.

قد تستخدم أتمتة Office لتحقيق هذا، ولكن أتمتة Office لها عيوبها الخاصة. هناك عدة أسباب وقضايا معقدة، على سبيل المثال الأمان والاستقرار والتوسعة / السرعة والسعر والميزات. بإختصار، هناك العديد من الأسباب، ولكن السبب الرئيسي هو أن شركة Microsoft نفسها توصي بشدة ضد أتمتة Office.
{{% /alert %}}

## ** باستخدام Aspose.Cells for JavaScript عبر C++ لتحويل ورقة العمل إلى ملف صورة**

توضح هذه المقالة كيفية إنشاء تطبيق وحدة تحكم، وتحويل ورقة عمل إلى صورة، وتحويل ورقة عمل إلى صورة واحدة لكل ورقة عمل باستخدام أقل عدد من الأسطر وأبسطها باستخدام API الخاص بـ Aspose.Cells.

تحتاج إلى استيراد العديد من الفئات القيمة المتعلقة بوظائف العرض في برنامجك أو مشروعك، مثل [**SheetRender**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/)، [**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/)، [**WorkbookRender**](https://reference.aspose.com/cells/javascript-cpp/workbookrender/)، وهكذا. تمثل فئة [**SheetRender**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/) ورقة عمل لعرض الصور لورقة العمل وتحتوي على طريقة [**toImage(number)**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/#toImage-number-) محملة زائدة يمكنها تحويل ورقة العمل إلى ملفات صورة مباشرة مع تحديد أي سمات أو خيارات. يمكنها إرجاع كائن صورة ويمكنك حفظ ملف صورة على القرص/تيار. تدعم عدة تنسيقات صور، على سبيل المثال، BMP، PNG، GIF، JPG، JPEG، TIFF، EMF، وغيرها.

يشرح هذا المقال كيفية:

- تحويل ورقة العمل إلى صورة
- تحويل كل صفحة في ورقة العمل إلى صورة

تظهر هذه المهمة كيفية استخدام Aspose.Cells لتحويل ورقة عمل من دفتر العمل القالب إلى ملف صورة.

### **إعداد المشروع**

1. أولاً، [قم بتنزيل Aspose.Cells for JavaScript عبر C++](https://downloads.aspose.com/cells/javascript-cpp).
1. قم بتثبيته على حاسوب التطوير الخاص بك. جميع مكونات [Aspose](http://www.aspose.com/)، عند تثبيتها، تعمل في وضع التقييم. وضع التقييم ليس له حد زمني ويضيف فقط العلامات المائية إلى المستندات التي يتم إنشاؤها. الآن ابدأ بيئة التطوير الخاصة بك وأنشئ تطبيق وحدة تحكم جديد. يستخدم هذا المثال تطبيق وحدة تحكم JavaScript، لكن يمكنك استخدام أي إعداد يتكامل مع JavaScript. أضف مرجعاً إلى Aspose.Cells في المشروع الذي أنشأته.

### **تحويل ورقة العمل إلى ملف صورة**

أنشأت دفتر عمل جديد في Microsoft Excel وأضفت بعض البيانات في ورقة العمل الأولى: **Testbook.xlsx** (ورقة عمل واحدة). ثم قم بتحويل ورقة العمل في الملف القالب Sheet1 إلى ملف صورة يُعرف باسم SheetImage.jpg.

التالي هو الكود الذي استخدمته العنصر لإنجاز المهمة. يحول Sheet1 في **Testbook.xlsx** إلى ملف صورة لشرح سهولة هذا التحويل.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Convert Worksheet to Image Example</title>
    </head>
    <body>
        <h1>Convert Worksheet to Image Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ImageOrPrintOptions, SheetRender, ImageType, Utils } = AsposeCells;

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

            // Get the first worksheet.
            const sheet = workbook.worksheets.get(0);

            // Define ImageOrPrintOptions
            const imgOptions = new ImageOrPrintOptions();
            imgOptions.onePagePerSheet = true;

            // Specify the image format
            imgOptions.imageType = ImageType.Jpeg;

            // Render the sheet with respect to specified image/print options
            const sr = new SheetRender(sheet, imgOptions);

            // Generate the image data for the first page (index 0)
            const outputData = sr.toImage(0);

            // Create a blob and provide a download link
            const blob = new Blob([outputData], { type: 'image/jpeg' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputConvertWorksheettoImageFile.jpg';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Image File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet converted to image successfully! Click the download link to get the image file.</p>';
        });
    </script>
</html>
```

## ** استخدام Aspose.Cells for JavaScript عبر C++ لتحويل ورقة العمل إلى ملف صورة حسب الصفحة**

يوضح هذا المثال كيفية استخدام Aspose.Cells لتحويل ورقة عمل من مصنف قوالب يحتوي على عدة صفحات إلى ملف صورة واحد لكل صفحة.

### **تحويل ورقة العمل إلى صورة حسب الصفحة**

لقد أنشأت ورق عمل جديد في Microsoft Excel وأضافت بعض البيانات في ورقة العمل الأولى: ملفTestbook2.xlsx (ورقة عمل واحدة).

الآن، قم بتحويل ورقة العمل Sheet1 في ملف القالب إلى ملفات صور (ملف واحد لكل صفحة). حيث أنني قمت بالفعل بإنشاء تطبيق الوحدة التحكم لأداء مهمة النسخ، سأتجاوز خطوات إنشاء تطبيق الوحدة التحكم تلك وأنتقل مباشرة إلى خطوات تحويل ورقة العمل.

وفيما يلي الكود الذي يستخدمه المكون لإنجاز المهمة. يقوم بتحويل الشريحة Sheet1 في Testbook2.xlsx إلى ملفات صورة حسب الصفحة.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Convert Worksheet to Images By Page</title>
    </head>
    <body>
        <h1>Convert Worksheet to Images By Page</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <div id="downloadLinks"></div>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, ImageOrPrintOptions, ImageType, SheetRender, Utils } = AsposeCells;

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
            const linksDiv = document.getElementById('downloadLinks');
            linksDiv.innerHTML = '';
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const sheet = workbook.worksheets.get(0);

            // Create image/print options and set properties
            const options = new ImageOrPrintOptions();
            options.horizontalResolution = 200;
            options.verticalResolution = 200;
            options.imageType = ImageType.Tiff;

            // Sheet to Image By Page conversion
            const sr = new SheetRender(sheet, options);

            const pageCount = sr.pageCount;
            const createdLinks = [];

            for (let j = 0; j < pageCount; j++) 
            {
                // toImage returns image data for the specified page
                const outputData = sr.toImage(j);
                const blob = new Blob([outputData], { type: 'image/tiff' });
                const url = URL.createObjectURL(blob);
                const link = document.createElement('a');
                const pageNumber = j + 1;
                const fileName = 'outputConvertWorksheetToImageByPage_' + pageNumber + '.tif';
                link.href = url;
                link.download = fileName;
                link.textContent = 'Download ' + fileName;
                link.style.display = 'block';
                linksDiv.appendChild(link);
                createdLinks.push(url);
            }

            resultDiv.innerHTML = '<p style="color: green;">Conversion completed! Click the links below to download the generated TIFF images.</p>';
        });
    </script>
</html>
```
