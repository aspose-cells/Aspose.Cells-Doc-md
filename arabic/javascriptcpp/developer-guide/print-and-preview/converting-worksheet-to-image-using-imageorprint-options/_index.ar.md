---
title: تحويل ورقة العمل إلى صورة باستخدام خيارات الصورة أو الطباعة مع JavaScript عبر C++
linktitle: تحويل ورقة العمل إلى صورة باستخدام خيارات الصورة أو الطباعة
type: docs
weight: 90
url: /ar/javascript-cpp/converting-worksheet-to-image-using-imageorprint-options/
description: تعلم كيفية تحويل ورقة العمل إلى ملف صورة وتطبيق خيارات الصور والطباعة المختلفة باستخدام Aspose.Cells for JavaScript عبر C++.   
---

{{% alert color="primary" %}}  
هذا المستند مصمم لتوفير فهم مفصل حول كيفية تحويل ورقة العمل إلى ملف صورة وتطبيق خيارات مختلفة للصورة وخيارات الطباعة للصورة، مثل الدقة وضغط TIFF وتنسيق الصورة وجودة الصفحة وغيرها.  
{{% /alert %}}  

## **حفظ الأوراق العمل إلى صور - نهج مختلفة**  

في بعض الأحيان، قد تحتاج إلى عرض ورقات العمل الخاصة بك كتمثيل بصري. عليك حقاً تقديم صور ورقة العمل في تطبيقاتك أو صفحات الويب. قد تحتاج إلى إدراج الصور في وثيقة Word أو ملف PDF أو عرض PowerPoint، أو استخدامها في سيناريو آخر ما. ببساطة ترغب في عرض ورقة عمل مقدمة كصورة بحيث يمكنك استخدامها في مكان آخر. Aspose.Cells يدعم تحويل ورقات العمل في ملفات Excel إلى صور. أيضًا، يدعم Aspose.Cells ضبط خيارات مختلفة مثل تنسيق الصورة، الدقة (عمودي وأفقي على حد سواء)، جودة الصورة، وخيارات الصورة والطباعة الأخرى.  

قد تجرب أوتوماتيكية Office لكن لها عيوبها الخاصة. هناك العديد من الأسباب والمشكلات المعنية: على سبيل المثال، الأمان، الاستقرار، القابلية للتوسع والسرعة، السعر، والميزات. باختصار، هناك العديد من الأسباب، وأهمها أن شركة مايكروسوفت توصي بشدة بعدم استخدام أوتوماتيكية Office من حلول البرمجيات.  

يوضح هذا المقال كيفية إنشاء تطبيق وحدة تحكم في Visual Studio .NET، وأداء تحويل ورقة العمل إلى صورة باستخدام خيارات مختلفة للصورة والطباعة ببضع وأبسط أسطر من الشفرة باستخدام API Aspose.Cells.  

تمثل فئة [**SheetRender**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/) ورقة عمل لتحويل الصور، ولها طريقة [**toImage(number)**](https://reference.aspose.com/cells/javascript-cpp/sheetrender/#toImage-number-) محملة زائدة يمكنها تحويل ورقة عمل مباشرة إلى ملف صور مطابق لخصائصك أو خياراتك المرغوبة. يمكنها إرجاع كائن يمكنك من خلاله حفظ ملف صورة على القرص/تدفق. تدعم عدة تنسيقات صور، مثل BMP، PNG، GIF، JPEG، TIFF، EMF وغيرها.  

## **استخدام Aspose.Cells لتحويل ورقة العمل إلى صورة باستخدام خيارات الصورة أو الطباعة**  

### **إنشاء ملف عمل قالب في Microsoft Excel**  

لقد أنشأت ورق عمل جديد في MS Excel وأضافت بعض البيانات في الورقة العمل الأولى. الآن، سأقوم بتحويل ورقة العمل في ملف القالب "Sheet1" إلى ملف صورة "SheetImage.tiff" وسأطبق خيارات الصور المختلفة مثل الدقة الأفقية والعمودية وضغط Tiff وما إلى ذلك.  

### **تنزيل وتثبيت Aspose.Cells**  

 أولاً، تحتاج إلى [تحميل](https://downloads.aspose.com/cells/javascript-cpp) Aspose.Cells for JavaScript عبر C++. قم بتثبيته على جهاز تطويرك. جميع مكونات [Aspose](http://www.aspose.com/)، عند تثبيتها، تعمل في وضع التقييم. وضع التقييم لا يوجد به حد زمني، ويضيف فقط علامات مائية إلى المستندات المنتجة.  

### **إنشاء مشروع**  

ابدأ بيئة التطوير المفضلة لديك (مثل Visual Studio). أنشئ تطبيق وحدة تحكم جديد.  

### **إضافة الإشارات**  

 ستستخدم هذه المشروع Aspose.Cells. لذلك، عليك إضافة مرجع إلى مكون Aspose.Cells في مشروعك. على سبيل المثال، أضف مرجعاً إلى ….\Program Files\Aspose\Aspose.Cells for JavaScript عبر C++\Bin\Aspose.Cells.node  

### **تحويل ورقة العمل إلى ملف صورة**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Worksheet to Image Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, ImageOrPrintOptions, SheetRender, ImageType, TiffCompression, PrintingPageType, Utils } = AsposeCells;

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

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Apply different Image and Print options
            const options = new ImageOrPrintOptions();

            // Set Horizontal Resolution
            options.horizontalResolution = 300;

            // Set Vertical Resolution
            options.verticalResolution = 300;

            // Set TiffCompression
            options.tiffCompression = TiffCompression.CompressionLZW;

            // Set Image Format
            options.imageType = ImageType.Tiff;

            // Set printing page type
            options.printingPage = PrintingPageType.Default;

            // Render the sheet with respect to specified image/print options
            const sr = new SheetRender(sheet, options);

            // Render/save the image for the sheet (pageIndex is zero-based)
            const pageIndex = 3;
            const imageData = sr.toImage(pageIndex);

            const blob = new Blob([imageData], { type: 'image/tiff' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = `outputWorksheetToAnImage_${pageIndex + 1}.tiff`;
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download TIFF Image';

            resultDiv.innerHTML = '<p style="color: green;">Image rendered successfully! Click the download link to get the image.</p>';
        });
    </script>
</html>
```  

## **خيارات التحويل**  

من الممكن حفظ صفحات محددة إلى صورة. يحول الرمز التالي الصفحتين الأولى والثانية في دفتر عمل إلى صور JPG.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Specific Pages To Images</title>
    </head>
    <body>
        <h1>Specific Pages To Images Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, ImageOrPrintOptions, SheetRender, ImageType, Utils } = AsposeCells;

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

            // Instantiating a Workbook object by opening the Excel file through the file stream
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet.
            const sheet = workbook.worksheets.get(0);

            // Define ImageOrPrintOptions
            const imgOptions = new ImageOrPrintOptions();

            // Specify the image format
            imgOptions.imageType = ImageType.Jpeg;

            // Render the sheet with respect to specified image/print options
            const sr = new SheetRender(sheet, imgOptions);

            // Specify page index to be rendered
            const idxPage = 3;

            // Render the third image for the sheet
            const bitmap = sr.toImage(idxPage);

            // Save the image file as a downloadable blob
            const blob = new Blob([bitmap], { type: 'image/jpeg' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = `outputSpecificPagesToImage_${idxPage + 1}.jpg`;
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Image File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Image rendered successfully! Click the download link to get the image file.</p>';
        });
    </script>
</html>
```  

## **تحويل الصور باستخدام WorkbookRender**  

يمكن أن تحتوي صورة TIFF على أكثر من إطار واحد. يمكنك حفظ دفتر العمل بأكمله إلى صورة TIFF واحدة متعددة الإطارات أو الصفحات:  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Use WorkbookRender for Image Conversion Example</title>
    </head>
    <body>
        <h1>Use WorkbookRender for Image Conversion Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;"></a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, ImageOrPrintOptions, ImageType, WorkbookRender, Utils } = AsposeCells;

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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Prepare image/print options
            const opts = new ImageOrPrintOptions();
            opts.imageType = AsposeCells.ImageType.Tiff;

            // Create WorkbookRender and convert to image
            const workbookRender = new WorkbookRender(workbook, opts);

            // toImage may return a single Uint8Array or an array of Uint8Array pages
            const imageResult = await workbookRender.toImage();

            let imageData = imageResult;
            if (Array.isArray(imageResult) && imageResult.length > 0) {
                imageData = imageResult[0];
            }

            // Ensure imageData is a Uint8Array or ArrayBuffer
            let blob;
            if (imageData instanceof Uint8Array || imageData instanceof ArrayBuffer) {
                blob = new Blob([imageData], { type: 'image/tiff' });
            } else {
                // Fallback: try to stringify/convert if possible
                blob = new Blob([imageData], { type: 'application/octet-stream' });
            }

            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputUseWorkbookRenderForImageConversion.tiff';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Converted TIFF Image';

            document.getElementById('result').innerHTML = '<p style="color: green;">Image conversion completed! Click the download link to get the TIFF file.</p>';
        });
    </script>
</html>
```
