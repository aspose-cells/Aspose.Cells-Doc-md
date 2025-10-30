---  
title: Node.js ve C++ kullanarak Sayfa Koruma ve Korumayı Kaldırma  
linktitle: Çalışma Sayfasını Koruma ve Kaldırma  
type: docs  
weight: 40  
url: /tr/nodejs-cpp/protect-and-unprotect-worksheets/  
description: Aspose.Cells for Node.js via C++ kullanarak Excel dosyasının sayfasını koruma veya korumasını kaldırma.  
---  

{{% alert color="primary" %}}  
Excel çalışma sayfanızdaki verilerin yanlışlıkla veya kasıtlı olarak değişmesini, taşınmasını veya silinmesini engellemek için hücreleri kilitleyebilir ve sayfayı bir şifre ile koruyabilirsiniz.  
{{% /alert %}}  

## **MS Excel'de Çalışma Sayfasını Koruma ve Kaldırma**  

**![çalışma sayfasını koruma ve kaldırma](protect-and-unprotect-worksheet.png)**  

1. Tıklayın **İncele > Sayfayı Koru**.  
1. **Şifre kutusuna** bir şifre girin.  
1. **izin ver** seçeneklerini seçin.  
1. **Tamam**'ı seçin, şifreyi teyit etmek için tekrar girin, ardından tekrar **Tamam**'ı seçin.  

## **Aspose.Cells for Node.js via C++ kullanarak Sayfa Koruma**  
Excel dosyalarının çalışma sayfasını korumak için sadece aşağıdaki basit kod satırlarına ihtiyaç vardır.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create a new file.
const workbook = new AsposeCells.Workbook();
// Gets the first worksheet.
const sheet = workbook.getWorksheets().get(0);
// Protect contents of the worksheet.
sheet.protect(AsposeCells.ProtectionType.Contents);
// Protect worksheet with password.
sheet.getProtection().setPassword("test");
// Save as Excel file.
workbook.save("Book1.xlsx");
```  

## **Aspose.Cells for Node.js via C++ kullanarak Sayfa Korumasını Kaldırma**  
Sayfa korumasını kaldırmak Aspose.Cells API ile kolaydır. Eğer sayfa parola korumalıysa, doğru parola gereklidir.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Create a new file.
const workbook = new AsposeCells.Workbook(filePath);
// Gets the first worksheet.
const sheet = workbook.getWorksheets().get(0);
// Protect contents of the worksheet.
sheet.unprotect("password");
// Save Excel file.
workbook.save("Book1.xlsx");
```  

## **Gelişmiş Konular**  
- [Excel XP’den bu yana Gelişmiş Koruma Ayarları](/cells/tr/nodejs-cpp/advanced-protection-settings-since-excel-xp/)  
- [Çalışma Sayfasının Şifre Korunup Korunmadığını Algılama](/cells/tr/nodejs-cpp/detect-if-worksheet-is-password-protected/)  
- [Çalışma Sayfalarını Koruma](/cells/tr/nodejs-cpp/protecting-worksheets/)  
- [Bir Çalışma Sayfasını Korumayı Kaldırma](/cells/tr/nodejs-cpp/unprotect-a-worksheet/)  
- [Çalışma Sayfasını Korumak İçin Kullanılan Şifreyi Doğrulama](/cells/tr/nodejs-cpp/verify-password-used-to-protect-the-worksheet/)  

{{< app/cells/assistant language="nodejs-cpp" >}}
