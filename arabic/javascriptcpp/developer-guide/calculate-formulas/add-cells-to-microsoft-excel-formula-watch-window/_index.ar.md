---
title: إضافة خلايا إلى نافذة مشاهدة الصيغ في Microsoft Excel باستخدام JavaScript عبر C++
linktitle: إضافة الخلايا إلى نافذة مراقبة الصيغ في Microsoft Excel
description: كيفية استخدام مكتبة Aspose.Cells لإضافة خلايا إلى نافذة مشاهدة الصيغ في Excel باستخدام JavaScript عبر C++. من خلال تحميل ملف Excel موجود أو إنشائه جديدًا، يمكننا التلاعب بالخلايا وتعيين المعادلات. وأخيرًا، نحفظ ملف Excel المعدل على القرص.
keywords: Aspose.Cells، Excel، نافذة مشاهدة الصيغ، خلايا، إضافة، JavaScript عبر C++
type: docs
weight: 60
url: /ar/javascript-cpp/add-cells-to-microsoft-excel-formula-watch-window/
---

## **سيناريوهات الاستخدام المحتملة**

نافذة مراقبة Excel من Microsoft هي أداة مفيدة لمراقبة قيم الخلايا وصيغها بسهولة في نافذة. يمكنك فتح *نافذة المراقبة* باستخدام Excel من Microsoft بالنقر على *الصيغ > مراقبة > نافذة*. تحتوي على زر *إضافة مراقبة* الذي يمكن استخدامه لإضافة خلايا للفحص. بالمثل، يمكنك استخدام [**CellWatchCollection.add(number, number)**](https://reference.aspose.com/cells/javascript-cpp/cellwatchcollection/#add-number-number-) لإضافة خلايا إلى *نافذة المراقبة* باستخدام API الخاص بـ Aspose.Cells.

## **إضافة الخلايا إلى نافذة مراقبة صيغ Microsoft Excel**

يعتمد الكود النموذجي التالي تعيين صيغة للخلايا C1 و E1 وإضافتهما إلى نافذة المراقبة. ثم نحفظ المصنف كـ ملف إكسل ناتج. إذا فتحت الملف الناتج وتطلعت على *نافذة المراقبة*، سترى كلا الخليتين كما هو موضح في لقطة الشاشة هذه.

![todo:image_alt_text](add-cells-to-microsoft-excel-formula-watch-window_1.png)

## **الكود المثالي**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Add Cells to Formula Watch Window</h1>
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
            // This example creates a new workbook (like the original JavaScript example).
            // If a user-selected file is provided, it will be ignored for this specific example.
            if (!fileInput) {
                document.getElementById('result').innerHTML = '<p style="color: red;">File input not available.</p>';
                return;
            }

            // Instantiate a new empty workbook
            const wb = new Workbook();

            // Access first worksheet
            const ws = wb.worksheets.get(0);

            // Put some integer values in cell A1 and A2
            ws.cells.get("A1").value = 10;
            ws.cells.get("A2").value = 30;

            // Access cell C1 and set its formula
            const c1 = ws.cells.get("C1");
            c1.formula = "=Sum(A1,A2)";

            // Add cell C1 into cell watches by name
            ws.cellWatches.add(c1.name);

            // Access cell E1 and set its formula
            const e1 = ws.cells.get("E1");
            e1.formula = "=A2*A1";

            // Add cell E1 into cell watches by its row and column indices
            ws.cellWatches.add(e1.row, e1.column);

            // Save workbook to output XLSX format and provide download link
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputAddCellsToMicrosoftExcelFormulaWatchWindow.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created. Click the download link to get the file.</p>';
        });
    </script>
</html>
```
