---
title: 使用 JavaScript 通过 C++ 更新 ActiveX 组合框控件
linktitle: 更新ActiveX组合框控件
type: docs
weight: 170
url: /zh/javascript-cpp/update-activex-combobox-control/
description: 了解如何使用 Aspose.Cells for JavaScript 通过 C++ 读取和写入 ActiveX 组合框控件的值。 
---

## **可能的使用场景**
你可以使用 Aspose.Cells for JavaScript 通过 C++ 读取或写入 ActiveX 组合框控件的值。请通过 [Shape.activeXControl](https://reference.aspose.com/cells/javascript-cpp/shape/#activeXControl--) 属性访问 ActiveX 控件，并通过 [ActiveXControlBase.type](https://reference.aspose.com/cells/javascript-cpp/activexcontrolbase/#type--) 属性检查其类型，应返回 [ControlType.ComboBox](https://reference.aspose.com/cells/javascript-cpp/controltype/) 值，然后将其强制转换成 [ComboBoxActiveXControl](https://reference.aspose.com/cells/javascript-cpp/comboboxactivexcontrol/) 对象，读取或修改其各种属性。

请下载以下示例代码中使用的 [示例 Excel 文件](5115124.xlsx)。
## **更新ActiveX ComboBox控件**
以下截图显示了样本代码对 [样本excel文件](5115124.xlsx) 的效果。正如你所看到的，活动X组合框的值已更新为"This is combo box control"。

|![todo:image_alt_text](update-activex-combobox-control_1.png)|
| :- |
## **示例代码**
以下样本代码更新了 [样本excel文件](5115124.xlsx) 中存在的活动X组合框控件的值。

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
