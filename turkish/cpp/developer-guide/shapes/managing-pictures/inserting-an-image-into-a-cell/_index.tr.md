---
title: Hücreye Resim Ekleme
linktitle: Hücreye Resim Ekleme
description: Aspose.Cells, elektronik tablo dosyalarıyla çalışmak için bir C++ kütüphanesidir. Bu makale, resmi hücrenin üzerine kayan bir resim yerleştirerek veya görüntüyü doğrudan hücreye gömerek tek bir hücreye tam olarak sığdırmayı açıklar.
keywords: Aspose.Cells, C++ kütüphanesi, elektronik tablo, resim ekleme, görüntü gömme, hücredeki resim, hücreye resim sığdırma, PictureCollection, EmbeddedImage
type: docs
weight: 80
url: /tr/cpp/inserting-an-image-into-a-cell/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells, bir görüntüyü tek bir hücreyle ilişkilendirmek için iki farklı yol sunar. Kayan resim, çalışma sayfasının çizim katmanında bir hücre aralığının üzerinde görsel olarak yer alan bir şekildir; gömülü görüntü ise hücrenin kendi içinde saklanır ve hücrenin görüntüleme alanına otomatik olarak ölçeklenir. Düzen gereksinimlerinize en uygun yaklaşımı seçin.
{{% /alert %}}

## **Introduction**
Bir resmi tam olarak tek bir hücreye sığdırmak, görsel raporlar, ürün katalogları, çalışan rehberleri, panolar veya envanter listeleri olarak işlev gören elektronik tablolar tasarlarken yaygın bir gereksinimdir. Görüntüyü birçok hücreye yayarak veya çalışma sayfasına gevşek bir şekilde yerleştirmek yerine, sahip olduğu hücreyle hizalı kalan, temiz ve hücreye bağlı bir resim isteyebilirsiniz.
Aspose.Cells bu senaryoyu iki tamamlayıcı şekilde destekler:
- **Yaklaşım 1 — Hücrenin üzerine kayan bir resim yerleştirin.** Çalışma sayfasına bir `Picture` ekleyin, `Placement` özelliğini `MoveAndSize` olarak ayarlayın ve resmin tam olarak bir hücreyi kaplaması için bağlantı hücrelerini (`UpperLeftRow`, `UpperLeftColumn`, `LowerRightRow`, `LowerRightColumn`) ayarlayın.
- **Yaklaşım 2 — Görüntüyü doğrudan bir hücreye gömün.** Görüntü baytlarını hücrenin `EmbeddedImage` özelliğine atayın. Görüntü, hücrenin görüntüleme alanına sığacak şekilde otomatik olarak ölçeklenir ve hücreyle birlikte hareket eder.
Bu makalenin geri kalanı her iki yaklaşımı da ele alır, ilgili API'leri açıklar ve bunların kodda nasıl kullanılacağını gösterir.

## **Approach 1: Place a Picture Over a Cell**
Kayan resim, çalışma sayfasının çizim katmanında bulunan bir `Picture` nesnesidir. Herhangi bir tek hücrenin parçası olmasa da bir hücre aralığına bağlıdır. Resmin bağlantı hücreleri — sol üst ve sağ alt köşeleri — çalışma sayfasındaki görsel kapsamını belirler. Varsayılan olarak, yeni eklenen bir resim birkaç hücreyi kaplar.
Bir kayan resmin **tam olarak bir hücreyi** kaplamasını sağlamak için şunları yapmanız gerekir:
1. Resmi, yeni resmi verilen hücreye bağlayan `Worksheet.Pictures.Add(int row, int column, Vector<uint8_t> stream)` kullanarak ekleyin.
2. Resmin sınırlayıcı dikdörtgeni hedef hücreyle çakışacak şekilde dört bağlantı özelliğini ayarlayın.
3. Kullanıcı sütun genişliğini veya satır yüksekliğini değiştirdiğinde resmin alttaki hücreyle birlikte hareket etmesi ve yeniden boyutlandırılması için `Picture.Placement` özelliğini `PlacementType.MoveAndSize` olarak ayarlayın.

### **Anchoring the Picture to a Single Cell**
Resmin bağlantısı, dört sıfır tabanlı dizin özelliği ile tanımlanır:
- `Picture.UpperLeftRow` — resmin üst kenarının satır dizini.
- `Picture.UpperLeftColumn` — resmin sol kenarının sütun dizini.
- `Picture.LowerRightRow` — resmin alt kenarının satır dizini. Resmin alt kenarının `r` satırının altına oturmasını sağlamak için bunu `r + 1` olarak ayarlayın.
- `Picture.LowerRightColumn` — resmin sağ kenarının sütun dizini. Resmin sağ kenarının `c` sütununun sağına oturmasını sağlamak için bunu `c + 1` olarak ayarlayın.

{{% alert color="primary" %}}
Aspose.Cells'deki satır ve sütun dizinleri **sıfır tabanlıdır**. C6 hücresinin satır dizini 5 ve sütun dizini 2'dir. Sağ alt bağlantı noktasındaki bir-ofset hataları, resimlerin bitişik bir hücreye taşmış gibi görünmesinin en yaygın kaynağıdır.

### **Controlling Placement Behavior**
`Picture.Placement`, kullanıcı alttaki satır veya sütunu yeniden boyutlandırdığında resmin nasıl davranacağını kontrol eden `PlacementType` türünde bir numaralandırmadır. Tek hücreli resim için önerilen değer `PlacementType.MoveAndSize` değeridir; bu, resmin alttaki hücreyle birlikte hareket etmesini ve yeniden boyutlandırılmasını sağlayarak tam sığmayı korur.

### **Step-by-Step Instructions**
1. Yeni bir `Workbook` oluşturun (veya mevcut birini açın).
2. Hedef `Worksheet`'e `workbook.GetWorksheets().Get(0]` aracılığıyla erişin.
3. Görüntü baytlarının API için kullanılabilir olması için görüntü dosyasını diskten bir `Vector<uint8_t>` bayt arabelleğine okuyun.
4. C6 hücresine bağlı bir resim eklemek için `worksheet.Pictures.Add(5, 2, imageData)` çağrısını yapın. Döndürülen `Picture` referansını yakalayın.
5. Resmin yalnızca C6 hücresini kaplaması için dört bağlantı koordinatını ayarlayın: `UpperLeftRow = 5`, `UpperLeftColumn = 2`, `LowerRightRow = 6`, `LowerRightColumn = 3`.
6. Sütun veya satır yeniden boyutlandırıldığında resmin C6 ile hizalı kalmasını sağlamak için `picture.Placement = PlacementType.MoveAndSize` ayarlayın.
7. İsteğe bağlı olarak, yalnızca C6 hücresinin resmi içerdiğini göstermek için çevreleyen hücrelere örnek metin ekleyin.
8. Çalışma kitabını diskte bir `.xlsx` dosyası olarak kaydedin.
Aşağıdaki kod, eksiksiz yaklaşımı gösterir.

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

## **Approach 2: Embed an Image Directly in a Cell**
Aspose.Cells ayrıca hücreye bağlı görüntüler için daha basit bir mekanizma sunar: `Cell.EmbeddedImage` özelliği. Görüntü baytlarını bu özelliğe atamak, görüntüyü satır içi içerikmiş gibi hücrenin kendisine ekler.

### **How Embedded Images Work**
- Görüntü, çizim katmanında bir şekil olarak değil, hücre içeriğinin bir parçası olarak saklanır.
- Görüntü, hücrenin işlenmiş sınırları içine sığacak şekilde otomatik olarak ölçeklenir. Bağlantı koordinatlarına veya yerleştirme ayarlarına gerek yoktur.
- Hücre, formüller tarafından referans alınabilen, bir satırın parçası olarak sıralanabilen veya diğer hücre düzeyindeki işlemlerde kullanılabilen gerçek bir adrese sahip gerçek bir hücre olarak kalır.
Bu, amacınız yalnızca "bu hücrenin içinde yaşayan bir görüntü" olduğunda `Cell.EmbeddedImage` özelliğini en kısa seçenek haline getirir.

### **Step-by-Step Instructions**
1. Yeni bir `Workbook` oluşturun (veya mevcut birini açın).
2. Hedef `Worksheet`'e `workbook.GetWorksheets().Get(0]` aracılığıyla erişin.
3. Görüntü dosyasını diskten bir `Vector<uint8_t>` bayt dizisine okuyun.
4. Hedef hücreye bir referans alın — `worksheet.GetCells().Get("C6"]` veya `worksheet.GetCells().Get(5, 2]` aracılığıyla.
5. Bayt dizisini hücrenin `EmbeddedImage` özelliğine atayın.
6. İsteğe bağlı olarak, gömülü görüntüye daha belirgin bir görünüm kazandırmak için hedef satır ve sütunun satır yüksekliğini ve sütun genişliğini ayarlayın.
7. Çalışma kitabını diskte bir `.xlsx` dosyası olarak kaydedin.
Aşağıdaki kod, eksiksiz yaklaşımı gösterir.

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
    // std::vector'ı pointer+size yapıcısını kullanarak Aspose::Cells::Vector'a dönüştür
    Vector<uint8_t> imageData(stdImageData.data(), (int32_t)stdImageData.size());
    // Görüntüyü doğrudan hücreye yerleştir
    cell.SetEmbeddedImage(imageData);
    // İsteğe bağlı olarak satır yüksekliğini ve sütun genişliğini ayarla; böylece yerleştirilmiş görüntü daha görünür olur
    worksheet.GetCells().SetColumnWidth(2, 30);   // C sütunu (2. indeks)
    worksheet.GetCells().SetRowHeight(5, 100);    // 6. satır (5. indeks)
    // Sonuç çalışma kitabını .xlsx dosyası olarak kaydet
    wb.Save(u"output.xlsx", SaveFormat::Xlsx);
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Choosing the Right Approach**
Her iki yaklaşım da tek bir hücrenin içine sığan bir resim üretir, ancak resmin nasıl depolandığı ve nasıl davrandığı konusunda farklılık gösterir:
- **Şu durumlarda kayan resim kullanın (Yaklaşım 1):**
  - Yerleştirme, katmanlama veya diğer çizim nesneleriyle hizalama üzerinde daha ayrıntılı denetime ihtiyaç duyduğunuzda.
  - Resmin, seçilebilen, yeniden sıralanabilen veya diğer şekillerle gruplanabilen bir şekil olarak davranmasını istediğinizde.
  - Zaten `PictureCollection` ile çalışan kodla eski sürüm uyumluluğuna ihtiyaç duyduğunuzda.
  - Bağlantı koordinatlarını çalışma sayfası düzenine göre dinamik olarak hesaplamanız gerektiğinde.
- **Şu durumlarda gömülü görüntü kullanın (Yaklaşım 2):**
  - Bir hücreye olabildiğince basit bir şekilde görüntü eklemek istediğinizde.
  - Görüntü, diğer hücre içerikleri gibi hücreyle birlikte hareket etmelidir.
{{% /alert %}}

## Related Articles
- [Aspose.Cells for C++'ta Excel Kamerası](/cells/tr/cpp/excel-camera/)
- [Aspose.Cells for C++'ta Pivot Tablosuna Filtre Alanları Ekleme](/cells/tr/cpp/add-page-field-in-pivot-table/)
- [Aspose.Cells for C++'ta Pivot Tablolarına Stil Uygulama](/cells/tr/cpp/apply-style-to-pivot-table/)
- [Pivot Tablosunda Sayfa Alanı Düzenini Değiştirme](/cells/tr/cpp/change-page-field-layout/)
- [Aspose.Cells for C++'ta Mini Grafiği Görüntüye ve HTML'ye Dönüştürme](/cells/tr/cpp/convert-sparkline-to-image-and-html/)

{{< app/cells/assistant language="cpp" >}}