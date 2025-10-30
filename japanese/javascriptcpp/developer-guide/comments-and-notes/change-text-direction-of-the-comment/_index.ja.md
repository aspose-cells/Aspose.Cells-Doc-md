---
title: JavaScriptを介してC++でコメントのテキスト方向を変更
linktitle: コメントのテキスト方向を変更する
type: docs
weight: 10
url: /ja/javascript-cpp/change-text-direction-of-the-comment/
description: Aspose.Cells for JavaスクリプトをC++を通じてコメントのテキスト方向を変更する方法を学び、コメントの配置設定を効果的にカスタマイズします。
---

{{% alert color="primary" %}}

 Microsoft Excelでは、セルにコメントを追加して追加情報を記載し、データを強調表示できます。開発者はコメントの配置設定やテキストの方向を指定するためにカスタマイズする必要があります。Aspose.Cells for JavaスクリプトをC++で使用し、そのAPIを提供します。

{{% /alert %}}

 Aspose.Cells for JavaスクリプトをC++で使用してコメントのフォント色を設定するための[**Shape.textDirection**](https://reference.aspose.com/cells/javascript-cpp/shape/#textDirection--)プロパティを提供します。以下のサンプルコードは、[**Shape.textDirection**](https://reference.aspose.com/cells/javascript-cpp/shape/#textDirection--)プロパティを使用してコメントのテキスト方向を設定する例です。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Add Comment Shape</title>
    </head>
    <body>
        <h1>Add Comment Shape Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, TextAlignmentType, TextDirectionType } = AsposeCells;

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
            // Instantiate a new Workbook
            const wb = new Workbook();

            // Get the first worksheet
            const sheet = wb.worksheets.get(0);

            // Add a comment to A1 cell
            const commentIndex = sheet.comments.add("A1");
            const comment = sheet.comments.get(commentIndex);

            // Set its vertical alignment setting            
            comment.commentShape.textVerticalAlignment = TextAlignmentType.Center;

            // Set its horizontal alignment setting
            comment.commentShape.textHorizontalAlignment = TextAlignmentType.Right;

            // Set the Text Direction - Right-to-Left
            comment.commentShape.textOrientationType = TextDirectionType.RightToLeft;

            // Set the Comment note
            comment.note = "This is my Comment Text. This is test";

            // Saving the modified Excel file
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'OutCommentShape.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Comment added successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
