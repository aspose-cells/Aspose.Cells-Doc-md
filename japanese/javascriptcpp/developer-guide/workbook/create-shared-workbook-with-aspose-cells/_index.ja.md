---
title: 共有ワークブックをAspose.Cells for JavaScriptをC++で作成する
linktitle: Aspose.Cellsで共有ブックを作成する
type: docs
weight: 40
url: /ja/javascript-cpp/create-shared-workbook-with-aspose-cells/
description: C++を使って共有ワークブックを作成する方法を学びます。
---

## **可能な使用シナリオ**  

Microsoft Excelでは、次のスクリーンショットのようにワークブックを共有できます。ワークブックを共有すると、複数のユーザーがネットワーク上で編集可能になります。Aspose.Cells for JavaScriptをC++を使うと、[**WorkbookSettings.shared**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#shared--)プロパティで共有ワークブックを作成できます。  

![todo:image_alt_text](create-shared-workbook-with-aspose-cells_1.png)  

## **Aspose.Cellsで共有ブックを作成する**  

以下のサンプルコードは、[**WorkbookSettings.shared**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#shared--)プロパティを**true**に設定して共有ワークブックを作成します。Microsoft Excelで[出力Excelファイル](55541786.xlsx)を開くと、「共有」ステータスとともに出力済みのワークブック名が表示されます。  

![todo:image_alt_text](create-shared-workbook-with-aspose-cells_2.png)  

## **サンプルコード**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Create Shared Workbook Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="createShared" disabled>Create Shared Workbook</button>
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
            document.getElementById('createShared').disabled = false;
        });

        document.getElementById('createShared').addEventListener('click', async () => {
            const wb = new Workbook();

            // Share the Workbook (converted getter/setter to property)
            wb.settings.shared = true;

            // Save the Shared Workbook
            const outputData = wb.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSharedWorkbook.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Shared Workbook';

            document.getElementById('result').innerHTML = '<p style="color: green;">Shared workbook created successfully! Click the download link to save the file.</p>';
        });
    </script>
</html>
```
