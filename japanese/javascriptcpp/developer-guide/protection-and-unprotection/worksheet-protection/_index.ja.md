---
title: JavaScriptを使用してワークシートの保護と解除（C++経由）
linktitle: ワークシートの保護と保護解除
type: docs
weight: 40
url: /ja/javascript-cpp/protect-and-unprotect-worksheets/
description: C++を経由してAspose.Cells for JavaScriptを使用してExcelファイルのワークシートを保護および解除。
---

{{% alert color="primary" %}}  
ワークシート上のデータの変更、移動、または削除を他のユーザーが誤ってまたは意図的に防ぐために、Excelワークシートのセルをロックし、その後シートをパスワードで保護できます。  
{{% /alert %}}  

## **MS Excelでのワークシートの保護と保護解除**  

**![ワークシートの保護と保護解除](protect-and-unprotect-worksheet.png)**  

1. **レビュー > ワークシートの保護** をクリックします。  
1. **パスワードボックス** にパスワードを入力します。  
1. **許可** オプションを選択します。  
1. **OK** を選択し、パスワードを再入力して確認し、その後再度 **OK** を選択します。  

## **C++経由でAspose.Cells for JavaScriptを使用してワークシートの保護**  
Excelファイルのワークシートの構造を保護するためには、次の簡単なコード行のみが必要です。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Protect Worksheet Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, ProtectionType } = AsposeCells;

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
            // Create a new file (workbook)
            const workbook = new Workbook();

            // Gets the first worksheet.
            const sheet = workbook.worksheets.get(0);

            // Protect contents of the worksheet.
            sheet.protect(ProtectionType.Contents);

            // Protect worksheet with password.
            sheet.protection.password = "test";

            // Save as Excel file and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Book1.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet protected and file is ready. Click the download link to get the file.</p>';
        });
    </script>
</html>
```  

## **C++経由でAspose.Cells for JavaScriptを使用したワークシートの保護解除**  
ワークシートの解除は、Aspose.Cells APIを使えば簡単です。ワークシートがパスワード保護されている場合、正しいパスワードが必要です。  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Unprotect Worksheet Example</title>
    </head>
    <body>
        <h1>Unprotect Worksheet Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Unprotect Worksheet</button>
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

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access the first worksheet
            const sheet = workbook.worksheets.get(0);

            // Unprotect contents of the worksheet using password
            sheet.unprotect("password");

            // Save the modified workbook to XLSX format and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'Book1.unprotected.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Unprotected Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Worksheet unprotected successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  

## **高度なトピック**  
- [Excel XP以降の高度な保護設定](/cells/ja/javascript-cpp/advanced-protection-settings-since-excel-xp/)  
- [ワークシートがパスワードで保護されているかどうかを検出する](/cells/ja/javascript-cpp/detect-if-worksheet-is-password-protected/)  
- [ワークシートの保護](/cells/ja/javascript-cpp/protecting-worksheets/)  
- [ワークシートの保護を解除する](/cells/ja/javascript-cpp/unprotect-a-worksheet/)  
- [ワークシートを保護するために使用されたパスワードの検証](/cells/ja/javascript-cpp/verify-password-used-to-protect-the-worksheet/)
