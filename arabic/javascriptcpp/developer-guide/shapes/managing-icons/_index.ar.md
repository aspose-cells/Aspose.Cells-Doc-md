---
title: إضافة رموز إلى ورقة العمل باستخدام جافا سكريبت عبر ++C
linktitle: إدارة الرموز
type: docs
weight: 100
url: /ar/javascript-cpp/insert-svg-to-excel/
---

## إضافة رموز إلى ورقة العمل في Aspose.Cells for Javaسكريبت عبر ++C

إذا كنت بحاجة إلى استخدام [Aspose.Cells](https://products.aspose.com/cells/) لإضافة 'رموز' في ملف Excel، فإن هذا المستند يمكن أن يوفر لك بعض المساعدة.

واجهة Excel المقابلة لعملية إدراج الرمز كما يلي:

![](1.png)

- حدد موقع رمز الاختيار ليتم إدراجه في ورقة العمل
- انقر يمينا على *إدراج*->*رموز*
- في النافذة التي تفتح، حدد الرمز في المربع الأحمر في الشكل أعلاه
- انقر بزر الماوس الأيسر *إدراج*، سيتم إدراجه في ملف إكسل.

التأثير كما يلي:

![](2.png)

هنا، قمنا بإعداد *رمز عينة* لمساعدتك على إدراج الأيقونات باستخدام [Aspose.Cells](https://products.aspose.com/cells/). يوجد أيضًا [ملف عينة](sample.xlsx) ضروري وملف [موارد الأيقونة](icon.zip). استخدمنا واجهة إكسل لإدراج أيقونة بنفس تأثير العرض كما هو في [ملف الموارد](icon.zip) في [ملف العينة](sample.xlsx).

### جافا سكريبت

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Add Icon to Worksheet Example</h1>
        <p>Select an Excel file and an SVG icon file, then click "Run Example".</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <input type="file" id="iconInput" accept=".svg" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Color } = AsposeCells;

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
            const iconInput = document.getElementById('iconInput');
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }
            if (!iconInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an SVG icon file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const iconFile = iconInput.files[0];

            const arrayBuffer = await file.arrayBuffer();
            const iconArrayBuffer = await iconFile.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet from the collection
            const sheet = workbook.worksheets.get(0);

            // Add the icon to the worksheet
            const iconBytes = new Uint8Array(iconArrayBuffer);
            sheet.shapes.addIcons(3, 0, 7, 0, 100, 100, iconBytes, null);

            // Set a prompt message
            const c = sheet.cells.get(8, 7);
            c.value = "Insert via Aspose.Cells";
            const s = c.style;
            s.font.color = Color.Blue;
            c.style = s;

            // Save and prepare download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample2.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Icon added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

عند تنفيذ الكود أعلاه في مشروعك، ستحصل على النتائج التالية:

![](3.png)
