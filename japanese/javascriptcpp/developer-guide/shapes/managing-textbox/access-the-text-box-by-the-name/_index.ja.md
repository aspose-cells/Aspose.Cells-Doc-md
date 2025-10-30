---
title: JavaScriptを使用してC++経由で名前によるテキストボックスにアクセスする
linktitle: 名前でテキストボックスにアクセス
type: docs
weight: 230
url: /ja/javascript-cpp/access-the-text-box-by-the-name/
description: Aspose.Cells for JavaScriptを使用してC++経由でコレクションから名前でテキストボックスにアクセスする方法を学ぶ。 
---

## 名前でテキストボックスにアクセスする

以前は、テキストボックスは[**Worksheet.textBoxes**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#textBoxes--)コレクションのインデックスでアクセスされていましたが、現在はこのコレクションから名前でアクセスすることもできます。これは、名前をすでに知っている場合に便利で迅速な方法です。

次のサンプルコードはまずテキストボックスを作成し、テキストと名前を割り当てます。次に、その名前で同じテキストボックスにアクセスし、そのテキストを出力します。

### 名前でテキストボックスにアクセスするJavaScriptコード

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells TextBox Example</title>
    </head>
    <body>
        <h1>TextBox Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const sheet = workbook.worksheets.get(0);

            const idx = sheet.textBoxes.add(10, 10, 10, 10);

            const tb1 = sheet.textBoxes.get(idx);
            tb1.name = "MyTextBox";
            tb1.text = "This is MyTextBox";

            const tb2 = sheet.textBoxes.get("MyTextBox");

            console.log(tb2.text);

            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'sample.modified.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = `<p style="color: green;">TextBox added. Text from named TextBox: ${tb2.text}</p>`;
        });
    </script>
</html>
```

### サンプルコードによって生成されたコンソール出力



{{< highlight javascript >}}
This is MyTextBox
{{< /highlight >}}
