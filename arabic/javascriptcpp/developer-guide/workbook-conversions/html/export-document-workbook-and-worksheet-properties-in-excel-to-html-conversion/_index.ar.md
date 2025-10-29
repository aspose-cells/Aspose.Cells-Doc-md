---
title: تصدير خصائص مجلد المستند وورقة العمل في تحويل إكسل إلى HTML باستخدام JavaScript عبر C++
linktitle: تصدير خصائص ورقة عمل ومصنف الوثيقة في تحويل Excel إلى HTML
type: docs
weight: 50
url: /ar/javascript-cpp/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/
description: تعرّف على كيفية تصدير خصائص المستند، ومجلد العمل، وورقة العمل في إكسل إلى HTML باستخدام Aspose.Cells for JavaScript عبر C++.
---

## **سيناريوهات الاستخدام المحتملة**  

عند تصدير ملف إكسل من مايكروسوفت إكسل إلى HTML باستخدام مايكروسوفت إكسل أو Aspose.Cells for JavaScript عبر C++، يتم أيضًا تصدير أنواع مختلفة من خصائص المستند، ومجلد العمل، وورقة العمل كما هو موضح في لقطة الشاشة التالية. يمكنك تجنب تصدير هذه الخصائص عن طريق ضبط [**HtmlSaveOptions.exportDocumentProperties**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#exportDocumentProperties--)، [**HtmlSaveOptions.exportWorkbookProperties**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#exportWorkbookProperties--) و [**HtmlSaveOptions.exportWorksheetProperties**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#exportWorksheetProperties--) على **false**. القيمة الافتراضية لهذه الخصائص هي **true**. تُظهر لقطة الشاشة التالية كيف تبدو هذه الخصائص في HTML المصدر.  

![todo:image_alt_text](export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion_1.png)  

## **تصدير خصائص الوثيقة والمصنف وورق العمل في تحويل Excel إلى HTML**  

يحمل رمز المثال التالي ملف Excel النموذجي ويحوّله إلى HTML بدون تصدير خصائص المستند ودفتر العمل وورقة العمل في [HTML الناتج](61767779.zip).  

## **الكود المثالي**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Export HTML without Properties</title>
    </head>
    <body>
        <h1>Export Excel to HTML (without document/workbook/worksheet properties)</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlSaveOptions, Utils } = AsposeCells;

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
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Load the sample Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Specify Html Save Options
            const options = new HtmlSaveOptions();

            // We do not want to export document, workbook and worksheet properties
            options.exportDocumentProperties = false;
            options.exportWorkbookProperties = false;
            options.exportWorksheetProperties = false;

            // Export the Excel file to Html with Html Save Options
            const outputData = workbook.save(SaveFormat.Html, options);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputExportDocumentWorkbookAndWorksheetPropertiesInHTML.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            resultDiv.innerHTML = '<p style="color: green;">Export completed successfully! Click the download link to get the HTML file.</p>';
        });
    </script>
</html>
```
