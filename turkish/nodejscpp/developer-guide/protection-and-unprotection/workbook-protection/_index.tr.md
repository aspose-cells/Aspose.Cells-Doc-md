---  
title: Node.js ve C++ kullanarak Çalışma Kitabı Yapısını Korumaya veya Korumayı Kaldırmaya  
linktitle: Çalışma Kitabı Yapısını Koruma Altına Alma ve Korumasız Yapma  
type: docs  
weight: 40  
url: /tr/nodejs-cpp/protect-and-unprotect-workbook-structure/  
description: Node.js ve C++ kullanarak Excel dosyalarının çalışma kitabı yapısını koruyabilir veya korumasını kaldırabilirsiniz.  
---  


{{% alert color="primary" %}}  
Diğer kullanıcıların gizli çalışma sayfalarını görüntülemesini, çalışma sayfalarını ekleme, taşıma, silme veya gizleme işlemlerini yapmalarını engellemek ve çalışma sayfalarını yeniden adlandırmak için Excel çalışma kitabınızın yapısını bir şifre ile koruyabilirsiniz.  
{{% /alert %}}  


## **MS Excel'de Çalışma Kitabı Yapısını Koruma ve Kaldırma**  

**![çalışma kitabı yapısını koruma ve kaldırma](protect-and-unprotect-workbook-structure.png)**  

1. Tıklayın **İncele > Çalışma Kitabını Koru**.  
1. **Şifre kutusuna** bir şifre girin.  
1. **Tamam**'ı seçin, şifreyi teyit etmek için tekrar girin, ardından tekrar **Tamam**'ı seçin.  


## **Aspose.Cells for Node.js via C++ kullanarak Çalışma Kitabı Yapısını Korumaya**  
Excel dosyalarının çalışma sayfasını korumak için sadece aşağıdaki basit kod satırlarına ihtiyaç vardır.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Create a new file.
const workbook = new AsposeCells.Workbook();
// Protect workbook structure.
workbook.protect(AsposeCells.ProtectionType.Structure, "password");
// Save Excel file.
workbook.save(filePath);
```  

## **Aspose.Cells for Node.js via C++ kullanarak Çalışma Kitabı Yapısının Korumasını Kaldırma**  
Aspose.Cells API ile çalışma kitabı yapısını korumak kolaydır.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Open an Excel file which workbook structure is protected.
const workbook = new AsposeCells.Workbook(filePath);
// Unprotect workbook structure.
workbook.unprotect("password");
// Save Excel file.
workbook.save(filePath);
```  

{{% alert color="primary" %}}  
Not: Doğru bir şifre gerekli.  
{{% /alert %}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
