---
title: JavaScriptを介してC++でコメントのフォントの色を変更する方法
linktitle: コメントのフォントの色を変更する方法
type: docs
weight: 180
url: /ja/javascript-cpp/how-to-change-the-comment-font-color/
---

{{% alert color="primary" %}}  
 Microsoft Excelでは、セルにコメントを追加して追加情報を記載し、データを強調表示できます。開発者はコメントの配置設定、テキストの方向、フォントカラーなどをカスタマイズする必要があります。Aspose.Cells for JavaスクリプトはそのためのAPIを提供します。  
{{% /alert %}}  

 Aspose.Cells for JavaスクリプトをC++で使用してコメントのフォントの色を設定するための[**Shape.textBody**](https://reference.aspose.com/cells/javascript-cpp/shape/#textBody--)プロパティを提供します。以下のサンプルコードは、[**Shape.textBody**](https://reference.aspose.com/cells/javascript-cpp/shape/#textBody--)プロパティを使ってコメントのテキスト方向を設定する例です。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Change Comment Font Color Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, TextAlignmentType, Color, StyleFlag } = AsposeCells;

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

            // Instantiate a new Workbook (if a file is provided, open it; otherwise create a new workbook)
            let workbook;
            if (fileInput.files.length) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Get the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Add some text in cell A1
            worksheet.cells.get("A1").putValue("Here");

            // Add a comment to A1 cell
            const commentIndex = worksheet.comments.add("A1");
            const comment = worksheet.comments.get(commentIndex);

            // Set its vertical alignment setting            
            comment.commentShape.textVerticalAlignment = TextAlignmentType.Center;

            // Set the Comment note
            comment.note = "This is my Comment Text. This is Test.";

            const shape = worksheet.comments.get("A1").commentShape;

            shape.fill.solidFill.color = Color.Black;
            const font = shape.font;
            font.color = Color.White;
            const styleFlag = new StyleFlag();
            styleFlag.fontColor = true;
            shape.textBody.format(0, shape.text.length, font, styleFlag);

            // Save the Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputChangeCommentFontColor.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

上記のコードによって生成された[出力ファイル](102662195.xlsx)を参照してください。
