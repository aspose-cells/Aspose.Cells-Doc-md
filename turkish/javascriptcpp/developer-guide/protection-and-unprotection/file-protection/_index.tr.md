---
title: Excel dosyalarını JavaScript kullanarak C++ ile şifrele ve çözüp, aç
linktitle: Excel Dosyalarını Şifrelemek ve Çözmek
type: docs
weight: 10
url: /tr/javascript-cpp/encrypt-and-decrypt-excel-files/
description: JavaScript kullanarak C++ ile Excel dosyalarını nasıl şifreleyip çözeceğinizi öğrenin. Excel dosyalarını kilitleyin ve kilidini açın.
---

{{% alert color="primary" %}}  
Microsoft Excel (97 - 365), elektronik tablolarınızı şifrelemeye ve parola koruması yapmaya olanak tanır. Bir şifreleme hizmet sağlayıcısı tarafından sağlanan algoritmalar, yani bir dizi farklı özelliklere sahip şifreleme algoritmaları kullanır. Varsayılan CSP 'Ofis 97/2000 Uyumlu' veya 'Zayıf Şifreleme (XOR)' dur. Doğru şifreleme anahtar uzunluğunu seçmek önemlidir. Bazı CSP'ler 40 veya 56 bit'ten fazlasını desteklemez. Bu zayıf şifreleme olarak kabul edilir. Güçlü şifreleme için minimum 128 bitlik bir anahtar uzunluğu gereklidir. Microsoft Windows, örneğin 'Microsoft Güçlü Kriptografik Sağlayıcısı' gibi güçlü şifreleme türleri sunan CSP'ler içerir. Size bir fikir vermek gerekirse, 128 bitlik şifreleme, bankaların İnternet Bankacılığı sistemleriyle olan bağlantıyı şifrelemek için kullandığı şeydir.  

Aspose.Cells, istediğiniz şifreleme türüyle Microsoft Excel dosyalarını şifrelemeye ve parola korumaya olanak tanır.  
{{% /alert %}}  

## **Microsoft Excel Kullanımı**  

Microsoft Excel'de (burada Microsoft Excel 2003) dosya şifreleme ayarlarını yapmak için:  

1. **Araçlar** menüsünden **Seçenekler**'i seçin. Bir iletişim kutusu görünecektir.  
2. **Güvenlik** sekmesini seçin.  
3. Bir şifre girin ve **Gelişmiş**e tıklayın  
4. Şifreleme türünü seçin ve şifreyi onaylayın.  

## **C++ kullanarak Aspose.Cells for JavaScript ile Excel dosyasını şifreleme**  

Aşağıdaki örnek, Aspose.Cells API kullanarak bir Excel dosyasını nasıl şifreleyip parola koruma altına alacağınızı gösterir.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Encrypt Workbook</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
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

            // Instantiate a Workbook object by opening the uploaded excel file.
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Specify XOR encryption type.
            workbook.encryptionOptions = { type: AsposeCells.EncryptionType.XOR, keyLength: 40 };

            // Specify Strong Encryption type (RC4, Microsoft Strong Cryptographic Provider).
            workbook.encryptionOptions = { type: AsposeCells.EncryptionType.StrongCryptographicProvider, keyLength: 128 };

            // Password protect the file.
            workbook.settings.password = "1234";

            // Save the excel file.
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'encryptedBook1.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Encrypted Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook encrypted and ready for download.</p>';
        });
    </script>
</html>
```  

### **Değişiklik yapmak için Parola Belirleme Seçeneği**  

Aşağıdaki örnek, mevcut bir dosya için Aspose.Cells API'sını kullanarak **Değiştirilecek Parolayı** Microsoft Excel seçeneğini nasıl ayarlayacağını göstermektedir.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Specify Password To Modify Example</h1>
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

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Set the password for modification.
            workbook.settings.writeProtection.password = "1234";

            // Save the excel file.
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'SpecifyPasswordToModifyOption.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Password-to-modify set successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  


## **C++ ile Aspose.Cells for JavaScript kullanarak Excel dosyasını çözüp açma**  
Bir parola ile korunan Excel dosyasını açmak ve şifreyi çözmek çok kolaydır; aşağıdaki kod örneğinde gösterildiği gibi Aspose.Cells API kullanabilirsiniz:  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Open Encrypted Excel and Remove Password</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, LoadOptions, SaveFormat, Utils } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an encrypted Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Prepare load options with password to open encrypted file
            const loadOptions = new LoadOptions();
            loadOptions.password = "password";

            // Instantiate workbook from uploaded file with load options
            const workbook = new Workbook(new Uint8Array(arrayBuffer), loadOptions);

            // Remove password from workbook settings
            workbook.settings.password = null;

            // Save the workbook and provide download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            // Use original filename with suffix to indicate password removed
            const originalName = file.name || 'output.xlsx';
            const baseName = originalName.replace(/(\.xls[xm]?|\.csv)$/i, '') || 'output';
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = baseName + '.unlocked.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Unlocked Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Password removed successfully! Click the download link to get the unlocked file.</p>';
        });
    </script>
</html>
```  


## **Gelişmiş Konular**  
- [ODS dosyalarını şifreleme ve şifresini çözme](/cells/tr/javascript-cpp/encrypt-and-decrypt-ods-files/)  
- [Güçlü Şifreleme Türü Belirleme](/cells/tr/javascript-cpp/setting-strong-encryption-type/)  
- [Çalışma Kitabını Yazma Koruması Sırasında Yazar Belirtme](/cells/tr/javascript-cpp/specify-author-while-write-protecting-workbook/)  
- [Şifreli Dosyaların Parolasını Doğrulama](/cells/tr/javascript-cpp/verify-password-of-encrypted-excel-and-ods-files/)
