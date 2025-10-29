---
title: استخدام خيارات فحص الأخطاء مع جافا سكريبت عبر ++C
linktitle: استخدام خيارات التحقق من الأخطاء
type: docs
weight: 140
url: /ar/javascript-cpp/use-error-checking-options/
description: تعلم كيفية استخدام خيارات فحص الأخطاء في أوراق عمل إكسل برمجياً باستخدام Aspose.Cells for JavaScript عبر ++C.
keywords: تخزين الرقم كنص في إكسل باستخدام جافا سكريبت عبر ++C، فحص خيارات إكسل للأخطاء جافا سكريبت عبر ++C
---

{{% alert color="primary" %}}  
يسمح Microsoft Excel للمستخدمين بتعريف خيارات وقواعد التحقق من الأخطاء. يرى المستخدمون في كثير من الأحيان التحقق من الأخطاء عند إنشاء الصيغ، حيث يوضح مثلث صغير في الزاوية العلوية اليمنى للخلية عند وجود مشكلة في الخلية. يوفر Excel معلومات تساعد المستخدمين على تصحيح المشاكل الشائعة.  
{{% /alert %}}  

## **أنواع الأخطاء**  

الأخطاء التي تعني أن الصيغة لا يمكنها إرجاع نتيجة - مثل قسمة رقم على صفر - تتطلب اهتمامًا فوريًا وتعرض قيمة خطأ في الخلية. النقر على المثلث الأخضر يعرض علامة تعجب، والنقر عليها يفتح قائمة الخيارات.  

يمكن حل الخطأ باستخدام الخيارات أو تجاهله. تجاهل الخطأ يعني أن الخطأ لن يظهر في فحوصات الأخطاء المستقبلية.  

يوفر Aspose.Cells ميزات فحص الأخطاء. تدير فئة [**ErrorCheckOption**](https://reference.aspose.com/cells/javascript-cpp/errorcheckoption) أنواع مختلفة من فحوصات الأخطاء، على سبيل المثال، الأرقام المخزنة كنص، أخطاء حساب الصيغة، وأخطاء التحقق من الصحة. استخدم تعداد [**ErrorCheckType**](https://reference.aspose.com/cells/javascript-cpp/errorchecktype) لضبط فحص الأخطاء المطلوب.  

## **الأرقام المخزنة كنص**  

في بعض الأحيان، قد تكون الأرقام مهيأة ومخزنة في الخلايا كنص. يمكن أن يسبب هذا مشاكل في الحسابات أو إنتاج ترتيبات فرز مربكة. الأرقام التي تم تهيئتها كنص تكون محاذية إلى اليسار بدلاً من اليمين في الخلية. إذا لم تُعَد الصيغة التي يجب أن تقوم بعملية رياضية على الخلايا قيمة، فحقق محاذاة في الخلايا التي تشير إليها الصيغة - قد تكون بعض أو كل تلك الخلايا أرقامًا تم تهيئتها كنص.  

يمكنك استخدام خيارات التحقق من الأخطاء لتحويل الأرقام المخزنة كنص إلى أرقام حقيقية بسرعة. في Microsoft Excel 2003:  

1. على قائمة **الأدوات**، انقر على **خيارات**.  
1. حدد علامة التبويب التحقق من الأخطاء.  
   خيار **العدد المخزن كنص** يتم التحقق منه بشكل افتراضي.  
1. قم بتعطيله.  

يوضح الكود المصدري العينة التالي كيفية تعطيل خيار التحقق من الأخطاء للأرقام المخزنة كنص لورقة العمل في ملف XLS القالب باستخدام واجهات برمجة التطبيقات Aspose.Cells.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Error Check Options</title>
    </head>
    <body>
        <h1>Error Check Options Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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

            // Instantiate a Workbook by reading the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Get the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Instantiate the error checking options
            const opts = sheet.errorCheckOptions;

            const index = opts.add();
            const opt = opts.get(index);
            // Disable the numbers stored as text option
            // Converted from opt.setErrorCheck(type, value) to a property-style assignment
            opt.errorCheck = opt.errorCheck || {};
            opt.errorCheck[AsposeCells.ErrorCheckType.NumberStoredAsText] = false;
            // Set the range
            opt.addRange(AsposeCells.CellArea.createCellArea(0, 0, 1000, 50));

            // Save the Excel file and prepare download
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'out_test.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
