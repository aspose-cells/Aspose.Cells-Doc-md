---
title: البحث واستبدال البيانات في نطاق باستخدام جافا سكريبت عبر C++
linktitle: البحث واستبدال البيانات في نطاق
type: docs
weight: 170
url: /ar/javascript-cpp/search-and-replace-data-in-a-range/
description: توضح هذه المقالة كيف تبحث وتستبدل البيانات في نطاق في إكسل باستخدام جافا سكريبت عبر كود C++.
keywords: بحث واستبدال البيانات في إكسل باستخدام جافا سكريبت، البحث عن البيانات في إكسل، البحث واستبدال البيانات في نطاق، البحث عن البيانات في نطاق، البحث عن البيانات في النطاق، البحث عن البيانات في إكسل، البحث عن البيانات في النطاق، البحث عن البيانات في إكسل، البحث عن البيانات واستبدالها باستخدام جافا سكريبت، البحث واستبدال البيانات في نطاق باستخدام جافا سكريبت، البحث عن واستبدال البيانات في النطاق باستخدام جافا سكريبت
---

{{% alert color="primary" %}}

أحيانًا تحتاج إلى البحث عن استبدال بيانات معينة في نطاق مع تجاهل أي قيم خلايا خارج النطاق المطلوب. يتيح لك سكربت Aspose.Cells for Java عبر C++ تحديد عملية البحث لنطاق معين. تشرح هذه المقالة كيف.

{{% /alert %}}

يوفر سكربت Aspose.Cells for Java عبر C++ أسلوب [**FindOptions.range(CellArea)**](https://reference.aspose.com/cells/javascript-cpp/findoptions/#range-cellarea-) لتحديد النطاق عند البحث عن البيانات. يختبر نموذج الكود أدناه البيانات ويستبدلها في النطاق.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Find and Replace Example</title>
    </head>
    <body>
        <h1>Find and Replace Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellArea, FindOptions, LookInType, LookAtType } = AsposeCells;

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

            // Instantiating a Workbook object by loading the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const worksheet = workbook.worksheets.get(0);

            // Define the search range (E9:H15)
            const area = CellArea.createCellArea("E9", "H15");

            // Configure find options
            const opts = new FindOptions();
            opts.lookInType = LookInType.Values;
            opts.lookAtType = LookAtType.EntireContent;
            opts.range = area;

            let cell = null;

            do {
                cell = worksheet.cells.find("search", cell, opts);
                if (cell === null || cell.isNull()) {
                    break;
                }
                // Replace found cell's value
                cell.value = "replace";
            } while (true);

            // Saving the modified Excel file and providing a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Find and replace completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
