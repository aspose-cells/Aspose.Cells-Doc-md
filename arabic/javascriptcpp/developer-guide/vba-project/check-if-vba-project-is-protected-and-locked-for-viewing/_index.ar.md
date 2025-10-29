---
title: التحقق مما إذا كان مشروع VBA محميًا ومقفلاً للمراجعة باستخدام JavaScript عبر C++
linktitle: التحقق مما إذا كان مشروع VBA محميًا ومقفلا للعرض
type: docs
weight: 30
url: /ar/javascript-cpp/check-if-vba-project-is-protected-and-locked-for-viewing/
description: تعلم كيفية التحقق مما إذا كان مشروع VBA في ملف إكسل محميًا ومقفلًا للمراجعة باستخدام Aspose.Cells for JavaScript عبر C++.
---

## التحقق مما إذا كان مشروع VBA محميًا ومقفلًا للمراجعة في JavaScript عبر C++

يسمح Aspose.Cells بالتحقق مما إذا كان مشروع VBA لملف Excel محميًا ومقفلًا للمراجعة. لهذا، يوفر API الخاصية [**VbaProject.islockedForViewing**](https://reference.aspose.com/cells/javascript-cpp/vbaproject/#islockedForViewing--). إذا كانت مغلقة للمراجعة، فإن الخاصية [**VbaProject.islockedForViewing**](https://reference.aspose.com/cells/javascript-cpp/vbaproject/#islockedForViewing--) تُرجع **true**.

## **الكود المثالي**

 يحمل نموذج الكود التالي ملف Excel النموذجي ([ملف Excel النموذجي](43352065.xlsm)) ويتحقق مما إذا كان مشروع VBA (برمجة Visual Basic للتطبيقات) الخاص بملف Excel محميًا ومغلقًا للمشاهدة. يرجى مراجعة خرج وحدة التحكم للمرجعية.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Check VBA Project Protection Example</title>
    </head>
    <body>
        <h1>Check if VBA Project is Protected</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsm,.xlsb,.csv" />
        <button id="runExample">Check VBA Protection</button>
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file (.xlsm) to check.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the VBA project of the workbook.
            const vbaProject = workbook.vbaProject;

            // Whether "Lock project for viewing" is true or not.
            const isLocked = vbaProject ? vbaProject.islockedForViewing : null;

            if (isLocked === null) {
                resultDiv.innerHTML = '<p style="color: orange;">The workbook does not contain a VBA project.</p>';
            } else {
                resultDiv.innerHTML = `<p>Is VBA Project Locked for Viewing: <strong>${isLocked}</strong></p>`;
                console.log("Is VBA Project Locked for Viewing: " + isLocked);
            }
        });
    </script>
</html>
```

## **مخرجات الوحدة**

هذا هو مخرج الكونسول للكود العيني أعلاه عند تنفيذه مع [ملف Excel عيني](43352065.xlsm) المقدم.

{{< highlight java >}}

Is VBA Project Locked for Viewing: True

{{< /highlight >}}
