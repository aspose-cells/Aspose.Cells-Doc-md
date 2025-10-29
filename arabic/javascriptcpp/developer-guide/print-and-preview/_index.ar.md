---
title: معاينة دفتر العمل باستخدام جافاسكريبت عبر C++
linktitle: معاينة دفتر العمل 
type: docs
weight: 70
url: /ar/javascript-cpp/workbook-and-worksheet-preview/
description: يدعم Aspose.Cells طباعة ومعاينة ملفات إكسل بدون تثبيت Microsoft Excel باستخدام جافاسكريبت عبر C++.
---

## **معاينة الطباعة**  

قد توجد حالات يكون فيها من الضروري تحويل ملفات Excel التي تحتوي على ملايين الصفحات إلى PDF أو صور. سيستهلك معالجة مثل هذه الملفات وقتًا وموارد كثيرة. في مثل هذه الحالات، قد تكون ميزة معاينة الطباعة للكتاب وورقة العمل مفيدة. قبل تحويل مثل هذه الملفات، يمكن للمستخدم فحص إجمالي عدد الصفحات ثم اتخاذ قرار بشأن ما إذا كان سيتم تحويل الملف أم لا. يركز هذا المقال على استخدام فصلي [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/) و [**SheetPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/sheetprintingpreview/) لمعرفة الإجمالي الكلي للصفحات.  

يوفر Aspose.Cells ميزة المعاينة المسبقة للطباعة. لهذا، توفر الـ API فصلي [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/) و [**SheetPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/sheetprintingpreview/). لإنشاء معاينة الطباعة للكتاب بأكمله، قم بإنشاء نسخة من فئة [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/) عن طريق تمرير كائنات [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook/) و [**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/) إلى الباني. توفر فئة [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/) طريقة [**evaluatedPageCount**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/#evaluatedPageCount--) التي تُرجع عدد الصفحات في المعاينة المُولدة. مماثلة لفئة [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/)، يُستخدم فئة [**SheetPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/sheetprintingpreview/) لإنشاء معاينة طباعة لورقة عمل محددة. لإنشاء معاينة الطباعة لورقة العمل، قم بإنشاء نسخة من فئة [**SheetPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/sheetprintingpreview/) عن طريق تمرير كائنات [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet/) و [**ImageOrPrintOptions**](https://reference.aspose.com/cells/javascript-cpp/imageorprintoptions/) إلى الباني. توفر فئة [**SheetPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/sheetprintingpreview/) أيضًا طريقة [**evaluatedPageCount**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/#evaluatedPageCount--) التي تُرجع عدد الصفحات في المعاينة المُولدة.  

يوضح مقتطف الشفرة التالي استخدام فصلي [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/workbookprintingpreview/) و [**SheetPrintingPreview**](https://reference.aspose.com/cells/javascript-cpp/sheetprintingpreview/) باستخدام [ملف إكسل النموذجي](94896177.xlsx).  

### **الكود المثالي**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Printing Preview</title>
    </head>
    <body>
        <h1>Printing Preview Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, ImageOrPrintOptions, WorkbookPrintingPreview, SheetPrintingPreview } = AsposeCells;

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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Creating image/print options
            const imgOptions = new ImageOrPrintOptions();

            // Workbook printing preview
            const preview = new WorkbookPrintingPreview(workbook, imgOptions);
            const workbookPageCount = preview.evaluatedPageCount;
            console.log("Workbook page count: " + workbookPageCount);

            // Worksheet printing preview for first worksheet
            const preview2 = new SheetPrintingPreview(workbook.worksheets.get(0), imgOptions);
            const worksheetPageCount = preview2.evaluatedPageCount;
            console.log("Worksheet page count: " + worksheetPageCount);

            document.getElementById('result').innerHTML = `<p>Workbook page count: ${workbookPageCount}</p><p>Worksheet page count: ${worksheetPageCount}</p>`;
        });
    </script>
</html>
```  

يُظهر ما يلي الناتج الذي تم توليده عن طريق تنفيذ الكود أعلاه.  

### **مخرجات الوحدة**  

{{< highlight javascript >}}  
Workbook page count: 1  
Worksheet page count: 1  
{{< /highlight >}}  

## **مواضيع متقدمة**  
- [تكوين الخطوط لعرض جداول البيانات](/cells/ar/javascript-cpp/configuring-fonts-for-rendering-spreadsheets/)  
- [تحويل ورقة العمل إلى صورة - إزالة الفراغات حول البيانات](/cells/ar/javascript-cpp/convert-worksheet-to-image-remove-whitespace-around-data/)  
- [تحويل الورقة العمل إلى صورة والورقة العمل إلى صورة حسب الصفحة](/cells/ar/javascript-cpp/converting-worksheet-to-image-and-worksheet-to-image-by-page/)  
- [تحويل ورقة العمل إلى صورة باستخدام خيارات الصورة أو الطباعة](/cells/ar/javascript-cpp/converting-worksheet-to-image-using-imageorprint-options/)  
- [تصدير مجموعة من الخلايا في ورقة عمل إلى صورة](/cells/ar/javascript-cpp/export-range-of-cells-in-a-worksheet-to-image/)  
- [تصدير ورقة العمل أو الرسم البياني إلى صورة بعرض وارتفاع مطلوبين](/cells/ar/javascript-cpp/export-worksheet-or-chart-into-image-with-desired-width-and-height/)  
- [استخراج الصور من أوراق العمل باستخدام خيارات الصورة أو الطباعة](/cells/ar/javascript-cpp/extract-images-from-worksheets-using-imageorprintoptions/)  
- [إنشاء مصغرة لورقة العمل](/cells/ar/javascript-cpp/generate-thumbnail-of-the-worksheet/)  
- [إخراج صفحة فارغة عند عدم وجود شيء للطباعة](/cells/ar/javascript-cpp/output-blank-page-when-there-is-nothing-to-print/)  
- [إعداد الصفحة وخيارات الطباعة](/cells/ar/javascript-cpp/page-setup-and-printing-options/)  
- [تقديم تسلسل من الصفحات باستخدام خصائص PageIndex وPageCount لخيارات الصورة أو الطباعة](/cells/ar/javascript-cpp/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/)  
- [عرض الورقة العمل إلى سياق رسومي](/cells/ar/javascript-cpp/render-worksheet-to-graphic-context/)  
- [تحديد مجموعة خطوط فردية أو خاصة لتقديم الدفتر](/cells/ar/javascript-cpp/specify-individual-or-private-set-of-fonts-for-workbook-rendering/)
