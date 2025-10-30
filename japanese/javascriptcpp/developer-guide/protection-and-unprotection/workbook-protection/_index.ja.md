---
title: JavaScriptを使用したExcelのブック構造の保護と解除（C++経由）
linktitle: ブック構造の保護と保護解除
type: docs
weight: 40
url: /ja/javascript-cpp/protect-and-unprotect-workbook-structure/
description: C++を経由してJavaScriptを使用したExcelファイルのブック構造の保護と解除。
---


{{% alert color="primary" %}}  
他のユーザーによる隠しワークシートの表示、追加、移動、削除、または非表示、およびワークシートの名前の変更を防ぐために、Excelブックの構造をパスワードで保護できます。  
{{% /alert %}}  


## **MS Excelでのブック構造の保護と保護解除**  

**![ブック構造の保護と保護解除](protect-and-unprotect-workbook-structure.png)**  

1. **レビュー > ブックの保護** をクリックします。  
1. **パスワードボックス** にパスワードを入力します。  
1. **OK** を選択し、パスワードを再入力して確認し、その後再度 **OK** を選択します。  


## **C++経由でAspose.Cells for JavaScriptを使用してブック構造を保護**  
Excelファイルのワークシートの構造を保護するためには、次の簡単なコード行のみが必要です。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Protect Workbook Structure Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ProtectionType, Utils } = AsposeCells;

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

            // Protect workbook structure with a password
            workbook.protect(ProtectionType.Structure, "password");

            // Save the workbook to a downloadable file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Book1_protected.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Protected Workbook';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and protected successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```  

## **C++経由でAspose.Cells for JavaScriptを使用してブック構造の保護解除**  
Aspose.Cells APIを使用してワークブック構造を保護解除するのは簡単です。正しいパスワードが必要です。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Unprotect Workbook Structure Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Unprotect Workbook</button>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const workbook = new Workbook(new Uint8Array(arrayBuffer));
            workbook.unprotect("password");
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            const baseName = file.name.replace(/(\.xlsx|\.xls|\.csv)$/i, '');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = baseName + '.unprotected.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Unprotected Excel File';
            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook structure unprotected successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

{{% alert color="primary" %}}  
注意：正しいパスワードが必要です。  
{{% /alert %}}
