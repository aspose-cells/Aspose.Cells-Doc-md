---
title: إلغاء حماية ورقة عمل باستخدام جافا سكريبت عبر C++
linktitle: إلغاء حماية ورقة العمل
type: docs
weight: 20
url: /ar/javascript-cpp/unprotect-a-worksheet/
---

{{% alert color="primary" %}}

إذا كان هناك حاجة لإزالة الحماية من ورقة العمل المحمية في وقت التشغيل بحيث يمكن إجراء بعض التغييرات على الملف؟ يمكن القيام بذلك بسهولة مع Aspose.Cells.

{{% /alert %}}

## **إلغاء حماية ورقة العمل**

### **استخدام Microsoft Excel**

لإزالة الحماية من ورقة العمل:

من قائمة **الأدوات**، اختر **الحماية** ثم **إلغاء حماية الورقة**. ستتم إزالة الحماية ما لم تكن ورقة العمل محمية بكلمة مرور. في هذه الحالة، يُطلب إدخال كلمة المرور. أدخل كلمة المرور وسيتوقف الحماية عن العمل.

### **إزالة الحماية من ورقة العمل المحمية بشكل بسيط باستخدام Aspose.Cells**

يمكن إلغاء حماية ورقة العمل من خلال استدعاء طريقة [**unprotect()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#unprotect--) من فئة [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). ورقة العمل المحمية ببساطة هي تلك التي ليست محمية بكلمة مرور. يمكن إلغاء حماية هذه الأوراق من خلال استدعاء طريقة [**unprotect()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#unprotect--) بدون تمرير معلمة.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Unprotect Worksheet Example</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Unprotecting the worksheet without a password
            worksheet.unprotect();

            // Saving the Workbook in Excel97To2003 format
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData], { type: "application/vnd.ms-excel" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Unprotected Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet unprotected successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **إلغاء حماية ورقة العمل المحمية بكلمة المرور باستخدام Aspose.Cells**

ورقة العمل المحمية بكلمة مرور هي تلك المحمية باستخدام كلمة مرور. يمكن إلغاء حماية هذه الأوراق من خلال استدعاء نسخة محملة من الطريقة [**unprotect()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#unprotect--) التي تأخذ كلمة المرور كمعامل.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Unprotect Worksheet Example</h1>
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

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Unprotecting the worksheet with a password (empty password in original code)
            worksheet.unprotect("");

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet unprotected successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
