---
title: تحسين استخدام الذاكرة أثناء العمل مع ملفات كبيرة تحتوي على مجموعات بيانات ضخمة باستخدام JavaScript عبر C++
linktitle: تحسين استخدام الذاكرة أثناء العمل مع ملفات كبيرة تحتوي على مجموعات بيانات كبيرة
type: docs
weight: 180
url: /ar/javascript-cpp/optimizing-memory-usage-while-working-with-big-files-having-large-datasets/
---

{{% alert color="primary" %}}

عند بناء دفتر عمل يحتوي على مجموعات بيانات كبيرة، أو قراءة ملف Excel كبير، فإن إجمالي كمية RAM التي ستستهلكها العملية هي دائمًا مصدر قلق. هناك تدابير يمكن تكييفها لمواجهة التحدي. يوفر Aspose.Cells for JavaScript عبر C++ بعض الخيارات ذات الصلة ونداءات API لخفض وتقليل وتحسين استخدام الذاكرة. بالإضافة إلى ذلك، يمكن أن تساعد العملية على العمل بكفاءة أكبر وتشغيلها بشكل أسرع.

استخدام الخيار [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/) لتحسين استخدام الذاكرة لبيانات الخلايا وتقليل التكلفة الإجمالية للذاكرة. عند بناء مجموعة بيانات كبيرة للخلايا، يمكن أن يوفر مبلغًا معينًا من الذاكرة بالمقارنة بالاستخدام الافتراضي ([**MemorySetting.Normal**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/)).

{{% /alert %}}

## **تحسين الذاكرة**

### **قراءة ملفات Excel الكبيرة**

توضح المثال التالي كيفية قراءة ملف إكسل كبير بوضع محسن.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - LoadOptions MemorySetting</title>
    </head>
    <body>
        <h1>LoadOptions MemorySetting Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, LoadOptions, MemorySetting, SaveFormat, Utils } = AsposeCells;

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

            // Specify the LoadOptions
            const opt = new LoadOptions();
            // Set the memory preferences (converted from setMemorySetting)
            opt.memorySetting = MemorySetting.MemoryPreference;

            // Instantiate the Workbook - load the big Excel file with options
            const workbook = new Workbook(new Uint8Array(arrayBuffer), opt);

            // Save the workbook to XLSX and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook loaded with MemoryPreference. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

### **كتابة ملفات إكسيل الكبيرة**

المثال التالي يوضح كيفية كتابة مجموعة بيانات كبيرة إلى ورقة عمل بوضع محسن.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Memory Setting Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Memory Setting Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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
                // If no file is selected, create a new workbook (similar to new AsposeCells.Workbook() in Node)
                // and proceed to set memory settings and populate sheets.
            }

            // Load workbook from file if provided, otherwise create empty workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Set the memory preferences on the workbook settings
            workbook.settings.memorySetting = AsposeCells.MemorySetting.MemoryPreference;

            // Note: The memory settings also would not work for the default sheet i.e., "Sheet1" etc. automatically created by the Workbook
            // To change the memory setting of existing sheets, change memory setting for them manually:
            let cells = workbook.worksheets.get(0).cells;
            cells.memorySetting = AsposeCells.MemorySetting.MemoryPreference;

            // Input large dataset into the cells of the worksheet.
            // Your code goes here.
            // Example: populate a few cells to demonstrate
            const firstCell = cells.get(0, 0);
            firstCell.value = "Sample Data 1";
            cells.get(1, 0).value = "Sample Data 2";

            // Get cells of the newly created Worksheet "Sheet2" whose memory setting is same with the one defined in WorkbookSettings:
            const sheet2 = workbook.worksheets.add("Sheet2");
            const cells2 = sheet2.cells;
            // .........
            // Input large dataset into the cells of the worksheet.
            // Your code goes here.
            // Example: populate a few cells in Sheet2
            cells2.get(0, 0).value = "Sheet2 Data 1";
            cells2.get(1, 0).value = "Sheet2 Data 2";

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Result';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **احترس**

الخيار الافتراضي، [**MemorySetting.Normal**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/)، يُطبق على جميع الإصدارات. في بعض الحالات، مثل بناء ملف عمل يحتوي على مجموعة بيانات كبيرة للخلايا، قد يُحسن خيار [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/) استهلاك الذاكرة ويقلل من تكلفتها على التطبيق. ومع ذلك، قد يؤدي هذا الخيار إلى تدهور الأداء في بعض الحالات الخاصة كما يلي.

1. **الوصول العشوائي والمتكرر للخلايا**: أكثر ترتيب كفاءة للوصول إلى مجموعة الخلايا هو خلية تلو الأخرى في صف واحد، ثم صف بصف. خاصة، إذا قمت بالوصول إلى الصفوف/الخلايا بواسطة Enumerator المستمد من [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells)، [**RowCollection**](https://reference.aspose.com/cells/javascript-cpp/rowcollection)، و[**Row**](https://reference.aspose.com/cells/javascript-cpp/row)، فسيتم تعظيم الأداء مع [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/).
2. **إدراج وحذف الخلايا والصفوف**: يرجى ملاحظة أنه إذا كانت هناك الكثير من العمليات لإدراج/حذف الخلايا/الصفوف، فإن تدهور الأداء سيكون ملحوظًا لوضع *MemoryPreference* مقارنة بوضع *Normal*.
3. **العمل على أنواع مختلفة من الخلايا**: إذا كانت معظم الخلايا تحتوي على قيم نصية أو صيغ، فإن تكلفة الذاكرة ستكون نفس وضع *Normal*، ولكن إذا كانت هناك الكثير من الخلايا الفارغة، أو القيم الرقمية، أو القيم البوليانية، وما إلى ذلك، فسيعطي الخيار [**MemorySetting.MemoryPreference**](https://reference.aspose.com/cells/javascript-cpp/memorysetting/) أداءً أفضل.
