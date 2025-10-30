---
title: JavaScriptを使用したExcelファイルの暗号化（C++経由）
linktitle: Excelファイルの暗号化
type: docs
weight: 90
url: /ja/javascript-cpp/encrypting-excel-files/
description: Aspose.Cells for JavaScriptを使用してExcelファイルを暗号化し、パスワード保護する方法を学びます。（C++経由） 
---

{{% alert color="primary" %}}

Microsoft Excel (97 - 365)を使用して、スプレッドシートを暗号化およびパスワード保護することができます。暗号化には、暗号化サービスプロバイダー（CSP）によって提供されるアルゴリズムが使用されます。暗号化キーの長さを適切に選択することが重要です。一部のCSPは40ビットまたは56ビットを超える長さをサポートしていません。これは弱い暗号化と見なされます。強力な暗号化には、最小128ビットのキー長が必要です。Microsoft Windowsには、強力な暗号化タイプを提供するCSPも含まれています。例えば、「Microsoft Strong Cryptographic Provider」などです。128ビットの暗号化は、銀行がインターネットバンキングシステムとの接続を暗号化する際に使用するものです。

Aspose.Cellsを使用すると、任意の暗号化タイプでMicrosoft Excelファイルを暗号化およびパスワード保護することができます。

{{% /alert %}}

## **Microsoft Excel の使用**

Microsoft Excel（ここではMicrosoft Excel 2003）でファイルの暗号化設定を行うには：

1. **ツール**メニューから**オプション**を選択します。ダイアログが表示されます。
1. **セキュリティ**タブを選択します。
1. パスワードを入力し、**詳細**をクリックします。
1. 暗号化方式を選択し、パスワードを確認します。

## **C++を使用したAspose.Cells for JavaScriptによる暗号化**

次の例は、Aspose.Cells APIを使用してExcelファイルを暗号化およびパスワード保護する方法を示しています。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
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
        const { Workbook, SaveFormat, Utils, EncryptionType } = AsposeCells;

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

            // Instantiate a Workbook object by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Specify XOR encryption type.
            workbook.encryptionOptions = { type: EncryptionType.XOR, keyLength: 40 };

            // Specify Strong Encryption type (RC4, Microsoft Strong Cryptographic Provider).
            workbook.encryptionOptions = { type: EncryptionType.StrongCryptographicProvider, keyLength: 128 };

            // Password protect the file.
            workbook.settings.password = "1234";

            // Save the excel file (Excel97To2003 format for .xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'encryptedBook1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Encrypted Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">File encrypted successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **修正パスワードを指定するオプション**

次の例は、Aspose.Cells APIを使用して既存のファイルの**修正パスワード**Microsoft Excelオプションを設定する方法を示しています。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Specify Password To Modify Option Example</title>
    </head>
    <body>
        <h1>Specify Password To Modify Option Example</h1>
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate a Workbook object by opening the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Set the password for modification.
            workbook.settings.writeProtection.password = "1234";

            // Save the excel file in Excel97-2003 format (.xls)
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'SpecifyPasswordToModifyOption.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Password to modify set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

## **暗号化されたファイルのパスワードを確認します**

暗号化されたファイルのパスワードを検証するには、Aspose.Cells for JavaScriptをC++で使用して[**FileFormatUtil.verifyPassword(Uint8Array, string)**](https://reference.aspose.com/cells/javascript-cpp/fileformatutil/#verifyPassword-uint8array-string-)メソッドを提供します。これらのメソッドは二つのパラメータ、ファイルストリームと確認したいパスワードを受け取ります。
以下のコードスニペットは、提供されたパスワードが有効かどうかを確認する[**FileFormatUtil.verifyPassword(Uint8Array, string)**](https://reference.aspose.com/cells/javascript-cpp/fileformatutil/#verifyPassword-uint8array-string-)メソッドの使用を示しています。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Verify Password Example</title>
    </head>
    <body>
        <h1>Verify Password Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv,.xlsm" />
        <button id="runExample">Verify Password</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

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
            const uint8 = new Uint8Array(arrayBuffer);

            const isPasswordValid = AsposeCells.FileFormatUtil.verifyPassword(uint8, "1234");

            document.getElementById('result').innerHTML = '<p>Password is Valid: ' + isPasswordValid + '</p>';
        });
    </script>
</html>
```

## **Aspose.Cells を使用して ODS ファイルの暗号化/復号化**

Aspose.Cellsは、ODSファイルの暗号化と復号化を可能にします。復号化されたODSファイルはExcelとOpenOfficeの両方で開くことができますが、暗号化されたODSファイルはパスワードを入力しないとOpenOfficeでのみ開くことができ、Excelは開けません。暗号化されたODSファイルは、他のファイル種と異なり、直接開くことができません。暗号化したい場合は、ファイルをロードし、保存前に[**WorkbookSettings.password**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#password--)値を実際のパスワードに設定してください。出力された暗号化ODSファイルはOpenOfficeでのみ開くことができます。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Encrypt ODS File Example</h1>
        <input type="file" id="fileInput" accept=".ods" />
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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an ODS file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiate Workbook from uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Password protect the file
            workbook.settings.password = "1234";

            // Save the ODS file
            const outputData = workbook.save(SaveFormat.Ods);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputEncryptedODSFile.ods';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Encrypted ODS File';

            document.getElementById('result').innerHTML = '<p style="color: green;">File encrypted successfully! Click the download link to get the encrypted file.</p>';
        });
    </script>
</html>
```

ODSファイルを復号化するには、[**LoadOptions.password**](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#password--)によるパスワードの提供でファイルを読み込みます。ファイルが読み込まれたら、[**WorkbookSettings.password**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#password--)文字列をnullに設定します。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Decrypt ODS Example</title>
    </head>
    <body>
        <h1>Decrypt ODS Example</h1>
        <input type="file" id="fileInput" accept=".ods" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, LoadFormat, Utils } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an ODS file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Create load options for ODS and set original password
            const loadOptions = new LoadOptions(LoadFormat.Ods);
            loadOptions.password = "1234";

            // Load the encrypted ODS file with the appropriate load options
            const workbook = new Workbook(new Uint8Array(arrayBuffer), loadOptions);

            // Set the password to null to remove encryption/password
            workbook.settings.password = null;

            // Save the decrypted ODS file
            const outputData = workbook.save(SaveFormat.Ods);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputDecryptedODSFile.ods';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Decrypted ODS File';

            document.getElementById('result').innerHTML = '<p style="color: green;">File decrypted successfully! Click the download link to get the decrypted file.</p>';
        });
    </script>
</html>
```
