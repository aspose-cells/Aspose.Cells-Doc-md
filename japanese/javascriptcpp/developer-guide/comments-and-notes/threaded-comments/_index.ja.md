---
title: JavaScriptを介したC++でのスレッド付きコメント
linktitle: スレッド型コメント
type: docs
weight: 140
url: /ja/javascript-cpp/threaded-comments/
description: Aspose.Cells for JavaスクリプトをC++で使用してExcelドキュメントのスレッド付きコメントの追加、閲覧、編集、削除方法を学びます。
---

## **スレッド化されたコメント**

MS Excel 365 では、スレッド型コメントを追加する機能が提供されています。これらのコメントは会話として機能し、ディスカッションに使用できます。新しいコメントにはスレッド型の会話が可能なリプライボックスが付属しています。古いコメントは Excel 365 ではノートと呼ばれます。以下のスクリーンショットは、Excel 365 でスレッド型コメントが開かれたときの表示例です。

![todo:image_alt_text](threaded-comments_1.jpg)

古いバージョンの Excel では、スレッド型コメントは以下のように表示されます。以下の画像は、サンプルファイルを Excel 2016 で開いたものです。

![todo:image_alt_text](threaded-comments_2.jpg)

![todo:image_alt_text](threaded-comments_3.jpg)

Aspose.Cells では、スレッド型コメントの管理機能も提供されています。

## **スレッド型コメントの追加**

### **Excel でスレッド型コメントを追加**

Excel 365 でスレッド型コメントを追加するには、以下の手順に従ってください。

- 方法 1
  - **レビュー** タブをクリック
  - **新しいコメント** ボタンをクリック
  - これにより、アクティブなセルにコメントを入力するためのダイアログが開きます。
  - ![todo:image_alt_text](threaded-comments_4.jpg)
- 方法 2
  - コメントを挿入したいセルを右クリック
  - **新しいコメント** オプションをクリック
  - これにより、アクティブなセルにコメントを入力するためのダイアログが開きます。
  - ![todo:image_alt_text](threaded-comments_5)

### **Aspose.Cells を使用してスレッド型コメントを追加**

Aspose.Cellsは、[**Comments.AddThreadedComment**](https://reference.aspose.com/cells/javascript-cpp/commentcollection/#addthreadedcomment-string-string-ThreadedCommentAuthor-)メソッドを使ってスレッド化コメントを追加します。[**Comments.AddThreadedComment**](https://reference.aspose.com/cells/javascript-cpp/commentcollection/#addthreadedcomment-string-string-ThreadedCommentAuthor-)メソッドは以下の3つのパラメータを受け取ります。

- セル名: コメントを挿入するセルの名前。
- コメントのテキスト: コメントのテキスト。
- [**ThreadedCommentAuthor**](https://reference.aspose.com/cells/javascript-cpp/threadedcommentauthor): コメントの作者

以下のコードサンプルは、[**Comments.AddThreadedComment**](https://reference.aspose.com/cells/javascript-cpp/commentcollection/#addthreadedcomment-string-string-ThreadedCommentAuthor-)メソッドを使用してセルA1にスレッド付きコメントを追加する方法を示しています。参考のために、コードによって生成された[出力Excelファイル](89849859.xlsx)を参照してください。

#### **サンプルコード**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Threaded Comment</title>
    </head>
    <body>
        <h1>Add Threaded Comment Example</h1>
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
            // Create a new workbook
            const workbook = new Workbook();

            // Add Author
            const authorIndex = workbook.worksheets.threadedCommentAuthors.add("Aspose Test", "", "");
            const author = workbook.worksheets.threadedCommentAuthors.get(authorIndex);

            // Add Threaded Comment to cell A1 in the first worksheet
            const worksheet = workbook.worksheets.get(0);
            worksheet.comments.addThreadedComment("A1", "Test Threaded Comment", author);

            // Save the modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'AddThreadedComments_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Threaded comment added successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

## **スレッド化されたコメントを読む**

### **Excelでスレッド化されたコメントを読む**

Excelでスレッド化されたコメントを読むには、単にコメントを含むセル上にマウスを動かすとコメントが表示されます。コメント表示は、次の画像に示すような表示になります。

![todo:image_alt_text](threaded-comments_1.jpg)

### **Aspose.Cellsを使用してスレッド化されたコメントを読む**

Aspose.Cellsは指定された列のスレッド化されたコメントを取得するための[**Comments.threadedComments**](https://reference.aspose.com/cells/javascript-cpp/commentcollection/#threadedComments-string-)メソッドを提供します。[**Comments.threadedComments**](https://reference.aspose.com/cells/javascript-cpp/commentcollection/#threadedComments-string-)メソッドは列名をパラメータとして受け取り、[**ThreadedCommentCollection**](https://reference.aspose.com/cells/javascript-cpp/threadedcommentcollection)を返します。[**ThreadedCommentCollection**](https://reference.aspose.com/cells/javascript-cpp/threadedcommentcollection)を繰り返し処理してコメントを表示できます。

次の例は、[サンプルエクセルファイル](89849861.xlsx)を読み込んで列A1からコメントを読み取ることを示しています。参照のためにコードによって生成されたコンソール出力をご覧ください。

#### **サンプルコード**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Threaded Comments Example</title>
    </head>
    <body>
        <h1>Threaded Comments Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Get Threaded Comments for cell A1
            const threadedComments = worksheet.comments.threadedComments("A1");

            const count = threadedComments.count;
            let html = '<h2>Threaded Comments</h2>';
            if (count === 0) {
                html += '<p>No threaded comments found for A1.</p>';
            } else {
                html += '<ul>';
                for (let i = 0; i < count; i++) {
                    const comment = threadedComments.get(i);
                    const notes = comment.notes;
                    const authorName = comment.author.name;
                    html += `<li><strong>Author:</strong> ${authorName} <br/><strong>Comment:</strong> ${notes}</li>`;
                }
                html += '</ul>';
            }

            resultDiv.innerHTML = html;
        });
    </script>
</html>
```

#### **コンソール出力**

{{< highlight javascript >}}

Comment: Test Threaded Comment

Author: Aspose Test

{{< /highlight >}}

### **スレッド化されたコメントの作成時間を読む**

Aspose.Cellsは、指定された列のスレッド付きコメントを取得するための[**Comments.threadedComments**](https://reference.aspose.com/cells/javascript-cpp/commentcollection/#threadedComments-string-)メソッドを提供します。[**Comments.threadedComments**](https://reference.aspose.com/cells/javascript-cpp/commentcollection/#threadedComments-string-)メソッドは列名をパラメータとして受け入れ、[**ThreadedCommentCollection**](https://reference.aspose.com/cells/javascript-cpp/threadedcommentcollection)を返します。[**ThreadedCommentCollection**](https://reference.aspose.com/cells/javascript-cpp/threadedcommentcollection)を繰り返し、[**ThreadedComment.createdTime**](https://reference.aspose.com/cells/javascript-cpp/threadedcomment/#createdTime--)プロパティを使用できます。

次の例は、[サンプルエクセルファイル](89849861.xlsx)を読み込んでスレッド化されたコメントの作成時間を読み取ることを示しています。参照のためにコードによって生成されたコンソール出力をご覧ください。

#### **サンプルコード**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Threaded Comments Example</title>
    </head>
    <body>
        <h1>Threaded Comments Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');
            const downloadLink = document.getElementById('downloadLink');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            // No try-catch: allow errors to propagate for testing
            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Loads the workbook from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Get Threaded Comments for cell A1
            const threadedComments = worksheet.comments.threadedComments("A1");

            const count = threadedComments.count;

            let html = '<h2>Threaded Comments (Cell A1)</h2>';
            if (count === 0) {
                html += '<p>No threaded comments found in cell A1.</p>';
            } else {
                html += '<ul>';
                for (let i = 0; i < count; i++) {
                    const comment = threadedComments.get(i);
                    const notes = comment.notes;
                    const authorName = comment.author.name;
                    const createdTime = comment.createdTime;

                    console.log("Comment: " + notes);
                    console.log("Author: " + authorName);
                    console.log("Created Time: " + createdTime);

                    html += `<li><strong>Author:</strong> ${authorName} <br/><strong>Created:</strong> ${createdTime} <br/><strong>Comment:</strong> ${notes}</li>`;
                }
                html += '</ul>';
            }

            resultDiv.innerHTML = html;

            // No file modifications or save in this example; hide download link
            downloadLink.style.display = 'none';
        });
    </script>
</html>
```

#### **コンソール出力**

{{< highlight javascript >}}

Comment: Test Threaded Comment

Author: Aspose Test

Created Time: 5/15/2019 12:46:23 PM

{{< /highlight >}}

## **スレッド化されたコメントの編集**

### **Excelでスレッド化されたコメントを編集する**

Excelでスレッド化されたコメントを編集するには、次の画像に示すようにコメントの**編集**リンクをクリックします。

![todo:image_alt_text](threaded-comments_7.jpg)

### **Aspose.Cellsを使用してスレッド化されたコメントを編集する**

Aspose.Cellsは、指定された列のスレッド付きコメントを取得するための[**Comments.threadedComments**](https://reference.aspose.com/cells/javascript-cpp/commentcollection/#threadedComments-string-)メソッドを提供します。[**Comments.threadedComments**](https://reference.aspose.com/cells/javascript-cpp/commentcollection/#threadedComments-string-)メソッドは列名をパラメータとして受け入れ、[**ThreadedCommentCollection**](https://reference.aspose.com/cells/javascript-cpp/threadedcommentcollection)を返します。必要なコメントを[**ThreadedCommentCollection**](https://reference.aspose.com/cells/javascript-cpp/threadedcommentcollection)で更新し、ワークブックを保存できます。

 以下の例は、[サンプルExcelファイル](89849861.xlsx)を読み込み、A1列の最初のスレッド付きコメントを編集し、更新されたコメントを示す[出力Excelファイル](89849862.xlsx)を生成します。参考にしてください。

#### **サンプルコード**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Edit Threaded Comments Example</h1>
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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by opening the Excel file from the file input
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Get Threaded Comment from cell A1
            const comment = worksheet.comments.threadedComments("A1").get(0);

            // Update the threaded comment notes
            comment.notes = "Updated Comment";

            // Save the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'EditThreadedComments.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Edited Excel File';

            resultDiv.innerHTML = '<p style="color: green;">Threaded comment updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **スレッド化されたコメントを削除する**

### **Excelでスレッド化されたコメントを削除する**

Excelでスレッド化されたコメントを削除するには、コメントを含むセルを右クリックし、次の画像に示すように**コメントを削除**オプションをクリックします。

![todo:image_alt_text](threaded-comments_8.jpg)
