---
title: كشف الأوراق الفارغة باستخدام جافا سكريبت عبر C++
linktitle: كشف الأوراق العمل الفارغة
type: docs
weight: 410
url: /ar/javascript-cpp/detecting-empty-worksheets/
description: يُظهر هذا المقال رمزًا يوضح كيفية اكتشاف الأوراق الفارغة في دفاتر إكسل باستخدام واجهة برمجة التطبيقات جافا سكريبت مع مكتبة C++.
keywords: اكتشاف الورقة الفارغة باستخدام جافا سكريبت عبر C++، العثور على ورقة إكسل فارغة باستخدام جافا سكريبت عبر C++
---

## **فحص الخلايا المعبأة**

يمكن أن تحتوي أوراق العمل على خلية واحدة أو أكثر مملوءة بقيم، حيث يمكن أن تكون القيمة بسيطة (نص، رقم، تاريخ/وقت) أو صيغة أو قيمة تستند إلى صيغة. في مثل هذه الحالة، من السهل الكشف عما إذا كانت ورقة العمل فارغة أم لا. كل ما علينا التحقق منه هو الخاصيتان [**Cells.maxDataRow**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxDataRow--) أو [**Cells.maxDataColumn**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxDataColumn--). إذا أعادت الخاصيتان المذكورتان أصلاً قيمًا صفرية أو إيجابية، فهذا يعني أن خلية واحدة أو أكثر قد تم ملؤها؛ ومع ذلك، إذا أعادت أي من هاتين الخاصيتين -1، فهذا يدل على عدم وجود خلايا مملوءة في ورقة العمل المعطاة.

{{% alert color="primary" %}}

تحتوي مجموعتا الصفوف والأعمدة على مؤشرات تبدأ بالصفر؛ لذلك، تعني الخلية عند الصف 0 والعمود 0 أول خلية في ورقة العمل، وهي A1.

{{% /alert %}}

## **فحص الخلايا المهيأة الفارغة**

يتم تهيئة جميع الخلايا التي تحتوي على قيم تلقائيًا؛ ومع ذلك، هناك احتمال أن تحتوي ورقة العمل على خلايا تحتوي فقط على تنسيق مطبق. في مثل هذا السيناريو، ستعيد الخاصيتان [**Cells.maxDataRow**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxDataRow--) أو [**Cells.maxDataColumn**](https://reference.aspose.com/cells/javascript-cpp/cells/#maxDataColumn--) -1، مما يشير إلى غياب القيم المعبأة، لكن الخلايا المهيأة بسبب تنسيق الخلية لا يمكن اكتشافها باستخدام هذا النهج. للتحقق مما إذا كانت لدى ورقة العمل خلايا مهيأة فارغة، يُنصح باستخدام طريقة `Enumerator.MoveNext` على المُعدّاد الذي تم الحصول عليه من مجموعة [**Cells**](https://reference.aspose.com/cells/javascript-cpp/cells). إذا أعادت `Enumerator.MoveNext` **true**، فهذا يعني أن هناك خلية مهيأة واحدة أو أكثر في ورقة العمل المعطاة.

## **فحص الأشكال**

من الممكن ألا تحتوي ورقة العمل المعطاة على خلايا مملوءة؛ ومع ذلك، قد تحتوي على أشكال وكائنات مثل الضوابط والمخططات والصور، وما إلى ذلك. إذا كنا بحاجة للتحقق مما إذا كانت تحتوي على أي شكل، يمكننا ذلك عن طريق فحص الخاصية [**ShapeCollection.count**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#count--). تشير أي قيمة إيجابية إلى وجود شكل (أشكال) في ورقة العمل.

## **نموذج برمجة**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Check Non-Empty Worksheets Example</h1>
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
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const book = new Workbook(new Uint8Array(arrayBuffer));

            const messages = [];

            // Loop over all worksheets in the workbook
            for (let i = 0; i < book.worksheets.count; i++) {
                const sheet = book.worksheets.get(i);
                // Check if worksheet has populated cells
                if (sheet.cells.maxDataRow !== -1) {
                    messages.push(`${sheet.name} is not empty because one or more cells are populated`);
                }
                // Check if worksheet has shapes
                else if (sheet.shapes.count > 0) {
                    messages.push(`${sheet.name} is not empty because there are one or more shapes`);
                }
                // Check if worksheet has empty initialized cells
                else {
                    const range = sheet.cells.maxDisplayRange;
                    const rangeIterator = range.getEnumerator();
                    if (rangeIterator.moveNext()) {
                        messages.push(`${sheet.name} is not empty because one or more cells are initialized`);
                    }
                }
            }

            if (messages.length) {
                resultDiv.innerHTML = '<ul>' + messages.map(m => `<li>${m}</li>`).join('') + '</ul>';
            } else {
                resultDiv.innerHTML = '<p style="color: green;">No non-empty worksheets found.</p>';
            }
        });
    </script>
</html>
```
