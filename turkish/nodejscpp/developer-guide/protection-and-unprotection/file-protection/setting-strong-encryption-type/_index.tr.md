---  
title: Node.js aracılığıyla C++ kullanarak Güçlü Şifreleme Türü Ayarlama  
linktitle: Güçlü Şifreleme Türü Ayarlama  
type: docs  
weight: 60  
url: /tr/nodejs-cpp/setting-strong-encryption-type/  
description: Aspose.Cells for Node.js via C++ kullanarak Excel dosyaları için güçlü şifreleme türlerini nasıl ayarlayacağınızı öğrenin.  
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

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Instantiate a Workbook object.
// Open an excel file.
const workbook = new AsposeCells.Workbook(filePath);

// Specify Strong Encryption type (RC4,Microsoft Strong Cryptographic Provider).
workbook.setEncryptionOptions(AsposeCells.EncryptionType.StrongCryptographicProvider, 128);

// Password protect the file.
workbook.getSettings().setPassword("1234");

// Save the Excel file.
workbook.save(path.join(dataDir, "encryptedBook1.out.xls"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
