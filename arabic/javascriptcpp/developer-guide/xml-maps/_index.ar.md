---
title: استيراد XML إلى دفتر عمل Excel باستخدام JavaScript عبر C++
linktitle: خرائط XML
type: docs
weight: 210
url: /ar/javascript-cpp/import-xml-map-inside-a-workbook-using-aspose-cells/
description: استيراد البيانات من ملفات XML إلى Excel باستخدام Aspose.Cells for JavaScript عبر C++.
---

{{% alert color="primary" %}}

يوفر Aspose.Cells إمكانية استيراد خريطة XML داخل ملف العمل باستخدام طريقة [**Workbook.importXml(string, string, number, number)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#importXml-string-string-number-number-). يمكنك استيراد خريطة XML باستخدام Microsoft Excel وفقًا للخطوات التالية:

- حدد علامة **المطور**
- انقر فوق **استيراد** في القسم XML واتبع الخطوات المطلوبة.

ستحتاج إلى تقديم بياناتك XML لإكمال الاستيراد. إليك [بيانات XML عينية](5115037.txt) يمكنك استخدامها للفحص.

{{% /alert %}}

## **استيراد خريطة XML باستخدام Microsoft Excel**

تُظهر اللقطة الشاشة التالية كيفية استيراد خريطة XML باستخدام Microsoft Excel.

|![todo:image_alt_text](import-xml-map-inside-a-workbook-using-aspose-cells_1.png)|
| :- |

## **استيراد خريطة XML باستخدام Aspose.Cells for JavaScript عبر C++**

يُظهر الكود العينة التالي كيفية استخدام الـ [**Workbook.importXml(string, string, number, number)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#importXml-string-string-number-number-). يُولّد ملف الإكسل [الناتج](5115036.xlsx) كما هو موضح في هذه اللقطة الشاشة.

|![todo:image_alt_text](import-xml-map-inside-a-workbook-using-aspose-cells_2.png)|
| :- |

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Import XML</title>
    </head>
    <body>
        <h1>Import XML into Workbook Example</h1>
        <input type="file" id="xmlInput" accept=".xml,.txt" />
        <button id="runExample">Import XML and Save</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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
            const fileInput = document.getElementById('xmlInput');
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an XML file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const xmlText = await file.text();

            // Create a workbook
            const workbook = new Workbook();

            // Import your XML Map data starting from cell A1 on Sheet1
            workbook.importXml(xmlText, "Sheet1", 0, 0);

            // Save workbook to XLSX and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">XML imported and workbook saved. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **مواضيع متقدمة**
- [أضف خريطة XML داخل دفتر العمل باستخدام طريقة XmlMapCollection.add()](/cells/ar/javascript-cpp/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/)
- [تصدير البيانات XML المرتبطة بخريطة XML داخل الكتيب](/cells/ar/javascript-cpp/export-xml-data-linked-to-xml-map-inside-the-workbook/)
- [العثور على اسم عنصر الجذر في خريطة XML](/cells/ar/javascript-cpp/find-the-root-element-name-of-xml-map/)
- [ربط الخلايا بعناصر خريطة XML](/cells/ar/javascript-cpp/link-cells-to-xml-map-elements/)
