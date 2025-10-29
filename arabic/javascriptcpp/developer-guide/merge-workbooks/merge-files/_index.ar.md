---
title: دمج الملفات باستخدام جافا سكريبت عبر C++
linktitle: دمج الملفات
type: docs
weight: 20
url: /ar/javascript-cpp/merge-files/
---

## **مقدمة**

يوفر Aspose.Cells طرقًا مختلفة لدمج الملفات. للملفات البسيطة التي تحتوي على بيانات، تنسيقات، وصيغ، يمكن استخدام طريقة [**Workbook.combine(Workbook)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#combine-workbook-) لدمج عدة دفاتر عمل، ويمكن استخدام طريقة [**Worksheet.copy(Worksheet)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#copy-worksheet-) لنسخ أوراق العمل إلى دفتر عمل جديد. هذه الطرق سهلة الاستخدام وفعالة، ولكن إذا كان لديك الكثير من الملفات للدمج، قد تجد أنها تستهلك الكثير من موارد النظام. لتجنب ذلك، استخدم الطريقة الثابتة [**CellsHelper.mergeFiles(string[], string, string)**](https://reference.aspose.com/cells/javascript-cpp/cellshelper/#mergeFiles-stringarray-string-string-)، وهو أسلوب أكثر كفاءة لدمج عدة ملفات.

## **دمج الملفات باستخدام سكربت Aspose.Cells for Java عبر C++**

يوضح رمز المثال التالي كيفية دمج ملفات كبيرة باستخدام أسلوب [**CellsHelper.mergeFiles(string[], string, string)**](https://reference.aspose.com/cells/javascript-cpp/cellshelper/#mergeFiles-stringarray-string-string-). يأخذ ملفين بسيطين لكن كبيرين، Book1.xls وBook2.xls. تحتوي الملفات على بيانات وصيغ منسقة فقط.

{{% alert color="primary" %}}

تدعم الطريقة [**CellsHelper.mergeFiles(string[], string, string)**](https://reference.aspose.com/cells/javascript-cpp/cellshelper/#mergeFiles-stringarray-string-string-) فقط دمج البيانات والأنماط والتنسيقات والصيغ. قد لا يتم دمج الكائنات مثل الرسوم البيانية والصور والتعليقات أو الكائنات الأخرى باستخدام هذه الطريقة. علاوة على ذلك، يتم استخدام ملف مخزن مؤقت لتخزين البيانات المؤقتة للعملية.

{{% /alert %}}

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Merge Excel Files and Rename Sheets Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" multiple />
        <button id="runExample">Merge and Rename Sheets</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CellsHelper } = AsposeCells;

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

            if (!fileInput.files.length || fileInput.files.length < 2) {
                resultDiv.innerHTML = '<p style="color: red;">Please select at least two Excel files to merge.</p>';
                return;
            }

            // Read selected files into Uint8Array array
            const files = [];
            for (let i = 0; i < fileInput.files.length; i++) {
                const file = fileInput.files[i];
                const arrayBuffer = await file.arrayBuffer();
                files.push(new Uint8Array(arrayBuffer));
            }

            // Create cacheFile name and destination name (virtual in browser)
            const cacheFile = "test.txt";
            const dest = "output.xlsx";

            // Call CellsHelper.mergeFiles with file byte arrays, cacheFile name and destination name
            // Note: In the browser environment mergeFiles is expected to accept file byte arrays and return merged file bytes.
            const mergedData = CellsHelper.mergeFiles(files, cacheFile, dest);

            // Log cacheFile as in original code
            console.log(cacheFile);

            // Load the merged workbook from returned bytes
            const workbook = new Workbook(new Uint8Array(mergedData));

            // Rename sheets sequentially starting at 1
            let i = 1;
            const worksheets = workbook.worksheets;
            for (let j = 0; j < worksheets.count; j++) {
                worksheets.get(j).name = `Sheet1${i}`;
                i++;
            }

            // Save the modified workbook and prepare download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Merged and Renamed Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Files merged and sheets renamed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
