---
title: انتشار الصيغة في جدول أو كائن قائمة تلقائيًا أثناء إدخال البيانات في صفوف جديدة باستخدام JavaScript عبر C++
linktitle: يحدد صيغة الجدول
type: docs
weight: 260
url: /ar/javascript-cpp/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/
description: تعلم كيفية نشر الصيغ تلقائيًا في الجداول أو كائنات القوائم أثناء إدخال البيانات في صفوف جديدة باستخدام Script Aspose.Cells for Java عبر C++.
---

## **سيناريوهات الاستخدام المحتملة**
أحيانًا، تريد أن تنتشر صيغة في جدولك أو كائن القائمة تلقائيًا إلى الصفوف الجديدة أثناء إدخال بيانات جديدة. هذا هو السلوك الافتراضي لبرنامج Microsoft Excel. لتحقيق نفس الوظيفة باستخدام Script Aspose.Cells for Java عبر C++، يرجى استخدام الخاصية [ListColumn.formula](https://reference.aspose.com/cells/javascript-cpp/listcolumn/#formula--).

## **نشر الصيغة تلقائيًا في جدول أو كائن قائمة أثناء إدخال البيانات في الصفوف الجديدة**
يخلق رمز المثال التالي جدول أو كائن قائمة بحيث تنتشر الصيغة في العمود ب تلقائيًا إلى الصفوف الجديدة عند إدخال بيانات جديدة. يرجى التحقق من [ملف إكسل الناتج](5115469.xlsx) الذي تم توليده بهذا الرمز. إذا أدخلت أي رقم في الخلية A3، سترى أن الصيغة في الخلية B2 تنتشر تلقائيًا إلى الخلية B3.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells ListObject Example</h1>
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
            // Create workbook object
            const book = new Workbook();

            // Access first worksheet
            const sheet = book.worksheets.get(0);

            // Add column headings in cell A1 and B1
            sheet.cells.get(0, 0).value = "Column A";
            sheet.cells.get(0, 1).value = "Column B";

            // Add list object, set its name and style
            const listObject = sheet.listObjects.get(
                sheet.listObjects.add(0, 0, 1, sheet.cells.maxColumn, true)
            );
            listObject.tableStyleType = AsposeCells.TableStyleType.TableStyleMedium2;
            listObject.displayName = "Table";

            // Set the formula of second column so that it propagates to new rows automatically while entering data
            listObject.listColumns.get(1).formula = "=[Column A] + 1";

            // Save the workbook in xlsx format
            const outputData = book.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
