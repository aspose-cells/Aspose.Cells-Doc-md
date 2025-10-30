---
title: C++を使用してJavaScript経由でリンクされたOleオブジェクトの表示ラベルを取得・変更
linktitle: リンクされたオブジェクトの表示ラベルへのアクセスと変更
type: docs
weight: 100
url: /ja/javascript-cpp/access-and-modify-the-display-label-of-the-linked-ole-object/
description: Aspose.Cells for JavaScriptを使用してリンクされたOleオブジェクトの表示ラベルのアクセスと変更方法を学びます。 
---

## **可能な使用シナリオ**

Microsoft Excelでは、以下のスクリーンショットのようにOleオブジェクトの表示ラベルを変更できます。また、Aspose.Cells APIの[**OleObject.label**](https://reference.aspose.com/cells/javascript-cpp/oleobject/#label--)プロパティを使用してOleオブジェクトの表示ラベルにアクセスまたは変更することも可能です。

![todo:image_alt_text](access-and-modify-the-display-label-of-the-linked-ole-object_1.png)

## **リンクされたオブジェクトの表示ラベルへのアクセスと変更**

次のサンプルコードをご覧ください。このコードはOleオブジェクトを含む[sample Excelファイル](64716810.xlsx)をロードします。コードはOleオブジェクトにアクセスし、そのラベルを「Sample APIs」から「Aspose APIs」に変更します。以下に示すコンソール出力は、サンプルコードがサンプルExcelファイルに与える効果を示しています。

## **サンプルコード**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Access and Modify Label of Ole Object Example</h1>
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
            resultDiv.innerHTML = '';

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Load the sample Excel file 
            const wb = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const ws = wb.worksheets.get(0);

            // Access first Ole Object
            let oleObject = ws.oleObjects.get(0);

            // Display the Label of the Ole Object
            const beforeLabel = oleObject.label;
            console.log("Ole Object Label - Before: " + beforeLabel);

            // Modify the Label of the Ole Object
            oleObject.label = "Aspose APIs";

            // Save workbook to memory stream
            const ms = wb.save(SaveFormat.Xlsx);

            // Set the workbook reference to null / dispose
            wb.dispose();

            // Load workbook from memory stream
            const wbFromStream = new Workbook(ms);

            // Access first worksheet
            const wsFromStream = wbFromStream.worksheets.get(0);

            // Access first Ole Object
            oleObject = wsFromStream.oleObjects.get(0);

            // Display the Label of the Ole Object that has been modified earlier
            const afterLabel = oleObject.label;
            console.log("Ole Object Label - After: " + afterLabel);

            // Prepare download
            const blob = new Blob([ms]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'modified.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            resultDiv.innerHTML = `<p style="color: green;">Operation completed successfully!</p>
                                   <p>Ole Object Label - Before: ${beforeLabel}</p>
                                   <p>Ole Object Label - After: ${afterLabel}</p>`;
        });
    </script>
</html>
```

## **コンソール出力**

{{< highlight javascript >}}

Ole Object Label - Before: Sample APIs

Ole Object Label - After: Aspose APIs

{{< /highlight >}}
