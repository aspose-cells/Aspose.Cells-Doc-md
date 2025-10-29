---
title: دمج عدة دفاترك في دفاتر عمل واحدة باستخدام جافاسكريبت عبر C++
linktitle: مدمج السجل
type: docs
weight: 66
url: /ar/javascript-cpp/combine-multiple-workbooks-into-a-single-workbook/
description: تعلم كيفية دمج دفاتر عمل متعددة في دفتر عمل واحد باستخدام Aspose.Cells for JavaScript عبر C++. 
---

{{% alert color="primary" %}}

أحيانًا، تحتاج إلى دمج دفاتر العمل بمحتوى متنوع مثل الصور والمخططات والبيانات في دفتر عمل واحد. يدعم Aspose.Cells for JavaScript عبر C++ هذه الميزة. يوضح هذا المقال كيفية إنشاء تطبيق وحدة تحكم ودمج دفاتر العمل ببضع أسطر بسيطة من الشفرة باستخدام Aspose.Cells.

{{% /alert %}}

## **دمج أسجل العمل مع الصور والرسوم البيانية**

يجمع مثال الشفرة دفترين للعمل معًا في دفتر عمل واحد باستخدام Aspose.Cells for JavaScript عبر C++. تقوم الشفرة بتحميل دفاتر العمل المصدر، وتستخدم طريقة [**Workbook.combine(Workbook)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#combine-workbook-) لدمجها، وتحفظ دفتر العمل الناتج.

### **السجلات المصدر**

- [charts.xlsx](5473097.xlsx)
- [picture.xlsx](5473096.xlsx)

### **مصنفات الإخراج**

- [combined.xlsx](5473095.xlsx)

### **لقطات الشاشة**

أدناه تظهر لقطات من المصنفات الأصلية والمخرّجة.

{{% alert color="primary" %}}

يمكنك استخدام أي مصنف أصلي. هذه الصور مجرد لأغراض توضيحية.

{{% /alert %}}

**الورقة العمل الأولى لمصنف الرسوم البيانية - مكدسة** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_1.jpg)

**الورقة العمل الثانية لمصنف الرسوم البيانية - خطية** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_2.jpg)

**الورقة العمل الأولى لمصنف الصور - صورة** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_3.jpg)

**كل الورقات الثلاثة في مصنف الدمج - مكدسة، خطية، صورة** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_4.jpg)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Combine Workbooks Example</title>
    </head>
    <body>
        <h1>Combine Workbooks Example</h1>
        <p>Select two Excel files to combine:</p>
        <input type="file" id="fileInput1" accept=".xls,.xlsx" />
        <input type="file" id="fileInput2" accept=".xls,.xlsx" />
        <button id="runExample">Combine Workbooks</button>
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
            const fileInput1 = document.getElementById('fileInput1');
            const fileInput2 = document.getElementById('fileInput2');

            if (!fileInput1.files.length || !fileInput2.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select two Excel files.</p>';
                return;
            }

            const file1 = fileInput1.files[0];
            const file2 = fileInput2.files[0];

            const arrayBuffer1 = await file1.arrayBuffer();
            const arrayBuffer2 = await file2.arrayBuffer();

            // Open the first excel file.
            const sourceBook1 = new Workbook(new Uint8Array(arrayBuffer1));

            // Open the second excel file.
            const sourceBook2 = new Workbook(new Uint8Array(arrayBuffer2));

            // Combining the two workbooks
            sourceBook1.combine(sourceBook2);

            // Save the combined workbook and provide download link
            const outputData = sourceBook1.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Combined.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Combined Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbooks combined successfully! Click the download link to get the combined file.</p>';
        });
    </script>
</html>
```

## **مواضيع متقدمة**
- [دمج الورقات المتعددة في ورقة عمل واحدة](/cells/ar/javascript-cpp/combine-multiple-worksheets-into-a-single-worksheet/)
- [دمج الملفات](/cells/ar/javascript-cpp/merge-files/)
