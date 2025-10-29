---
title: إعادة استخدام كائنات النمط
linktitle: إعادة استخدام كائنات النمط
description: في Aspose.Cells for JavaScript عبر C++، من خلال إنشاء واستخدام كائنات نمط قابلة لإعادة الاستخدام، يمكنك تبسيط إدارة الأنماط وتحسين كفاءة الشفرة. ستساعدك دليلك على الاستفادة من مميزات الكائنات القابلة لإعادة الاستخدام وتطبيقها في تطبيقك.
keywords: Aspose.Cells for JavaScript عبر C++، إعادة استخدام كائنات النمط، إدارة النمط، كفاءة الشفرة، أنماط قابلة لإعادة الاستخدام، تطوير التطبيقات، مرجع API، مثال على الشفرة، التحميل، الدعم.
type: docs
weight: 3000
url: /ar/javascript-cpp/reusing-style-objects/
---

{{% alert color="primary" %}}  
يمكن لإعادة استخدام كائنات النمط توفير الذاكرة وجعل البرنامج أسرع.  
{{% /alert %}}  

لتطبيق بعض التنسيق على مجموعة كبيرة من الخلايا في ورقة العمل:

1. إنشاء كائن النمط.
1. تحديد السمات.
1. تطبيق النمط على الخلايا في النطاق.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Create Workbook and Set Font</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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
            // Creating a new workbook (empty)
            const workbook = new Workbook();

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access cells
            const cell1 = worksheet.cells.get("A1");
            const cell2 = worksheet.cells.get("B1");

            // Set the styles of both cells to Times New Roman
            const styleObject = workbook.createStyle();
            styleObject.font.color = Color.Red;
            styleObject.font.name = "Times New Roman";
            cell1.style = styleObject;
            cell2.style = styleObject;

            // Put the values inside the cell
            cell1.value = "Hello World!";
            cell2.value = "Hello World!!";

            // Save to XLSX
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'SampleOutput_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and saved successfully. Click the download link to get the file.</p>';
        });
    </script>
</html>
```


{{% alert color="primary" %}}  
نظرًا لأن نهج [**Cell.style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style--) / [**Cell.style**](https://reference.aspose.com/cells/javascript-cpp/cell/#style-style-) يستخدم ذاكرة أقل بكثير، وهو أكثر كفاءة، تم إزالة خاصية Cell.style القديمة التي كانت تستهلك الكثير من الذاكرة غير الضرورية مع إصدار Aspose.Cells 7.1.0.  
{{% /alert %}}
