---
title: تغيير الخط على حروف اليونيكود المحددة فقط أثناء حفظها إلى PDF باستخدام JavaScript عبر C++
linktitle: تغيير الخط فقط في الأحرف اليونيكود المحددة أثناء الحفظ إلى PDF
type: docs
weight: 260
url: /ar/javascript-cpp/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/
description: تعلم كيفية تغيير خط حروف اليونيكود المحددة أثناء حفظها إلى PDF باستخدام Aspose.Cells for Java سكربت عبر C++. 
---

{{% alert color="primary" %}} 

بعض الأحرف اليونيكود غير قابلة للعرض بواسطة الخط المحدد من قبل المستخدم. أحد الأحرف اليونيكود هو **الشرطة الغير قابلة للانفصال** (U+2011) ورقمه اليونيكود هو 8209. هذا الحرف لا يمكن عرضه باستخدام الخط **تايمز نيو رومان**, ولكن يمكن عرضه بالخطوط الأخرى مثل **أريال يونيكود ام اس**.

 عندما يحدث مثل هذا الحرف داخل كلمة أو جملة وكانت الخط المستخدم مثل Times New Roman، فإن Aspose.Cells يغير خط كامل الكلمة أو الجملة إلى خط يمكنه عرض هذا الحرف، مثل Arial Unicode إلى MS.

 ومع ذلك، هذا سلوك غير مرغوب لبعض المستخدمين ويرغبون في تغيير خط الحرف المحدد فقط بدلاً من تغيير خط الكلمة أو الجملة بأكملها.

 لمعالجة هذه المشكلة، توفر Aspose.Cells خاصية `PdfSaveOptions.isFontSubstitutionCharGranularity` التي يجب تعيينها على true بحيث يتغير خط الأحرف غير القابلة للعرض فقط إلى خط قابل للعرض، بينما تبقى بقية الكلمة أو الجملة في الخط الأصلي.

{{% /alert %}} 

## **مثال**
الصورة المرفقة تقارن بين ملفي PDF الناتجين من الشفرة النموذجية التالية.

 يتم إنشاء أحد الملفين بدون ضبط خاصية `PdfSaveOptions.isFontSubstitutionCharGranularity` والآخر بعد تعيينها على true.

كما ترى في أول ملف PDF، تغير خط الجملة بأكملها من Times New Roman إلى Arial Unicode MS بسبب الهايبن غير القابل للكسر. بينما في الملف الثاني، تغير خط الهايبن غير القابل للكسر فقط.

|**ملف PDF الأول**|
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_1.png)|


|**ملف PDF الثاني**|
| :- |
|![todo:image_alt_text](change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf_2.png)|
### **الكود المثالي**


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
        <a id="downloadLink1" style="display: none; margin-right: 10px;">Download Result PDF 1</a>
        <a id="downloadLink2" style="display: none;">Download Result PDF 2</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions } = AsposeCells;

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
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '<p>Running example...</p>';

            // Create workbook object
            const workbook = new Workbook();

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access cells
            const cell1 = worksheet.cells.get("A1");
            const cell2 = worksheet.cells.get("B1");

            // Set the styles of both cells to Times New Roman
            let style = cell1.style;
            style.font.name = "Times New Roman";
            cell1.style = style;
            cell2.style = style;

            // Put the values inside the cell
            cell1.value = "Hello without Non-Breaking Hyphen";
            cell2.value = "Hello" + String.fromCharCode(8209) + " with Non-Breaking Hyphen";

            // Autofit the columns
            worksheet.autoFitColumns();

            // Save to Pdf without setting PdfSaveOptions.IsFontSubstitutionCharGranularity
            const outputData1 = workbook.save(SaveFormat.Pdf);
            const blob1 = new Blob([outputData1]);
            const downloadLink1 = document.getElementById('downloadLink1');
            downloadLink1.href = URL.createObjectURL(blob1);
            downloadLink1.download = 'SampleOutput_out.pdf';
            downloadLink1.style.display = 'inline-block';
            downloadLink1.textContent = 'Download SampleOutput_out.pdf';

            // Save to Pdf after setting PdfSaveOptions.IsFontSubstitutionCharGranularity to true
            const opts = new PdfSaveOptions();
            opts.isFontSubstitutionCharGranularity = true;
            const outputData2 = workbook.save(SaveFormat.Pdf, opts);
            const blob2 = new Blob([outputData2]);
            const downloadLink2 = document.getElementById('downloadLink2');
            downloadLink2.href = URL.createObjectURL(blob2);
            downloadLink2.download = 'SampleOutput2_out.pdf';
            downloadLink2.style.display = 'inline-block';
            downloadLink2.textContent = 'Download SampleOutput2_out.pdf';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Use the download links to get the generated PDFs.</p>';
        });
    </script>
</html>
```
