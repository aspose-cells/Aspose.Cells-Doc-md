---
title: البحث عما إذا كانت الورقة ورقة حوار باستخدام جافا سكريبت عبر C++
linktitle: البحث عما إذا كانت ورقة العمل هي ورقة حوار
type: docs
weight: 90
url: /ar/javascript-cpp/find-if-the-worksheet-is-dialog-sheet/
description: توفر هذه المقالة إرشادات ورمزًا نمطيًا لتحديد برمجيًا فيما إذا كانت ورقة إكسل حوار باستخدام Aspose.Cells for JavaScript عبر C++.
keywords: العثور على نوع حوار ورقة إكسل باستخدام جافا سكريبت عبر C++، جافة ورقة حوار باستخدام C++
---

## **سيناريوهات الاستخدام المحتملة**

ورقة الحوار هي تنسيق قديم من الورقة تحتوي على مربع حوار. يمكن إدراج مثل هذه الورقة بواسطة إصدار أقدم من مايكروسوفت إكسل، مثل 2003، كما هو موضح في لقطة الشاشة هذه. يمكن أيضًا إدراجها باستخدام VBA في الإصدارات الأحدث، مثل مايكروسوفت إكسل 2016.

![todo:image_alt_text](find-if-the-worksheet-is-dialog-sheet_1.png)

يمكنك معرفة ما إذا كانت الورقة حوار أو نوع آخر من الورق باستخدام الخاصية [**Worksheet.type**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#type--) التي توفرها الشفرة Aspose.Cells for JavaScript عبر C++. إذا أعادت قيمة التعداد [**SheetType.Dialog**](https://reference.aspose.com/cells/javascript-cpp/sheettype)، فهذا يعني أنك تتعامل مع ورقة حوار.

## **العثور على ورقة العمل هل هي ورقة حوار**

الرمز النموذجي التالي يحمل [ملف إكسل العيني](64716820.xlsx) الذي يحتوي على ورقة حوار. يفحص الخاصية [**Worksheet.type**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#type--)، يقارنها مع [**SheetType.Dialog**](https://reference.aspose.com/cells/javascript-cpp/sheettype)، ثم يطبع الرسالة. يرجى الاطلاع على مخرجات وحدة التحكم للرمز النموذجي أدناه للمساعدة.

## **الكود المثالي**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Detect Dialog Sheet</title>
    </head>
    <body>
        <h1>Detect if Worksheet Is a Dialog Sheet</h1>
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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const ws = workbook.worksheets.get(0);

            // Find if the sheet type is dialog and print the message
            if (ws.type === AsposeCells.SheetType.Dialog) {
                document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet is a Dialog Sheet.</p>';
            } else {
                document.getElementById('result').innerHTML = '<p>Worksheet is NOT a Dialog Sheet.</p>';
            }
        });
    </script>
</html>
```

## **مخرجات الوحدة**

{{< highlight js >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
