---
title: Aspose.Cells for C++ ile Excel Kamera
linktitle: Aspose.Cells for C++ ile Excel Kamera
description: Aspose.Cells for C++'ta Excel Kamerayı kullanarak kaynak verilerle yenilenen ve tüm kaynak biçimlendirmesini koruyan bir hücre aralığına bağlı dinamik bir resim oluşturmayı öğrenin.
keywords: Aspose.Cells, C++, Excel Kamera, dinamik resim, bağlı resim, Picture.Formula, UpdateSelectedValue, CreateRange, ToImage, Vector
type: docs
weight: 90
url: /tr/cpp/excel-camera/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Excel Kamera, bir hücre aralığının canlı bir görüntüsünü oluşturan ve çizim katmanında sıradan bir resim gibi yüzen bir çalışma sayfası nesnesidir. Aspose.Cells iki oluşturma modunu destekler: kaynak veriler değiştiğinde otomatik olarak yenilenen dinamik bir resim ve bir aralığın tek seferlik anlık görüntüsünü yakalayan statik bir resim. Bu makale, düzeninize uyan yaklaşımı seçebilmeniz için her iki yaklaşımı da adım adım açıklar.

## Excel Kamera Nedir?
Excel Kamera, çalışma sayfasının çizim katmanında belirli bir satır ve sütuna sabitlenmiş temelde bir resim nesnesidir. Normal eklenmiş bir resmin aksine, Kamera `"A1:F10"` gibi A1 tarzı bir formül aracılığıyla bir kaynak aralığına bağlıdır. Bu aralıktaki herhangi bir hücre değiştiğinde, Kameranın görüntüsü yeni içeriği yansıtacak şekilde otomatik olarak yenilenir. Kamera, kaynak alanın tam biçimlendirmesini korur — kenarlıklar, arka plan renkleri, yazı tipleri ve sayı biçimleri — böylece hücrelerin içinde görünen her şey Kameranın görüntüsünde de görünür. Bu, Kameranın uzak bir bölgenin kaydırma veya veri tekrarı olmadan görünür bir önizlemesini istediğiniz panolar, özetler, yan paneller ve rapor düzenleri için özellikle kullanışlı olmasını sağlar. İki uyarı geçerlidir: çalışma kitabını kaydetmeden önce `UpdateSelectedValue()` çağrısı yapmalısınız ve dosya HTML veya PDF olarak dışa aktarılacaktır, çünkü bu biçimler canlı yeniden hesaplama yerine gömülü görüntü verilerine dayanır.

## Yöntem 1 — Dinamik Kamera Resmi Ekleme
Dinamik Kamera en yaygın yaklaşımdır ve Excel'in yerleşik Kamera aracına en yakın eşleşmedir. Başlangıçta görüntü içeriği olmayan bir resim ekleyerek, ardından kaynak aralığına başvuran bir `Formula` atayarak çalışır. Formül atandıktan sonra, `UpdateSelectedValue()` çağrısı, yansıttığı hücrelerle senkronize olması için gömülü görüntü verilerini yeniler. Kamera, özel bir sınıf aracılığıyla uygulanmaz — tamamen standart `Picture` türü üzerine kuruludur.
Temel API'ler şunlardır:
- `Pictures.Add(int upperLeftRow, int upperLeftColumn, Vector<uint8_t> data)` — verilen satır ve sütuna sabitlenmiş bir resim ekler. Boş bir `Vector<uint8_t>()` geçirilmesi, dinamik Kamera için yer tutucu olarak işlev gören boş bir resim oluşturur. Yöntem, yeni resmin dizinini döndürür.
- `worksheet.GetPictures().Get(int index)` — koleksiyondan dizine göre belirli bir `Picture` alır.
- `Picture.SetFormula(U16String value)` — Kameranın yansıttığı kaynak aralığına A1 tarzı başvuruyu ayarlar, örneğin `U16String("A1:F10")`.
- `Picture.UpdateSelectedValue()` — `Formula` tarafından başvurulan hücrelerden gömülü görüntü verilerini yeniler.

{{% alert color="primary" %}}
Çıktı HTML veya PDF olduğunda, kaydetmeden önce `UpdateSelectedValue()` çağrısı yapılmalıdır; aksi takdirde dışa aktarılan dosya resim verilerini içermeyecek ve Kamera oluşturulan çıktıda boş görünecektir.
{{% /alert %}}

Aşağıdaki kod bir çalışma kitabı oluşturur, 10. satır 6. sütuna sabitlenmiş boş bir resim ekler, onu `Formula` özelliği aracılığıyla `A1:F10` kaynak aralığına bağlar, gömülü görüntü verilerini yeniler ve çalışma kitabını kaydeder.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main()
{
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName(U16String("CameraDemo"));
    // Dinamik Kamera: boş bir resim ekleyin, Formül ile A1:F10'a bağlayın, ardından yenileyin
    int index = worksheet.GetPictures().Add(10, 6, Vector<uint8_t>());
    Picture picture = worksheet.GetPictures().Get(index);
    picture.SetFormula(U16String("A1:F10"));
    picture.UpdateSelectedValue();
    workbook.Save(U16String("output_dynamic.xlsx"), SaveFormat::Xlsx);
    Aspose::Cells::Cleanup();
    return 0;
}
```

## Yöntem 2 — Statik Kamera Resmi Ekleme
Statik Kamera temelde bir hücre aralığının tek seferlik oluşturulmuş bir önizlemesidir. Canlı bağlantıyı sürdürmek yerine, aralığı bir kez `Vector<uint8_t>` bayt arabelleğine dönüştürür ve bu arabelleği doğrudan `Pictures.Add(row, col, data)` öğesine geçirirsiniz. Görüntü içeriği oluşturma anında sabitlenir ve kaynak hücreler değiştiğinde otomatik olarak yenilenmez.
Temel API'ler şunlardır:
- `Cells.CreateRange(U16String address)` — A1 tarzı bir adresten (örneğin `U16String("A1:F10")`) bir `Range` nesnesi oluşturur.
- `Range.ToImage(ImageOrPrintOptions options)` — aralığı bir `Vector<uint8_t>` bayt arabelleğine dönüştürür. `nullptr` geçirilmesi varsayılan oluşturma seçeneklerini kullanır; çıktı üzerinde daha ayrıntılı kontrol için aşırı yüklemeler mevcuttur.
- `Pictures.Add(int upperLeftRow, int upperLeftColumn, Vector<uint8_t> data)` — resmi verilen satır ve sütuna sabitler, bu sefer `Range.ToImage` tarafından üretilen bayt arabelleğini geçirir.
Aşağıdaki kod bir çalışma kitabı oluşturur, `A1:F10` için bir `Range` oluşturur, onu `Range.ToImage(nullptr)` aracılığıyla görüntü baytlarına dönüştürür, 10. satır 6. sütuna sabitlenmiş resmi ekler ve çalışma kitabını kaydeder.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main()
{
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName(U16String("CameraDemo"));
    // Statik Kamera: Range oluştur, bayt olarak işle, resim olarak ekle
    Range range = worksheet.GetCells().CreateRange(U16String("A1:F10"));
    Vector<uint8_t> imageBytes = range.ToImage(nullptr);
    worksheet.GetPictures().Add(10, 6, imageBytes);
    workbook.Save(U16String("output_static.xlsx"), SaveFormat::Xlsx);
    Aspose::Cells::Cleanup();
    return 0;
}
```

## Dinamik ve Statik Arasında Seçim Yapma
- **Dinamik Kamera:** her yeniden hesaplamada güncellenir, `UpdateSelectedValue()` sonrasında HTML ve PDF dışa aktarımını destekler ve dosyanın ömrü boyunca canlı bağlantı davranışını korur.
- **Statik Kamera:** asla güncellenmeyen tek seferlik bir oluşturma, oluşturma zamanında gömülü sabit bir görsel anlık görüntü istediğiniz durumlarda verilerin canlı yansıması yerine kullanışlıdır.
Aspose.Cells, hem `Picture.Formula` ve `UpdateSelectedValue()` üzerine kurulu dinamik, otomatik yenilenen bir Kamerayı hem de `Range.ToImage` ve `Vector<uint8_t>` üzerine kurulu statik, tek seferlik bir Kamerayı destekler. Çıktınızın kaynak hücrelerle senkronize kalması gerektiğinde dinamik yaklaşımı, oluşturma zamanında yalnızca sabit bir görsel anlık görüntüye ihtiyacınız olduğunda ise statik yaklaşımı seçin.

{{< app/cells/assistant language="cpp" >}}