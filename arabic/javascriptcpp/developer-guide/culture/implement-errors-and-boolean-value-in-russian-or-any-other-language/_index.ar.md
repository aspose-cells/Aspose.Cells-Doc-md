---
title: تنفيذ الأخطاء والقيم البوليانية باللغة الروسية أو أي لغة أخرى باستخدام JavaScript عبر C++
linktitle: تنفيذ الأخطاء وقيمة بوليانية باللغة الروسية أو أي لغة أخرى
type: docs
weight: 40
url: /ar/javascript-cpp/implement-errors-and-boolean-value-in-russian-or-any-other-language/
description: تعلم كيفية تنفيذ القيم الأخطاء والبوليانية بلغات مختلفة باستخدام Aspose.Cells for JavaScript عبر C++. 
---

## **سيناريوهات الاستخدام المحتملة**

 إذا كنت تستخدم Microsoft Excel باللغة الروسية أو أي لغة أخرى، فستعرض الأخطاء والقيم البوليانية وفقًا لهذه اللغة. يمكنك تحقيق سلوك مماثل باستخدام Aspose.Cells for JavaScript عبر C++ عن طريق استخدام الخاصية [**WorkbookSettings.globalizationSettings**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#globalizationSettings--). عليك تجاوز الطرق التالية من فئة [**GlobalizationSettings**](https://reference.aspose.com/cells/javascript-cpp/globalizationsettings).

- [**GlobalizationSettings.errorValueString(string)**](https://reference.aspose.com/cells/javascript-cpp/globalizationsettings/#errorValueString-string-)
- [**GlobalizationSettings.booleanValueString(boolean)**](https://reference.aspose.com/cells/javascript-cpp/globalizationsettings/#booleanValueString-boolean-)

## **تنفيذ الأخطاء والقيمة البوليانية باللغة الروسية أو أي لغة أخرى**

الشيفرة النموذجية التالية توضح كيفية تنفيذ الأخطاء والقيمة البوليانية باللغة الروسية أو أي لغة أخرى. يرجى التحقق من [ملف الإكسل النموذجي](73990159.xlsx) المستخدم في هذا الشيفرة و [PDF الناتج](73990160.pdf) الخاص به. تُظهر اللقطة الفوتوغرافية الفرق بين ملف الإكسل النموذجي والملف الناتج بصيغة PDF للرجوع إليها.

![todo:image_alt_text](implement-errors-and-boolean-value-in-russian-or-any-other-language_1.png)

## **الكود المثالي**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            #downloadLink { display: none; margin-top: 10px; display: inline-block; }
            #result p { margin: 8px 0; }
        </style>
    </head>
    <body>
        <h1>Russian Globalization Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink">Download Result</a>
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

        // Russian Globalization
        class RussianGlobalization extends AsposeCells.GlobalizationSettings {
            errorValueString(err) {
                switch (err.toUpperCase()) {
                    case "#NAME?":
                        return "#RussianName-имя?";
                }
                return "RussianError-ошибка";
            }

            booleanValueString(bv) {
                return bv ? "RussianTrue-правда" : "RussianFalse-ложный";
            }
        }

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Load the source workbook
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Set GlobalizationSettings in Russian Language
            workbook.settings.globalizationSettings = new RussianGlobalization();

            // Calculate the formula
            workbook.calculateFormula();

            // Save the workbook in pdf format
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputRussianGlobalization.pdf';
            downloadLink.style.display = 'inline-block';
            downloadLink.textContent = 'Download PDF File';

            resultDiv.innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the PDF.</p>';
        });
    </script>
</html>
```
