---
title: الوصول وتحديث أجزاء النص الغني للخلية
linktitle: تنسيق النص الغني
type: docs
weight: 40
url: /ar/javascript-cpp/access-and-update-the-portions-of-rich-text-of-cell/
description: تعلم كيفية الوصول إلى أجزاء النص الغني من الخلية وتحديثها عبر واجهة برمجة التطبيقات Aspose.Cells for JavaScript باستخدام C++.
keywords: الوصول إلى وتحديث نص غني للخلية، الحصول على نص غني للخلية، تحرير نص غني للخلية، الوصول إلى نص غني للخلية، تحديث نص غني للخلية، تغيير نص غني للخلية
---

{{% alert color="primary" %}}

 يسمح لك Aspose.Cells for JavaScript باستخدام C++ بالوصول إلى أجزاء النص الغني من الخلية وتحديثها. يمكنك استخدام خصائص [**Cell.characters**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters--) و[**Cell.characters**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters-fontsettingarray-) لهذا الغرض. ستعيد وتقبل هذه الخصائص مصفوفة من كائنات [**FontSetting**](https://reference.aspose.com/cells/javascript-cpp/fontsetting) والتي يمكنك استخدامها للوصول إلى وتحديث خصائص الخط المتنوعة مثل اسم الخط، لون الخط، سمك الخط، وغيرها.

{{% /alert %}}

## **الوصول إلى وتحديث أجزاء النص الغني للخلية**

يوضح الكود التالي كيفية استخدام خاصيتي [**Cell.characters**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters--) و[**Cell.characters**](https://reference.aspose.com/cells/javascript-cpp/cell/#characters-fontsettingarray-) باستخدام ملف Excel المصدر ([ملف المصدر](5112369.xlsx)) والذي يمكنك تنزيله من الرابط المقدم. يحتوي ملف المصدر على نص غني في الخلية A1. لديه 3 أجزاء وكل جزء له خط مختلف. يطابق الكود التالي هذه الأجزاء ويحدث الجزء الأول باسم خط جديد. وأخيرًا، يحفظ الملف باسم ملف Excel الناتج ([ملف الإخراج](5112366.xlsx)). عند فتحه، ستجد أن خط الجزء الأول من النص قد تغير إلى **"Arial"**.

### كود جافاسكريبت للوصول إلى أجزاء النص الغني من الخلية وتحديثها

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Update Cell Character Font Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

        const readyPromise = AsposeCells.onReady({
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

            // Ensure Aspose.Cells is initialized
            await readyPromise;

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet and its cells
            const cells = workbook.worksheets.get(0).cells;
            const cell = cells.get("A1");

            console.log("Before updating the font settings....");
            let fnts = cell.characters;
            const count = fnts.length;
            for (let i = 0; i < count; i++) {
                console.log(fnts[i].font.name);
            }

            // Modify the first FontSetting Font Name
            fnts[0].font.name = "Arial";

            // And update it using characters property
            cell.characters = fnts;

            console.log("After updating the font settings....");

            fnts = cell.characters;

            for (let i = 0; i < count; i++) {
                console.log(fnts[i].font.name);
            }

            // Save workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### المخرجات في وحدة الطرفية التي تم إنشاؤها بواسطة الكود النموذجي



{{< highlight java >}}

Before updating the font settings....

Century

Courier New

Verdana

After updating the font settings....

Arial

Courier New

Verdana

{{< /highlight >}}
