---
title: تعيين نوع التشفير القوي باستخدام جافا سكريبت عبر C++
linktitle: ضبط نوع التشفير القوي
type: docs
weight: 60
url: /ar/javascript-cpp/setting-strong-encryption-type/
description: تعلم كيفية تعيين أنواع التشفير القوية لملفات إكسل باستخدام Aspose.Cells for JavaScript عبر C++.
---

{{% alert color="primary" %}} 

يتيح Microsoft Excel (97-2007/2010) لك تشفير وحماية كلمة المرور لجداول البيانات. إنه يستخدم خوارزميات مقدمة من موفر خدمة التشفير. موفر خدمة التشفير (أو CSP) هو مجموعة من الخوارزميات التشفيرية ذات خصائص مختلفة. يعد موفر خدمة التشفير الافتراضي "متوافق مع Office 97/2000". هذا هو موفر خدمة تشفير مع بعض المشاكل الأمنية المعروفة علناً. يمكن كسر جداول البيانات التي تم تأمينها بـ "تشفير ضعيف (XOR)" أو بنوع التشفير "متوافق مع Office 97/2000" بسهولة.

لتجاوز هذه المشكلة، استخدم أحد أنواع التشفير القوية المقدمة من Microsoft Excel. يمكنك تغيير نوع التشفير إلى أقوى موفر خدمة تشفير متاح. للتشفير القوي، يتطلب طول مفتاح أدنى من 128 بت، على سبيل المثال، 'موفر خدمة التشفير القوي لشركة Microsoft'.

يمكنك أيضًا تشفير ملفات إكسل بنوع تشفير قوي وحمايتها بكلمة مرور باستخدام واجهة برمجة التطبيقات Aspose.Cells.

{{% /alert %}}  
## **تطبيق التشفير مع مايكروسوفت إكسل**  
لتنفيذ تشفير الملف في مايكروسوفت إكسل (مثلاً 2007):

١. من قائمة **الأدوات**, حدد **خيارات**.  
١. حدد علامة التبويب **الأمان**.  
١. أدخل قيمة لحقل **كلمة المرور للفتح**.  
1. انقر على **متقدم**.  
١. اختر نوع التشفير وقم بتأكيد كلمة المرور.  

## **تطبيق التشفير مع Aspose.Cells**  
تطبيق الشفرة أدناه يطبق تشفيرًا قويًا على ملف ويعين كلمة مرور.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Encrypt Workbook</title>
    </head>
    <body>
        <h1>Encrypt Workbook Example</h1>
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
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            workbook.encryptionOptions = [AsposeCells.EncryptionType.StrongCryptographicProvider, 128];
            workbook.settings.password = "1234";

            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'encryptedBook1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Encrypted Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">File encrypted successfully! Click the download link to get the encrypted file.</p>';
        });
    </script>
</html>
```
