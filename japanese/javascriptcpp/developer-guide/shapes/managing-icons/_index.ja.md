---
title: JavaScriptを使ったワークシートにアイコンを追加（C++経由）
linktitle: アイコンを管理する
type: docs
weight: 100
url: /ja/javascript-cpp/insert-svg-to-excel/
---

## C++経由のAspose.Cells for JavaScriptでワークシートにアイコンを追加

Excel ファイルに 'アイコン' を追加する必要がある場合は、このドキュメントが役立ちます。[Aspose.Cells](https://products.aspose.com/cells/) を使用して、Excel ファイルにアイコンを追加する方法について説明します。

挿入アイコン操作に対応する Excel インターフェースは次のとおりです。

![](1.png)

- ワークシートに挿入するアイコンの位置を選択します
- *挿入*->*アイコン* を左クリックします
- 開いたウィンドウで、上図の赤い四角内のアイコンを選択します
- 左クリックで*挿入*を選択すると、Excelファイルに挿入されます。

効果は以下のようになります。

![](2.png)

ここでは、[Aspose.Cells](https://products.aspose.com/cells/)を使ったアイコン挿入を支援するための*サンプルコード*を用意しています。また、必要な[サンプルファイル](sample.xlsx)とアイコン[リソースファイル](icon.zip)もあります。Excelのインターフェースを使用して、[リソースファイル](icon.zip)と同じ表示効果のアイコンを[サンプルファイル](sample.xlsx)に挿入しました。

### JavaScript

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Add Icon to Worksheet Example</h1>
        <p>Select an Excel file and an SVG icon file, then click "Run Example".</p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <input type="file" id="iconInput" accept=".svg" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Color } = AsposeCells;

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
            const iconInput = document.getElementById('iconInput');
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }
            if (!iconInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an SVG icon file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const iconFile = iconInput.files[0];

            const arrayBuffer = await file.arrayBuffer();
            const iconArrayBuffer = await iconFile.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet from the collection
            const sheet = workbook.worksheets.get(0);

            // Add the icon to the worksheet
            const iconBytes = new Uint8Array(iconArrayBuffer);
            sheet.shapes.addIcons(3, 0, 7, 0, 100, 100, iconBytes, null);

            // Set a prompt message
            const c = sheet.cells.get(8, 7);
            c.value = "Insert via Aspose.Cells";
            const s = c.style;
            s.font.color = Color.Blue;
            c.style = s;

            // Save and prepare download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample2.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Icon added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

プロジェクトで上記のコードを実行すると、次の結果が得られます。

![](3.png)
