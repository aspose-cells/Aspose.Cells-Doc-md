---
title: التحقق من كلمة المرور للتعديل باستخدام Aspose.Cells for JavaScript عبر C++
linktitle: التحقق من كلمة المرور للتعديل
type: docs
weight: 2400
url: /ar/javascript-cpp/check-password-to-modify-using-aspose-cells/
description: تعلم كيفية التحقق إذا كانت كلمة مرور التعديل تطابق باستخدام Aspose.Cells for JavaScript عبر C++.
---

{{% alert color="primary" %}}  
أحيانًا، تحتاج إلى التحقق من أن كلمة المرور المعطاة تتطابق مع **كلمة المرور للتعديل** برمجياً. يوفر Aspose.Cells طريقة `WorkbookSettings.writeProtection.validatePassword()` التي يمكنك استخدامها للتحقق مما إذا كانت كلمة المرور للتعديل صحيحة أم لا.  
{{% /alert %}}  

## **التحقق من كلمة المرور للتعديل في Microsoft Excel**  

يمكنك تعيين **كلمة السر للفتح** و**كلمة السر للتعديل** أثناء إنشاء جداول البيانات الخاصة بك في Microsoft Excel. يُرجى الرجوع إلى هذا اللقط الشاشة الذي يظهر واجهة Microsoft Excel المُقدمة لتحديد هذه الكلمات السرية.  

|![todo:image_alt_text](check-password-to-modify-using-aspose-cells_1.png)|  
| :- |  

## **تحقق من كلمة المرور للتعديل باستخدام Aspose.Cells for JavaScript عبر C++**  

يحمّل الأمثلة التالية ملف Excel المصدر (5112232.xlsx). يحتوي على كلمة مرور عند الفتح وهي 1234 وكلمة مرور للتعديل وهي 5678. يبحث الكود أولاً عن صحة كلمة المرور 567 ويعيد false، ثم يبحث عن كلمة المرور 5678 ويعيد true.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Check Write Protection Passwords</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, LoadOptions, SaveFormat, Utils } = AsposeCells;

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

            // Specify password to open inside the load options
            const opts = new LoadOptions();
            opts.password = "1234";

            // Open the source Excel file with load options
            const workbook = new Workbook(new Uint8Array(arrayBuffer), opts);

            // Check if 567 is Password to modify
            let ret = workbook.settings.writeProtection.validatePassword("567");
            let outputHtml = `<p>Is 567 correct Password to modify: ${ret}</p>`;

            // Check if 5678 is Password to modify
            ret = workbook.settings.writeProtection.validatePassword("5678");
            outputHtml += `<p>Is 5678 correct Password to modify: ${ret}</p>`;

            document.getElementById('result').innerHTML = outputHtml;
        });
    </script>
</html>
```  

### **مخرجات الوحدة**  



{{< highlight java >}}  
Is 567 correct Password to modify: False  
Is 5678 correct Password to modify: True  
{{< /highlight >}}
