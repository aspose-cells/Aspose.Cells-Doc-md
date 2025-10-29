---
title: إدارة خصائص المستند مع جافا سكريبت عبر ++C
linktitle: خصائص المستند
type: docs
weight: 80
url: /ar/javascript-cpp/managing-document-properties/
description: تعلم كيفية إدارة خصائص المستند من خلال API الخاصة بـ Script عبر C++.
keywords: كيفية إدارة خصائص المستند في جافا سكريبت عبر C++، الحصول على أو تعيين خصائص المستند باستخدام جافا سكريبت عبر C++، إضافة أو حذف خصائص المستند via JavaScript عبر C++، إدراج أو إزالة خصائص المستند مع جافا سكريبت عبر C++، كيفية الوصول إلى خصائص المستند باستخدام API الخاصة بـ Script عبر C++.
---

## **مقدمة**

يوفر Microsoft Excel القدرة على إضافة خصائص إلى ملفات جداول البيانات. توفر هذه الخصائص المستندية معلومات مفيدة وتنقسم إلى فئتين كما هو موضح أدناه.

- الخصائص المعرفة مسبقًا (المدمجة): الخصائص المدمجة تحتوي على معلومات عامة حول المستند مثل عنوان المستند واسم المؤلف وإحصائيات المستند وما إلى ذلك.
- الخصائص المخصصة (المخصصة): الخصائص المخصصة المحددة من قبل المستخدم النهائي في شكل زوج اسم-قيمة.

{{% alert color="primary" %}}

أهم نقطة لمعرفتها حول الخصائص المدمجة والمخصصة هي أنه يمكن الوصول إلى الخصائص المدمجة وتعديلها، ولكن لا يمكن إنشاؤها أو إزالتها. ومع ذلك، يمكن إنشاء الخصائص المخصصة وإدارتها.

{{% /alert %}}

## **كيفية إدارة خصائص المستند باستخدام Microsoft Excel**

تمكنك Microsoft Excel من إدارة خصائص المستندات لملفات Excel بطريقة WYSIWYG. يرجى اتباع الخطوات أدناه لفتح مربع الحوار **الخصائص** في Excel 2016.

1. من القائمة **ملف**, حدد **معلومات**.

|**اختيار قائمة المعلومات**|
| :- |
|![todo:image_alt_text](managing-document-properties_1.png)|
1. انقر على عنوان **الخصائص** وحدد "الخصائص المتقدمة".

|**النقر على اختيار الخصائص المتقدمة**|
| :- |
|![todo:image_alt_text](managing-document-properties_2.png)|
1. إدارة خصائص مستند الملف.

|**مربع الحوار الخصائص**|
| :- |
|![todo:image_alt_text](managing-document-properties_3.png)|
في مربع حوار الخصائص، هناك علامات تبويب مختلفة، مثل العامة، والملخص، والإحصائيات، والمحتويات، والمخصصة. تساعد كل علامة تبويب في تكوين أنواع مختلفة من المعلومات ذات الصلة بالملف. تُستخدم علامة التبويب المخصصة لإدارة الخصائص المخصصة.

## **كيفية العمل مع خصائص المستند باستخدام Aspose.Cells**

يمكن للمطورين إدارة خصائص الوثيقة بشكل ديناميكي باستخدام واجهات برمجة التطبيقات Aspose.Cells. تساعد هذه الميزة المطورين في تخزين معلومات مفيدة إلى جانب الملف، مثل متى تم استلام الملف ومعالجته وتسجيل الوقت وما إلى ذلك.

{{% alert color="primary" %}}

يكتب Script عبر C++ مباشرة معلومات حول API ورقم الإصدار في مستندات الإخراج. على سبيل المثال، عند تصيير المستند إلى PDF، يملا Script عبر C++ حقل **Application** بالقيمة 'Aspose.Cells' وحقل **منتج PDF** بالقيمة، مثل 'Aspose.Cells v17.9'.

يرجى ملاحظة أنه لا يمكنك تعليم Script عبر C++ لتغيير أو إزالة هذه المعلومات من مستندات الإخراج.

{{% /alert %}}

### **كيفية الوصول إلى خصائص المستند**

تدعم واجهات برمجة تطبيقات Aspose.Cells كلا نوعي خصائص المستند، المدمجة والخصائص المخصصة. Class [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) من Aspose.Cells يمثل ملف إكسل، ومثل ملف إكسل، يمكن لـ [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) أن يحتوي على عدة ورقات عمل، كل منها يُمثل بواسطة [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)، في حين تُمثل مجموعة ورقات العمل بواسطة [**WorksheetCollection**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection).

استخدم [**WorksheetCollection**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection) للوصول إلى خصائص المستند للملف كما هو موضح أدناه.

- للوصول إلى خصائص المستند المدمجة، استخدم [**WorksheetCollection.builtInDocumentProperties()**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#builtInDocumentProperties--).
- للوصول إلى خصائص المستند المخصصة ، استخدم [**WorksheetCollection.customDocumentProperties()**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#customDocumentProperties--).

كل من [**WorksheetCollection.builtInDocumentProperties()**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#builtInDocumentProperties--) و [**WorksheetCollection.customDocumentProperties()**](https://reference.aspose.com/cells/javascript-cpp/worksheetcollection/#customDocumentProperties--) تُرجع مثيل [**Aspose.Cells.Properties.DocumentPropertyCollection**](https://reference.aspose.com/cells/javascript-cpp/documentpropertycollection/)، الذي يحتوي على [**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/) من الكائنات، كل منها يمثل خاصية مستند مدمجة أو مخصصة.

يعتمد الأمر على متطلبات التطبيق على كيفية الوصول إلى الخاصية، سواء باستخدام الفهرس أو الاسم من [**DocumentPropertyCollection**](https://reference.aspose.com/cells/javascript-cpp/documentpropertycollection/) كما هو موضح في المثال أدناه.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Document Properties</title>
    </head>
    <body>
        <h1>Document Properties Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Load Document Properties</button>
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
            const resultEl = document.getElementById('result');
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                resultEl.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object and opening the Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Retrieve a list of all custom document properties of the Excel file
            const customProperties = workbook.customDocumentProperties;

            // Accessing a custom document property by using the property name
            const customProperty1 = customProperties.get("ContentTypeId");
            // Accessing the same custom document property by using the property index
            const customProperty2 = customProperties.get(0);

            const outputs = [];
            if (customProperty1) {
                outputs.push(`<p>${customProperty1.name} ${customProperty1.value}</p>`);
            }
            if (customProperty2) {
                outputs.push(`<p>${customProperty2.name} ${customProperty2.value}</p>`);
            }
            if (!outputs.length) {
                resultEl.innerHTML = '<p style="color: orange;">No custom document properties found.</p>';
            } else {
                resultEl.innerHTML = outputs.join('');
            }
        });
    </script>
</html>
```

يسمح لك [**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/) باسترجاع اسم، قيمة، ونوع الخاصية المستند:

- للحصول على اسم الخاصية ، استخدم [**DocumentProperty.name()**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/#name--).
- للحصول على قيمة الخاصية، استخدم [**DocumentProperty.value()**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/#value--). [**DocumentProperty.value()**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/#value--) يُرجع القيمة ككائن.
- للحصول على نوع الخاصية، استخدم [**DocumentProperty.type()**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/#type--). يُرجع أحد قيم التعداد [**PropertyType**](https://reference.aspose.com/cells/javascript-cpp/propertytype/). بعد الحصول على نوع الخاصية، استخدم واحدة من طرق **DocumentProperty.ToXXX** للحصول على قيمة النوع المناسب بدلاً من استخدام [**DocumentProperty.value()**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/#value--). يتم وصف طرق **DocumentProperty.ToXXX** في الجدول أدناه.

{{% alert color="primary" %}}

يوفر [**DocumentProperty**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/) أيضًا مجموعة من الطرق التي ترجع قيم الأنواع الأخرى من البيانات.

{{% /alert %}}

|**اسم العضو**|**الوصف**|**طريقة ToXXX**|
| :- | :- | :- |
|Boolean| نوع البيانات الخاصية هو بوليان|ToBool|
|Date| نوع البيانات الخاصية هو التاريخ والوقت. لاحظ أن Microsoft Excel يخزن فقط <br> الجزء التاريخي ، لا يمكن تخزين الوقت في خاصية مخصصة من هذا النوع|ToDateTime|
|Float| نوع البيانات الخاصية هو Double|ToDouble|
|Number| نوع البيانات الخاصية هو Int32|ToInt|
|String| نوع بيانات الخاصية هو string|ToString|

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Retrieve Custom Document Properties Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Retrieve a list of all custom document properties of the Excel file
            const customProperties = workbook.customDocumentProperties;

            let outputHtml = '<h2>Custom Document Properties</h2>';

            // Accessing a custom document property (first)
            const customProperty1 = customProperties.get(0);
            if (customProperty1) {
                // Storing the value of the document property as an object
                const objectValue = customProperty1.value;
                outputHtml += `<p><strong>${customProperty1.name}</strong> (type: ${customProperty1.type}) : ${objectValue}</p>`;
            } else {
                outputHtml += '<p>No first custom property found.</p>';
            }

            // Accessing a custom document property (second)
            const customProperty2 = customProperties.get(1);
            if (customProperty2) {
                // Checking the type of the document property and then storing the value according to that type
                if (customProperty2.type === AsposeCells.PropertyType.String) {
                    const value = customProperty2.value.toString();
                    outputHtml += `<p>${customProperty2.name} : ${value}</p>`;
                } else {
                    outputHtml += `<p>${customProperty2.name} (type: ${customProperty2.type}) : ${customProperty2.value}</p>`;
                }
            } else {
                outputHtml += '<p>No second custom property found.</p>';
            }

            resultDiv.innerHTML = outputHtml;
        });
    </script>
</html>
```

### **كيفية إضافة أو إزالة خصائص المستند المخصصة**

كما وصفنا في وقت سابق في بداية هذا الموضوع ، لا يمكن للمطورين إضافة أو إزالة الخصائص المدمجة لأن هذه الخصائص محددة من النظام ولكن من الممكن إضافة أو إزالة الخصائص المخصصة لأنها معرفة من قبل المستخدم.

### **كيفية إضافة الخصائص المخصصة**

واجهت واجهات برمجة تطبيقات Aspose.Cells الطريقة [**add(string, string)**](https://reference.aspose.com/cells/javascript-cpp/customdocumentpropertycollection/#add-string-string-) للفئة [**CustomDocumentPropertyCollection**](https://reference.aspose.com/cells/javascript-cpp/customdocumentpropertycollection/) لإضافة خصائص مخصصة للمجموعة. تضيف طريقة [**add(string, string)**](https://reference.aspose.com/cells/javascript-cpp/customdocumentpropertycollection/#add-string-string-) الخاصية إلى ملف إكسل وتُعيد مرجعًا لخاصية المستند الجديدة ككائن [**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Add Custom Document Property</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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

            document.getElementById('runExample').addEventListener('click', async () => {
                const fileInput = document.getElementById('fileInput');
                if (!fileInput.files.length) {
                    document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                    return;
                }

                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();

                // Instantiating a Workbook object and opening the Excel file
                const workbook = new Workbook(new Uint8Array(arrayBuffer));

                // Retrieve a list of all custom document properties of the Excel file
                const customProperties = workbook.customDocumentProperties;

                // Adding a custom document property to the Excel file
                customProperties.add("Publisher", "Aspose");

                // Saving the modified Excel file
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = 'out_sample-document-properties.xlsx';
                downloadLink.style.display = 'block';
                downloadLink.textContent = 'Download Modified Excel File';

                document.getElementById('result').innerHTML = '<p style="color: green;">Custom property added successfully! Click the download link to get the modified file.</p>';
            });
        });
    </script>
</html>
```

### **كيفية تكوين خاصية مخصصة مرتبطة بالمحتوى**

لإنشاء خاصية مخصصة مرتبطة بمحتوى نطاق معين، استدعِ طريقة [**CustomDocumentPropertyCollection.addLinkToContent(string, string)**](https://reference.aspose.com/cells/javascript-cpp/customdocumentpropertycollection/#addLinkToContent-string-string-) ومرر اسم الخاصية والمصدر. يمكنك التحقق مما إذا كانت الخاصية مهيأة على أنها مرتبطة بالمحتوى باستخدام الخاصية [**DocumentProperty.isLinkedToContent()**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/#isLinkedToContent--). علاوة على ذلك، من الممكن أيضًا الحصول على نطاق المصدر باستخدام الخاصية [**source()**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/#source--) من فئة [**DocumentProperty**](https://reference.aspose.com/cells/javascript-cpp/documentproperty/).

نحن نستخدم ملف نموذجي بسيط لبرنامج Microsoft Excel في المثال. يحتوي دفتر العمل على نطاق مسمى محدد يحمل التسمية **MyRange** والذي يشير إلى قيمة الخلية.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Custom Document Properties</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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
            const resultEl = document.getElementById('result');
            if (!fileInput.files.length) {
                resultEl.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a Workbook by loading the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Retrieve a list of all custom document properties of the Excel file
            const customProperties = workbook.worksheets.customDocumentProperties;

            // Add link to content.
            customProperties.addLinkToContent("Owner", "MyRange");

            // Accessing the custom document property by using the property name
            const customProperty1 = customProperties.get("Owner");

            // Check whether the property is linked to content
            const isLinkedToContent = customProperty1.isLinkedToContent;

            // Get the source for the property
            const source = customProperty1.source;

            // Save the file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out_sample-document-properties.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultEl.innerHTML = `<p style="color: green;">Operation completed successfully! Property linked: ${isLinkedToContent}. Source: ${source}. Click the download link to get the modified file.</p>`;
        });
    </script>
</html>
```

### **كيفية إزالة الخصائص المخصصة**

لإزالة الخصائص المخصصة باستخدام Aspose.Cells، استدعي طريقة [**DocumentPropertyCollection.remove(string)**](https://reference.aspose.com/cells/javascript-cpp/documentpropertycollection/#remove-string-) ومرر اسم الخاصية الخاصة بالمستند المراد إزالته.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Remove Custom Document Property Example</title>
    </head>
    <body>
        <h1>Remove Custom Document Property Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Retrieve a list of all custom document properties of the Excel file
            const customProperties = workbook.customDocumentProperties;

            // Removing a custom document property named "Publisher"
            customProperties.remove("Publisher");

            // Save the file and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out_sample-document-properties.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Custom property removed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **مواضيع متقدمة**
- [إضافة خصائص مخصصة مرئية داخل لوحة معلومات الوثيقة](/cells/ar/javascript-cpp/adding-custom-properties-visible-inside-document-information-panel/)
- [ضبط خصائص ScaleCrop و LinksUpToDate لخصائص المستند المضمنة](/cells/ar/javascript-cpp/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/)
- [تحديد إصدار المستند لملف الإكسل باستخدام خصائص المستند المضمنة](/cells/ar/javascript-cpp/specify-document-version-of-the-excel-file-using-builtin-document-properties/)
- [تحديد لغة ملف إكسل باستخدام الخصائص المدمجة للمستند](/cells/ar/javascript-cpp/specify-the-language-of-the-excel-file-using-builtin-document-properties/)
