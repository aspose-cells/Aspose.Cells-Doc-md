---  
title: Excel dosyalarını Node.js kullanarak şifreleme ve şifresini çözme  
linktitle: Excel Dosyalarını Şifrelemek ve Çözmek  
type: docs  
weight: 10  
url: /tr/nodejs-cpp/encrypt-and-decrypt-excel-files/  
description: Node.js kullanarak Excel dosyasını şifreleme ve şifresini çözme, kilitleme ve kilidini açma  
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

## **Aspose.Cells for Node.js via C++ ile Excel dosyasını Şifrele**  

Aşağıdaki örnek, Aspose.Cells API kullanarak bir Excel dosyasını nasıl şifreleyip parola koruma altına alacağınızı gösterir.  

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

### **Değişiklik yapmak için Parola Belirleme Seçeneği**  

Aşağıdaki örnek, mevcut bir dosya için Aspose.Cells API'sını kullanarak **Değiştirilecek Parolayı** Microsoft Excel seçeneğini nasıl ayarlayacağını göstermektedir.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a Workbook object.
// Open an excel file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Book1.xls"));

// Set the password for modification.
workbook.getSettings().getWriteProtection().setPassword("1234");

// Save the excel file.
workbook.save(path.join(dataDir, "SpecifyPasswordToModifyOption.out.xls"));
```  


## **Aspose.Cells for Node.js via C++ ile Excel dosyasını Şifre Çöz**  
Bir parola ile korunan Excel dosyasını açmak ve şifreyi çözmek çok kolaydır; aşağıdaki kod örneğinde gösterildiği gibi Aspose.Cells API kullanabilirsiniz:  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Open encrypted file with password.
const loadOptions = new AsposeCells.LoadOptions();
loadOptions.setPassword("password");
const workbook = new AsposeCells.Workbook(filePath, loadOptions);

// Remove password.
workbook.getSettings().setPassword(null);

// Save the file.
workbook.save(filePath);
```  


## **Gelişmiş Konular**  
- [ODS dosyalarını şifreleme ve şifresini çözme](/cells/tr/nodejs-cpp/encrypt-and-decrypt-ods-files/)  
- [Güçlü Şifreleme Türü Belirleme](/cells/tr/nodejs-cpp/setting-strong-encryption-type/)  
- [Çalışma Kitabını Yazma Koruması Sırasında Yazar Belirtme](/cells/tr/nodejs-cpp/specify-author-while-write-protecting-workbook/)  
- [Şifreli Dosyaların Parolasını Doğrulama](/cells/tr/nodejs-cpp/verify-password-of-encrypted-excel-and-ods-files/)  


{{< app/cells/assistant language="nodejs-cpp" >}}
