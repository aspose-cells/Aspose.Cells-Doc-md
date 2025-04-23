---  
title: Node.js üzerinden C++ kullanarak Kullanıcıların Excel Dosyasını Yazdırmasını Nasıl Engellersiniz  
linktitle: Excel Dosyasının Yazdırılmasını Nasıl Engelleriz  
type: docs  
weight: 600  
url: /tr/nodejs-cpp/how-to-prevent-printing-excel/  
description: Aspose.Cells for Node.js via C++ kullanarak kullanıcıların Excel dosyalarını yazdırmasını nasıl engelleyeceğinizi öğrenin.  
keywords: excel yazdırma, excel yazdırmayı engelleme, kullanıcıların excel i yazdırmaması nasıl engellenir, excel yazdırma engelleme, çalışma kitabının yazdırılmasını engelleme, Kullanıcıların VBA ile tam çalışma kitabını yazdırmalarını engelleyin.  
---  

## **Olası Kullanım Senaryoları**  
Günlük çalışmalarımızda, Excel dosyasında önemli bilgiler olabilir; iç verilerin yayılmasını önlemek için şirketimiz bunların yazdırılmasını engelleyecektir. Bu belge, başkalarının Excel dosyalarını yazdırmasını nasıl engelleyeceğinizi anlatacaktır.  

## **MS-Excel'de Kullanıcıların Dosyayı Yazdırmasını Nasıl Engelleriz**  
Aşağıdaki VBA kodunu kullanarak belirli dosyanızın yazdırılmasını engelleyebilirsiniz.  
1. Başkalarına yazdırmalarına izin vermediğiniz çalışma kitabınızı açın.  
1. Excel şeridinde "Geliştirici" sekmesini seçin ve "Kod Görüntüle" düğmesine tıklayın "Kontroller" bölümünde. Alternatif olarak, Microsoft Visual Basic for Applications penceresini açmak için ALT + F11 tuşlarını basılı tutabilirsiniz.  
<br>  
<img src="1.png" width=70% />  
1. Ardından sol Project Explorer'da, BuÇalışma kitabına çift tıklayın ve modülü açın, birkaç VBA kodu ekleyin.  
<br>  
<img src="2.png" width=70% />  
1. Daha sonra bu kodu kaydedin ve kapatın, tekrar çalışma kitabına dönün ve şimdi örnek dosyayı yazdırmak istediğinizde, yazdırılamayacak ve aşağıdaki uyarı kutusunu alacaksınız:  
<br>  
<img src="3.png" width=70% />  

## **Aspose.Cells for Node.js via C++ kullanarak Kullanıcıların Excel Dosyasını Yazdırmasını Nasıl Engellersiniz**  

Aşağıdaki örnek kod, kullanıcıların Excel dosyasını yazdırmasını nasıl engelleyeceğinizi gösterir:  

1. [Örnek dosyayı](örnek.xlsx) yükleyin.  
1. VbaProject özelliğinden VbaModuleCollection nesnesini alın.  
1. "ThisWorkbook" adıyla VbaModule nesnesini alın.  
1. VbaModule'nin kodları özelliğini ayarlayın.  
1. Örnek dosyayı [xlsm biçimine](out.xlsm) kaydedin.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Sample.xlsx");

// Loads the workbook which contains hidden external links
const wb = new AsposeCells.Workbook(filePath);
const modules = wb.getVbaProject().getModules();
modules.get("ThisWorkbook").setCodes("Private Sub Workbook_BeforePrint(Cancel As Boolean)\r\n  Cancel = True\r\n  MsgBox \"Refusing to print in paperless office\"\r\nEnd Sub\r\n");

wb.save("out.xlsm");
```  

