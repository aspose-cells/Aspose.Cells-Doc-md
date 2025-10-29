---
title: ترتيب مخصص في جدول محوري
type: docs
weight: 130
url: /ar/javascript-cpp/custom-sorting-in-pivot-table/
description: كيفية فرز الجداول المحورية على قيم الحقول باستخدام Aspose.Cells for Javaنص برمجي عبر C++.
keywords: Aspose.Cells for Javaنص برمجي عبر C++ إكسل، مكتبة جافا سكريبت إكسل، فرز الجداول المحورية على قيم الحقول باستخدام Aspose.Cells for Javaنص برمجي عبر C++ إكسل.
---

## **كيفية تعيين تصنيف مخصص في الجدول المحوري باستخدام Aspose.Cells for Javaنص برمجي عبر مكتبة C++**
باستخدام واجهة برمجة التطبيقات Aspose.Cells for Javaنص برمجي عبر C++، يمكنك فرز الجداول المحورية على قيم الحقول. يستعرض الكود التالي الملف Excel النموذجي ويضيف ثلاثة جداول محورية. الجدول المحوري الأول بدون تصنيف مخصص، والثاني مصنف على قيم حقل الصف "SeaFood"، والثالث مصنف على قيم حقل العمود "28/07/2000".

يمكن تنزيل ملف المصدر وملفات الإخراج التجريبية من هنا لاختبار الشيفرة التجريبية:

[ملف إكسيل المصدر](98107428.xlsx)

[ملف إكسيل الناتج](98107429.xlsx)

[ملف PDF الناتج](98107430.pdf)


## **الكود المثالي**
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells PivotTable Sort Example</title>
    </head>
    <body>
        <h1>Aspose.Cells PivotTable Sort Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadXlsxLink" style="display: none; margin-right: 10px;">Download Excel File</a>
        <a id="downloadPdfLink" style="display: none;">Download PDF File</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions } = AsposeCells;

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
            const downloadXlsxLink = document.getElementById('downloadXlsxLink');
            const downloadPdfLink = document.getElementById('downloadPdfLink');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file (SamplePivotSort.xlsx).</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet in the Excel file
            const sheet = workbook.worksheets.get(0);
            const pivotTables = sheet.pivotTables;

            // source PivotTable
            // Adding a PivotTable to the worksheet
            let index = pivotTables.add("=Sheet1!A1:C10", "E3", "PivotTable2");
            // Accessing the instance of the newly added PivotTable
            let pivotTable = pivotTables.get(index);
            // Unshowing grand totals for rows.
            pivotTable.rowGrand = false;
            pivotTable.columnGrand = false;
            // Dragging the first field to the row area.
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, 1);
            let rowField = pivotTable.rowFields.get(0);
            rowField.isAutoSort = true;
            rowField.isAscendSort = true;
            // Dragging the second field to the column area.
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, 0);
            let colField = pivotTable.columnFields.get(0);
            colField.numberFormat = "dd/mm/yyyy";
            colField.isAutoSort = true;
            colField.isAscendSort = true;
            // Dragging the third field to the data area.
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, 2);
            pivotTable.refreshData();
            pivotTable.calculateData();
            // end of source PivotTable

            // sort the PivotTable on "SeaFood" row field values
            index = pivotTables.add("=Sheet1!A1:C10", "E10", "PivotTable2");
            pivotTable = pivotTables.get(index);
            pivotTable.rowGrand = false;
            pivotTable.columnGrand = false;
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, 1);
            rowField = pivotTable.rowFields.get(0);
            rowField.isAutoSort = true;
            rowField.isAscendSort = true;
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, 0);
            colField = pivotTable.columnFields.get(0);
            colField.numberFormat = "dd/mm/yyyy";
            colField.isAutoSort = true;
            colField.isAscendSort = true;
            colField.autoSortField = 0;
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, 2);
            pivotTable.refreshData();
            pivotTable.calculateData();

            // sort the PivotTable on "28/07/2000" column field values
            index = pivotTables.add("=Sheet1!A1:C10", "E18", "PivotTable2");
            pivotTable = pivotTables.get(index);
            pivotTable.rowGrand = false;
            pivotTable.columnGrand = false;
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, 1);
            rowField = pivotTable.rowFields.get(0);
            rowField.isAutoSort = true;
            rowField.isAscendSort = true;
            rowField.autoSortField = 0;
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, 0);
            colField = pivotTable.columnFields.get(0);
            colField.numberFormat = "dd/mm/yyyy";
            colField.isAutoSort = true;
            colField.isAscendSort = true;
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, 2);
            pivotTable.refreshData();
            pivotTable.calculateData();

            // Saving the Excel file (XLSX)
            const xlsxData = workbook.save(SaveFormat.Xlsx);
            const xlsxBlob = new Blob([xlsxData], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
            downloadXlsxLink.href = URL.createObjectURL(xlsxBlob);
            downloadXlsxLink.download = 'out_java.xlsx';
            downloadXlsxLink.style.display = 'inline-block';
            downloadXlsxLink.textContent = 'Download Modified Excel File';

            // Saving as PDF
            const options = new AsposeCells.PdfSaveOptions();
            options.onePagePerSheet = true;
            const pdfData = workbook.save(SaveFormat.Pdf, options);
            const pdfBlob = new Blob([pdfData], { type: "application/pdf" });
            downloadPdfLink.href = URL.createObjectURL(pdfBlob);
            downloadPdfLink.download = 'out_java.pdf';
            downloadPdfLink.style.display = 'inline-block';
            downloadPdfLink.textContent = 'Download PDF File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Use the links above to download the results.</p>';
        });
    </script>
</html>
```
