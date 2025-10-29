---
title: حماية مستندات PDF باستخدام جافا سكريبت عبر C++
linktitle: مستندات PDF الآمنة
type: docs
weight: 120
url: /ar/javascript-cpp/secure-pdf-documents/
description: تعلم كيفية حماية مستندات PDF عن طريق استخدام كلمات سر للمالك والمستخدم، وتعيين الأذونات لملفات PDF باستخدام Aspose.Cells for JavaScript عبر C++.
---

{{% alert color="primary" %}}

في بعض الأحيان، يحتاج المطورون إلى العمل مع ملفات PDF المُشفرة. على سبيل المثال:

- تأمين المستندات بكلمات مرور للمالك والمستخدم حتى لا يمكن لأي شخص فتحه.
- تعيين قيود أو أذونات للمستند بعد فتحه، على سبيل المثال: تقييد ما إذا كان بإمكان محتوى المستند أن يُطبع أو يستخرج.

يشرح هذا المقال كيفية تمرير خيارات أمان PDF عند حفظ الجداول الإلكترونية إلى PDF.

{{% /alert %}}

توفر Aspose.Cells [**PdfSecurityOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsecurityoptions/) للعمل مع الأمان. يمكنك تعيين كلمات مرور المالك والمستخدم أثناء الحفظ إلى PDF. ستكون كلمة مرور المالك أو كلمة مرور المستخدم مطلوبة لفتح مستند PDF المشفر للمشاهدة.

- يمكن أن تكون كلمة مرور المستخدم فارغة أو سلسلة فارغة؛ في هذه الحالة، لن يُطلب من المستخدم إدخال كلمة مرور عند فتح مستند PDF.
- يتيح فتح مستند PDF بكلمة مرور المالك الصحيحة الوصول الكامل (بدون أي قيود وصول محددة) إلى المستند.
- فتح مستند PDF بكلمة مرور المستخدم الصحيحة (أو فتح مستند لا يحتوي على كلمة مرور للمستخدم) يسمح بوصول محدود حيث تم تحديد الأذونات.

يصف الكود النموذجي أدناه كيفية تأمين ملفات PDF باستخدام Aspose.Cells.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Secure PDF Example</title>
    </head>
    <body>
        <h1>Secure PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions, PdfSecurityOptions, Utils } = AsposeCells;

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

            // Create PDF save options and security options
            const saveOption = new PdfSaveOptions();
            saveOption.securityOptions = new PdfSecurityOptions();

            // Set security options (converted from getters/setters to properties)
            saveOption.securityOptions.userPassword = "user";
            saveOption.securityOptions.ownerPassword = "owner";
            saveOption.securityOptions.extractContentPermission = false;
            saveOption.securityOptions.printPermission = false;

            // Save the workbook to PDF with security options
            const outputData = workbook.save(SaveFormat.Pdf, saveOption);
            const blob = new Blob([outputData], { type: "application/pdf" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'securepdf_test.out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Secure PDF';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the secured PDF file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

إذا كانت جداول البيانات تحتوي على صيغ، فمن الأفضل استدعاء [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--) قبل عرضها إلى PDF. يضمن هذا إعادة حساب القيم المعتمدة على الصيغ وعرض القيم الصحيحة في PDF.

{{% /alert %}}
