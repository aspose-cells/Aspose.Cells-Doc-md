---
title: تحديث عنصر تحكم ComboBox ActiveX باستخدام JavaScript عبر C++
linktitle: تحديث عنصر التحكم ActiveX ComboBox
type: docs
weight: 170
url: /ar/javascript-cpp/update-activex-combobox-control/
description: تعلم كيفية قراءة وكتابة قيم عنصر تحكم ComboBox ActiveX باستخدام Aspose.Cells for JavaScript عبر C++،. 
---

## **سيناريوهات الاستخدام المحتملة**
 يمكنك قراءة أو كتابة قيم عنصر تحكم ComboBox ActiveX باستخدام Aspose.Cells for JavaScript عبر C++. يرجى الوصول إلى عنصر التحكم ActiveX عبر الخاصية [Shape.activeXControl](https://reference.aspose.com/cells/javascript-cpp/shape/#activeXControl--) والتحقق من نوعه عبر الخاصية [ActiveXControlBase.type](https://reference.aspose.com/cells/javascript-cpp/activexcontrolbase/#type--), يجب أن يرجع قيمة [ControlType.ComboBox](https://reference.aspose.com/cells/javascript-cpp/controltype/) ثم تحويل النوع إلى كائن [ComboBoxActiveXControl](https://reference.aspose.com/cells/javascript-cpp/comboboxactivexcontrol/) وقراءة أو تعديل خصائصه المختلفة.

يرجىتنزيل[ملف الإكسل العيني](5115124.xlsx) المستخدمفيالكود العينيالتالي.
## **تحديث عنصر تحكم ActiveX ComboBox**
الصورة التي تلي تظهر تأثير كود العينة على [ملف الإكسل عينة](5115124.xlsx). كما يمكنك رؤية أن قيمة عنصر التحكم ComboBox في ActiveX تم تحديثها إلى "هذا عنصر التحكم في مربع القائمة"

|![todo:image_alt_text](update-activex-combobox-control_1.png)|
| :- |
## **الكود المثالي**
تحديث قيمة عنصر التحكم في مربع القائمة ActiveX داخل [ملف الإكسل عينة](5115124.xlsx).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Update ActiveX ComboBox</title>
    </head>
    <body>
        <h1>Update ActiveX ComboBox in Workbook</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsm" />
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

            // Instantiate a Workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet and first shape
            const worksheet = workbook.worksheets.get(0);
            const shape = worksheet.shapes.get(0);

            // Access ActiveX ComboBox Control and update its value
            if (shape.activeXControl != null) {
                const c = shape.activeXControl;

                if (c instanceof AsposeCells.ComboBoxActiveXControl) {
                    // Type cast ActiveXControl into ComboBoxActiveXControl and change its value
                    const comboBoxActiveX = new AsposeCells.ComboBoxActiveXControl(c);
                    comboBoxActiveX.value = "This is combo box control with updated value.";
                }
            }

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'OutputFile_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
