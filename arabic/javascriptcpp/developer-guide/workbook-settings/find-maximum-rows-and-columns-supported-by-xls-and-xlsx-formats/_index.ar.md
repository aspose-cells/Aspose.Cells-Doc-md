---
title: إيجاد الحد الأقصى من الصفوف والأعمدة المدعومة بواسطة تنسيقات XLS و XLSX باستخدام جافا سكريبت عبر C++
linktitle: العثور على الصفوف والأعمدة القصوى المدعومة من قبل تنسيقات XLS و XLSX
type: docs
weight: 20
url: /ar/javascript-cpp/find-maximum-rows-and-columns-supported-by-xls-and-xlsx-formats/
---

## **سيناريوهات الاستخدام المحتملة**  

هناك أعداد مختلفة من الصفوف والأعمدة المدعومة بواسطة تنسيقات Excel. على سبيل المثال، تدعم XLS 65536 صفًا و 256 عمودًا، بينما تدعم XLSX 1048576 صفًا و 16384 عمودًا. إذا كنت تريد معرفة عدد الصفوف والأعمدة التي يدعمها تنسيق معين، يمكنك استخدام الخصائص [**WorkbookSettings.maxRow**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#maxRow--) و [**WorkbookSettings.maxColumn**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#maxColumn--).  

## **العثور على الصفوف والأعمدة القصوى المدعومة من قبل تنسيقات XLS و XLSX**  

يخلق المثال التالي ملف عمل أولاً بصيغة XLS ثم بصيغة XLSX. بعد الإنشاء، يطبع قيم خصائص [**WorkbookSettings.maxRow**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#maxRow--) و [**WorkbookSettings.maxColumn**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#maxColumn--). يرجى مراجعة مخرجات وحدة التحكم الخاصة بالكود أدناه للمرجعية.  

## **الكود المثالي**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Maximum Rows and Columns Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample" disabled>Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, Utils } = AsposeCells;

        const runBtn = document.getElementById('runExample');
        const resultDiv = document.getElementById('result');

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
            runBtn.disabled = false;
        });

        runBtn.addEventListener('click', async () => {
            // Print message about XLS format.
            resultDiv.innerHTML = '<p>Maximum Rows and Columns supported by XLS format.</p>';

            // Create workbook in XLS format.
            let wb = new Workbook(AsposeCells.FileFormatType.Excel97To2003);

            // Print the maximum rows and columns supported by XLS format.
            let maxRows = wb.settings.maxRow + 1;
            let maxCols = wb.settings.maxColumn + 1;
            resultDiv.innerHTML += `<p>Maximum Rows: ${maxRows}</p>`;
            resultDiv.innerHTML += `<p>Maximum Columns: ${maxCols}</p>`;
            resultDiv.innerHTML += '<hr/>';

            // Print message about XLSX format.
            resultDiv.innerHTML += '<p>Maximum Rows and Columns supported by XLSX format.</p>';

            // Create workbook in XLSX format.
            wb = new Workbook(AsposeCells.FileFormatType.Xlsx);

            // Print the maximum rows and columns supported by XLSX format.
            maxRows = wb.settings.maxRow + 1;
            maxCols = wb.settings.maxColumn + 1;
            resultDiv.innerHTML += `<p>Maximum Rows: ${maxRows}</p>`;
            resultDiv.innerHTML += `<p>Maximum Columns: ${maxCols}</p>`;
        });
    </script>
</html>
```  

## **مخرجات الوحدة**  

{{< highlight java >}}  

Maximum Rows and Columns supported by XLS format.  

Maximum Rows: 65536  

Maximum Columns: 256  

Maximum Rows and Columns supported by XLSX format.  

Maximum Rows: 1048576  

Maximum Columns: 16384  

{{< /highlight >}}
