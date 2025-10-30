---
title: JavaScriptを使用してActiveX ComboBoxコントロールを更新する C++
linktitle: ActiveX ComboBoxコントロールを更新
type: docs
weight: 170
url: /ja/javascript-cpp/update-activex-combobox-control/
description: Aspose.Cells for JavaScriptを使用してActiveX ComboBoxコントロールの値を読み書きする方法を学びます。 
---

## **可能な使用シナリオ**
 Aspose.Cells for JavaScriptを通じてActiveX ComboBoxコントロールの値を読み書きできます。 [Shape.activeXControl](https://reference.aspose.com/cells/javascript-cpp/shape/#activeXControl--) プロパティを介してActiveXコントロールにアクセスし、 [ActiveXControlBase.type](https://reference.aspose.com/cells/javascript-cpp/activexcontrolbase/#type--) プロパティでタイプを確認してください。これにより [ControlType.ComboBox](https://reference.aspose.com/cells/javascript-cpp/controltype/) 戻り、[ComboBoxActiveXControl](https://reference.aspose.com/cells/javascript-cpp/comboboxactivexcontrol/) オブジェクトにキャストしてさまざまなプロパティを読み取ったり修正したりできます。

以下のサンプルコードで使用される[サンプルExcelファイル](5115124.xlsx)をダウンロードしてください。
## **ActiveX ComboBoxコントロールを更新**
以下のスクリーンショットは、[サンプルExcelファイル](5115124.xlsx)に対するサンプルコードの効果を示しています。見るとおり、ActiveX ComboBoxの値が"これはコンボボックスコントロールです"に更新されています。

|![todo:image_alt_text](update-activex-combobox-control_1.png)|
| :- |
## **サンプルコード**
次のサンプルコードでは、[サンプルExcelファイル](5115124.xlsx)内のActiveX ComboBoxコントロールの値を更新します。

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
