---  
title: Node.js ve C++ kullanarak Çalışma Kitabı nda gizli Dış Bağlantı olup olmadığını kontrol edin  
linktitle: Çalışma Kitabı gizli Harici Bağlantıları içeriyorsa kontrol edin  
type: docs  
weight: 230  
url: /tr/nodejs-cpp/check-if-workbook-contains-hidden-external-links/  
description: Aspose.Cells for Node.js via C++ kullanarak bir çalışma kitabının gizli harici bağlantılar içerip içermediğini nasıl kontrol edeceğinizi öğrenin.  
---  

## **Olası Kullanım Senaryoları**  
Bazen, çalışma kitabı gizli olan ve Microsoft Excel'de görüntülenemeyen harici bağlantılar içerir. Aspose.Cells, görünür veya gizli olsun tüm harici bağlantıları getirir. Ancak, [ExternalLink.isVisible()](https://reference.aspose.com/cells/nodejs-cpp/externallink/#isVisible--) özelliğini kontrol ederek harici bağlantının görünür olup olmadığını kontrol edebilirsiniz.

## **Çalışma Kitabı gizli Harici Bağlantıları içeriyorsa kontrol edin**  
Aşağıdaki örnek kod, gizli harici bağlantılar içeren [kaynak Excel dosyasını](5115413.xlsx) yükler. Bu bağlantılar Microsoft Excel'de görüntülenemez, ancak çalışma kitabı içinde mevcuttur. [ExternalLink.getDataSource()](https://reference.aspose.com/cells/nodejs-cpp/externallink/#getDataSource--) ve [ExternalLink.isReferred()](https://reference.aspose.com/cells/nodejs-cpp/externallink/#isReferred--) özelliklerini yazdırdıktan sonra, [ExternalLink.isVisible()](https://reference.aspose.com/cells/nodejs-cpp/externallink/#isVisible--) özelliğini ekrana getirir. Aşağıdaki konsol çıktısında, tüm harici bağlantılarının görünmediğini görebilirsiniz.

### **Örnek Kod**  
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access the external link collection of the workbook
const links = workbook.getWorksheets().getExternalLinks();

// Print all the external links and check their IsVisible property
for (let i = 0; i < links.getCount(); i++) {
console.log("Data Source: " + links.get(i).getDataSource());
console.log("Is Referred: " + links.get(i).getIsReferred());
console.log("Is Visible: " + links.get(i).getIsVisible());
console.log();
}
```  

### **Konsol Çıktısı**  
Aşağıdaki örnek kodun, verilen [örnek excel dosyası](5115413.xlsx) ile çalıştırılması sonucu konsol çıktısı aşağıdaki gibidir.

{{< highlight java >}}  
 Data Source: C:\International\DDB\FAS 133\Swap Rates\GS_1M_3M_1_2_5_¥$_(B)IRSwaps_0400.xls  

Is Referred: True  

Is Visible: False  

Data Source: C:\DIST DAY\MAY TEMPLATES\030601t.xls  

Is Referred: True  

Is Visible: False  

Data Source: C:\AREVIEW\2002 Controllable\Autobrct.xls  

Is Referred: True  

Is Visible: False  

Data Source: C:\CARDSFO\Main Files\Rate Forecast\FY 11\IFR 11 01 (New Model REPORTS 11.08.07).xls  

Is Referred: True  

Is Visible: False  
{{< /highlight >}}  
