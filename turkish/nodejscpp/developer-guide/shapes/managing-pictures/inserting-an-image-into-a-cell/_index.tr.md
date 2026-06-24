---
title: Bir Hücreye Resim Ekleme
description: Aspose.Cells, elektronik tablo dosyalarıyla çalışmak için bir Node.js via C++ kütüphanesidir. Bu makale, resmi tam olarak tek bir hücre boyutuna sığdırmayı iki farklı yaklaşımla açıklamaktadır, hücrenin üzerine kayan bir resim yerleştirmek veya resmi doğrudan hücreye gömmek.
keywords: Aspose.Cells, Node.js via C++ kütüphanesi, elektronik tablo, resim ekle, resim göm, hücredeki resim, resmi hücreye sığdır, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /tr/nodejs-cpp/inserting-an-image-into-a-cell/
---

{{% alert color="primary" %}}

Aspose.Cells, bir resmi tek bir hücreyle ilişkilendirmek için iki farklı yol sunar. Kayan resim, çalışma sayfası çizim katmanında bir hücre aralığının üzerinde görsel olarak yer alan bir şekildir; gömülü resim ise hücrenin kendisinin içinde saklanır ve hücrenin görüntüleme alanına otomatik olarak ölçeklenir. Düzen gereksinimlerinize en uygun yaklaşımı seçin.

{{% /alert %}}

## **Giriş**

Bir resmi tam olarak tek bir hücreye sığdırmak, görsel raporlar, ürün katalogları, çalışan rehberleri, panolar veya envanter listeleri olarak işlev gören elektronik tablolar tasarlanırken yaygın bir gereksinimdir. Resmi birçok hücreye yaymak veya çalışma sayfasına gevşek bir şekilde yerleştirmek yerine, sahip olduğu hücreyle hizalı kalan, temiz, hücreye bağlı bir resim isteyebilirsiniz.

Aspose.Cells bu senaryoyu iki tamamlayıcı şekilde destekler:

- **Yaklaşım 1 — Bir hücrenin üzerine kayan resim yerleştirin.** Çalışma sayfasına bir `Picture` ekleyin, `placement` özelliğini `MoveAndSize` olarak ayarlayın ve resmi tam olarak bir hücreyi kaplayacak şekilde çapa hücrelerini (`upperLeftRow`, `upperLeftColumn`, `lowerRightRow`, `lowerRightColumn`) ayarlayın.
- **Yaklaşım 2 — Resmi doğrudan bir hücreye gömün.** Resim baytlarını hücrenin `embeddedImage` özelliğine atayın. Resim, hücrenin görüntüleme alanına sığacak şekilde otomatik olarak ölçeklenir ve hücreyle birlikte taşınır.

Bu makalenin geri kalanı her iki yaklaşımı da adım adım açıklar, ilgili API'leri anlatır ve bunların kodda nasıl kullanılacağını gösterir.

## **Yaklaşım 1: Bir Hücrenin Üzerine Resim Yerleştirme**

Kayan resim, çalışma sayfası çizim katmanında bulunan bir `Picture` nesnesidir. Herhangi bir tek hücrenin parçası olmasa da, bir hücre aralığına sabitlenir. Resmin çapa hücreleri — sol üst ve sağ alt köşeleri — çalışma sayfasındaki görsel kapsamını belirler. Varsayılan olarak, yeni eklenen bir resim birkaç hücreyi kaplar.

Kayan bir resmin **tam olarak bir hücreyi** kaplamasını sağlamak için şunları yapmanız gerekir:

1. Resmi `worksheet.pictures.add(row, column, stream)` kullanarak ekleyin; bu, yeni resmi verilen hücreye sabitler.
2. Resmin sınırlayıcı dikdörtgeninin hedef hücreyle çakışması için dört çapa özelliğini ayarlayın.
3. Kullanıcı sütun genişliğini veya satır yüksekliğini değiştirdiğinde resmin alttaki hücreyle birlikte hareket etmesi ve yeniden boyutlandırılması için `picture.placement` özelliğini `PlacementType.MoveAndSize` olarak ayarlayın.

### **Resmi Tek Bir Hücreye Sabitleme**

Resmin çapası, dört sıfır tabanlı dizin özelliğiyle tanımlanır:

- `picture.upperLeftRow` — resmin üst kenarının satır dizini.
- `picture.upperLeftColumn` — resmin sol kenarının sütun dizini.
- `picture.lowerRightRow` — resmin alt kenarının satır dizini. Resmin alt kenarının `r` satırının alt kısmında bitmesini sağlamak için bunu `r + 1` olarak ayarlayın.
- `picture.lowerRightColumn` — resmin sağ kenarının sütun dizini. Resmin sağ kenarının `c` sütununun sağında bitmesini sağlamak için bunu `c + 1` olarak ayarlayın.

Örneğin, resmi tam olarak **C6** hücresine (satır dizini `5`, sütun dizini `2`) sığdırmak için `upperLeftRow = 5`, `upperLeftColumn = 2`, `lowerRightRow = 6` ve `lowerRightColumn = 3` ayarlayın.

{{% alert color="primary" %}}

Aspose.Cells'de satır ve sütun dizinleri **sıfır tabanlıdır**. C6 hücresinin satır dizini 5 ve sütun dizini 2'dir. Sağ alt çapadaki bir birimlik hatalar, resimlerin bitişik hücreye taşmış gibi görünmesinin en yaygın kaynağıdır.

{{% /alert %}}

### **Yerleşim Davranışını Kontrol Etme**

`picture.placement`, kullanıcı alttaki satır veya sütunu yeniden boyutlandırdığında resmin nasıl davranacağını kontrol eden `PlacementType` türünde bir numaralandırmadır. Tek hücreli bir resim için önerilen değer `PlacementType.MoveAndSize` değeridir; bu, resmin alttaki hücreyle birlikte hareket etmesini ve yeniden boyutlandırılmasını sağlayarak tam sığmayı korur.

### **Adım Adım Talimatlar**

1. Yeni bir `Workbook` oluşturun (veya mevcut birini açın).
2. `workbook.worksheets[0]` üzerinden hedef `Worksheet`'e erişin.
3. Resim dosyasını disk üzerinden bir akışa açın ve akışın kullanımdan sonra düzgün şekilde kapatıldığından emin olun.
4. C6 hücresine sabitlenmiş bir resim eklemek için `worksheet.pictures.add(5, 2, stream)` çağırın. Döndürülen `Picture` referansını yakalayın.
5. Resmin yalnızca C6 hücresini kaplaması için dört çapa koordinatını ayarlayın: `upperLeftRow = 5`, `upperLeftColumn = 2`, `lowerRightRow = 6`, `lowerRightColumn = 3`.
6. Sütun veya satır yeniden boyutlandırıldığında resmin C6 ile hizalı kalması için `picture.placement = PlacementType.MoveAndSize` ayarlayın.
7. İsteğe bağlı olarak, yalnızca C6 hücresinin resmi içerdiğini göstermek için çevreleyen hücrelere örnek metinler ekleyin.
8. Çalışma kitabını disk üzerine `.xlsx` dosyası olarak kaydedin.

Aşağıdaki kod, tüm yaklaşımı göstermektedir.

```javascript
const AsposeCells = require("aspose.cells");
const fs = require("fs");

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);

const fs_stream = fs.createReadStream("logo.png");
const picIndex = worksheet.getPictures().add(5, 2, fs_stream);
const picture = worksheet.getPictures().get(picIndex);
picture.setUpperLeftRow(5);
picture.setUpperLeftColumn(2);
picture.setLowerRightRow(6);
picture.setLowerRightColumn(3);
picture.setPlacement(AsposeCells.PlacementType.MoveAndSize);

workbook.save("output.xlsx", AsposeCells.SaveFormat.Xlsx);
```

## **Yaklaşım 2: Resmi Doğrudan Bir Hücreye Gömme**

Aspose.Cells ayrıca hücreye bağlı resimler için daha basit bir mekanizma sunar: `cell.embeddedImage` özelliği. Resim baytlarını bu özelliğe atamak, resmi satır içi içerikmiş gibi hücrenin kendisine ekler.

### **Gömülü Resimler Nasıl Çalışır**

- Resim, çizim katmanındaki bir şekil olarak değil, hücre içeriğinin bir parçası olarak saklanır.
- Resim, hücrenin oluşturulan sınırları içine sığacak şekilde otomatik olarak ölçeklenir. Çapa koordinatları veya yerleşim ayarları gerekmez.
- Hücre, formüller tarafından başvurulabilen, bir satırın parçası olarak sıralanabilen veya diğer hücre düzeyinde işlemlerde kullanılabilen gerçek bir adrese sahip gerçek bir hücre olarak kalır.

Bu, hedefiniz yalnızca "bu hücrenin içinde yaşayan bir resim" olduğunda `cell.embeddedImage` özelliğini en kısa seçenek haline getirir.

### **Adım Adım Talimatlar**

1. Yeni bir `Workbook` oluşturun (veya mevcut birini açın).
2. `workbook.worksheets[0]` üzerinden hedef `Worksheet`'e erişin.
3. Resim dosyasını Node.js dosya sistemi API'lerini (örneğin, `fs.readFileSync`) kullanarak diskten bir Buffer veya bayt dizisine okuyun.
4. Hedef hücreye bir referans alın — `worksheet.cells["C6"]` veya `worksheet.cells[5, 2]` aracılığıyla.
5. Bayt dizisini hücrenin `embeddedImage` özelliğine atayın.
6. İsteğe bağlı olarak, gömülü resme daha belirgin bir görünüm kazandırmak için hedef satır ve sütunun satır yüksekliğini ve sütun genişliğini ayarlayın.
7. Çalışma kitabını disk üzerine `.xlsx` dosyası olarak kaydedin.

Aşağıdaki kod, tüm yaklaşımı göstermektedir.

```javascript
var workbook = new AsposeCells.Workbook();
var worksheet = workbook.getWorksheets().get(0);

// C6 hedef hücresini al
var cell = worksheet.getCells().get("C6");

// Görüntü dosyasını bir bayt dizisine oku
var imageData = fs.readFileSync("logo.png");

// Görüntüyü doğrudan hücreye göm
cell.setEmbeddedImage(imageData);

// Gömülü görüntünün daha görünür olması için isteğe bağlı olarak satır yüksekliğini ve sütun genişliğini ayarla
worksheet.getCells().setColumnWidth(2, 30);   // C Sütunu (indeks 2)
worksheet.getCells().setRowHeight(5, 100);     // 6. Satır (indeks 5)

// Ortaya çıkan çalışma kitabını .xlsx dosyası olarak kaydet
workbook.save("output.xlsx", AsposeCells.SaveFormat.Xlsx);
```

## **Doğru Yaklaşımı Seçme**

Her iki yaklaşım da tek bir hücreye sığan bir resim üretir, ancak resmin nasıl saklandığı ve nasıl davrandığı konusunda farklılık gösterir:

- **Aşağıdaki durumlarda kayan resim kullanın (Yaklaşım 1):**
  - Yerleşim, katmanlama veya diğer çizim nesneleriyle hizalama üzerinde daha ayrıntılı kontrole ihtiyacınız olduğunda.
  - Resmin, diğer şekillerle birlikte seçilebilen, yeniden sıralanabilen veya gruplanabilen bir şekil olarak davranmasını istediğinizde.
  - Zaten resim koleksiyonuyla çalışan kodla eski sürüm uyumluluğu gerektirdiğinizde.
  - Çalışma sayfası düzenine dayalı olarak çapa koordinatlarını dinamik olarak hesaplamanız gerektiğinde.

- **Aşağıdaki durumlarda gömülü resim kullanın (Yaklaşım 2):**
  - Bir hücreye en basit resim ekleme işlemini istediğinizde.
  - Resmin, diğer hücre içerikleri gibi hücreyle birlikte taşınması gerektiğinde.
  - Resmi bir şekil olarak değiştirmeniz gerekmediğinde.

{{% alert color="primary" %}}

Her iki yaklaşım da aynı çalışma kitabında bir arada bulunabilir. Bir hücre kümesinin üzerine kayan resimler yerleştirebilir ve diğer hücrelere doğrudan resimler gömebilirsiniz; çünkü iki mekanizma dosyada farklı depolama katmanlarını kullanır.

{{% /alert %}}

## **İlgili Makaleler**

- [Hücreye Resim Nasıl Yerleştirilir](/cells/tr/nodejs-cpp/how-to-place-image-to-cell/)
- [Resim Köprüleri Ekleme](/cells/tr/nodejs-cpp/add-image-hyperlinks/)
- [URL'den Web Resmi Excel Çalışma Sayfasına Yükleme](/cells/tr/nodejs-cpp/load-a-web-image-from-a-url-into-an-excel-worksheet/)
- [Konum, Boyut ve Tasarımcı Grafiğini Değiştirme](/cells/tr/nodejs-cpp/manipulate-position-size-and-designer-chart/)

{{< app/cells/assistant language="javascript" >}}