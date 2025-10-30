---
title: 共有ブックをパスワード保護または保護解除する（JavaScript/C++対応）
linktitle: 共有ブックをパスワードで保護または保護解除
type: docs
weight: 10
url: /ja/javascript-cpp/password-protect-or-unprotect-the-shared-workbook/
---

## **可能な使用シナリオ**

以下のスクリーンショットのように、Microsoft Excelを使って共有ブックを保護または保護解除できます。Aspose.Cells for JavaScriptをC++で使用した場合も、[**Workbook.protectSharedWorkbook(string)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#protectSharedWorkbook-string-)と[**Workbook.unprotectSharedWorkbook(string)**](https://reference.aspose.com/cells/javascript-cpp/workbook/#unprotectSharedWorkbook-string-)メソッドでサポートします。

![todo:image_alt_text](password-protect-or-unprotect-the-shared-workbook_1.png)

## **共有ワークブックのパスワード保護または保護解除**

次のサンプルコードは、ブックを作成し、共有を有効にした状態で保護し、[出力Excelファイル](55541777.xlsx)として保存します。スクリーンショットに示すように、保護を解除しようとすると、Microsoft Excelがパスワードの入力を要求します。

![todo:image_alt_text](password-protect-or-unprotect-the-shared-workbook_2.png)

## **サンプルコード**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Protect Shared Workbook Example</h1>
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
            // Creating an empty Workbook
            const workbook = new Workbook();

            // Protect the Shared Workbook with Password
            workbook.protectSharedWorkbook("1234");

            // Uncomment this line to Unprotect the Shared Workbook
            // workbook.unprotectSharedWorkbook("1234");

            // Saving the modified Excel file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputProtectSharedWorkbook.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook protected successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
