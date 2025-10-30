---
title: JavaScriptを介してPDFドキュメントを保護
linktitle: セキュアなPDFドキュメント
type: docs
weight: 120
url: /ja/javascript-cpp/secure-pdf-documents/
description: 所有者とユーザーパスワードを使ったPDFの保護方法と、C++を使用したAspose.Cells for JavaScriptでPDFファイルのアクセス許可を設定する方法を学びます。
---

{{% alert color="primary" %}}

開発者は、暗号化されたPDFファイルと作業する必要がある場合があります。

- ドキュメントをオーナーパスワードとユーザーパスワードでセキュリティ保護して、誰もがそれを開けなくする。
- ドキュメントを開いた後にドキュメントに制限や権限を設定します。例: ドキュメントの内容を印刷または抽出できるかどうかを制限します。

この記事では、スプレッドシートをPDFに保存する際にPDFセキュリティオプションを渡す方法について説明します。

{{% /alert %}}

Aspose.Cellsはセキュリティを扱うための[**PdfSecurityOptions**](https://reference.aspose.com/cells/javascript-cpp/pdfsecurityoptions/)を提供します。PDFに保存する際に所有者パスワードとユーザーパスワードを設定できます。暗号化されたPDFドキュメントを開くには、所有者またはユーザーパスワードが必要です。

- ユーザーパスワードは null または空文字列に設定可能です。この場合、PDFを開くときにパスワードは必要ありません。
- 正しい所有者パスワードを使ってPDFドキュメントを開くと、アクセス制限なしでドキュメントに完全にアクセスできます。
- 正しいユーザーパスワードでPDFドキュメントを開く（またはユーザーパスワードのないドキュメントを開く）と、指定された権限に応じて限定されたアクセスが可能です。

以下のサンプルコードは、Aspose.CellsでPDFをセキュアにする方法を説明しています。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Secure PDF Example</title>
    </head>
    <body>
        <h1>Secure PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions, PdfSecurityOptions, Utils } = AsposeCells;

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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create PDF save options and security options
            const saveOption = new PdfSaveOptions();
            saveOption.securityOptions = new PdfSecurityOptions();

            // Set security options (converted from getters/setters to properties)
            saveOption.securityOptions.userPassword = "user";
            saveOption.securityOptions.ownerPassword = "owner";
            saveOption.securityOptions.extractContentPermission = false;
            saveOption.securityOptions.printPermission = false;

            // Save the workbook to PDF with security options
            const outputData = workbook.save(SaveFormat.Pdf, saveOption);
            const blob = new Blob([outputData], { type: "application/pdf" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'securepdf_test.out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Secure PDF';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the secured PDF file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

スプレッドシートに数式が含まれている場合、スプレッドシートをPDFにレンダリングする直前に[**Workbook.calculateFormula()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--)を呼び出すことが最善です。これにより、数式に依存した値が再計算され、正しい値がPDFに表示されます。

{{% /alert %}}
