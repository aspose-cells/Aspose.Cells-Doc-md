---
title: Sayfa Ayarları Özellikleri Node.js ve C++ ile
linktitle: Sayfa Ayarı Özellikleri
type: docs
weight: 60
url: /tr/nodejs-cpp/page-setup-features/
description: Aspose.Cells for Node.js via C++ kullanılarak sayfa ayar özelliklerini keşfedin. Sayfa boyutları, yönleri ve ayarlarını nasıl yapılandıracağınızı öğrenin.
keywords: Sayfa ayarları Node.js ve C++ ile, Sayfa boyutu yapılandırma Node.js ve C++ ile, Sayfa yönü ayarları Node.js ve C++ ile
---



## **Giriş**
Aspose.Cells for Node.js via C++ ile, bir Excel çalışma kitabının çeşitli sayfa ayar özelliklerini manipüle edebilirsiniz. Bu özellikler arasında sayfa boyutu, yönü, kenar boşlukları ve daha fazlası bulunur. Bu özelliklerin doğru yapılandırılması, daha iyi bir yazdırma ve görüntüleme deneyimi sağlar.

## **Sayfa Boyutu ve Yönü Ayarlama**
Bir çalışma sayfasının sayfa boyutunu ve yönünü `PageSetup` sınıfını kullanarak belirtebilirsiniz. Bu sınıf, sayfa boyutları ve düzenini yönetmek için çeşitli özellikler sağlar.

### **Örnek Kod**
Sayfa boyutunu ve yönünü ayarlamak için örnek kod parçası burada.

```javascript
const { Workbook } = require("aspose.cells");

// Create a new workbook
let workbook = new Workbook();
let worksheet = workbook.getWorksheets().get(0);

// Set the page size
worksheet.getPageSetup().setPaperSize(0); // A4 size

// Set the page orientation
worksheet.getPageSetup().setOrientation(1); // Landscape orientation

// Save the workbook
workbook.save("PageSetupExample.xlsx");
```

## **Kenar Boşlukları Ayarlama**
Ayrıca, aynı `PageSetup` sınıfını kullanarak sayfa kenar boşluklarını da ayarlayabilirsiniz. Kenar boşlukları sol, sağ, üst ve alt olarak ayarlanabilir.

### **Örnek Kod**
İşte, çalışma sayfasının kenar boşluklarını ayarlama adımları.

```javascript
// Set the margins
worksheet.getPageSetup().setLeftMargin(0.5);
worksheet.getPageSetup().setRightMargin(0.5);
worksheet.getPageSetup().setTopMargin(1.0);
worksheet.getPageSetup().setBottomMargin(1.0);

// Save the workbook
workbook.save("PageMarginsExample.xlsx");
```

## **Sonuç**
Bu belgeyle, Excel'de sayfa ayar özelliklerini Aspose.Cells for Node.js via C++ kullanarak nasıl manipüle edeceğinizi öğrendiniz. `PageSetup` sınıfını etkin kullanarak, çalışma sayfalarınızın yazdırılma ve görüntülenme biçimini kontrol edebilir, genel sunumu iyileştirebilirsiniz.

---
{{< app/cells/assistant language="nodejs-cpp" >}}
