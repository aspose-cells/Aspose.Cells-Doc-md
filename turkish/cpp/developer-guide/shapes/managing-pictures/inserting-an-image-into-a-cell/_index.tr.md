---
title: Bir Hücreye Görüntü Ekleme
description: Aspose.Cells, elektronik tablo dosyalarıyla çalışmak için kullanılan bir C++ kütüphanesidir. Bu makale, resmi tek bir hücre boyutuna tam olarak sığdırmak için iki farklı yaklaşımı açıklar: hücrenin üzerine kayan bir resim yerleştirmek veya görüntüyü doğrudan hücrenin içine gömmek.
keywords: Aspose.Cells, C++ kütüphanesi, elektronik tablo, görüntü ekleme, görüntü gömme, hücredeki resim, resmi hücreye sığdırma, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /tr/cpp/inserting-an-image-into-a-cell/
---

{{% alert color="primary" %}}

Aspose.Cells, bir görüntüyü tek bir hücreyle ilişkilendirmek için iki farklı yol sunar. Kayan resim, çalışma sayfası çizim katmanındaki bir hücre aralığının üzerinde görsel olarak yer alan bir şekildir; gömülü görüntü ise hücrenin kendisinin içinde saklanır ve hücrenin görüntüleme alanına otomatik olarak ölçeklenir. Düzen gereksinimlerinize en uygun yaklaşımı seçin.

{{% /alert %}}

## **Giriş**

Bir resmi tam olarak tek bir hücreye sığdırmak, görsel raporlar, ürün katalogları, çalışan rehberleri, panolar veya envanter listeleri olarak işlev gören elektronik tablolar tasarlanırken yaygın bir gereksinimdir. Görüntüyü birçok hücreye yaymak veya çalışma sayfasına gevşek bir şekilde yerleştirmek yerine, kendisine ait hücreyle hizalı kalan temiz, hücreye bağlı bir görüntü isteyebilirsiniz.

Aspose.Cells bu senaryoyu iki tamamlayıcı şekilde destekler:

- **Yaklaşım 1 — Hücrenin üzerine kayan bir resim yerleştirin.** Çalışma sayfasına bir `Picture` ekleyin, `Placement` özelliğini `MoveAndSize` olarak ayarlayın ve resmin tam olarak bir hücreyi kaplaması için çapa hücrelerini (`UpperLeftRow`, `UpperLeftColumn`, `LowerRightRow`, `LowerRightColumn`) ayarlayın.
- **Yaklaşım 2 — Görüntüyü doğrudan bir hücreye gömün.** Görüntü baytlarını hücrenin `EmbeddedImage` özelliğine atayın. Görüntü, hücrenin görüntüleme alanına sığacak şekilde otomatik olarak ölçeklenir ve hücreyle birlikte taşınır.

Bu makalenin geri kalanı her iki yaklaşımı da ele alır, ilgili API'leri açıklar ve bunların kodda nasıl kullanılacağını gösterir.

## **Yaklaşım 1: Hücrenin Üzerine Bir Resim Yerleştirme**

Kayan resim, çalışma sayfası çizim katmanında bulunan bir `Picture` nesnesidir. Herhangi bir tek hücrenin parçası olmasa da bir hücre aralığına sabitlenir. Resmin çapa hücreleri — sol üst ve sağ alt köşeleri — çalışma sayfasındaki görsel kapsamını belirler. Varsayılan olarak, yeni eklenen bir resim birkaç hücreyi kapsar.

Kayan bir resmin **tam olarak bir hücreyi** kaplamasını sağlamak için şunları yapmanız gerekir:

1. Resmi `Worksheet.Pictures.Add(int row, int column, Vector<uint8_t> stream)` kullanarak ekleyin; bu yeni resmi verilen hücreye sabitler.
2. Resmin sınırlayıcı dikdörtgeni hedef hücreyle çakışacak şekilde dört çapa özelliğini ayarlayın.
3. Kullanıcı sütun genişliğini veya satır yüksekliğini değiştirdiğinde resmin alttaki hücreyle birlikte hareket etmesi ve yeniden boyutlandırılması için `Picture.Placement` özelliğini `PlacementType.MoveAndSize` olarak ayarlayın.

### **Resmi Tek Bir Hücreye Sabitleme**

Resmin çapası, dört sıfır tabanlı dizin özelliğiyle tanımlanır:

- `Picture.UpperLeftRow` — resmin üst kenarının satır dizini.
- `Picture.UpperLeftColumn` — resmin sol kenarının sütun dizini.
- `Picture.LowerRightRow` — resmin alt kenarının satır dizini. Resmin alt kenarının `r` satırının altına oturmasını sağlamak için bunu `r + 1` olarak ayarlayın.
- `Picture.LowerRightColumn` — resmin sağ kenarının sütun dizini. Resmin sağ kenarının `c` sütununun sağına oturmasını sağlamak için bunu `c + 1` olarak ayarlayın.

Örneğin, resmi tam olarak **C6** hücresine (satır dizini `5`, sütun dizini `2`) sığdırmak için `UpperLeftRow = 5`, `UpperLeftColumn = 2`, `LowerRightRow = 6` ve `LowerRightColumn = 3` olarak ayarlayın.

{{% alert color="primary" %}}

Aspose.Cells'te satır ve sütun dizinleri **sıfır tabanlıdır**. C6 hücresinin satır dizini 5 ve sütun dizini 2'dir. Sağ alt çapa üzerindeki off-by-one hataları, bitişik hücreye taşmış gibi görünen resimlerin en yaygın kaynağıdır.

{{% /alert %}}

### **Yerleşim Davranışını Kontrol Etme**

`Picture.Placement`, kullanıcı alttaki satır veya sütunu yeniden boyutlandırdığında resmin nasıl davranacağını kontrol eden `PlacementType` türünde bir numaralandırmadır. Tek hücreli bir resim için önerilen değer `PlacementType.MoveAndSize`'dır; bu, resmin alttaki hücreyle birlikte hareket etmesine ve yeniden boyutlandırılmasına neden olarak tam sığmayı korur.

### **Adım Adım Talimatlar**

1. Yeni bir `Workbook` oluşturun (veya mevcut birini açın).
2. `workbook.Worksheets[0]` üzerinden hedef `Worksheet`'e erişin.
3. Görüntü dosyasını diskten bir `Vector<uint8_t>` bayt arabelleğine okuyun, böylece görüntü baytları API için kullanılabilir hale gelir.
4. Resmi C6 hücresine sabitlenmiş şekilde eklemek için `worksheet.Pictures.Add(5, 2, imageData)` çağırın. Döndürülen `Picture` referansını yakalayın.
5. Resmin yalnızca C6 hücresini kaplaması için dört çapa koordinatını ayarlayın: `UpperLeftRow = 5`, `UpperLeftColumn = 2`, `LowerRightRow = 6`, `LowerRightColumn = 3`.
6. Sütun veya satır yeniden boyutlandırıldığında resmin C6 ile hizalı kalmasını sağlamak için `picture.Placement = PlacementType.MoveAndSize` ayarlayın.
7. İsteğe bağlı olarak, yalnızca C6 hücresinin resmi içerdiğini göstermek için çevreleyen hücrelere örnek metin ekleyin.
8. Çalışma kitabını diskte `.xlsx` dosyası olarak kaydedin.

Aşağıdaki kod, yaklaşımın tamamını gösterir.

```cpp
#include "Aspose.Cells.h"
#include <fstream>
#include <vector>
#include <iterator>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    std::ifstream fs("logo.png", std::ios::binary);
    std::vector<uint8_t> stdData((std::istreambuf_iterator<char>(fs)),
                                  std::istreambuf_iterator<char>());
    fs.close();

    Vector<uint8_t> imageData(reinterpret_cast<const uint8_t*>(stdData.data()),
                              static_cast<int32_t>(stdData.size()));

    int picIndex = worksheet.GetPictures().Add(5, 2, imageData);
    Picture picture = worksheet.GetPictures().Get(picIndex);
    picture.SetUpperLeftRow(5);
    picture.SetUpperLeftColumn(2);
    picture.SetLowerRightRow(6);
    picture.SetLowerRightColumn(3);
    picture.SetPlacement(PlacementType::MoveAndSize);

    workbook.Save(u"output.xlsx", SaveFormat::Xlsx);

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Yaklaşım 2: Bir Görüntüyü Doğrudan Bir Hücreye Gömme**

Aspose.Cells ayrıca hücreye bağlı görüntüler için daha basit bir mekanizma sunar: `Cell.EmbeddedImage` özelliği. Görüntü baytlarını bu özelliğe atamak, görüntüyü satır içi içerikmiş gibi hücrenin kendisine ekler.

### **Gömülü Görüntüler Nasıl Çalışır**

- Görüntü, çizim katmanındaki bir şekil olarak değil, hücre içeriğinin bir parçası olarak saklanır.
- Görüntü, hücrenin işlenmiş sınırları içine sığacak şekilde otomatik olarak ölçeklenir. Çapa koordinatları veya yerleşim ayarları gerekmez.
- Hücre, formüller tarafından başvurulabilen, bir satırın parçası olarak sıralanabilen veya diğer hücre düzeyinde işlemlerde kullanılabilen gerçek bir adrese sahip gerçek bir hücre olarak kalır.

Bu, amacınızın yalnızca "bu hücrenin içinde yaşayan bir görüntü" olduğu durumlarda `Cell.EmbeddedImage`'ı en kısa seçenek haline getirir.

### **Adım Adım Talimatlar**

1. Yeni bir `Workbook` oluşturun (veya mevcut birini açın).
2. `workbook.Worksheets[0]` üzerinden hedef `Worksheet`'e erişin.
3. Görüntü dosyasını diskten bir `Vector<uint8_t>` bayt dizisine okuyun.
4. Hedef hücreye bir referans alın — `worksheet.Cells["C6"]` veya `worksheet.Cells[5, 2]` aracılığıyla.
5. Bayt dizisini hücrenin `EmbeddedImage` özelliğine atayın.
6. İsteğe bağlı olarak, gömülü görüntüye daha belirgin bir görünüm kazandırmak için hedef satırın ve sütunun satır yüksekliğini ve sütun genişliğini ayarlayın.
7. Çalışma kitabını diskte `.xlsx` dosyası olarak kaydedin.

Aşağıdaki kod, yaklaşımın tamamını gösterir.

```cpp
#include "Aspose.Cells.h"
#include <vector>
#include <fstream>
#include <iterator>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook wb;
    Worksheet worksheet = wb.GetWorksheets().Get(0);

    Cell cell = worksheet.GetCells().Get(u"C6");

    // Görüntü dosyasını bir bayt dizisine oku
    std::ifstream file("logo.png", std::ios::binary);
    std::vector<uint8_t> stdImageData((std::istreambuf_iterator<char>(file)), std::istreambuf_iterator<char>());
    file.close();

    // std::vector'ü işaretçi+boyut yapıcısını kullanarak Aspose::Cells::Vector'e dönüştür
    Vector<uint8_t> imageData(stdImageData.data(), (int32_t)stdImageData.size());

    // Görüntüyü doğrudan hücreye yerleştir
    cell.SetEmbeddedImage(imageData);

    // İsteğe bağlı olarak, gömülü görüntünün daha görünür olması için satır yüksekliğini ve sütun genişliğini ayarlayın
    worksheet.GetCells().SetColumnWidth(2, 30);   // Sütun C (indeks 2)
    worksheet.GetCells().SetRowHeight(5, 100);    // Satır 6 (indeks 5)

    // Elde edilen çalışma kitabını bir .xlsx dosyası olarak kaydedin
    wb.Save(u"output.xlsx", SaveFormat::Xlsx);

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Doğru Yaklaşımı Seçme**

Her iki yaklaşım da tek bir hücrenin içine sığan bir resim üretir, ancak resmin nasıl saklandığı ve nasıl davrandığı konusunda farklılık gösterir:

- **Şu durumlarda kayan resim kullanın (Yaklaşım 1):**
  - Yerleşim, katmanlama veya diğer çizim nesneleriyle hizalama üzerinde daha ayrıntılı denetime ihtiyacınız olduğunda.
  - Resmin diğer şekillerle seçilebilen, yeniden sıralanabilen veya gruplanabilen bir şekil olarak davranmasını istediğinizde.
  - Zaten `PictureCollection` ile çalışan kodla eski sürüm uyumluluğu gerektirdiğinizde.
  - Çalışma sayfası düzenine göre çapa koordinatlarını dinamik olarak hesaplamanız gerektiğinde.

- **Şu durumlarda gömülü görüntü kullanın (Yaklaşım 2):**
  - Bir hücreye görüntü eklemenin en basit olası yolunu istediğinizde.
  - Görüntünün diğer hücre içerikleri gibi hücreyle birlikte taşınması gerektiğinde.
  - Görüntüyü bir şekil olarak işlemeniz gerekmediğinde.

{{% alert color="primary" %}}

Her iki yaklaşım da aynı çalışma kitabında birlikte var olabilir. Bir hücre kümesinin üzerine kayan resimler yerleştirebilir ve diğer hücrelere doğrudan görüntüler gömebilirsiniz, çünkü iki mekanizma dosyada farklı depolama katmanları kullanır.

{{% /alert %}}

## **İlgili Makaleler**

- [Hücreye Resim Nasıl Yerleştirilir](/cells/tr/cpp/how-to-place-image-to-cell/)
- [Görüntü Köprüleri Ekleme](/cells/tr/cpp/add-image-hyperlinks/)
- [URL'den Web Görüntüsünü Excel Çalışma Sayfasına Yükleme](/cells/tr/cpp/load-a-web-image-from-a-url-into-an-excel-worksheet/)
- [Konum, Boyut ve Tasarımcı Grafiğini Düzenleme](/cells/tr/cpp/manipulate-position-size-and-designer-chart/)

{{< app/cells/assistant language="cpp" >}}