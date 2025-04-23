---
title: Node.js kullanarak C++ üzerinden Excel hesaplama tablosu dosyalarının ayarlarını yönetin
linktitle: Çalışma Kitabı Ayarları
type: docs
weight: 185
url: /tr/nodejs-cpp/workbook-settings/
description: Aspose.Cells for Node.js via C++ kullanarak Excel dosyalarının ayarlarını yönetin.
---


## **Çalışma Kitabı Ayarları Genel Bakış**
Excel dosyalarıyla çalışmak, Aspose.Cells for Node.js via C++ kullanılarak programatik olarak manipüle edilebilecek çeşitli ayarları içerir. Bu belge, bu ayarları etkili bir şekilde yönetmenin yollarını açıklamaktadır.

## **Olası Kullanım Senaryoları**
Aşağıdaki senaryolar, çalışma kitabı ayarlarını yönetmenizi gerektirebilecek durumları göstermektedir:
- Görünüm seçeneklerini ayarlama
- Hesaplama modunu ayarlama
- Sayfa düzeni parametrelerini yapılandırma

## **Aspose.Cells for Node.js via C++ kullanarak Çalışma Kitabı Ayarlarını Yönetin**
Bu örnek, hesaplama seçenekleri ve görüntü ayarları gibi çalışma kitabı ayarlarını nasıl yöneteceğinizi gösterir.

1. Yeni bir çalışma kitabı oluşturun veya mevcut bir tane yükleyin.
2. Gereksinimlerinize göre çalışma kitabı ayarlarını değiştirin.
3. Değişiklikleri kalıcı kılmak için çalışma kitabını kaydedin.

### **Örnek Kod**

```javascript
const { Workbook, SaveFormat } = require('aspose.cells');

// Create a new workbook
let workbook = new Workbook();

// Access the settings of the workbook
let settings = workbook.getSettings();
settings.setCalculationMode(1); // Manual calculation

// Display options
settings.setShowGridLines(false); // Disable gridlines

// Save the workbook
workbook.save('WorkbookSettingsExample.xlsx', SaveFormat.XLSX);
```

## **Anahtar Çalışma Kitabı Ayarları Özellikleri ve Yöntemleri**
Aspose.Cells for Node.js, çalışma kitabı ayarlarını ayarlamak için çeşitli özellikler ve yöntemler sağlar:
- **Workbook.getSettings()**: Çalışma kitabının ayarlarına erişir.
- **Settings.setCalculationMode(mode)**: Çalışma kitabı için hesaplama modunu ayarlar.
- **Settings.setShowGridLines(value)**: Görüntüde ızgara çizgilerini etkinleştirir veya devre dışı bırakır.

## **Sonuç**
Aspose.Cells for Node.js via C++ kullanarak çalışma kitabı ayarlarını yönetmek oldukça basittir ve Excel dosyası davranışlarını özelleştirmek için çeşitli seçenekler sunar. Kullanılabilir ayarları kullanarak çalışma kitabını özel ihtiyaçlarınıza göre uyarlayabilirsiniz.

