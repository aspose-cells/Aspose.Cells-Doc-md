---
title: JavaScriptを使用したC++によるODSファイルの暗号化と復号化
linktitle: ODSファイルの暗号化と複合化
type: docs
weight: 10
url: /ja/javascript-cpp/encrypt-and-decrypt-ods-files/
description: Aspose.Cells for JavaScriptを使ってODSファイルをパスワード保護と暗号化（C++） 
---

{{% alert color="primary" %}}
OpenOffice.orgは、パスワード保護とファイルの暗号化をサポートするフル機能のオフィススイートです。ただし、暗号化されたODSファイルは、パスワードを提供した後にのみOpenOfficeで開くことができます。Excelは暗号化されたODSファイルを開けず、警告メッセージを表示する場合があります。暗号化オプションは他のファイルタイプとは異なり、ODSファイルには適用されません。 
Aspose.Cellsを使用すれば、ODSファイルの暗号化と復号化が可能です。復号化されたODSファイルはExcelとOpenOfficeの両方で開くことができます。
{{% /alert %}}

## **OpenOffice Calcで暗号化**
1. **名前を付けて保存**を選択し、**パスワードを設定して保存**ボックスをクリックします。
1. **保存**ボタンをクリックします。
1. 開いた「パスワードの設定」ウィンドウの「開くためのパスワードを入力」および「パスワードを確認」フィールドに希望するパスワードを入力します。 
1. ファイルを保存するために **OK** ボタンをクリックします。

## **C++を用いたAspose.Cells for JavaScriptでODSファイルを暗号化**
ODSファイルを暗号化するには、ファイルを読み込み、[**WorkbookSettings.password**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#password--)の値を実際のパスワードに設定して保存します。出力される暗号化されたODSファイルはOpenOfficeでのみ開くことができます。

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Protect ODS File</title>
    </head>
    <body>
        <h1>Protect ODS File Example</h1>
        <input type="file" id="fileInput" accept=".ods" />
        <button id="runExample">Protect and Download ODS</button>
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

            // Instantiating a Workbook object by opening the uploaded ODS file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Password protect the file (converted from getSettings().setPassword -> settings.password)
            workbook.settings.password = "1234";

            // Saving the ODS file
            const outputData = workbook.save(SaveFormat.Ods);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputEncryptedODSFile.ods';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Encrypted ODS File';

            document.getElementById('result').innerHTML = '<p style="color: green;">File protected successfully! Click the download link to get the encrypted file.</p>';
        });
    </script>
</html>
```

## **C++を通じてAspose.Cells for JavaScriptでODSファイルを復号化**
ODSファイルを復号化するには、[**LoadOptions.password**](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#password--)にパスワードを入力してファイルを読み込みます。ファイルが読み込まれたら、[**WorkbookSettings.password**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#password--)の文字列をnullに設定してください。

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

            // Open an encrypted ODS file with load options
            const loadOptions = new LoadOptions(LoadFormat.Ods);

            // Set original password
            loadOptions.password = "1234";

            // Load the encrypted ODS file with the appropriate load options
            const workbook = new Workbook(new Uint8Array(arrayBuffer), loadOptions);

            // Set the password to null (remove password from settings)
            workbook.settings.password = null;

            // Save the decrypted ODS file and provide download link
            const outputData = workbook.save(SaveFormat.Ods);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputDecryptedODSFile.ods';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Decrypted ODS File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Decryption completed successfully! Click the download link to get the decrypted file.</p>';
        });
    </script>
</html>
```
