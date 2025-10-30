---
title: C++ ile Güçlü Şifreleme Türü Ayarlama
linktitle: Güçlü Şifreleme Türü Ayarlama
type: docs
weight: 60
url: /tr/javascript-cpp/setting-strong-encryption-type/
description: C++ ile Aspose.Cells for JavaScript kullanarak Excel dosyaları için güçlü şifreleme türleri nasıl belirlenir öğrenin.
---

{{% alert color="primary" %}} 

Microsoft Excel (97-2007/2010) elektronik tabloları şifrelemeye ve parola koruması sağlamaya olanak tanır. Bunun için bir Kripto Servis Sağlayıcı tarafından sağlanan algoritmayı kullanır. Kripto Servis Sağlayıcısı (veya CSP), farklı özelliklere sahip bir dizi kriptografik algoritmadır. Varsayılan CSP 'Office 97/2000 Uyumlu'dur. Bu, bazı kamuya bilinen güvenlik sorunları olan bir CSP'dir. 'Zayıf şifreleme (XOR)' veya 'Office 97/2000 Uyumlu' şifreleme türleriyle korunan elektronik tablolar kolayca kırılabilir.

Bu sorunu aşmak için Microsoft Excel tarafından sağlanan güçlü şifreleme türlerinden birini kullanın. Şifreleme türünü en güçlü CSP'ye değiştirebilirsiniz. Güçlü şifreleme için en az 128 bitlik bir anahtar uzunluğu gereklidir, örneğin, 'Microsoft Güçlü Kriptografik Sağlayıcı'.

Aspose.Cells API'sı kullanarak güçlü şifreleme türü ile Excel dosyalarını da şifreleyebilir ve parola koruyabilirsiniz.

{{% /alert %}}  
## **Microsoft Excel'de Şifreleme Uygulama**  
Microsoft Excel'de dosya şifrelemeyi uygulamak için (örneğin 2007):

1. **Araçlar** menüsünden **Seçenekler**'i seçin.  
1. **Güvenlik** sekmesini seçin.  
1. **Açmak için Parola** alanı için bir değer girin.  
1. **Gelişmiş**'i tıklayın.  
1. Şifreleme türünü seçin ve parolayı onaylayın.  

## **Aspose.Cells ile Şifreleme Uygulama**  
Aşağıdaki kod örnekleri bir dosyaya güçlü şifreleme uygular ve bir şifre ayarlar.

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
