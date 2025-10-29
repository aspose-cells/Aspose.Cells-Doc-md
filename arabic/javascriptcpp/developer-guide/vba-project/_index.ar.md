---
title: إدارة أكواد VBA لمصنف إكسل مشغل، مع ماكرو
linktitle: مشروع الماكرو
type: docs
weight: 200
url: /ar/javascript-cpp/manage-vba-project/
description: إضافة وحدة VBA وتعديل VBA أو الماكرو باستخدام Aspose.Cells for JavaScript عبر C++.
---

## **إضافة وحدة VBA في جافا سكريبت عبر C++**
{{% alert color="primary" %}}

تسمح Aspose.Cells بإضافة وحدة VBA جديدة وكود الماكرو باستخدام Aspose.Cells for JavaScript عبر C++. يرجى استخدام طريقة [**Workbook.add(Worksheet)**](https://reference.aspose.com/cells/javascript-cpp/vbamodulecollection/#add-worksheet-) لإضافة وحدة VBA الجديدة داخل دفتر العمل

{{% /alert %}}

إن الكود النموذجي التالي ينشئ مصنفًا جديدًا ويضيف وحدة VBA جديدة وكود ماكرو ويحفظ الناتج بصيغة XLSM. بمجرد فتح ملف XLSM الناتج في Microsoft Excel والنقر على أوامر قائمة **المطور > Visual Basic**، سترى وحدة باسم "TestModule" وداخلها سترى كود الماكرو التالي.

{{< highlight javascript >}}
Sub ShowMessage() {
    MsgBox "Welcome to Aspose!"
}
{{< /highlight >}}



```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add VBA Module</title>
    </head>
    <body>
        <h1>Add VBA Module Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsm,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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
            // Create new workbook
            const workbook = new Workbook();

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Add VBA Module
            const idx = workbook.vbaProject.modules.add(worksheet);

            // Access the VBA Module, set its name and codes
            const module = workbook.vbaProject.modules.get(idx);
            module.name = "TestModule";
            module.codes = "Sub ShowMessage()\r\n" +
                           "    MsgBox \"Welcome to Aspose!\"\r\n" +
                           "End Sub";

            // Save the workbook as XLSM and prepare download
            const outputData = workbook.save(SaveFormat.Xlsm);
            const blob = new Blob([outputData], { type: "application/vnd.ms-excel.sheet.macroEnabled.12" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsm';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">VBA module added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **تعديل VBA أو الماكرو في جافا سكريبت عبر C++**

{{% alert color="primary" %}} 

يمكنك تعديل كود VBA أو الماكرو باستخدام Aspose.Cells for JavaScript عبر C++. أضافت Aspose.Cells الوحدة والفئات التالية لقراءة وتعديل مشروع VBA في ملف إكسل.

- Aspose.Cells.Vba
- VbaProject
- VbaModuleCollection
- VbaModule

سيعرض هذا المقال لك كيفية تغيير رمز VBA أو الماكرو داخل ملف Excel المصدر باستخدام Aspose.Cells.

{{% /alert %}} 

يحمّل الكود النموذجي التالي ملف Excel المصدر الذي يحتوي على كود VBA أو الماكرو التالي بداخله

{{< highlight javascript >}}
Sub Button1_Click() {
    MsgBox "This is test message."
}
{{< /highlight >}}

بعد تنفيذ رمز عينات Aspose.Cells، سيتم تعديل رمز VBA أو الماكرو مثل هذا

{{< highlight javascript >}}
Sub Button1_Click() {
    MsgBox "This is Aspose.Cells message."
}
{{< /highlight >}}

يمكنك تنزيل [ملف Excel المصدر](5112508.xlsm) و[ملف Excel الناتج](5112511.xlsm) من الروابط المعطاة.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Change VBA Module Code Example</title>
    </head>
    <body>
        <h1>Change VBA Module Code Example</h1>
        <input type="file" id="fileInput" accept=".xlsm,.xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file (.xlsm).</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access VBA project modules
            const modules = workbook.vbaProject.modules;
            const moduleCount = modules.count;
            for (let i = 0; i < moduleCount; i++) {
                const module = modules.get(i);
                let code = module.codes;
                if (code && code.includes("This is test message.")) {
                    code = code.replace("This is test message.", "This is Aspose.Cells message.");
                    module.codes = code;
                }
            }

            const outputData = workbook.save(SaveFormat.Xlsm);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsm';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">VBA module code updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **مواضيع متقدمة**
- [إضافة مرجع مكتبة إلى مشروع VBA في مصنف العمل](/cells/ar/javascript-cpp/add-a-library-reference-to-vba-project-in-workbook/)
- [تعيين الماكرو إلى عنصر تحكم النموذج](/cells/ar/javascript-cpp/assign-macro-to-form-control/)
- [التحقق مما إذا كان التوقيع الرقمي لرمز VBA صالحًا](/cells/ar/javascript-cpp/check-if-digital-signature-of-vba-code-is-valid/)
- [فحص ما إذا كان رمز VBA موقعًا](/cells/ar/javascript-cpp/check-if-vba-code-is-signed/)
- [التحقق مما إذا كان مشروع VBA في مصنف عمل موقعًا](/cells/ar/javascript-cpp/check-if-vba-project-in-a-workbook-is-signed/)
- [فحص ما إذا كان مشروع VBA محميًا ومقفلاً للعرض](/cells/ar/javascript-cpp/check-if-vba-project-is-protected-and-locked-for-viewing/)
- [نسخ تصميم الاستوديو Form UserForm VBA Macro من القالب إلى دفتر العمل الهدف](/cells/ar/javascript-cpp/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/)
- [توقيع رقمي لمشروع رمز VBA باستخدام شهادة](/cells/ar/javascript-cpp/digitally-sign-a-vba-code-project-with-certificate/)
- [تصدير شهادة VBA إلى ملف أو تيار](/cells/ar/javascript-cpp/export-vba-certificate-to-file-or-stream/)
- [تصفية مشروع VBA أثناء تحميل مصنف عمل](/cells/ar/javascript-cpp/filter-vba-project-while-loading-a-workbook/)
- [معرفة ما إذا كان مشروع VBA محميًا](/cells/ar/javascript-cpp/find-out-if-vba-project-is-protected/)
- [حماية كلمة المرور لمشروع VBA لمصنف عمل Excel](/cells/ar/javascript-cpp/password-protect-the-vba-project-of-excel-workbook/)
