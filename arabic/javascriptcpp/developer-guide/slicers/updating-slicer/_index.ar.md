---
title: تحديث القطعة الفاصلة باستخدام جافا سكريبت عبر C++
linktitle: تحديث المقسم
type: docs
weight: 50
url: /ar/javascript-cpp/updating-slicer/
description: تعرض هذه المقالة كيفية تحديث الجداول المحورية المرتبطة عن طريق تحديث القطعة الفاصلة باستخدام Aspose.Cells for JavaScript عبر C++.
keywords: Aspose.Cells جافا سكريبت عبر C++، تحديث القطعة الفاصلة، كيفية تغيير القطعة الفاصلة في جافا سكريبت، كيفية تعديل القطعة الفاصلة في جافا سكريبت، كيفية اختيار أو إلغاء اختيار عناصر القطعة الفاصلة باستخدام JavaScript عبر C++.
---

## **سيناريوهات الاستخدام المحتملة**

 إذا كنت تريد تحديث مقسم في Microsoft Excel، قم باختيار أو إلغاء اختيار عناصره، وسيتحدث المقسم وفقًا لذلك. يرجى استخدام [**Slicer.slicerCacheItems**](https://reference.aspose.com/cells/javascript-cpp/slicercache/#slicerCacheItems--) لاختيار أو إلغاء اختيار عناصر المقسم مع Aspose.Cells ثم استدعاء [**Slicer.refresh()**](https://reference.aspose.com/cells/javascript-cpp/slicer/#refresh--) لتحديث جدول المقسم أو الجدول المحوري.

## **كيفية تحديث العارض**

يحمل الكود العيني التالي الملف اكسل العيني الذي يحتوي على عارض موجود. يلغي تحديد العناصر الثانية والثالثة من العارض ويحدث العارض. ثم يحفظ الدفتر كملف أكسل بإسم ملف الأكسل العيني الناتج. تظهر الصورة العينية التالية تأثير الكود العيني على ملف الأكسل العيني العيني. كما ترون في الصورة العينية، تم تحديث العارض بالعناصر المحددة وكذلك تم تحديث الجدول المحوري وفقًا لذلك.

![todo:image_alt_text](updating-slicer_1.png)

## **الكود المثالي**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Update Slicer</title>
    </head>
    <body>
        <h1>Update Slicer Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
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

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const ws = workbook.worksheets.get(0);

            // Access the first slicer inside the slicer collection
            const slicer = ws.slicers.get(0);

            // Access the slicer items via slicer cache
            const items = slicer.slicerCache.slicerCacheItems;

            // Iterate items and deselect "Pink" and "Green"
            for (let i = 0; i < items.count; i++) {
                const item = items.get(i);
                if (item.value === "Pink" || item.value === "Green") {
                    item.selected = false;
                }
            }

            // Refresh slicer to apply changes
            slicer.refresh();

            // Save modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Slicer updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
