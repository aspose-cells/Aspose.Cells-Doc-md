---
title: كيفية التحكم في شريط علامات تبويب الورقة باستخدام جافا سكريبت عبر C++
linktitle: كيفية التحكم في شريط علامة الورقة
type: docs
weight: 600
url: /ar/javascript-cpp/how-to-control-sheet-tab-bar/
description: تعلم كيفية التحكم في شريط علامات تبويب الورقة باستخدام Aspose.Cells for JavaScript عبر C++.
keywords: كيفية التحكم في شريط علامات تبويب الورقة جافا سكريبت عبر C++، تشغيل جافا سكريبت في شريط علامات تبويب الورقة عبر C++، تعيين جافا سكريبت في شريط علامات تبويب الورقة عبر C++، التحكم في جافا سكريبت في شريط علامات تبويب الورقة عبر C++.  
---

## **سيناريوهات الاستخدام المحتملة**  
 عندما تحتاج إلى تعديل عرض شريط ورقة إكسل، يجب أن تعرف كيفية التحكم في شريط علامات تبويب الورقة، مثل إخفائه أو إظهاره، تغيير عرض شريط علامات التبويب، تحديد أول علامة تبويب مرئية، وغيرها. يدعم Aspose.Cells for JavaScript عبر C++ هذه الميزات. تقدم Aspose.Cells الخصائص والطُرُق التالية لمساعدتك على تحقيق أهدافك.

- [**WorkbookSettings.showTabs**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#showTabs--)
- [**WorkbookSettings.sheetTabBarWidth**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#sheetTabBarWidth--)
- [**WorkbookSettings.firstVisibleTab**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#firstVisibleTab--)

## ** كيفية التحكم في شريط علامات تبويب الورقة باستخدام Aspose.Cells for JavaScript عبر C++**  
يوضح هذا المثال كيف:

1. إنشاء دفتر عمل.
1. إضافة بيانات إلى الخلايا في ورقة العمل الأولى.
1. عرض علامة الورقة وتعيين عرض شريط التبويب.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Populate Worksheet and Save</h1>
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

            // If a file is provided, load it; otherwise create a new workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Obtaining the reference of the first worksheet
            const ws = workbook.worksheets.get(0);
            const cells = ws.cells;

            // Setting the value to the cells (converted putValue -> value assignment)
            let cell = cells.get("A1");
            cell.value = "Fruit";
            cell = cells.get("B1");
            cell.value = "Count";
            cell = cells.get("C1");
            cell.value = "Price";

            cell = cells.get("A2");
            cell.value = "Apple";
            cell = cells.get("A3");
            cell.value = "Mango";
            cell = cells.get("A4");
            cell.value = "Blackberry";
            cell = cells.get("A5");
            cell.value = "Cherry";

            // Display the sheet tab and set the width of the tab bar (converted getters/setters -> properties)
            workbook.settings.showTabs = true;
            workbook.settings.sheetTabBarWidth = 150;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

معاينة ملف النتائج:  
<br>  
<image src="result.png" width="70%" />
