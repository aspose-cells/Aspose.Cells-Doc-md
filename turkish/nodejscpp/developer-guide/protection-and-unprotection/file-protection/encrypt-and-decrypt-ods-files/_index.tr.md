---
title: ODS dosyalarını Node.js ve C++ kullanarak şifreyle koruma ve şifre çözme
linktitle: ODS Dosyalarını Şifreleme ve Şifre Çözme
type: docs
weight: 10
url: /tr/nodejs-cpp/encrypt-and-decrypt-ods-files/
description: Aspose.Cells for Node.js via C++ kullanarak ODS dosyalarını şifreleyin ve koruyun. 
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

## **Aspose.Cells for Node.js via C++ ile ODS dosyasını şifreleyin**
Bir ODS dosyasını şifrelemek için, dosyayı yükleyin ve kaydetmeden önce [**WorkbookSettings.getPassword()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getPassword--) değerini gerçek parola ile ayarlayın. Çıktı şifrelenmiş ODS dosyası yalnızca OpenOffice'da açılabilir.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "source");
const outputDir = path.join(__dirname, "output");

// Open an ODS file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleODSFile.ods"));

// Password protect the file
workbook.getSettings().setPassword("1234");

// Save the ODS file
workbook.save(path.join(outputDir, "outputEncryptedODSFile.ods"));
```

## **Aspose.Cells for Node.js via C++ ile ODS dosyasını deşifre edin**
Bir ODS dosyasını deşifre etmek için, dosyayı [**LoadOptions.getPassword()**](https://reference.aspose.com/cells/nodejs-cpp/loadoptions/#getPassword--) içeren bir parola sağlayarak yükleyin. Dosya yüklendikten sonra, [**WorkbookSettings.getPassword()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getPassword--) dizesini null olarak ayarlayın.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

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
