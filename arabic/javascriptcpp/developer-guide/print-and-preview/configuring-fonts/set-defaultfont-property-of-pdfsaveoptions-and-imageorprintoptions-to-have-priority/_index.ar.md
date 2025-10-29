---
title: تعيين خاصية DefaultFont من خيارات PdfSaveOptions و ImageOrPrintOptions لتكون لها الأولوية باستخدام جافا سكريبت عبر C++
linktitle: تعيين خاصية DefaultFont في خيارات PdfSave و ImageOrPrint لديها الأولوية
type: docs
weight: 30
url: /ar/javascript-cpp/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/
description: اكتشف كيفية تعيين خاصية DefaultFont من خيارات PdfSaveOptions و ImageOrPrintOptions باستخدام Aspose.Cells for JavaScript عبر C++. التأكد من عرض الخط بشكل صحيح عند عدم وجود الخطوط.
---

## **سيناريوهات الاستخدام المحتملة**

أثناء ضبط خاصية **DefaultFont** لـ [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions) و [**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/)، قد تتوقع أن يقوم الحفظ إلى ملف PDF أو صورة بضبط ذلك DefaultFont لجميع النص في مصفوفة العمل الذي يحتوي على خط مفقود (غير مثبت).

عموماً، عند الحفظ بصيغة PDF أو صورة، ستقوم Aspose.Cells for JavaScript عبر C++ بمحاولة تعيين الخط الافتراضي للكتاب (أي `Workbook.DefaultStyle.Font`). إذا لم يظهر نص بشكل صحيح، فسيحاول Aspose.Cells التصيير باستخدام الخط المذكور مقابل خاصية DefaultFont في [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions). 

للتعامل مع توقعاتك، لدينا خاصية بولية تسمى "**CheckWorkbookDefaultFont**" في [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/). يمكنك ضبطها على **false** لتعطيل محاولة الخط الافتراضي للمصفوفة العمل أو ترك الإعداد **DefaultFont** في [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/) ليكون له الأولوية.

## **تعيين خاصية DefaultFont في خيارات PdfSave/ImageOrPrintOptions**

يفتح رمز النموذج التالي ملف Excel. الخلية A1 في ورقة العمل الأولى تحتوي على نص مضبط ليكون "نص خط وقت عيد الميلاد". اسم الخط هو "Christmas Time Personal Use" غير مثبت على الجهاز. نقوم بضبط خاصية **DefaultFont** لـ [**PdfSaveOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/) إلى "Times New Roman". ونضبط الخاصية **CheckWorkbookDefaultFont** إلى **"false"** لضمان عرض نص الخلية A1 باستخدام خط "Times New Roman" وعدم استخدام الخط الافتراضي للملف ("Calibri" في هذه الحالة). يقوم الكود بعرض ورقة العمل الأولى بصيغة PNG و TIFF، وأخيرًا بصيغة ملف PDF.

{{% alert color="primary" %}}

القيمة الافتراضية لخاصية **CheckWorkbookDefaultFont** هي **true**.

{{% /alert %}}

هذه هي صورة الشاشة من [ملف القالب](49446913.xlsx) المستخدم في كود المثال.

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_1.png)

هذه هي صورة PNG الناتجة بعد ضبط الخاصية [**ImageOrPrintOptions.defaultFont**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#defaultFont--) على "Times New Roman".

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_2.png)

انظر الصورة [TIFF](48496672.tiff) الناتجة بعد ضبط الخاصية [**ImageOrPrintOptions.defaultFont**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/#defaultFont--) على "Times New Roman".

انظر ملف [PDF](48496673.pdf) الناتج بعد ضبط الخاصية [**PdfSaveOptions.defaultFont**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#defaultFont--) على "Times New Roman".

## **الكود المثالي**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Set Default Font for Export (PNG, TIFF, PDF)</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <div>
            <a id="downloadPng" style="display: none;">Download PNG</a><br/>
            <a id="downloadTiff" style="display: none;">Download TIFF</a><br/>
            <a id="downloadPdf" style="display: none;">Download PDF</a>
        </div>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ImageOrPrintOptions, ImageType, SheetRender, WorkbookRender, PdfSaveOptions } = AsposeCells;

        const readyPromise = AsposeCells.onReady({
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
            const resultEl = document.getElementById('result');
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                resultEl.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            await readyPromise;

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Rendering to PNG while setting checkWorkbookDefaultFont = false and defaultFont to Times New Roman
            const imgOpt = new ImageOrPrintOptions();
            imgOpt.imageType = ImageType.Png;
            imgOpt.checkWorkbookDefaultFont = false;
            imgOpt.defaultFont = "Times New Roman";

            const sr = new SheetRender(workbook.worksheets.get(0), imgOpt);
            const pngData = sr.toImage(0);
            const pngBlob = new Blob([pngData], { type: 'image/png' });
            const downloadPng = document.getElementById('downloadPng');
            downloadPng.href = URL.createObjectURL(pngBlob);
            downloadPng.download = 'out1_imagePNG.png';
            downloadPng.style.display = 'inline-block';
            downloadPng.textContent = 'Download PNG';

            // Rendering to TIFF while setting checkWorkbookDefaultFont = false and defaultFont to Times New Roman
            imgOpt.imageType = ImageType.Tiff;
            const wr = new WorkbookRender(workbook, imgOpt);
            const tiffData = wr.toImage();
            const tiffBlob = new Blob([tiffData], { type: 'image/tiff' });
            const downloadTiff = document.getElementById('downloadTiff');
            downloadTiff.href = URL.createObjectURL(tiffBlob);
            downloadTiff.download = 'out1_imageTIFF.tiff';
            downloadTiff.style.display = 'inline-block';
            downloadTiff.textContent = 'Download TIFF';

            // Rendering to PDF while setting the default font and checkWorkbookDefaultFont
            const saveOptions = new PdfSaveOptions();
            saveOptions.defaultFont = "Times New Roman";
            saveOptions.checkWorkbookDefaultFont = false;
            const pdfData = workbook.save(SaveFormat.Pdf, saveOptions);
            const pdfBlob = new Blob([pdfData], { type: 'application/pdf' });
            const downloadPdf = document.getElementById('downloadPdf');
            downloadPdf.href = URL.createObjectURL(pdfBlob);
            downloadPdf.download = 'out1_pdf.pdf';
            downloadPdf.style.display = 'inline-block';
            downloadPdf.textContent = 'Download PDF';

            resultEl.innerHTML = '<p style="color: green;">Export completed. Click the links above to download the generated files.</p>';
        });
    </script>
</html>
```
