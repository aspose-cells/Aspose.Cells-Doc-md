---
title: كيفية التحكم في عرض دفتر العمل باستخدام جافا سكريبت عبر C++
linktitle: كيفية التحكم في عرض دفتر العمل
type: docs
weight: 600
url: /ar/javascript-cpp/how-to-control-workbook-view/
description: تعلم كيفية التحكم في عرض دفتر العمل من خلال الشفرة Aspose.Cells for JavaScript عبر واجهة برمجة التطبيقات C++.
keywords: كيفية التحكم في عرض دفتر العمل باستخدام جافا سكريبت عبر C++، ضبط عرض إكسل باستخدام جافا سكريبت عبر C++، تشغيل عرض دفتر العمل باستخدام جافا سكريبت عبر C++، ضبط عرض دفتر العمل باستخدام جافا سكريبت عبر C++، التحكم في عرض إكسل باستخدام جافا سكريبت عبر C++.
---

## **سيناريوهات الاستخدام المحتملة**
عند الحاجة لضبط عرض صفحات إكسل، يتطلب الأمر معرفة كيفية التحكم في كل وحدة، مثل أشرطة التمرير الأفقية والرأسية، سواء لإخفاء ملفات إكسل المفتوحة، وما إلى ذلك. توفر الشفرة Aspose.Cells for JavaScript عبر C++ هذه الميزة. توفر الشفرة Aspose.Cells for JavaScript عبر C++ الخصائص والأساليب التالية لمساعدتك على تحقيق أهدافك.

- [**WorkbookSettings.isHScrollBarVisible()**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#isHScrollBarVisible--)
- [**WorkbookSettings.isVScrollBarVisible()**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#isVScrollBarVisible--)
- [**WorkbookSettings.isHidden()**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#isHidden--)
- [**WorkbookSettings.isMinimized()**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#isMinimized--)
- [**WorkbookSettings.windowHeight**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#windowHeight--)
- [**WorkbookSettings.windowWidth**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#windowWidth--)
- [**WorkbookSettings.windowLeft**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#windowLeft--)
- [**WorkbookSettings.windowTop**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#windowTop--)

## **كيفية التحكم في عرض دفتر العمل باستخدام Aspose.Cells for JavaScript عبر C++**
يوضح هذا المثال كيف:

1. إنشاء دفتر عمل.
1. إضافة بيانات إلى الخلايا في ورقة العمل الأولى.
1. إخفاء شرائط التمرير الأفقية والعمودية لعرض دفتر العمل.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Aspose.Cells Example - Create/Modify Workbook</h1>
        <p>Select an existing .xls/.xlsx file to modify, or leave empty to create a new workbook.</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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
            // If a file is selected, open it; otherwise create a new workbook (matches original Node behavior)
            let workbook;
            if (fileInput.files && fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Obtaining the reference of the first worksheet
            const ws = workbook.worksheets.get(0);
            const cells = ws.cells;

            // Setting the value to the cells (converted putValue => value)
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

            cell = cells.get("B2");
            cell.value = 5;
            cell = cells.get("B3");
            cell.value = 3;
            cell = cells.get("B4");
            cell.value = 6;
            cell = cells.get("B5");
            cell.value = 4;

            cell = cells.get("C2");
            cell.value = 5;
            cell = cells.get("C3");
            cell.value = 20;
            cell = cells.get("C4");
            cell.value = 30;
            cell = cells.get("C5");
            cell.value = 60;

            // Apply style: createStyle(), font/color adjustments converted from get/set to properties
            cell = cells.get("E10");
            const temp = workbook.createStyle();
            temp.font.color = AsposeCells.Color.Red;
            cell.style = temp;

            // Hide horizontal and vertical scrollbars (converted getSettings().set... -> settings.is... = ...)
            workbook.settings.isHScrollBarVisible = false;
            workbook.settings.isVScrollBarVisible = false;

            // Save the modified workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

معاينة ملف النتائج:
<br>
<image src="result.png" width="70%" />
