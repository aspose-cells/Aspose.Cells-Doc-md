---
title: Bir Hücreye Görüntü Ekleme
description: Aspose.Cells, elektronik tablo dosyalarıyla çalışmak için bir .NET kütüphanesidir. Bu makale, resmi tam olarak tek bir hücre boyutuna sığdırmayı iki farklı yaklaşımla açıklar, hücrenin üzerine kayan bir resim yerleştirmek veya görüntüyü doğrudan hücreye gömmek.
keywords: Aspose.Cells, .NET kütüphanesi, elektronik tablo, görüntü ekleme, görüntü gömme, hücrede resim, resmi hücreye sığdırma, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /tr/net/inserting-an-image-into-a-cell/
---

{{% alert color="primary" %}}

Aspose.Cells, bir görüntüyü tek bir hücreyle ilişkilendirmek için iki farklı yol sunar. Kayan resim, çalışma sayfası çizim katmanında bir hücre aralığının üzerine görsel olarak yerleştirilen bir şekildir; gömülü görüntü ise hücrenin kendisinin içinde saklanır ve hücrenin görüntüleme alanına otomatik olarak ölçeklenir. Düzen gereksinimlerinize en uygun yaklaşımı seçin.

{{% /alert %}}

## **Giriş**

Bir resmi tam olarak tek bir hücreye sığdırmak, görsel raporlar, ürün katalogları, çalışan dizinleri, panolar veya envanter listeleri gibi işlev gören elektronik tablolar tasarlanırken sık karşılaşılan bir gereksinimdir. Görüntüyü birçok hücreye yaymak veya çalışma sayfasına gevşek bir şekilde yerleştirmek yerine, kendisine sahip olan hücreyle hizalı kalan, temiz ve hücreye bağlı bir görüntü isteyebilirsiniz.

Aspose.Cells bu senaryoyu birbirini tamamlayan iki şekilde destekler:

- **Yaklaşım 1 — Hücrenin üzerine kayan bir resim yerleştirin.** Çalışma sayfasına bir `Picture` ekleyin, `Placement` özelliğini `MoveAndSize` olarak ayarlayın ve resmin tam olarak bir hücreyi kapsaması için bağlantı hücrelerini (`UpperLeftRow`, `UpperLeftColumn`, `LowerRightRow`, `LowerRightColumn`) ayarlayın.
- **Yaklaşım 2 — Görüntüyü doğrudan bir hücreye gömün.** Hücrenin `EmbeddedImage` özelliğine görüntü baytlarını atayın. Görüntü, hücrenin görüntüleme alanına sığacak şekilde otomatik olarak ölçeklenir ve hücreyle birlikte taşınır.

Bu makalenin geri kalanında her iki yaklaşım adım adım açıklanmakta, ilgili API'ler anlatılmakta ve bunların kodda nasıl kullanılacağı gösterilmektedir.

## **Yaklaşım 1: Hücrenin Üzerine Bir Resim Yerleştirme**

Kayan resim, çalışma sayfası çizim katmanında bulunan bir `Picture` nesnesidir. Herhangi bir tek hücrenin parçası olmasa da bir hücre aralığına bağlıdır. Resmin bağlantı hücreleri — sol üst ve sağ alt köşeleri — çalışma sayfasındaki görsel kapsamını belirler. Varsayılan olarak, yeni eklenen bir resim birkaç hücreye yayılır.

Kayan bir resmi **tam olarak bir hücreyi** kapsayacak şekilde ayarlamak için şunları yapmanız gerekir:

1. Resmi `Worksheet.Pictures.Add(int row, int column, Stream stream)` kullanarak ekleyin; bu, yeni resmi belirtilen hücreye bağlar.
2. Resmin sınırlayıcı dikdörtgeni hedef hücreyle çakışacak şekilde dört bağlantı özelliğini ayarlayın.
3. Kullanıcı sütun genişliğini veya satır yüksekliğini değiştirdiğinde resmin alttaki hücreyle birlikte hareket etmesi ve yeniden boyutlandırılması için `Picture.Placement` özelliğini `PlacementType.MoveAndSize` olarak ayarlayın.

### **Resmi Tek Bir Hücreye Bağlama**

Resmin bağlantısı dört sıfır tabanlı indeks özelliğiyle tanımlanır:

- `Picture.UpperLeftRow` — resmin üst kenarının satır indeksi.
- `Picture.UpperLeftColumn` — resmin sol kenarının sütun indeksi.
- `Picture.LowerRightRow` — resmin alt kenarının satır indeksi. Resmin alt kenarını `r` satırının altına yerleştirmek için bunu `r + 1` olarak ayarlayın.
- `Picture.LowerRightColumn` — resmin sağ kenarının sütun indeksi. Resmin sağ kenarını `c` sütununun sağına yerleştirmek için bunu `c + 1` olarak ayarlayın.

Örneğin, resmi tam olarak **C6** hücresine (satır indeksi `5`, sütun indeksi `2`) sığdırmak için `UpperLeftRow = 5`, `UpperLeftColumn = 2`, `LowerRightRow = 6` ve `LowerRightColumn = 3` olarak ayarlayın.

{{% alert color="primary" %}}

Aspose.Cells'te satır ve sütun indeksleri **sıfır tabanlıdır**. C6 hücresinin satır indeksi 5, sütun indeksi 2'dir. Sağ alt bağlantı noktasındaki off-by-one hataları, resimlerin bitişik bir hücreye taşmış gibi görünmesinin en yaygın nedenidir.

{{% /alert %}}

### **Yerleştirme Davranışını Kontrol Etme**

`Picture.Placement`, kullanıcı alttaki satır veya sütunu yeniden boyutlandırdığında resmin nasıl davranacağını kontrol eden `PlacementType` türünde bir enum'dur. Tek hücreli bir resim için önerilen değer `PlacementType.MoveAndSize`'dır; bu, resmin alttaki hücreyle birlikte hareket etmesini ve yeniden boyutlandırılmasını sağlayarak tam sığmayı korur.

### **Adım Adım Talimatlar**

1. Yeni bir `Workbook` oluşturun (veya mevcut birini açın).
2. `workbook.Worksheets[0]` üzerinden hedef `Worksheet`'e erişin.
3. Görüntü dosyasını disk üzerinden bir `using` bloğu kullanarak `FileStream`'e açın; böylece stream düzgün bir şekilde dispose edilir.
4. Resmi C6 hücresine bağlı olarak eklemek için `worksheet.Pictures.Add(5, 2, stream)` çağrısını yapın. Döndürülen `Picture` referansını yakalayın.
5. Resmin yalnızca C6 hücresini kapsaması için dört bağlantı koordinatını ayarlayın: `UpperLeftRow = 5`, `UpperLeftColumn = 2`, `LowerRightRow = 6`, `LowerRightColumn = 3`.
6. Sütun veya satır yeniden boyutlandırıldığında resmin C6 ile hizalı kalması için `picture.Placement = PlacementType.MoveAndSize` olarak ayarlayın.
7. İsteğe bağlı olarak, yalnızca C6 hücresinin resmi içerdiğini göstermek için çevreleyen hücrelere örnek metin ekleyin.
8. Çalışma kitabını diske `.xlsx` dosyası olarak kaydedin.

Aşağıdaki kod, tüm yaklaşımı göstermektedir.

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Drawing;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];

using (FileStream fs = new FileStream("logo.png", FileMode.Open, FileAccess.Read))
{
    int picIndex = worksheet.Pictures.Add(5, 2, fs);
    Picture picture = worksheet.Pictures[picIndex];
    picture.UpperLeftRow = 5;
    picture.UpperLeftColumn = 2;
    picture.LowerRightRow = 6;
    picture.LowerRightColumn = 3;
    picture.Placement = PlacementType.MoveAndSize;
}

workbook.Save("output.xlsx", SaveFormat.Xlsx);
```

## **Yaklaşım 2: Görüntüyü Doğrudan Bir Hücreye Gömme**

Aspose.Cells ayrıca hücreye bağlı görüntüler için daha basit bir mekanizma sunar: `Cell.EmbeddedImage` özelliği. Bu özelliğe görüntü baytlarını atamak, görüntüyü sanki satır içi içerikmiş gibi hücrenin kendisine ekler.

### **Gömülü Görüntüler Nasıl Çalışır?**

- Görüntü, çizim katmanında bir şekil olarak değil, hücre içeriğinin bir parçası olarak saklanır.
- Görüntü, hücrenin işlenmiş sınırlarına sığacak şekilde otomatik olarak ölçeklenir. Herhangi bir bağlantı koordinatı veya yerleştirme ayarı gerekmez.
- Hücre, formüller tarafından başvurulabilen, bir satırın parçası olarak sıralanabilen veya diğer hücre düzeyinde işlemlerde kullanılabilen gerçek bir hücre olarak kalır.

Bu, amacınız yalnızca "bu hücrenin içinde yaşayan bir görüntü" olduğunda `Cell.EmbeddedImage`'ı en kısa seçenek haline getirir.

### **Adım Adım Talimatlar**

1. Yeni bir `Workbook` oluşturun (veya mevcut birini açın).
2. `workbook.Worksheets[0]` üzerinden hedef `Worksheet`'e erişin.
3. Görüntü dosyasını disk üzerinden bir `byte[]` dizisine okuyun (örneğin, `File.ReadAllBytes` kullanarak).
4. Hedef hücreye bir referans alın — `worksheet.Cells["C6"]` veya `worksheet.Cells[5, 2]` aracılığıyla.
5. Bayt dizisini hücrenin `EmbeddedImage` özelliğine atayın.
6. İsteğe bağlı olarak, gömülü görüntüye daha belirgin bir görünüm kazandırmak için hedef satırın ve sütunun satır yüksekliğini ve sütun genişliğini ayarlayın.
7. Çalışma kitabını diske `.xlsx` dosyası olarak kaydedin.

Aşağıdaki kod, tüm yaklaşımı göstermektedir.

```csharp
var workbook = new Workbook();
var worksheet = workbook.Worksheets[0];

// Hedef hücre C6'yı al
var cell = worksheet.Cells["C6"];

// Görüntü dosyasını bir bayt dizisine oku
byte[] imageData = File.ReadAllBytes("logo.png");

// Görüntüyü doğrudan hücreye göm
cell.EmbeddedImage = imageData;

// Gömülü görüntünün daha görünür olması için isteğe bağlı olarak satır yüksekliğini ve sütun genişliğini ayarlayın
worksheet.Cells.SetColumnWidth(2, 30);   // Sütun C (indeks 2)
worksheet.Cells.SetRowHeight(5, 100);     // Satır 6 (indeks 5)

// Ortaya çıkan çalışma kitabını .xlsx dosyası olarak kaydedin
workbook.Save("output.xlsx", SaveFormat.Xlsx);
```

## **Doğru Yaklaşımı Seçme**

Her iki yaklaşım da tek bir hücrenin içine sığan bir resim üretir, ancak resmin nasıl saklandığı ve nasıl davrandığı konusunda farklılık gösterir:

- **Şu durumlarda kayan resim kullanın (Yaklaşım 1):**
  - Yerleştirme, katmanlama veya diğer çizim nesneleriyle hizalama üzerinde daha ayrıntılı kontrole ihtiyacınız olduğunda.
  - Resmin, diğer şekillerle seçilebilen, yeniden sıralanabilen veya gruplanabilen bir şekil olarak davranmasını istediğinizde.
  - Zaten `PictureCollection` ile çalışan kodla eski sürüm uyumluluğuna ihtiyaç duyduğunuzda.
  - Çalışma sayfası düzenine göre bağlantı koordinatlarını dinamik olarak hesaplamanız gerektiğinde.

- **Şu durumlarda gömülü görüntü kullanın (Yaklaşım 2):**
  - Bir hücreye görüntü eklemenin en basit yolunu istediğinizde.
  - Görüntünün diğer hücre içerikleri gibi hücreyle birlikte taşınması gerektiğinde.
  - Görüntüyü bir şekil olarak değiştirmenize gerek olmadığında.

{{% alert color="primary" %}}

Her iki yaklaşım aynı çalışma kitabında birlikte var olabilir. İki mekanizma dosyada farklı depolama katmanları kullandığından, bir hücre kümesinin üzerine kayan resimler yerleştirebilir ve diğer hücrelere doğrudan görüntüler gömebilirsiniz.

{{% /alert %}}

## **İlgili Makaleler**

- [Hücreye Resim Nasıl Yerleştirilir](/cells/tr/net/how-to-place-image-to-cell/)
- [Görüntü Hücre Genişliği ve Yüksekliğine Nasıl Sığdırılır](/cells/tr/net/how-to-fit-image-to-cell-width-height/)
- [Görüntü Köprüleri Ekleme](/cells/tr/net/add-image-hyperlinks/)
- [Bir URL'den Web Görüntüsünü Excel Çalışma Sayfasına Yükleme](/cells/tr/net/load-a-web-image-from-a-url-into-an-excel-worksheet/)
- [Konum, Boyut ve Tasarımcı Grafiğini Değiştirme](/cells/tr/net/manipulate-position-size-and-designer-chart/)

{{< app/cells/assistant language="csharp" >}}