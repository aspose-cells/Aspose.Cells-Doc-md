---
title: JavaScriptを用いて行または列の固定解除を行う（C++経由）
linktitle: ペインの固定解除
type: docs
weight: 190
url: /ja/javascript-cpp/unfreeze-rows-or-columns-of-excel-worksheet
description: この記事では、JavaScript APIをC++とともに使用して、Excelワークシートの行、列、またはウィンドウのフリーズ解除をプログラムで行う方法を学びます。
keywords: ウィンドウの固定解除、行の固定解除、列の固定解除、JavaScriptをC++経由でのウィンドウの固定解除。
---

## **紹介**

この記事では、行、列、ペインのアンフリーズ方法を学びます。Excelファイルのシートが固定されている場合、シートをアンフリーズしたり、固定された行や列、ペインを調整したりしたいことがあります。


## **Excelで**

1. 表示タブ > 固定ウィンドウ > 固定ウィンドウの解除 をクリックします。

**![Excel でのペインの固定解除](Unfreeze-Panes.png)**




## **C++を使用してAspose.Cells for Javaスクリプトで行、列、またはペインを固定解除**
C++を使用してAspose.Cells for Javaスクリプトで行、列、またはペインを固定解除するのは簡単です。[**Worksheet.unFreezePanes()**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#unFreezePanes--)メソッドを使用してペインの固定解除を行ってください。

1. 凍結したファイルを開くためにワークブックを作成します。
2. Worksheet.unFreezePanes()メソッドを使用してペインの固定解除。
3. ファイルを保存します。

```html
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>Aspose.Cells Example - Unfreeze Panes</title>
    </head>
    <body>
        <h1>Unfreeze Panes Example</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the first worksheet and unfreezing panes
            const worksheet = workbook.worksheets.get(0);
            worksheet.unFreezePanes();

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Unfrozen.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Unfrozen Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Panes unfrozen successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

添付 [サンプルソースの Excel ファイル](Frozen.xlsx) です。
