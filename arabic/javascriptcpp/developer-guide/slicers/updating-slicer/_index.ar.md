---
title: تحديث العارض باستخدام جافا سكريبت عبر C++
linktitle: تحديث العارض
type: docs
weight: 50
url: /ar/javascript-cpp/updating-slicer/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
description: تعرض هذه المقالة كيفية تحديث العارض لتصفية بيانات الجدول المحوري أو الجدول المرتبط باستخدام Aspose.Cells for JavaScript via C++.
keywords: Aspose.Cells JavaScript عبر C++، تحديث العارض في JavaScript، كيفية تغيير العارض في JavaScript، كيفية تصفية الجدول المحوري بواسطة العارض في JavaScript، Slicer selectItems، Slicer clearFilter، Slicer unselectItems.
---

## **سيناريوهات الاستخدام المحتملة**
يعني تحديث العارض تصفية بيانات الجدول المحوري أو الجدول المرتبط بالعارض. عندما تقوم بتحديد عناصر العارض أو إلغاء تحديدها في Microsoft Excel، يُعاد حساب الجدول المحوري أو الجدول المرتبط وفقًا لذلك. باستخدام Aspose.Cells for JavaScript via C++، لا تحتاج إلى المرور على عناصر ذاكرة التخزين المؤقت للعارض وتحديث العارض يدويًا — تقوم طريقة [**Slicer.selectItems(labels, append)**](https://reference.aspose.com/cells/javascript-cpp/slicer/) بتحديث العارض وإعادة حساب الجدول المحوري أو الجدول المرتبط مباشرةً من عناصر التصفية:
- `Slicer.selectItems(labels, append)` — تحدد التسميات المطلوبة وتعيد حساب الجدول المحوري أو الجدول المرتبط. عندما تكون قيمة `append` هي `true`، يتم الاحتفاظ بالتسميات المحددة في الأصل وتُضاف التسميات المطلوبة إلى التحديد؛ وعندما تكون قيمة `append` هي `false`، يتم مسح جميع التحديدات الأصلية وتبقى التسميات المطلوبة فقط محددة.
- `Slicer.unselectItems(labels)` — تلغي تحديد جزء من العناصر المحددة حاليًا.
- `Slicer.clearFilter()` — تزيل التصفية وتحدد جميع العناصر.

{{% alert color="primary" %}}
بدءًا من Aspose.Cells for JavaScript via C++ 26.10، أصبحت خاصية `SlicerCacheItem.selected` للقراءة فقط ولم يعد تعيين قيمتها مدعومًا. استخدم الطرق `Slicer.selectItems` و`Slicer.unselectItems` و`Slicer.clearFilter` بدلاً من تعيين `SlicerCacheItem.selected` عنصرًا بعنصر.
{{% /alert %}}

## **كيفية تحديث العارض**
يقوم الكود النموذجي التالي بتحميل [ملف Excel النموذجي](67338475.xlsx) الذي يحتوي على عارض موجود مرتبط بجدول محوري. يحدد عناصر "Blue" و"Pink" فقط من العارض باستخدام `Slicer.selectItems(labels, false)` — يُعاد حساب الجدول المحوري مباشرةً من عناصر التصفية دون استدعاء `Slicer.refresh()` يدويًا. ثم يحفظ المصنف كـ [ملف Excel الناتج](67338476.xlsx). تُظهر لقطة الشاشة التالية تأثير الكود النموذجي على ملف Excel النموذجي. كما يمكنك أن ترى في لقطة الشاشة، يعرض الجدول المحوري العناصر المصفّاة فقط.

## **الكود النموذجي**

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
        const { Workbook, SaveFormat } = AsposeCells;

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

            // Select only "Blue" and "Pink"; the linked pivot table or table
            // is recalculated directly from the filter items
            slicer.selectItems(["Blue", "Pink"], false);

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

احتفظ بالتسميات المحددة حاليًا وحدد عناصر إضافية:

```javascript
// Keep the current selection and add "Red" to it.
slicer.selectItems(["Red"], true);
```

ألغِ تحديد جزء من العناصر المحددة:

```javascript
// Remove "Pink" from the current selection.
slicer.unselectItems(["Pink"]);
```

أزل التصفية (حدد جميع العناصر):

```javascript
// Clear the filter; all slicer items become selected again.
slicer.clearFilter();
```

{{< app/cells/assistant language="javascript-cpp" >}}