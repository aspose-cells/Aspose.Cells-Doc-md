---
title: حفظ دفتر العمل بصيغة جدول بيانات XML المفتوحة الصارمة باستخدام جافا سكريبت عبر ++C
linktitle: حفظ الدفتر إلى تنسيق جدول بيانات إكس الإكس إم الصارم
type: docs
weight: 150
url: /ar/javascript-cpp/save-workbook-to-strict-open-xml-spreadsheet-format/
description: تعلم كيفية حفظ دفتر العمل بصيغة جدول بيانات XML المفتوحة الصارمة باستخدام سكريبت Aspose.Cells for Java عبر ++C.
---

## **سيناريوهات الاستخدام المحتملة**

يسمح سكريبت Aspose.Cells for Java عبر ++C لك بحفظ دفتر العمل بصيغة *XML المفتوحة الصارمة*. لهذا الغرض، يوفر الخاصية [**WorkbookSettings.compliance**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#compliance--). إذا قمت بضبط قيمتها على [**OoxmlCompliance.iso29500_2008_strict**](https://reference.aspose.com/cells/javascript-cpp/ooxmlcompliance)، فسيتم حفظ ملف Excel الناتج بصيغة XML المفتوحة الصارمة.

## **حفظ الدفتر إلى تنسيق جدول بيانات إكس الإكس إم الصارم**

 ينشئ رمز العينة التالي ملف عمل ويضبط قيمة الخاصية [**WorkbookSettings.compliance**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#compliance--) إلى [**OoxmlCompliance.iso29500_2008_strict**](https://reference.aspose.com/cells/javascript-cpp/ooxmlcompliance) ويحفظه كـ [ملف Excel المخرج](67338272.xlsx). إذا فتحت ملف Excel المخرج في Microsoft Excel وفتحت مربع الحوار Save As...، سترى تنسيقه كـ *Open XML الصارم* كما هو موضح في هذه الصورة.

![todo:image_alt_text](save-workbook-to-strict-open-xml-spreadsheet-format_1.png)

## **الكود المثالي**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Save Workbook to Strict Open XML Spreadsheet Format</title>
    </head>
    <body>
        <h1>Save Workbook to Strict Open XML Spreadsheet Format</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, OoxmlCompliance, Utils } = AsposeCells;

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
            // Create a new workbook
            const workbook = new Workbook();

            // Specify - Strict Open XML Spreadsheet - Format.
            workbook.settings.compliance = OoxmlCompliance.Iso29500_2008_Strict;

            // Access first worksheet and set value in B4
            const worksheet = workbook.worksheets.get(0);
            const b4 = worksheet.cells.get("B4");
            b4.value = "This Excel file has Strict Open XML Spreadsheet format.";

            // Save to output Excel file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSaveWorkbookToStrictOpenXMLSpreadsheetFormat.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and saved to Strict Open XML Spreadsheet format. Click the download link to get the file.</p>';
        });
    </script>
</html>
```
