---
title: استخدام الأنماط المدمجة
linktitle: استخدام الأنماط المدمجة
type: docs
weight: 80
url: /ar/javascript-cpp/using-built-in-styles/
description: رمز JavaScript لاستخدام أنماط Excel المدمجة مع Aspose.Cells for JavaScript عبر C++.
keywords: استخدام JavaScript أنماط Excel المدمجة، تطبيق الأنماط برمجياً في دفتر العمل، تطبيق الأنماط برمجياً في دفتر العمل، تطبيق أنماط مدمجة في Excel، تطبيق أنماط مدمجة في دفتر العمل، رمز JavaScript لتطبيق الأنماط المدمجة في دفتر العمل، رمز JavaScript لتطبيق الأنماط المدمجة في Excel
---

{{% alert color="primary" %}}  
توفر Aspose.Cells مجموعة واسعة من الأنماط القابلة لإعادة الاستخدام لتنسيق الخلية في مستند جدول البيانات. يمكننا استخدام الأنماط المضمنة في سجلنا وأيضًا إنشاء أنماط مخصصة.  
{{% /alert %}}  

## **كيفية استخدام الأنماط المدمجة**  

الطريقة [**Workbook.createBuiltinStyle(BuiltinStyleType)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#createBuiltinStyle-builtinstyletype-) والتعداد [**BuiltinStyleType**](https://reference.aspose.com/cells/javascript-cpp/builtinstyletype) تجعل من السهل استخدام الأنماط المضمنة. إليك قائمة بجميع الأنماط المضمنة الممكنة:  

- TwentyPercentAccent1
- TwentyPercentAccent2
- TwentyPercentAccent3
- TwentyPercentAccent4
- TwentyPercentAccent5
- TwentyPercentAccent6
- FortyPercentAccent1
- FortyPercentAccent2
- FortyPercentAccent3
- FortyPercentAccent4
- لفتة عَرَبيّة 40٪ 5
- لفتة عَرَبيّة 40٪ 6
- لفتة عَرَبيّة 60٪ 1
- لفتة عَرَبيّة 60٪ 2
- لفتة عَرَبيّة 60٪ 3
- لفتة عَرَبيّة 60٪ 4
- لفتة عَرَبيّة 60٪ 5
- لفتة عَرَبيّة 60٪ 6
- لفتة 1
- لفتة 2
- لفتة 3
- لفتة 4
- لفتة 5
- لفتة 6
- سيئ
- حساب
- فحص الخلية
- فاصلة
- فاصلة 1
- عملة
- عملة 1
- نص تفسيري
- جيد
- رأس 1
- رأس 2
- رأس 3
- رأس 4
- الارتباط التشعبي
- ارتباط عند النقر
- مدخل
- خلية مرتبطة
- محايد
- عادي
- ملاحظة
- المخرجات
- النسبة المئوية
- العنوان
- الإجمالي
- نص التحذير
- مستوى الصف
- مستوى العمود


## رمز JavaScript لاستخدام الأنماط المدمجة  
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink1" style="display: none; margin-right: 10px;">Download Output.xlsx</a>
        <a id="downloadLink2" style="display: none;">Download Output.out.ods</a>
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

        document.getElementById('runExample').addEventListener('click', () => {
            // Creating a new Workbook
            const workbook = new Workbook();

            // Creating a built-in style (Title)
            const style = workbook.createBuiltinStyle(AsposeCells.BuiltinStyleType.Title);

            // Accessing first worksheet, its cells, and cell A1
            const worksheet = workbook.worksheets.get(0);
            const cell = worksheet.cells.get("A1");

            // Setting cell value and style (converted setter)
            cell.putValue("Aspose");
            cell.style = style;

            // Auto-fit column and row
            worksheet.autoFitColumn(0);
            worksheet.autoFitRow(0);

            // Save as XLSX
            const outputData1 = workbook.save(SaveFormat.Xlsx);
            const blob1 = new Blob([outputData1]);
            const downloadLink1 = document.getElementById('downloadLink1');
            downloadLink1.href = URL.createObjectURL(blob1);
            downloadLink1.download = 'Output.xlsx';
            downloadLink1.style.display = 'inline-block';
            downloadLink1.textContent = 'Download Output.xlsx';

            // Save as ODS
            const outputData2 = workbook.save(SaveFormat.Ods);
            const blob2 = new Blob([outputData2]);
            const downloadLink2 = document.getElementById('downloadLink2');
            downloadLink2.href = URL.createObjectURL(blob2);
            downloadLink2.download = 'Output.out.ods';
            downloadLink2.style.display = 'inline-block';
            downloadLink2.textContent = 'Download Output.out.ods';

            document.getElementById('result').innerHTML = '<p style="color: green;">Files generated. Click the download links to save them.</p>';
        });
    </script>
</html>
```
