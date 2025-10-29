---
title: تنفيذ النطاقات غير المتسلسلة باستخدام JavaScript عبر C++
linktitle: تنفيذ النطاقات غير المتتالية
type: docs
weight: 700
url: /ar/javascript-cpp/implementing-non-sequential-ranges/
description: تعلم كيفية إنشاء نطاقات غير متسلسلة مسماة باستخدام Aspose.Cells for JavaScript عبر C++. استخدام النطاقات بين الخلايا غير المجاورة بشكل فعال.
---

{{% alert color="primary" %}} 

عادةً، تكون النطاقات المسماة مستطيلة مع خلايا متصلة ومتجاورة. لكن أحيانًا، قد تحتاج إلى استخدام نطاق خلايا غير متسلسلة حيث لا تتصل الخلايا ببعضها البعض. يدعم Aspose.Cells for JavaScript عبر C++ إنشاء نطاق مسمى بخلايا غير متصلة.

{{% /alert %}} 

يُظهر نموذج الكود أدناه كيفية إنشاء نطاق غير متسلسل مسمى باستخدام Aspose.Cells for JavaScript عبر C++.


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Add NonSequenced Range Name</h1>
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
            // Creating a new Workbook object
            const workbook = new Workbook();

            // Adding a Name for non sequenced range
            const index = workbook.worksheets.names.add("NonSequencedRange");

            const name = workbook.worksheets.names.get(index);

            // Creating a non sequence range of cells
            name.refersTo = "=Sheet1!$A$1:$B$3,Sheet1!$D$5:$E$6";

            // Saving the workbook and providing a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Output.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and name added successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
