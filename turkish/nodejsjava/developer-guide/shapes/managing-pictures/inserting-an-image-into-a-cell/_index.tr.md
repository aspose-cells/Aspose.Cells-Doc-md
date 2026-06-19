---
title: Bir Hücreye Resim Ekleme
description: Aspose.Cells, elektronik tablo dosyalarıyla çalışmak için kullanılan bir Node.js via Java kütüphanesidir. Bu makale, resmi tek bir hücre boyutuna tam olarak sığdırmayı iki farklı yaklaşımla açıklar: hücrenin üzerine kayan bir resim yerleştirme veya resmi doğrudan hücrenin içine gömme.
keywords: Aspose.Cells, Node.js via Java kütüphanesi, elektronik tablo, resim ekleme, resmi gömme, hücredeki resim, resmi hücreye sığdırma, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /tr/nodejs-java/inserting-an-image-into-a-cell/
---

{{% alert color="primary" %}}

Aspose.Cells, bir resmi tek bir hücreyle ilişkilendirmek için iki farklı yol sunar. Kayan resim, çalışma sayfası çizim katmanında bir hücre aralığının üzerinde görsel olarak yer alan bir şekildir; gömülü resim ise hücrenin kendi içinde depolanır ve hücrenin görüntü alanına otomatik olarak ölçeklenir. Düzen gereksinimlerinize en uygun yaklaşımı seçin.

{{% /alert %}}

## **Giriş**

Bir resmi tam olarak tek bir hücreye sığdırmak; görsel raporlar, ürün katalogları, çalışan rehberleri, panolar veya envanter listeleri olarak işlev gören elektronik tablolar tasarlarken sık karşılaşılan bir gereksinimdir. Resmi birçok hücreye yaymak veya çalışma sayfasına gevşek bir şekilde yerleştirmek yerine, sahibi olan hücreyle hizalı kalan, temiz ve hücreye bağlı bir resim isteyebilirsiniz.

Aspose.Cells bu senaryoyu birbirini tamamlayan iki şekilde destekler:

- **Yaklaşım 1 — Hücrenin üzerine kayan bir resim yerleştirin.** Çalışma sayfasına bir `Picture` ekleyin, `Placement` özelliğini `MoveAndSize` olarak ayarlayın ve resmin tam olarak bir hücreyi kapsaması için bağlantı hücrelerini (`UpperLeftRow`, `UpperLeftColumn`, `LowerRightRow`, `LowerRightColumn`) düzenleyin.
- **Yaklaşım 2 — Resmi doğrudan bir hücrenin içine gömün.** Hücrenin `EmbeddedImage` özelliğine resim baytlarını atayın. Resim, hücrenin görüntü alanına sığacak şekilde otomatik olarak ölçeklenir ve hücreyle birlikte taşınır.

Bu makalenin geri kalanı her iki yaklaşımı da adım adım açıklar, ilgili API'leri anlatır ve bunların kodda nasıl kullanılacağını gösterir.

## **Yaklaşım 1: Hücrenin Üzerine Bir Resim Yerleştirme**

Kayan resim, çalışma sayfası çizim katmanında bulunan bir `Picture` nesnesidir. Herhangi bir tek hücrenin parçası olmasa da bir hücre aralığına bağlıdır. Resmin bağlantı hücreleri — sol üst ve sağ alt köşeleri — çalışma sayfasındaki görsel kapsamını belirler. Varsayılan olarak, yeni eklenen bir resim birkaç hücreyi kapsar.

Kayan bir resmi **tam olarak tek bir hücreyi** kapsayacak şekilde ayarlamak için şunları yapmanız gerekir:

1. Resmi `worksheet.getPictures().add(int row, int column, InputStream stream)` kullanarak ekleyin; bu, yeni resmi belirtilen hücreye bağlar.
2. Resmin sınırlayıcı dikdörtgeni hedef hücreyle çakışacak şekilde dört bağlantı özelliğini ayarlayın.
3. Kullanıcı sütun genişliğini veya satır yüksekliğini değiştirdiğinde resmin alttaki hücreyle birlikte hareket etmesi ve yeniden boyutlandırılması için `picture.setPlacement(PlacementType.MOVE_AND_SIZE)` ayarlayın.

### **Resmi Tek Bir Hücreye Bağlama**

Resmin bağlantısı, sıfır tabanlı dizin özellikleriyle tanımlanır:

- `picture.setUpperLeftRow(int)` — resmin üst kenarının satır dizini.
- `picture.setUpperLeftColumn(int)` — resmin sol kenarının sütun dizini.
- `picture.setLowerRightRow(int)` — resmin alt kenarının satır dizini. Resmin alt kenarını `r` satırının altına yerleştirmek için bu değeri `r + 1` olarak ayarlayın.
- `picture.setLowerRightColumn(int)` — resmin sağ kenarının sütun dizini. Resmin sağ kenarını `c` sütununun sağına yerleştirmek için bu değeri `c + 1` olarak ayarlayın.

Örneğin, resmi tam olarak **C6** hücresine (satır dizini `5`, sütun dizini `2`) sığdırmak için `UpperLeftRow = 5`, `UpperLeftColumn = 2`, `LowerRightRow = 6` ve `LowerRightColumn = 3` olarak ayarlayın.

{{% alert color="primary" %}}

Aspose.Cells'te satır ve sütun dizinleri **sıfır tabanlıdır**. C6 hücresinin satır dizini 5 ve sütun dizini 2'dir. Sağ-alt bağlantı noktasındaki off-by-one hataları, resimlerin bitişik hücreye taşmış gibi görünmesinin en yaygın nedenidir.

{{% /alert %}}

### **Yerleştirme Davranışını Kontrol Etme**

`Picture.Placement`, kullanıcı alttaki satır veya sütunu yeniden boyutlandırdığında resmin nasıl davranacağını kontrol eden `PlacementType` türünde bir numaralandırmadır. Tek hücreli bir resim için önerilen değer `PlacementType.MoveAndSize` olup, resmin alttaki hücreyle birlikte hareket etmesini ve yeniden boyutlandırılmasını sağlayarak tam sığmayı korur.

### **Adım Adım Talimatlar**

1. Yeni bir `Workbook` oluşturun (veya var olan birini açın).
2. `workbook.getWorksheets().get(0)` üzerinden hedef `Worksheet`'e erişin.
3. Resim dosyasını diskten bir `InputStream`'e açın (örneğin, `FileInputStream` kullanarak) böylece akış düzgün bir şekilde kapatılır.
4. C6 hücresine bağlı bir resim eklemek için `worksheet.getPictures().add(5, 2, stream)` çağırın. Döndürülen `Picture` referansını yakalayın.
5. Resmin yalnızca C6 hücresini kapsaması için dört bağlantı koordinatını ayarlayın: `UpperLeftRow = 5`, `UpperLeftColumn = 2`, `LowerRightRow = 6`, `LowerRightColumn = 3`.
6. Sütun veya satır yeniden boyutlandırıldığında resmin C6 ile hizalı kalması için `picture.setPlacement(PlacementType.MOVE_AND_SIZE)` ayarlayın.
7. İsteğe bağlı olarak, yalnızca C6 hücresinin resmi içerdiğini göstermek için çevreleyen hücrelere örnek metin ekleyin.
8. Çalışma kitabını diske `.xlsx` dosyası olarak kaydedin.

Aşağıdaki kod, eksiksiz yaklaşımı göstermektedir.

```javascript
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

## **Yaklaşım 2: Resmi Doğrudan Bir Hücreye Gömme**

Aspose.Cells ayrıca hücreye bağlı resimler için daha basit bir mekanizma sunar: `Cell.EmbeddedImage` özelliği. Bu özelliğe resim baytları atamak, resmi hücrenin kendisine satır içi içerikmiş gibi ekler.

### **Gömülü Resimler Nasıl Çalışır**

- Resim, çizim katmanındaki bir şekil olarak değil, hücre içeriğinin bir parçası olarak depolanır.
- Resim, hücrenin işlenmiş sınırları içine sığacak şekilde otomatik olarak ölçeklenir. Bağlantı koordinatları veya yerleştirme ayarları gerekmez.
- Hücre, formüllerle referans verilebilen, bir satırın parçası olarak sıralanabilen veya diğer hücre düzeyinde işlemlerde kullanılabilen gerçek bir adrese sahip gerçek bir hücre olmaya devam eder.

Bu, amacınız yalnızca "bu hücrenin içinde yaşayan bir resim" olduğunda `Cell.EmbeddedImage` özelliğini en kısa seçenek haline getirir.

### **Adım Adım Talimatlar**

1. Yeni bir `Workbook` oluşturun (veya var olan birini açın).
2. `workbook.getWorksheets().get(0)` üzerinden hedef `Worksheet`'e erişin.
3. Resim dosyasını diskten bir bayt dizisine okuyun (örneğin, `java.nio.file.Files` üzerinden `Files.readAllBytes` kullanarak).
4. Hedef hücreye bir referans alın — `worksheet.getCells().get("C6")` veya `worksheet.getCells().get(5, 2)` aracılığıyla.
5. Bayt dizisini `cell.setEmbeddedImage(bytes)` aracılığıyla hücrenin `EmbeddedImage` özelliğine atayın.
6. İsteğe bağlı olarak, gömülü resme daha belirgin bir görünüm kazandırmak için hedef satırın ve sütunun satır yüksekliğini ve sütun genişliğini ayarlayın.
7. Çalışma kitabını diske `.xlsx` dosyası olarak kaydedin.

Aşağıdaki kod, eksiksiz yaklaşımı göstermektedir.

```javascript
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);

// Hedef hücre C6'yı al
var cell = worksheet.getCells().get("C6");

// Görüntü dosyasını bir bayt dizisine oku
var imageData = fs.readFileSync("logo.png");

// Görüntüyü doğrudan hücreye göm
cell.setEmbeddedImage(imageData);

// İsteğe bağlı olarak satır yüksekliğini ve sütun genişliğini gömülü görüntünün daha görünür olması için ayarla
worksheet.getCells().setColumnWidth(2, 30);   // C Sütunu (indeks 2)
worksheet.getCells().setRowHeight(5, 100);     // Satır 6 (indeks 5)

// Ortaya çıkan çalışma kitabını .xlsx dosyası olarak kaydet
workbook.save("output.xlsx", AsposeCells.SaveFormat.Xlsx);
```

## **Doğru Yaklaşımı Seçme**

Her iki yaklaşım da tek bir hücrenin içine sığan bir resim üretir, ancak resmin nasıl depolandığı ve davrandığı açısından farklılık gösterir:

- **Şu durumlarda kayan bir resim kullanın (Yaklaşım 1):**
  - Yerleştirme, katmanlama veya diğer çizim nesneleriyle hizalama üzerinde daha ayrıntılı denetime ihtiyaç duyduğunuzda.
  - Resmin diğer şekillerle seçilebilen, yeniden sıralanabilen veya gruplanabilen bir şekil olarak davranmasını istediğinizde.
  - Zaten `PictureCollection` ile çalışan kodla eski uyumluluk gerektirdiğinizde.
  - Çalışma sayfası düzenine göre bağlantı koordinatlarını dinamik olarak hesaplamanız gerektiğinde.

- **Şu durumlarda gömülü bir resim kullanın (Yaklaşım 2):**
  - Bir hücreye resim eklemenin mümkün olan en basit yolunu istediğinizde.
  - Resim, diğer hücre içerikleri gibi hücreyle birlikte taşınmalıdır.
  - Resmi bir şekil olarak düzenlemenize gerek yoktur.

{{% alert color="primary" %}}

Her iki yaklaşım da aynı çalışma kitabında birlikte var olabilir. İki mekanizma dosyada farklı depolama katmanları kullandığından, bir hücre kümesinin üzerine kayan resimler yerleştirebilir ve diğer hücrelere doğrudan resimler gömebilirsiniz.

{{% /alert %}}



{{< app/cells/assistant language="javascript" >}}