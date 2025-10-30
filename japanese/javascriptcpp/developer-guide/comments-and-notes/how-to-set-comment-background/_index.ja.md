---
title: JavaScriptを介してC++でExcelのコメントの背景を変更する方法
linktitle: コメント背景
type: docs
weight: 190
url: /ja/javascript-cpp/how-to-set-comment-background/
description: Aspose.Cells for JavaスクリプトをC++を使い、コメントの色を変更したり、コメント内に画像や写真を挿入する方法
keywords: C++を使ったJavaScriptによるExcelコメント背景の色付けと画像挿入
---

{{% alert color="primary" %}}
セルにコメントを追加してメモやレビューの質問、値の由来など情報を記録します。複数人が異なる時間にドキュメントを議論やレビューを行う場合、コメントは非常に重要です。コメントごとに背景色を設定することは可能ですが、多数のドキュメントやコメントを処理する場合、手作業は大変です。幸い、[**Aspose.Cells**](https://products.aspose.com/cells/javascript-cpp/) はこれをコードで行うためのAPIを提供しています。
{{% /alert %}}

## **Excel でコメントの色を変更する方法**

コメントのデフォルト背景色が不要な場合は、お好きな色に置き換えることもできます。Excelのコメントボックスの背景色を変更するにはどうすればよいですか？

以下のコードは、[**Aspose.Cells**](https://products.aspose.com/cells/javascript-cpp/) を使用して自分の選択したコメントに好きな背景色を追加する方法を案内します。

こちらに[サンプルファイル](exmaple.xlsx)を用意しました。このファイルは、以下のコードでWorkbookオブジェクトを初期化するために使われます。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Change Comment Background Color Example</title>
    </head>
    <body>
        <h1>Change Comment Background Color Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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

            // Initialize a new workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Accessing the newly added comment
            const comment = workbook.worksheets.get(0).comments.get(0);

            // change background color
            const shape = comment.commentShape;
            shape.fill.solidFill.color = AsposeCells.Color.Red;

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'result.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Comment background color changed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

上記のコードを実行すると、[出力ファイル](result.xlsx) が生成されます。

## **Excel でコメントに画像を挿入する方法**

Microsoft Excelは、スプレッドシートの外観と感触を大きくカスタマイズ可能です。コメントに背景画像を追加することも可能です。背景画像の追加は、見た目の工夫やブランディング強化に役立ちます。

以下のサンプルコードは、[**Aspose.Cells**](https://products.aspose.com/cells/javascript-cpp/) APIを使用して、好きな背景色を持つコメントを作成し、セルA1に追加する方法を示しています。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Add Comment with Picture Example</h1>
        <p>
            Select an existing Excel file (optional) and an image file to attach to a comment in cell A1.
        </p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <br/><br/>
        <label for="imageInput">Select image to insert in comment (required):</label>
        <input type="file" id="imageInput" accept="image/*" />
        <br/><br/>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

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
            const imageInput = document.getElementById('imageInput');
            const resultDiv = document.getElementById('result');

            if (!imageInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an image file to insert into the comment.</p>';
                return;
            }

            // Instantiate or load Workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Get comments collection for the first sheet
            const comments = worksheet.comments;

            // Add a comment to cell A1 (row 0, column 0)
            const commentIndex = comments.add(0, 0);
            const comment = comments.get(commentIndex);

            // Set comment text and font name (converted from setters to properties)
            comment.note = "First note.";
            comment.font.name = "Times New Roman";

            // Load the selected image file and set it to the comment's shape fill imageData
            const imageFile = imageInput.files[0];
            const imgArrayBuffer = await imageFile.arrayBuffer();
            const imageData = new Uint8Array(imgArrayBuffer);

            comment.commentShape.fill.imageData = imageData;

            // Save the workbook to a blob and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'commentwithpicture1.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Comment with picture added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</body>
</html>
```
