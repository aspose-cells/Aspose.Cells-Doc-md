---
title: C++を使用してAspose.Cells for JavaScriptによるActiveXコントロールを追加
linktitle: Aspose.Cells を使用して ActiveX コントロールを追加する
type: docs
weight: 260
url: /ja/javascript-cpp/add-activex-controls-using-aspose-cells/
description: C++を使用してAspose.Cells for JavaScript経由でシートにActiveXコントロールを追加する方法を学びます。 
---

{{% alert color="primary" %}}

Aspose.Cellsを使用して[**ShapeCollection.addActiveXControl(ControlType, number, number, number, number, number, number)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addActiveXControl-controltype-number-number-number-number-number-number-)メソッドでActiveXコントロールを追加できます。このメソッドは、ワークシート内に追加するActiveXコントロールの種類を指定するパラメータ[**ControlType**](https://reference.aspose.com/cells/javascript-cpp/controltype/)を取ります。値は以下の通りです。

- ControlType.CheckBox
- ControlType.ComboBox
- ControlType.CommandButton
- ControlType.Image
- ControlType.Label
- ControlType.ListBox
- ControlType.RadioButton
- ControlType.ScrollBar
- ControlType.SpinButton
- ControlType.TextBox
- ControlType.ToggleButton
- ControlType.Unknown

ActiveXコントロールをシェイプコレクション内に追加したら、[**Shape.activeXControl**](https://reference.aspose.com/cells/javascript-cpp/shape/#activeXControl--)プロパティを介してActiveXコントロールオブジェクトにアクセスでき、その後さまざまなプロパティを設定できます。

{{% /alert %}}

Aspose.Cellsを使用してToggle Button ActiveXコントロールを追加するサンプルコードは、次のとおりです。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add ActiveX Control</title>
    </head>
    <body>
        <h1>Add ActiveX Control Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ControlType, Utils } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");

            document.getElementById('runExample').addEventListener('click', async () => {
                // Create workbook object (empty workbook)
                const wb = new Workbook();

                // Access first worksheet
                const sheet = wb.worksheets.get(0);

                // Add Toggle Button ActiveX Control inside the Shape Collection
                const s = sheet.shapes.addActiveXControl(ControlType.ToggleButton, 4, 0, 4, 0, 100, 30);

                // Access the ActiveX control object and set its linked cell property
                const c = s.activeXControl;
                c.linkedCell = "A1";

                // Save the workbook in xlsx format and provide download link
                const outputData = wb.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = 'AddActiveXControls_out.xlsx';
                downloadLink.style.display = 'block';
                downloadLink.textContent = 'Download Excel File';

                document.getElementById('result').innerHTML = '<p style="color: green;">ActiveX control added successfully! Click the download link to get the modified file.</p>';
            });
        });
    </script>
</html>
```
