---
title: إصدار الموارد غير المدارة لمصنف العمل عبر جافا سكريبت بواسطة ++C
linktitle: تحرير الموارد غير المُدارة لدفتر العمل
type: docs
weight: 310
url: /ar/javascript-cpp/release-unmanaged-resources-of-the-workbook/
description: تعلم كيفية إصدار الموارد غير المدارة لكائن مصنف العمل باستخدام Aspose.Cells for JavaScript بواسطة ++C 
---

{{% alert color="primary" %}}

يقدم Aspose.Cells طريقة [**Workbook.dispose()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#dispose--) لتحرير الموارد غير المُدارة لكائن [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook). يُستخدم نمط التدمير فقط للكائنات التي تصل إلى موارد غير مُدارة، مثل مؤشرات الملفات والأنابيب وقيم السجل ومفاتيح الانتظار أو مؤشرات لكتل الذاكرة غير المُدارة. ويعود ذلك إلى كفاءة جامع القمامة في استرداد الكائنات المُدارة غير المستخدمة، ولكنه غير قادر على استرداد الأوائل غير المُدارة.

{{% /alert %}}

الكيان [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) الآن يطبق واجهة *System.IDisposable* التي تحتوي على طريقة واحدة [**Workbook.dispose()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#dispose--). يمكنك إما استدعاء طريقة [**Workbook.dispose()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#dispose--) مباشرة أو استخدام عبارة *Using* لاستدعاء هذه الطريقة تلقائيًا.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Dispose Example</h1>
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

            // Loads the workbook which contains hidden external links
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create workbook object
            const wb1 = new Workbook();

            // Call Dispose method
            wb1.dispose();

            // Call Dispose method via a scoped approach
            (async () => {
                const wb2 = new Workbook();
                // Any other code goes here
                wb2.dispose();
            })();

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully!</p>';
        });
    </script>
</html>
```
