---
title: Excel Dosyalarını Node.js kullanarak şifreleme ve parola koruma
linktitle: Excel Dosyalarını Şifreleme
type: docs
weight: 90
url: /tr/nodejs-cpp/encrypting-excel-files/
description: Aspose.Cells for Node.js via C++ kullanarak Excel dosyalarını şifreleme ve parola ile koruma nasıl yapılır öğrenin. 
---

{{% alert color="primary" %}}

Microsoft Excel (97 - 365), elektronik tablolarınızı şifrelemeye ve parola koruması yapmaya olanak tanır. Bir şifreleme hizmet sağlayıcısı tarafından sağlanan algoritmalar, yani bir dizi farklı özelliklere sahip şifreleme algoritmaları kullanır. Varsayılan CSP 'Ofis 97/2000 Uyumlu' veya 'Zayıf Şifreleme (XOR)' dur. Doğru şifreleme anahtar uzunluğunu seçmek önemlidir. Bazı CSP'ler 40 veya 56 bit'ten fazlasını desteklemez. Bu zayıf şifreleme olarak kabul edilir. Güçlü şifreleme için minimum 128 bitlik bir anahtar uzunluğu gereklidir. Microsoft Windows, örneğin 'Microsoft Güçlü Kriptografik Sağlayıcısı' gibi güçlü şifreleme türleri sunan CSP'ler içerir. Size bir fikir vermek gerekirse, 128 bitlik şifreleme, bankaların İnternet Bankacılığı sistemleriyle olan bağlantıyı şifrelemek için kullandığı şeydir.

Aspose.Cells, istediğiniz şifreleme türüyle Microsoft Excel dosyalarını şifrelemeye ve parola korumaya olanak tanır.

{{% /alert %}}

## **Microsoft Excel Kullanımı**

Microsoft Excel'de (burada Microsoft Excel 2003) dosya şifreleme ayarlarını yapmak için:

1. **Araçlar** menüsünden **Seçenekler**'i seçin. Bir iletişim kutusu görünecektir.
1. **Güvenlik** sekmesini seçin.
1. Bir parola girin ve **Gelişmiş**'i tıklayın.
1. Şifreleme türünü seçin ve parolayı onaylayın.

## **Aspose.Cells for Node.js via C++ ile Şifreleme**

Aşağıdaki örnek, Aspose.Cells API'sını kullanarak bir Excel dosyasını şifrelemek ve parolayla korumak için nasıl yapılacağını göstermektedir.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xls");

// Instantiate a Workbook object.
// Open an excel file.
const workbook = new AsposeCells.Workbook(filePath);

// Specify XOR encryption type.
workbook.setEncryptionOptions(AsposeCells.EncryptionType.XOR, 40);

// Specify Strong Encryption type (RC4, Microsoft Strong Cryptographic Provider).
workbook.setEncryptionOptions(AsposeCells.EncryptionType.StrongCryptographicProvider, 128);

// Password protect the file.
workbook.getSettings().setPassword("1234");

// Save the excel file.
workbook.save(path.join(dataDir, "encryptedBook1.out.xls"));
```

### **Değiştirilecek Parolayı Belirtme Seçeneği**

Aşağıdaki örnek, mevcut bir dosya için Aspose.Cells API'sını kullanarak **Değiştirilecek Parolayı** Microsoft Excel seçeneğini nasıl ayarlayacağını göstermektedir.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xls");

// Instantiate a Workbook object.
// Open an excel file.
const workbook = new AsposeCells.Workbook(filePath);

// Set the password for modification.
workbook.getSettings().getWriteProtection().setPassword("1234");

// Save the excel file.
workbook.save(path.join(dataDir, "SpecifyPasswordToModifyOption.out.xls"));
```

## **Şifrelenmiş dosyanın parolasını doğrulama**

Şifreli dosyanın şifresini doğrulamak için, Aspose.Cells for Node.js via C++ [**FileFormatUtil.verifyPassword(Uint8Array, string)**](https://reference.aspose.com/cells/nodejs-cpp/fileformatutil/#verifyPassword-uint8array-string-) metodunu sağlar. Bu metodlar, dosya akışını ve doğrulanacak şifreyi iki parametre alır.
Aşağıdaki kod parçası, sağlanan parolanın geçerli olup olmadığını doğrulamak için [**FileFormatUtil.verifyPassword(Uint8Array, string)**](https://reference.aspose.com/cells/nodejs-cpp/fileformatutil/#verifyPassword-uint8array-string-) yönteminin nasıl kullanıldığını göstermektedir.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "EncryptedBook1.xlsx");

// Create a Stream object
const fs = require("fs");
const fstream = fs.readFileSync(filePath);

const isPasswordValid = AsposeCells.FileFormatUtil.verifyPassword(fstream, "1234");

console.log("Password is Valid: " + isPasswordValid);
```

## **Aspose.Cells ile ODS dosyasının Şifrelenmesi/Şifresinin Çözülmesi**

Aspose.Cells ile ODS dosyasını şifreleme ve şifresini çözme imkanı sağlar. Şifreli ODS dosyası hem Excel hem de OpenOffice’de açılabilir; şifreli ODS dosyası ise yalnızca şifre girildikten sonra OpenOffice tarafından açılabilir. Excel, şifreli ODS dosyasını açamaz ve uyarı mesajı gösterebilir. ODS dosyasına uygulanan şifreleme seçenekleri, diğer dosya türlerine göre farklılık gösterir. Şifrelemek için dosyayı yükleyin ve kaydetmeden önce [**WorkbookSettings.getPassword()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getPassword--) değerini gerçek şifre ile ayarlayın. Çıktı şifreli ODS dosyası yalnızca OpenOffice’de açılabilir.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = RunExamples.Get_SourceDirectory();
// Output directory
const outputDir = RunExamples.Get_OutputDirectory();

// Open an ODS file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleODSFile.ods"));

// Password protect the file
workbook.getSettings().setPassword("1234");

// Save the ODS file
workbook.save(path.join(outputDir, "outputEncryptedODSFile.ods"));
```

ODS dosyasını çözmek için, dosyayı yüklemek için [**LoadOptions.getPassword()**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getPassword--) ile bir parola sağlayın. Dosya yüklendikten sonra, [**WorkbookSettings.getPassword()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getPassword--) dizesini null olarak ayarlayın.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Open an encrypted ODS file
const loadOptions = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Ods);

// Set original password
loadOptions.setPassword("1234");

// Load the encrypted ODS file with the appropriate load options
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleEncryptedODSFile.ods"), loadOptions);

// Set the password to null
workbook.getSettings().setPassword(null);

// Save the decrypted ODS file
workbook.save(outputDir + "outputDecryptedODSFile.ods");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
