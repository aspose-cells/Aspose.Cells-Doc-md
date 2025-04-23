---
title: Node.js ile C++ kullanarak şekilleri kilitle veya kilidini aç
linktitle: Şekilleri kilitle veya kilidi aç
type: docs
weight: 200
url: /tr/nodejs-cpp/lock-or-unlock-shapes/
description: Bu makale, Shapes u korumak için şekilleri kilitleme veya kilidini açma kodunu gösterir ve Aspose.Cells kitaplığını kullanarak Node.js ile C++ üzerinden şekilleri koruma yöntemini açıklar.
keywords: Node.js ile Şekilleri Kilitle ve Koruma, Node.js kullanarak şekilleri kilitleme veya açma, Shapes u korumak için şekilleri kilitle ya da kilidini aç
---

## **Olası Kullanım Senaryoları**

Bazı durumlarda, istenmeyen durumlar tarafından yok edilmekten korumak için belirli çalışma sayfalarındaki tüm şekilleri korumanız gerekebilir. Bu durumda, belirtilen çalışma sayfasındaki tüm şekilleri kilitlemeniz gerekir. 

Bir elektronik tabloda veya dokümanda şekillerin kilitlenmesi çeşitli nedenlerle faydalı olabilir:
1. Kazara Değişiklikleri Önleme: Şekilleri kilitlemek, kullanıcıların bunları kazara taşımalarını, yeniden boyutlandırmalarını veya silmelerini engeller. Bu, şekillerin açıklama, çizim veya dokümanın tasarımının bir parçası olarak kullanıldığı karmaşık belgelerde özellikle önemlidir.
1. Düzeni ve Tasarımı Koru: Şekiller genellikle bir belgenin düzeninde ve görsel tasarımında önemli rol oynar. Bunları kilitlemek, istenen görünümü koruyarak, belgenin profesyonel ve görsel olarak çekici kalmasını sağlar.
1. Veri Bütünlüğü: Elektronik tablolarda, şekiller önemli veri noktalarını vurgulamak, yorum eklemek veya görsel açıklamalar yapmak için kullanılabilir. Bu şekillerin kilitlenmesi, sağladıkları bağlamsal bilginin doğru ve bütün kalmasını sağlar.
1. Paylaşılan Belgelerde Tutarlılık: Birlikte çalışırken, farklı kullanıcıların uzmanlık seviyeleri farklı olabilir. Şekillerin kilitlenmesi, beklenmedik değişiklikleri engelleyerek belgenin tutarlılığını korumaya yardımcı olur.
1. Güvenlik: Hassas belgelerde şekillerin kilitlenmesi, bilgileri korumak için daha geniş bir stratejinin parçası olabilir. Örneğin, finansal raporlarda veya yasal belgelerde, kilitli şekiller, kritik bağlam sağlayan açıklamaları veya vurguları korumak için kullanılabilir.

Bazen, belirli korumalı çalışma sayfalarında bazı şekilleri değiştirebilmeniz gerekebilir; bu durumda, bu şekilleri kilidini çözmeniz gerekir. Bu makale, belirli şekillerin nasıl kilitlenip kilidinin açılacağını ayrıntılı şekilde tanıtacaktır.

## **Excel'de Şekilleri Nasıl Kilitlersiniz ve Korursunuz**

İşte Microsoft Excel'de hücreleri kilitlemenin yolu:

1. Excel Dosyanızı Açın: Kilitlemek istediğiniz şekillerin bulunduğu Excel dosyasını açın.

1. Şekli Seçin: Kilitlemek istediğiniz şekle tıklayın. Ayrıca, Ctrl tuşunu basılı tutarak birden çok şekli de seçebilirsiniz.

1. Şekil Biçimlendirme Panelini Açın: Seçilen şekle sağ tıklayın ve "Boyut ve Özellikler"i seçin. Alternatif olarak, Şerit üzerindeki "Biçim" sekmesine gidip "Boyut" grubundan, küçük ok işaretine tıklayarak "Şekil Biçimi" panelini açabilirsiniz.
1. Şekli Kilitleyin: "Şekil Biçimi" panelinde, "Boyut ve Özellikler" sekmesine (kare ve ok işareti gibi görünen ikon) gidin. "Özellikler" bölümünde, "Kilitle" kutusunu işaretleyin.
<br>
<img src="1.png" width=60% />
1. Sayfayı Koruyun: Şerit üzerindeki "Gözden Geçir" sekmesine gidin. "Sayfayı Koru" seçeneğine tıklayın. Bir şifre belirleyin (isteğe bağlı) ve izin vermek istediğiniz işlemleri seçin (ör. kilitli hücreleri seçme, hücreleri biçimlendirme vb.). "Tamam" düğmesine tıklayın.
<br>
<img src="2.png" width=60% />

## **Belirli bir çalışma sayfasındaki tüm şekilleri nasıl kilitlersiniz**

Bütün şekilleri korunan bir çalışma sayfasında kilitlemek için, aşağıdaki örnek kodda gösterildiği gibi `worksheet.protect(ProtectionType.Objects)` metodunu kullanabilirsiniz.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

const text = "This is a test";
const worksheet = workbook.getWorksheets().get(0);

let shape = worksheet.getShapes().addTextBox(1, 0, 1, 0, 30, 100);
shape.setText(text);

shape = worksheet.getShapes().addRectangle(5, 0, 1, 0, 30, 100);
shape.setText(text);

shape = worksheet.getShapes().addButton(9, 0, 1, 0, 30, 100);
shape.setText(text);

shape = worksheet.getShapes().addOval(13, 0, 1, 0, 50, 100);
shape.setText(text);

// Protect all shapes in a specified worksheet 
shape.getWorksheet().protect(AsposeCells.ProtectionType.Objects); // Protects the entire worksheet.
// or shape.getWorksheet().protect(AsposeCells.ProtectionType.All); // Protects all shapes in the specified worksheet.
// or worksheet.protect(AsposeCells.ProtectionType.Objects); // Protects the entire worksheet.
// or worksheet.protect(AsposeCells.ProtectionType.All); // Protects all shapes in the specified worksheet.

workbook.save("Locked.xlsx", AsposeCells.SaveFormat.Xlsx);
```

## **Korunan bir çalışma sayfasında belirli şekillerin kilidini nasıl açarsınız**

Korunan bir çalışma sayfasında belirli bir şekli çözmek için, `shape.isLocked` kullanılır, aşağıdaki örnek kodda gösterildiği gibi.

Not: `shape.isLocked` yalnızca çalışma sayfası korunduğunda anlamlıdır.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Locked.xlsx");

// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Get protected worksheet
const worksheet = workbook.getWorksheets().get(0);

// Get the specified shape to be unlocked
const shape = worksheet.getShapes().get("TextBox 1");

// Unlock the specified shape
if (!worksheet.getProtection().getAllowEditingObject() && shape.isLocked()) {
shape.setIsLocked(false);
}

workbook.save("UnLocked.xlsx", AsposeCells.SaveFormat.Xlsx);
```

