---
title: عرض وإخفاء أوراق العمل والعلامات باستخدام جافا سكريبت عبر ++C
linktitle: إظهار وإخفاء الأوراق والألسنة
type: docs
weight: 10
url: /ar/javascript-cpp/show-and-hide-worksheets-and-tabs/
description: يوفر هذا المقال رمزًا يوضح استخدام واجهة برمجة التطبيقات جافا سكريبت أو مكتبة جافا سكريبت لعرض وإخفاء ورقة عمل إكسل برمجياً. بالإضافة إلى ذلك، كيفية عرض وإخفاء علامات المصنف إكسل.
---

{{% alert color="primary" %}}
تسمح Aspose.Cells للمستخدم بإظهار وإخفاء عناصر دفتر العمل بما في ذلك الأوراق والألسنة.
{{% /alert %}}

## **إظهار وإخفاء ورقة عمل**

يمكن أن يحتوي ملف إكسل على ورقة عمل واحدة أو أكثر. كلما أنشأنا ملف إكسل، نضيف أوراق عمل إلى الملف إكسل الذي نعمل فيه. تكون كل ورقة عمل في ملف إكسل مستقلة عن الورقة العمل الأخرى بوجود بياناتها الخاصة وإعدادات التنسيق وما إلى ذلك. في بعض الأحيان، قد يحتاج المطورون إلى إخفاء بعض الأوراق العمل وجعل البعض الآخر مرئية في ملف إكسل لمصلحتهم الخاصة. لذا، **Aspose.Cells** يتيح للمطورين التحكم في رؤية أوراق العمل في ملفاتهم إكسل.

توفر Aspose.Cells فئة، [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)، التي تمثل ملف إكسل. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) على مجموعة [**workbook.worksheets**](https://reference.aspose.com/cells/javascript-cpp/workbook/#worksheets--) تمكن من الوصول إلى كل ورقة عمل في الملف.

تمثل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). تقدم فئة [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) مجموعة واسعة من الخصائص والطرق لإدارة أوراق العمل. للتحكم في رؤية ورقة العمل، استخدم خاصية [**Worksheet.isVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isVisible--) من فئة [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet). [**Worksheet.isVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isVisible--) هي خاصية منطقية، مما يعني أنها يمكن أن تخزن فقط قيمة **صحيح** أو **خطأ**.

### **جعل ورقة العمل مرئية**

اجعل ورقة عمل مرئية عن طريق تعيين خاصية [**Worksheet.isVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isVisible--) لفئة [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) إلى **صحيح**.

### **إخفاء ورقة عمل**

أخفِ ورقة عمل عن طريق تعيين خاصية [**Worksheet.isVisible()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#isVisible--) لفئة [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) إلى **خطأ**.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Hide Worksheet Example</title>
    </head>
    <body>
        <h1>Hide Worksheet Example</h1>
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

            // Instantiating a Workbook object by opening the Excel file from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Hiding the first worksheet of the Excel file
            worksheet.isVisible = false;

            // Saving the modified Excel file in Excel 97-2003 format
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet hidden successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **إظهار وإخفاء الألسنة**

إذا نظرت عن كثب في أسفل ملف Microsoft Excel، سترى عددًا من الضوابط. تشمل هذه:

- ألسنة الصفحات.
- أزرار تمرير الألسنة.

تمثل ألسنة الصفحات الأوراق العمل في ملف الإكسل. انقر على أي علامة تبويب للانتقال إلى تلك الورقة العمل. كلما زاد عدد الأوراق العمل في الدفتر الحسابي، زادت ألسنة الصفحة. إذا كان لديك عدد جيد من الأوراق العمل في دفتر العمل، يلزمك الأزرار للتنقل خلالها. لذا، يوفر مايكروسوفت إكسل أزرار تمرير الألسنة للتمرير من خلال ألسنة الصفحات.

باستخدام Aspose.Cells، يمكن للمطورين التحكم في رؤية علامات الجدول وأزرار التمرير في ملفات Excel.

توفر Aspose.Cells فئة، [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook)، التي تمثل ملف إكسل. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) على مجموعة واسعة من الخصائص والطرق لإدارة ملف إكسل. للتحكم في رؤية علامات التبويب في ملف إكسل، يمكن للمطورين استخدام خاصية [**WorkbookSettings.showTabs**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#showTabs--) من فئة [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook). [**WorkbookSettings.showTabs**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#showTabs--) هي خاصية منطقية، مما يعني أنها يمكن أن تخزن فقط قيمة **صحيح** أو **خطأ**.

### **جعل علامات التبويب مرئية**

اجعل علامات التبويب مرئية باستخدام خاصية [**WorkbookSettings.showTabs**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#showTabs--) من فئة [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) لتكون **صحيح**.

### **إخفاء علامات التبويب**

اخفِ علامات التبويب في ملف إكسل عن طريق تعيين خاصية [**WorkbookSettings.showTabs**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#showTabs--) من فئة [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) إلى **خطأ**.

فيما يلي مثال كامل يفتح ملف Excel (book1.xls)، يخفي علاماته ويحفظ الملف المعدل بصيغة output.xls. بعد تنفيذ الكود، سترى أن تبويبات الدفتر مخفية.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Hide Worksheet Tabs Example</h1>
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

            // Instantiating a Workbook object by opening the Excel file from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Hiding the tabs of the Excel file
            workbook.settings.showTabs = false;

            // To show the tabs instead, you could set:
            // workbook.settings.showTabs = true;

            // Saving the modified Excel file (Excel 97-2003 format for .xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Tabs hidden successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **السيطرة على عرض شريط التبويب**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Hide Tabs</title>
    </head>
    <body>
        <h1>Hide Tabs Example</h1>
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

            // Hiding the tabs of the Excel file (converted setter to property)
            workbook.settings.showTabs = true;

            // Adjusting the sheet tab bar width (converted setter to property)
            workbook.settings.sheetTabBarWidth = 800;

            // Saving the modified Excel file (SaveFormat.Xls -> SaveFormat.Excel97To2003)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
