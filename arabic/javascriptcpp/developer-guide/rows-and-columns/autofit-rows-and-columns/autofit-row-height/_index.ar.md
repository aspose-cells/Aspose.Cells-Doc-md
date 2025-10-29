---
title: التلقائي لضبط ارتفاع الصف عند تحميل الملف باستخدام جافا سكريبت عبر C++
linktitle: تكييف ارتفاع الصف تلقائياً عند تحميل الملف
type: docs
weight: 120
url: /ar/javascript-cpp/autofit-row-height/
description: تعلم كيفية ملاءمة الصفوف التي لا يتغير ارتفاعها عند تحميل ملف باستخدام Aspose.Cells for JavaScript عبر C++.
keywords: التلقائي لضبط ارتفاع الصف عند تحميل الملف جافا سكريبت عبر C++، لضبط ارتفاع الصف تلقائيًا عند فتح ملف Excel جافا سكريبت عبر C++ 
---

## **سيناريوهات الاستخدام المحتملة**
ارتفاع الصف يتطابق تلقائيًا مع حجم الخط للمحتوى، ولكن عند عدم تطابق ارتفاع الصف المؤقت مع ارتفاع المحتوى في الملف، سيقوم MS Excel بضبط ارتفاع الصف تلقائيًا عند تحميل الملف، في حين أن Aspose.Cells for JavaScript عبر C++ لن يقوم بضبطه تلقائيًا لتحسين الأداء. إذا كنت بحاجة لاستخدام برنامج Aspose.Cells لمطابقة ارتفاعات الخط تلقائيًا عند تحميل الملفات، يمكنك تحقيق ذلك من خلال المعامل [autoFitterOptions(AutoFitterOptions)](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#autoFitterOptions-autofitteroptions-) في رمزك.

يرجى الرجوع إلى صورة البيانات التالية. نلاحظ أن ارتفاع الصف المخزن في السطر 11 هو 15، لكن إكسل قام بضبط ارتفاع الصف تلقائيًا عند تحميل الملف.
<br>
<img src="1.png" width=70% />

## **ضبط ارتفاع الصف باستخدام Aspose.Cells for JavaScript عبر C++**
إذا حملت الملف مباشرة وقمت بحفظه كملف PDF، لن يتم عرض البيانات بالكامل في PDF لأن ارتفاع الخط المخزن هو فقط 15.
<br>
<img src="2.png" width=70% />
<br>
إذا قمت بضبط المعامل [autoFitterOptions(AutoFitterOptions)]](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#autoFitterOptions-autofitteroptions-) إلى true عند تحميل الملف، فإن Aspose.Cells سيقوم تلقائيًا بضبط ارتفاع الصف. يمكن لارتفاع السطر المعدل تلبية متطلبات عرض النص بشكل فعال.
<br>
<img src="3.png" width=70% />

## **كود عينة جافا سكريبت**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells LoadOptions & AutoFitter Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <div>
            <a id="downloadLink1" style="display: none;">Download out.pdf</a>
        </div>
        <div>
            <a id="downloadLink2" style="display: none;">Download out2.pdf</a>
        </div>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, AutoFitterOptions } = AsposeCells;

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
            const downloadLink1 = document.getElementById('downloadLink1');
            const downloadLink2 = document.getElementById('downloadLink2');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const data = new Uint8Array(arrayBuffer);

            // Load workbook and save as out.pdf
            const workbook = new Workbook(data);
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            downloadLink1.href = URL.createObjectURL(blob);
            downloadLink1.download = 'out.pdf';
            downloadLink1.style.display = 'inline';
            downloadLink1.textContent = 'Download out.pdf';

            // Prepare LoadOptions with AutoFitterOptions and onlyAuto = true
            const loadOptions = new LoadOptions();
            loadOptions.autoFitterOptions = new AutoFitterOptions();
            loadOptions.autoFitterOptions.onlyAuto = true;

            // Load workbook with loadOptions and save as out2.pdf
            const book = new Workbook(data, loadOptions);
            const outputData2 = book.save(SaveFormat.Pdf);
            const blob2 = new Blob([outputData2], { type: 'application/pdf' });
            downloadLink2.href = URL.createObjectURL(blob2);
            downloadLink2.download = 'out2.pdf';
            downloadLink2.style.display = 'inline';
            downloadLink2.textContent = 'Download out2.pdf';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download links to get the generated PDF files.</p>';
        });
    </script>
</html>
```
