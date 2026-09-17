---
title: Hücreye Görsel Ekleme
linktitle: Hücreye Görsel Ekleme
description: Aspose.Cells, elektronik tablo dosyalarıyla çalışmak için bir Node.js via Java kütüphanesidir. Bu makale, bir resmi hücrenin üzerine kayan bir resim yerleştirerek veya görüntüyü doğrudan hücreye gömerek tek bir hücreye tam olarak sığdırmayı açıklar.
keywords: Aspose.Cells, Node.js via Java kütüphanesi, elektronik tablo, görsel ekleme, görsel gömme, hücredeki resim, resmi hücreye sığdırma, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /tr/nodejs-java/inserting-an-image-into-a-cell/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells, bir görüntüyü tek bir hücreyle ilişkilendirmek için iki farklı yol sunar. Kayan resim, çalışma sayfası çizim katmanında bir hücre aralığının üzerine yerleştirilen bir şekildir; gömülü görsel ise hücrenin kendisinin içinde saklanır ve hücrenin görüntüleme alanına otomatik olarak ölçeklenir. Düzen gereksinimlerinize en uygun yaklaşımı seçin.
{{% /alert %}}

## **Giriş**
Bir resmi tek bir hücreye tam olarak sığdırmak, görsel raporlar, ürün katalogları, çalışan rehberleri, panolar veya envanter listeleri olarak işlev gören elektronik tablolar tasarlarken sık karşılaşılan bir gereksinimdir. Görüntüyü birçok hücreye yaymak veya çalışma sayfasına gevşek bir şekilde yerleştirmek yerine, kendisine sahip olan hücreyle hizalı kalan temiz, hücreye bağlı bir görsel isteyebilirsiniz.
Aspose.Cells bu senaryoyu iki tamamlayıcı şekilde destekler:
- **Yaklaşım 1 — Hücrenin üzerine kayan bir resim yerleştirin.** Çalışma sayfasına bir `Picture` ekleyin, `Placement` özelliğini `MoveAndSize` olarak ayarlayın ve resmin tam olarak bir hücreyi kaplaması için çapa hücrelerini (`UpperLeftRow`, `UpperLeftColumn`, `LowerRightRow`, `LowerRightColumn`) ayarlayın.
- **Yaklaşım 2 — Görüntüyü doğrudan bir hücreye gömün.** Görüntü baytlarını hücrenin `EmbeddedImage` özelliğine atayın. Görsel, hücrenin görüntüleme alanına sığacak şekilde otomatik olarak ölçeklenir ve hücreyle birlikte taşınır.
Bu makalenin geri kalanı her iki yaklaşımı da adım adım açıklar, ilgili API'leri tanımlar ve kodda nasıl kullanılacağını gösterir.

## **Yaklaşım 1: Hücrenin Üzerine Bir Resim Yerleştirme**
Kayan resim, çalışma sayfası çizim katmanında bulunan bir `Picture` nesnesidir. Herhangi bir tek hücrenin parçası olmasa da, bir hücre aralığına çapalanmıştır. Resmin çapa hücreleri — sol üst ve sağ alt köşeleri — çalışma sayfasındaki görsel kapsamını belirler. Varsayılan olarak, yeni eklenen bir resim birkaç hücreyi kaplar.
Kayan bir resmin **tam olarak bir hücreyi** kaplamasını sağlamak için şunları yapmanız gerekir:
1. Resmi `worksheet.getPictures().add(int row, int column, InputStream stream)` kullanarak ekleyin; bu yöntem yeni resmi verilen hücreye çapalar.
2. Resmin sınırlayıcı dikdörtgeni hedef hücreyle çakışacak şekilde dört çapa özelliğini ayarlayın.
3. Kullanıcı sütun genişliğini veya satır yüksekliğini değiştirdiğinde resmin alttaki hücreyle birlikte hareket etmesi ve yeniden boyutlandırılması için `picture.setPlacement(PlacementType.MOVE_AND_SIZE)` ayarlayın.

### **Resmi Tek Bir Hücreye Çapalama**
Resmin çapası dört sıfır tabanlı dizin özelliği tarafından tanımlanır:
- `picture.setUpperLeftRow(int)` — resmin üst kenarının satır dizini.
- `picture.setUpperLeftColumn(int)` — resmin sol kenarının sütun dizini.
- `picture.setLowerRightRow(int)` — resmin alt kenarının satır dizini. Resmin alt kenarının `r` satırının altına yerleşmesini sağlamak için bunu `r + 1` olarak ayarlayın.
- `picture.setLowerRightColumn(int)` — resmin sağ kenarının sütun dizini. Resmin sağ kenarının `c` sütununun sağına yerleşmesini sağlamak için bunu `c + 1` olarak ayarlayın.

{{% alert color="primary" %}}
Aspose.Cells'deki satır ve sütun dizinleri **sıfır tabanlıdır**. C6 hücresinin satır dizini 5 ve sütun dizini 2'dir. Sağ alt çapasındaki off-by-one hataları, resimlerin bitişik hücreye taşmış gibi görünmesinin en yaygın kaynağıdır.

### **Yerleştirme Davranışını Kontrol Etme**
`Picture.Placement`, kullanıcı alttaki satırı veya sütunu yeniden boyutlandırdığında resmin nasıl davranacağını kontrol eden `PlacementType` türünde bir enum'dur. Tek hücreli resim için önerilen değer, resmin alttaki hücreyle birlikte hareket etmesini ve yeniden boyutlandırılmasını sağlayarak tam sığmayı koruyan `PlacementType.MoveAndSize`'tır.

### **Adım Adım Talimatlar**
1. Yeni bir `Workbook` oluşturun (veya var olanı açın).
2. Hedef `Worksheet`'e `workbook.getWorksheets().get(0)` üzerinden erişin.
3. Görüntü dosyasını diskten bir `InputStream`'e açın (örneğin, `FileInputStream` kullanarak) böylece akış düzgün şekilde kapatılır.
4. C6 hücresine çapalanmış bir resim eklemek için `worksheet.getPictures().add(5, 2, stream)` çağırın. Döndürülen `Picture` referansını yakalayın.
5. Resmin yalnızca C6 hücresini kaplaması için dört çapa koordinatını ayarlayın: `UpperLeftRow = 5`, `UpperLeftColumn = 2`, `LowerRightRow = 6`, `LowerRightColumn = 3`.
6. Sütun veya satır yeniden boyutlandırıldığında resmin C6 ile hizalı kalmasını sağlamak için `picture.setPlacement(PlacementType.MOVE_AND_SIZE)` ayarlayın.
7. İsteğe bağlı olarak, yalnızca C6 hücresinin resmi içerdiğini göstermek için çevresindeki hücrelere örnek metin ekleyin.
8. Çalışma kitabını diskte bir `.xlsx` dosyası olarak kaydedin.
Aşağıdaki kod tüm yaklaşımı gösterir.

```javascript
const AsposeCells = require("aspose.cells-node");
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);
var picIndex = worksheet.getPictures().add(5, 2, "logo.png");
var picture = worksheet.getPictures().get(picIndex);
picture.setUpperLeftRow(5);
picture.setUpperLeftColumn(2);
picture.setLowerRightRow(6);
picture.setLowerRightColumn(3);
picture.setPlacement(AsposeCells.PlacementType.MoveAndSize);
workbook.save("output.xlsx", AsposeCells.SaveFormat.Xlsx);
```

## **Yaklaşım 2: Görüntüyü Doğrudan Bir Hücreye Gömme**
Aspose.Cells ayrıca hücreye bağlı görseller için daha basit bir mekanizma sunar: `Cell.EmbeddedImage` özelliği. Görüntü baytlarını bu özelliğe atamak, görüntüyü satır içi içerikmiş gibi hücrenin kendisine ekler.

### **Gömülü Görseller Nasıl Çalışır**
- Görsel, çizim katmanında bir şekil olarak değil, hücre içeriğinin bir parçası olarak saklanır.
- Görsel, hücrenin görüntülenen sınırlarının içine sığacak şekilde otomatik olarak ölçeklenir. Çapa koordinatları veya yerleştirme ayarları gerekmez.
- Hücre, formüller tarafından referans alınabilen, bir satırın parçası olarak sıralanabilen veya diğer hücre düzeyindeki işlemlerde kullanılabilen gerçek bir adrese sahip gerçek bir hücre olarak kalır.
Bu, amacınız basitçe "bu hücrenin içinde yaşayan bir görsel" olduğunda `Cell.EmbeddedImage`'ı en kısa seçenek haline getirir.

### **Adım Adım Talimatlar**
1. Yeni bir `Workbook` oluşturun (veya var olanı açın).
2. Hedef `Worksheet`'e `workbook.getWorksheets().get(0)` üzerinden erişin.
3. Görüntü dosyasını diskten bir bayt dizisine okuyun (örneğin, `java.nio.file.Files` üzerinden `Files.readAllBytes` kullanarak).
4. Hedef hücreye bir referans alın — `worksheet.getCells().get("C6")` veya `worksheet.getCells().get(5, 2)` aracılığıyla.
5. Bayt dizisini `cell.setEmbeddedImage(bytes)` aracılığıyla hücrenin `EmbeddedImage` özelliğine atayın.
6. İsteğe bağlı olarak, gömülü görsele daha belirgin bir görünüm kazandırmak için hedef satırın ve sütunun satır yüksekliğini ve sütun genişliğini ayarlayın.
7. Çalışma kitabını diskte bir `.xlsx` dosyası olarak kaydedin.
Aşağıdaki kod tüm yaklaşımı gösterir.

```javascript
const AsposeCells = require("aspose.cells-node");
const fs = require("fs");
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);
// Hedef hücre C6'yı al
var cell = worksheet.getCells().get("C6");
// Görüntü dosyasını bir bayt dizisine oku
var imageData = fs.readFileSync("logo.png");
// Görüntüyü doğrudan hücreye göm
cell.setEmbeddedImage(imageData);
// Gömülü görüntünün daha görünür olması için isteğe bağlı olarak satır yüksekliğini ve sütun genişliğini ayarla
worksheet.getCells().setColumnWidth(2, 30);   // Sütun C (indeks 2)
worksheet.getCells().setRowHeight(5, 100);     // Satır 6 (indeks 5)
// Ortaya çıkan çalışma kitabını .xlsx dosyası olarak kaydet
workbook.save("output.xlsx", AsposeCells.SaveFormat.Xlsx);
```

## **Doğru Yaklaşımı Seçme**
Her iki yaklaşım da tek bir hücrenin içine sığan bir resim üretir, ancak resmin nasıl saklandığı ve nasıl davrandığı konusunda farklılık gösterir:
- **Şu durumlarda kayan bir resim kullanın (Yaklaşım 1):**
  - Yerleştirme, katmanlama veya diğer çizim nesneleriyle hizalama üzerinde daha hassas bir kontrol gerektirdiğinizde.
  - Resmin seçilebilen, yeniden sıralanabilen veya diğer şekillerle gruplanabilen bir şekil olarak davranmasını istediğinizde.
  - Zaten `PictureCollection` ile çalışan kodla eski sürüm uyumluluğu gerektirdiğinizde.
  - Çalışma sayfası düzenine göre çapa koordinatlarını dinamik olarak hesaplamanız gerektiğinizde.
- **Şu durumlarda gömülü bir görsel kullanın (Yaklaşım 2):**
  - Bir hücreye bir görüntünün mümkün olan en basit eklenmesini istediğinizde.
  - Görselin diğer hücre içerikleri gibi hücreyle birlikte taşınması gerektiğinde.
{{% /alert %}}

{{< app/cells/assistant language="javascript" >}}