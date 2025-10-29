---
title: اكتشف ما إذا كان مشروع VBA محميًا باستخدام جافا سكريبت عبر C++
linktitle: اكتشاف ما إذا كان المشروع VBA محميًا
type: docs
weight: 20
url: /ar/javascript-cpp/find-out-if-vba-project-is-protected/
---

## **اكتشف ما إذا كان مشروع VBA محميًا في جافا سكريبت**

يمكنك معرفة ما إذا كان مشروع VBA (تطبيقات Visual Basic) لملف إكسل الخاص بك محميًا أم لا باستخدام Aspose.Cells property [**VbaProject.isProtected()**](https://reference.aspose.com/cells/javascript-cpp/vbaproject/#isProtected--).

## **الكود المثالي**

يقوم الرمز العملي التالي بإنشاء دفتر عمل ثم يتحقق مما إذا كان مشروع VBA محميًا أم لا. ثم يقوم بحماية مشروع VBA ويعيد التحقق مما إذا كان محميًا أم لا. يرجى مراجعة الناتج في وحدة التحكم كمرجع. قبل الحماية، يعيد [**VbaProject.isProtected()**](https://reference.aspose.com/cells/javascript-cpp/vbaproject/#isProtected--) القيمة **خطأ** ولكن بعد الحماية، يعيد القيمة **صحيح**.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Protect VBA Project Example</title>
    </head>
    <body>
        <h1>Protect VBA Project Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsm" />
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
            let workbook;

            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                // Create a new workbook if no file is provided
                workbook = new Workbook();
            }

            // Access the VBA project of the workbook.
            const vbaProj = workbook.vbaProject;

            // Find out if VBA Project is Protected using isProtected method.
            const beforeProtected = vbaProj.isProtected();
            console.log("IsProtected - Before Protecting VBA Project: " + beforeProtected);

            // Protect the VBA project.
            vbaProj.protect(true, "11");

            // Find out if VBA Project is Protected using isProtected method.
            const afterProtected = vbaProj.isProtected();
            console.log("IsProtected - After Protecting VBA Project: " + afterProtected);

            // Save the modified workbook as XLSM to preserve VBA project
            const outputData = workbook.save(SaveFormat.Xlsm);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'vba_protected.xlsm';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Protected Workbook';

            document.getElementById('result').innerHTML = `
                <p style="color: green;">Operation completed successfully!</p>
                <p>IsProtected before: ${beforeProtected}</p>
                <p>IsProtected after: ${afterProtected}</p>
            `;
        });
    </script>
</html>
```

## **مخرجات الوحدة**

هذا هو إخراج المجموعة الخرجية للرمز العيني أعلاه للمرجع.

{{< highlight java >}}

IsProtected - Before Protecting VBA Project: False

IsProtected - After Protecting VBA Project: True

{{< /highlight >}}
