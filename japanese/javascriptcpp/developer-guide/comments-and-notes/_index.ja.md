---
title: コメントとメモの管理（JavaScriptを使ったC++経由）
linktitle: コメントとノート
type: docs
weight: 128
url: /ja/javascript-cpp/comments-and-notes/
description: Aspose.Cells for JavaScript via C++を使ってコメントやメモを挿入および管理します。
keywords: コメントの挿入、メモの挿入（JavaScriptをC++経由）
---

## **紹介**

コメントはセルに追加情報を付加するために使用されます。Aspose.Cells for JavaScript via C++は、セルにコメントを追加するための二つの方法を提供します。最初はデザイナーファイル内で手動でコメントを作成し、これをAspose.Cellsを使ってインポートする方法です。二つ目は、実行時にAspose.Cells APIを使ってコメントを追加する方法です。このトピックでは、Aspose.Cells APIを使ったセルへのコメント追加について説明し、コメントのフォーマットについても解説します。

## **コメントの追加**

[**Comments**](https://reference.aspose.com/cells/javascript-cpp/commentcollection)コレクションの[**CommentCollection.add(number, number)**](https://reference.aspose.com/cells/javascript-cpp/commentcollection/#add-number-number-)メソッドを呼び出してセルにコメントを追加します（[**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet)オブジェクトにカプセル化されています）。新しい[**Comment**](https://reference.aspose.com/cells/javascript-cpp/comment)オブジェクトには、コメントのインデックスを渡して[**Comments**](https://reference.aspose.com/cells/javascript-cpp/commentcollection)コレクションからアクセスします。[**Comment**](https://reference.aspose.com/cells/javascript-cpp/comment)オブジェクトにアクセスした後、[**note**](https://reference.aspose.com/cells/javascript-cpp/comment/#note--)プロパティを使ってコメントメモをカスタマイズします。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Add Comment Example</h1>
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
            // Instantiating a Workbook object
            const workbook = new Workbook();

            // Adding a new worksheet to the Workbook object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding a comment to "F5" cell
            const commentIndex = worksheet.comments.add("F5");

            // Accessing the newly added comment
            const comment = worksheet.comments.get(commentIndex);

            // Setting the comment note
            comment.note = "Hello Aspose!";

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Comment added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **コメントの書式設定**

コメントの高さ、幅、フォント設定を構成することで、コメントの外観を書式設定することも可能です。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Comment</title>
    </head>
    <body>
        <h1>Add Comment Example</h1>
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
            // Creating a new Workbook object
            const workbook = new Workbook();

            // Adding a new worksheet to the Workbook object
            const sheetIndex = workbook.worksheets.add();

            // Obtaining the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding a comment to "F5" cell
            const commentIndex = worksheet.comments.add("F5");

            // Accessing the newly added comment
            const comment = worksheet.comments.get(commentIndex);

            // Setting the comment note
            comment.note = "Hello Aspose!";

            // Setting the font size of a comment to 14
            comment.font.size = 14;

            // Setting the font of a comment to bold
            comment.font.isBold = true;

            // Setting the height of the font to 10
            comment.heightCM = 10;

            // Setting the width of the font to 2
            comment.widthCM = 2;

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and saved. Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **コメントに画像を追加する**

Microsoft Excel 2007では、セルコメントの背景として画像を使用することもできます。Excel 2007では、次の手順を実行することでこれが実現されます。（すでにセルにコメントを追加していることを前提とします。）

1. コメントを含むセルを右クリックします。
1. **表示/非表示**を選択し、コメント内のテキストをクリアします。
1. コメントの境界線をクリックして選択します。
1. **書式**、次に**コメント**を選択します。
1. **色と線**タブで、**色**リストを展開します。
1. **塗りつぶしの効果**をクリックします。
1. **図**タブで、**ピクチャを選択**をクリックします。
1. 画像を探し、選択します。
1. すべてのダイアログが閉じるまで**OK**をクリックします。

Aspose.Cellsもこの機能を提供します。以下は、セル"A1"に画像を背景として設定したコメントを追加し、からXLSXファイルをスクラッチから作成するコードサンプルです。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Comment with Image</title>
    </head>
    <body>
        <h1>Add Comment with Image Example</h1>
        <p>
            Select an existing Excel file to modify (optional). If no file is selected, a new workbook will be created.
        </p>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <p>
            Select an image file to attach to the comment (required):
        </p>
        <input type="file" id="imageInput" accept="image/*" />
        <br/><br/>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

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
            const resultEl = document.getElementById('result');
            resultEl.innerHTML = '';

            const fileInput = document.getElementById('fileInput');
            const imageInput = document.getElementById('imageInput');

            if (!imageInput.files.length) {
                resultEl.innerHTML = '<p style="color: red;">Please select an image file for the comment.</p>';
                return;
            }

            // Load or create workbook
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Get a reference of comments collection with the first sheet
            const comments = workbook.worksheets.get(0).comments;

            // Add a comment to cell A1
            const commentIndex = comments.add(0, 0);
            const comment = comments.get(commentIndex);

            // Set the comment note and font name (converted from set/get to properties)
            comment.note = "First note.";
            comment.font.name = "Times New Roman";

            // Load image file data
            const imgFile = imageInput.files[0];
            const imgArrayBuffer = await imgFile.arrayBuffer();
            const imgUint8 = new Uint8Array(imgArrayBuffer);

            // Set image data to the shape associated with the comment
            comment.commentShape.fill.imageData = imgUint8;

            // Save the workbook to browser-downloadable file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'book1.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultEl.innerHTML = '<p style="color: green;">Comment added with image successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **高度なトピック**
- [コメントのテキスト方向を変更する](/cells/ja/javascript-cpp/change-text-direction-of-the-comment/)
- [コメントのフォント色を変更する方法](/cells/ja/javascript-cpp/how-to-change-the-comment-font-color/)
- [コメントの背景を設定する方法](/cells/ja/javascript-cpp/how-to-set-comment-background/)
- [スレッド化されたコメント](/cells/ja/javascript-cpp/threaded-comments/)
