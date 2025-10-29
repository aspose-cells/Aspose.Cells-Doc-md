---
title: Обновите элемент управления ComboBox ActiveX с помощью JavaScript через C++
linktitle: Обновить элемент управления ActiveX ComboBox
type: docs
weight: 170
url: /ru/javascript-cpp/update-activex-combobox-control/
description: Узнайте, как читать и записывать значения элемента управления ActiveX ComboBox с помощью Aspose.Cells for JavaScript через C++. 
---

## **Возможные сценарии использования**
Вы можете читать или записывать значения элемента управления ActiveX ComboBox с помощью Aspose.Cells for JavaScript через C++. Получите доступ к элементу управления ActiveX через свойство [Shape.activeXControl](https://reference.aspose.com/cells/javascript-cpp/shape/#activeXControl--) и проверьте его тип через свойство [ActiveXControlBase.type](https://reference.aspose.com/cells/javascript-cpp/activexcontrolbase/#type--), оно должно возвращать значение [ControlType.ComboBox](https://reference.aspose.com/cells/javascript-cpp/controltype/), затем приведение к типу [ComboBoxActiveXControl](https://reference.aspose.com/cells/javascript-cpp/comboboxactivexcontrol/) и чтение или изменение его различных свойств.

Пожалуйста, загрузите [образец файла Excel](5115124.xlsx), используемый в следующем примере кода.
## **Обновление элемента управления ComboBox ActiveX**
На следующем скриншоте показан эффект примера кода на [образец файла Excel](5115124.xlsx). Как видно, значение элемента управления ActiveX ComboBox было обновлено на "This is combo box control".

|![todo:image_alt_text](update-activex-combobox-control_1.png)|
| :- |
## **Образец кода**
Следующий образец кода обновляет значение элемента управления ActiveX ComboBox, находящегося внутри [образца файла Excel](5115124.xlsx).

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
