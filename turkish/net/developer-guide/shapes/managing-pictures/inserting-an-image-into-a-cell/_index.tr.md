---
title: Bir Hücreye Resim Ekleme
linktitle: Bir Hücreye Resim Ekleme
description: Aspose.Cells, elektronik tablo dosyalarıyla çalışmak için kullanılan bir .NET kütüphanesidir. Bu makale, resmi bir hücrenin üzerine kayan resim olarak yerleştirerek veya doğrudan hücreye gömerek bir resmi tek bir hücreye tam olarak sığdırmayı açıklar.
keywords: Aspose.Cells, .NET kütüphanesi, elektronik tablo, resim ekleme, gömülü resim, hücredeki resim, resmi hücreye sığdırma, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /tr/net/inserting-an-image-into-a-cell/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells, bir resmi tek bir hücreyle ilişkilendirmenin iki farklı yolunu sunar. Kayan resim, çalışma sayfasının çizim katmanında bulunan ve bir hücre aralığının üzerinde görsel olarak yer alan bir şekildir; gömülü resim ise hücrenin kendisinin içinde saklanır ve hücrenin görüntüleme alanına otomatik olarak ölçeklenir. Yerleşim gereksinimlerinize en uygun yaklaşımı seçin.
{{% /alert %}}

## **Introduction**
Bir resmi tam olarak tek bir hücreye sığdırmak, görsel raporlar, ürün katalogları, çalışan rehberleri, panolar veya envanter listeleri olarak işlev gören elektronik tablolar tasarlanırken sık karşılaşılan bir gereksinimdir. Bir resmi birçok hücreye yaymak veya çalışma sayfasına gevşek bir şekilde yerleştirmek yerine, sahip olduğu hücreyle hizalı kalan temiz, hücreye bağlı bir resim isteyebilirsiniz.
Aspose.Cells bu senaryoyu iki tamamlayıcı şekilde destekler:
- **Yaklaşım 1 — Hücrenin üzerine kayan bir resim yerleştirin.** Çalışma sayfasına bir `Picture` ekleyin, `Placement` özelliğini `MoveAndSize` olarak ayarlayın ve resmin tam olarak bir hücreyi kaplaması için bağlantı hücrelerini (`UpperLeftRow`, `UpperLeftColumn`, `LowerRightRow`, `LowerRightColumn`) ayarlayın.
- **Yaklaşım 2 — Resmi doğrudan bir hücreye gömün.** Hücrenin `EmbeddedImage` özelliğine resim baytlarını atayın. Resim, hücrenin görüntüleme alanına sığacak şekilde otomatik olarak ölçeklenir ve hücreyle birlikte hareket eder.
Bu makalenin geri kalanı her iki yaklaşımı da inceler, ilgili API'leri açıklar ve kodda nasıl kullanılacaklarını gösterir.

## **Approach 1: Place a Picture Over a Cell**
Kayan resim, çalışma sayfasının çizim katmanında bulunan bir `Picture` nesnesidir. Herhangi bir tek hücrenin parçası olmasa da bir hücre aralığına bağlıdır. Resmin bağlantı hücreleri — sol üst ve sağ alt köşeleri — çalışma sayfasındaki görsel kapsamını belirler. Varsayılan olarak, yeni eklenen bir resim birkaç hücreyi kaplar.
Kayan bir resmi **tam olarak bir hücreyi** kaplayacak şekilde yapmak için şunları yapmanız gerekir:
1. Resmi `Worksheet.Pictures.Add(int row, int column, Stream stream)` kullanarak ekleyin; bu, yeni resmi belirtilen hücreye bağlar.
2. Dört bağlantı özelliğini, resmin sınırlayıcı dikdörtgeni hedef hücreyle çakışacak şekilde ayarlayın.
3. Kullanıcı sütun genişliğini veya satır yüksekliğini değiştirdiğinde resmin alttaki hücreyle birlikte hareket edip yeniden boyutlandırılması için `Picture.Placement` özelliğini `PlacementType.MoveAndSize` olarak ayarlayın.

### **Anchoring the Picture to a Single Cell**
Resmin bağlantısı, dört sıfır tabanlı dizin özelliğiyle tanımlanır:
- `Picture.UpperLeftRow` — resmin üst kenarının satır dizini.
- `Picture.UpperLeftColumn` — resmin sol kenarının sütun dizini.
- `Picture.LowerRightRow` — resmin alt kenarının satır dizini. Resmin alt kenarının `r` satırının altına oturmasını sağlamak için bunu `r + 1` olarak ayarlayın.
- `Picture.LowerRightColumn` — resmin sağ kenarının sütun dizini. Resmin sağ kenarının `c` sütununun sağına oturmasını sağlamak için bunu `c + 1` olarak ayarlayın.

{{% alert color="primary" %}}
Aspose.Cells'deki satır ve sütun dizinleri **sıfır tabanlıdır**. C6 hücresinin satır dizini 5 ve sütun dizini 2'dir. Sağ alt bağlantısındaki off-by-one hataları, resimlerin bitişik hücreye taşmış gibi görünmesinin en yaygın nedenidir.

### **Controlling Placement Behavior**
`Picture.Placement`, kullanıcı alttaki satırı veya sütunu yeniden boyutlandırdığında resmin nasıl davranacağını kontrol eden `PlacementType` türünde bir numaralandırmadır. Tek hücreli bir resim için önerilen değer `PlacementType.MoveAndSize`'dır; bu, resmin alttaki hücreyle birlikte hareket etmesine ve yeniden boyutlandırılmasına neden olarak tam sığmayı korur.

### **Step-by-Step Instructions**
1. Yeni bir `Workbook` oluşturun (veya var olanı açın).
2. `workbook.Worksheets[0]` üzerinden hedef `Worksheet`'e erişin.
3. Görüntü dosyasını diskten bir `using` bloğu kullanarak `FileStream` olarak açın, böylece akış düzgün şekilde imha edilir.
4. C6 hücresine bağlı bir resim eklemek için `worksheet.Pictures.Add(5, 2, stream)` çağırın. Döndürülen `Picture` referansını yakalayın.
5. Resmin yalnızca C6 hücresini kaplaması için dört bağlantı koordinatını ayarlayın: `UpperLeftRow = 5`, `UpperLeftColumn = 2`, `LowerRightRow = 6`, `LowerRightColumn = 3`.
6. Sütun veya satır yeniden boyutlandırıldığında resmin C6 ile hizalı kalması için `picture.Placement = PlacementType.MoveAndSize` ayarlayın.
7. İsteğe bağlı olarak, yalnızca C6 hücresinin resmi içerdiğini göstermek için çevresindeki hücrelere örnek metin ekleyin.
8. Çalışma kitabını diskte `.xlsx` dosyası olarak kaydedin.
Aşağıdaki kod tüm yaklaşımı göstermektedir.

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

## **Approach 2: Embed an Image Directly in a Cell**
Aspose.Cells, hücreye bağlı resimler için daha basit bir mekanizma da sunar: `Cell.EmbeddedImage` özelliği. Resim baytlarını bu özelliğe atamak, resmi sanki satır içi içerikmiş gibi hücrenin kendisine ekler.

### **How Embedded Images Work**
- Resim, çizim katmanında bir şekil olarak değil, hücre içeriğinin bir parçası olarak saklanır.
- Resim, hücrenin oluşturulan sınırları içine sığacak şekilde otomatik olarak ölçeklenir. Bağlantı koordinatları veya yerleştirme ayarları gerekmez.
- Hücre, formüller tarafından başvurulabilen, bir satırın parçası olarak sıralanabilen veya diğer hücre düzeyinde işlemlerde kullanılabilen gerçek bir adrese sahip gerçek bir hücre olarak kalır.
Bu, hedefiniz yalnızca "bu hücrenin içinde yaşayan bir resim" olduğunda `Cell.EmbeddedImage`'ı en özlü seçenek haline getirir.

### **Step-by-Step Instructions**
1. Yeni bir `Workbook` oluşturun (veya var olanı açın).
2. `workbook.Worksheets[0]` üzerinden hedef `Worksheet`'e erişin.
3. Görüntü dosyasını diskten bir `byte[]` dizisine okuyun (örneğin, `File.ReadAllBytes` kullanarak).
4. Hedef hücreye bir referans alın — `worksheet.Cells["C6"]` veya `worksheet.Cells[5, 2]` aracılığıyla.
5. Bayt dizisini hücrenin `EmbeddedImage` özelliğine atayın.
6. İsteğe bağlı olarak, gömülü resme daha belirgin bir görünüm kazandırmak için hedef satırın ve sütunun satır yüksekliğini ve sütun genişliğini ayarlayın.
7. Çalışma kitabını diskte `.xlsx` dosyası olarak kaydedin.
Aşağıdaki kod tüm yaklaşımı göstermektedir.

```csharp
var workbook = new Workbook();
var worksheet = workbook.Worksheets[0];
// C6 hedef hücresini al
var cell = worksheet.Cells["C6"];
// Görüntü dosyasını bir bayt dizisine oku
byte[] imageData = File.ReadAllBytes("logo.png");
// Görüntüyü doğrudan hücreye göm
cell.EmbeddedImage = imageData;
// İsteğe bağlı olarak satır yüksekliğini ve sütun genişliğini gömülü görüntünün daha görünür olması için ayarla
worksheet.Cells.SetColumnWidth(2, 30);   // C sütunu (2. indeks)
worksheet.Cells.SetRowHeight(5, 100);     // 6. satır (5. indeks)
// Elde edilen çalışma kitabını .xlsx dosyası olarak kaydet
workbook.Save("output.xlsx", SaveFormat.Xlsx);
```

## **Choosing the Right Approach**
Her iki yaklaşım da tek bir hücrenin içine sığan bir resim üretir, ancak resmin nasıl saklandığı ve nasıl davrandığı konusunda farklılık gösterir:
- **Şu durumlarda kayan resim kullanın (Yaklaşım 1):**
  - Yerleştirme, katmanlama veya diğer çizim nesneleriyle hizalama üzerinde daha ayrıntılı denetime ihtiyacınız olduğunda.
  - Resmin diğer şekillerle seçilebilen, yeniden sıralanabilen veya gruplanabilen bir şekil olarak davranmasını istediğinizde.
  - `PictureCollection` ile zaten çalışan kodla eski sürüm uyumluluğu gerektirdiğinizde.
  - Çalışma sayfası düzenine göre bağlantı koordinatlarını dinamik olarak hesaplamanız gerektiğinde.
- **Şu durumlarda gömülü resim kullanın (Yaklaşım 2):**
  - Bir hücreye en basit olası resim eklemeyi istediğinizde.
  - Resmin diğer hücre içerikleri gibi hücreyle birlikte hareket etmesi gerektiğinde.
{{% /alert %}}

## Related Articles
- [Aspose.Cells for .NET'te Excel Kamera](/cells/tr/net/excel-camera/)
- [Aspose.Cells for .NET'te Pivot Tabloya Filtre Alanları Ekleme](/cells/tr/net/add-page-field-in-pivot-table/)
- [Aspose.Cells for .NET'te Pivot Tablolarına Stil Uygulama](/cells/tr/net/apply-style-to-pivot-table/)
- [Pivot Tablosunda Sayfa Alanı Düzenini Değiştirme](/cells/tr/net/change-page-field-layout/)
- [Aspose.Cells for .NET'te Sparkline'ı Resme ve HTML'ye Dönüştürme](/cells/tr/net/convert-sparkline-to-image-and-html/)

{{< app/cells/assistant language="csharp" >}}