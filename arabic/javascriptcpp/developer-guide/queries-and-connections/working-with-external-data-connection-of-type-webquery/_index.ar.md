---
title: العمل مع اتصال بيانات خارجي من نوع WebQuery باستخدام جافا سكريبت عبر C++
linktitle: العمل مع اتصال البيانات الخارجية من نوع الاستعلام عبر الويب
type: docs
weight: 30
url: /ar/javascript-cpp/working-with-external-data-connection-of-type-webquery/
description: تعلم كيفية العمل مع اتصالات البيانات الخارجية من نوع WebQuery باستخدام Aspose.Cells for JavaScript عبر C++. 
---

{{% alert color="primary" %}}

يمكنك الوصول إلى اتصال البيانات الخارجية من أي نوع باستخدام مجموعة Workbook.DataConnections. نوع واحد من هذا النوع من اتصال البيانات هو استعلام الويب. سيوضح هذا المقال كيفية العمل مع اتصال بيانات استعلام الويب. يمكنك إنشاء اتصال بيانات استعلام الويب في برنامج Microsoft Excel باستخدام القائمة **البيانات** > **من الويب**.

{{% /alert %}}

## العمل مع اتصال البيانات الخارجية من نوع WebQuery

الكود التالي يوضح كيفية العمل مع اتصال البيانات الخارجية من نوع **WebQuery**. يستخدم [ملف الإكسل عينة](5112365.xlsx) الذي يمكنك تنزيله من الرابط المقدم. يمكنك أيضًا رؤية مخرجات الوحدة (console output) لهذا الكود فيما بعد.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Web Query Connection Reader</h1>
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

            // Loading the workbook from the selected file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access data connections
            const connections = workbook.dataConnections;
            if (connections.count > 0) {
                const connection = connections.get(0);

                if (connection instanceof AsposeCells.WebQueryConnection) {
                    const webQuery = connection;
                    console.log("Web Query URL: " + webQuery.url);
                    resultDiv.innerHTML = '<p>Web Query URL: ' + webQuery.url + '</p>';
                } else {
                    resultDiv.innerHTML = '<p>No WebQueryConnection found in the first connection.</p>';
                }
            } else {
                resultDiv.innerHTML = '<p>No data connections found.</p>';
            }
        });
    </script>
</html>
```

## مخرج الكونسول



{{< highlight javascript >}}

Web Query URL: https://docs.aspose.com/cells/javascript-cpp/

{{< /highlight >}}
