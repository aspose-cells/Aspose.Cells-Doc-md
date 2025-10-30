---
title: ODs dosyalarını JavaScript ile C++ kullanarak şifrele ve çöz
linktitle: ODS Dosyalarını Şifreleme ve Şifre Çözme
type: docs
weight: 10
url: /tr/javascript-cpp/encrypt-and-decrypt-ods-files/
description: Aspose.Cells for JavaScript kullanarak ODS dosyalarını parola koruma ve şifreleme 
---

{{% alert color="primary" %}}
OpenOffice.org, şifre koruma ve şifreleme destekleyen tam özellikli bir ofis paketidir. Ancak, şifreli bir ODS dosyası, şifre girildikten sonra OpenOffice tarafından açılabilir. Excel, şifreli ODS dosyasını açamaz ve uyarı mesajları gösterebilir. Şifreleme seçenekleri, diğer dosya türlerine göre ODS dosyalarında uygulanamaz. 
Aspose.Cells, ODS dosyalarını şifreleme ve şifre çözme imkanı sağlar. Şifreleri çözülen ODS dosyaları hem Excel hem de OpenOffice tarafından açılabilir.
{{% /alert %}}

## **OpenOffice Calc ile Şifrele**
1. **Save as** seçeneğini belirleyin ve **Save With Password** kutusuna tıklayın.
1. **Kaydet** düğmesini tıklayın.
1. Açılan Set Parola penceresinde, hem **Açmak için Parolayı Girin** hem de **Parolayı Onaylayın** alanlarına istediğiniz parolayı yazın. 
1. Dosyayı kaydetmek için **Tamam** düğmesini tıklayın.

## **C++ ile Aspose.Cells for JavaScript kullanarak ODS dosyasını şifrele**
Bir ODS dosyasını şifrelemek için, dosyayı yükleyin ve kaydetmeden önce [**WorkbookSettings.password**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#password--) değerini gerçek parola ile ayarlayın. Çıktı şifrelenmiş ODS dosyası yalnızca OpenOffice'da açılabilir.

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

## **C++ ile Aspose.Cells for JavaScript kullanarak ODS dosyasını çöz**
Bir ODS dosyasını deşifre etmek için, dosyayı [**LoadOptions.password**](https://reference.aspose.com/cells/javascript-cpp/loadoptions/#password--) içeren bir parola sağlayarak yükleyin. Dosya yüklendikten sonra, [**WorkbookSettings.password**](https://reference.aspose.com/cells/javascript-cpp/workbooksettings/#password--) dizesini null olarak ayarlayın.

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
