---
title: JavaScriptを用いた強力暗号化タイプの設定（C++）
linktitle: 強力な暗号化方式の設定
type: docs
weight: 60
url: /ja/javascript-cpp/setting-strong-encryption-type/
description: Aspose.Cells for JavaScriptを用いてExcelファイルの強力暗号化タイプを設定する方法を学ぶ（C++）
---

{{% alert color="primary" %}} 

Microsoft Excel (97-2007/2010)では、スプレッドシートにパスワードを設定して保護し、暗号化することができます。これには暗号化アルゴリズムを提供するCrypto Service Providerが使用されます。Crypto Service Provider（CSP）は、異なる特性を持つ暗号化アルゴリズムのセットです。デフォルトのCSPは「Office 97/2000 Compatible」です。これは一部の公に知られているセキュリティの問題を持つCSPです。「弱い暗号化（XOR）」または「Office 97/2000 Compatible」暗号化タイプで保護されたスプレッドシートは容易にクラックできます。

この問題を解決するには、Microsoft Excelが提供する強力な暗号化タイプの1つを使用します。最強のCSPに暗号化タイプを変更することができます。強力な暗号化には、最低128ビットの鍵長が必要です；たとえば、「Microsoft Strong Cryptographic Provider」。

Aspose.Cells APIを使用して、強力な暗号化方式を使ったExcelファイルに暗号化し、パスワードを設定することもできます。

{{% /alert %}}  
## **Microsoft Excelでの暗号化の適用**  
Microsoft Excel（たとえば2007）でファイルの暗号化を実装するには:

1. **ツール**メニューから**オプション**を選択します。  
1. **セキュリティ**タブを選択します。  
1. **開くためのパスワード**フィールドに値を入力します。  
1. **高度** をクリックします。  
1. 暗号化方式を選択し、パスワードを確認します。  

## **Aspose.Cellsを使用した暗号化の適用**  
以下のコード例は、ファイルに強力な暗号化を適用し、パスワードを設定します。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Encrypt Workbook</title>
    </head>
    <body>
        <h1>Encrypt Workbook Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            workbook.encryptionOptions = [AsposeCells.EncryptionType.StrongCryptographicProvider, 128];
            workbook.settings.password = "1234";

            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'encryptedBook1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Encrypted Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">File encrypted successfully! Click the download link to get the encrypted file.</p>';
        });
    </script>
</html>
```
