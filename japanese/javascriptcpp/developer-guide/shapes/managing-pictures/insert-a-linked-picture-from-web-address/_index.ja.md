---
title: JavaScriptを使用したC++経由でWebアドレスからリンクされた画像を挿入する
linktitle: Webアドレスからリンクされた画像の挿入
type: docs
weight: 450
url: /ja/javascript-cpp/insert-a-linked-picture-from-web-address/
description: Aspose.Cells for JavaScriptを使用してC++経由でWebアドレスからワークシートにリンクされた画像を挿入する方法を学びます。
---

{{% alert color="primary" %}}
時には、ウェブ（http://）から画像をワークシートに挿入する必要があります。その場合、画像のURLを指定すると、そのスプレッドシートをExcelで開くたびに画像がダウンロードされます。画像はExcelドキュメントに物理的に埋め込まれるのではなく、ウェブリソースを指し示します。
{{% /alert %}}

## **Microsoft Excel の使用**

Microsoft Excel（たとえば2007）で：

1. **挿入**メニューをクリックし、**画像**を選択します。  
1. 挿入画像ダイアログで画像のWebアドレスを指定します。

## **Aspose.Cells for JavaScriptをC++経由で使用**

C++経由のAspose.Cells for JavaScriptは、[**ShapeCollection.addLinkedPicture(upperLeftRow, upperLeftColumn, heightPixels, widthPixels, sourceFullName)**](https://reference.aspose.com/cells/javascript-cpp/shapecollection/#addLinkedPicture-number-number-number-number-string-)を使用したリンクされた画像の追加をサポートしています。この方法は[**Picture**](https://reference.aspose.com/cells/javascript-cpp/picture)オブジェクトを返します。

以下の例では、Webアドレスからリンクされた画像をワークシートに追加する方法を示しています。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Insert Linked Picture Example</h1>
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

            if (fileInput.files.length) {
                // If file provided, use it as the base workbook
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                var workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                // Otherwise create a new workbook
                var workbook = new Workbook();
            }

            // Access the first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Insert a linked picture (from Web Address) to B2 Cell.
            const pic = worksheet.shapes.addLinkedPicture(1, 1, 100, 100, "http://www.aspose.com/Images/aspose-logo.jpg");

            // Set the height and width of the inserted image.
            pic.heightInch = 1.04;
            pic.widthInch = 2.6;

            // Save the Excel file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outLinkedPicture.out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Linked picture inserted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
