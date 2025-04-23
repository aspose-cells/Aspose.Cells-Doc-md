---
title: C++ ile Aralıkları Yönetme
linktitle: Aralıklar
type: docs
weight: 105
url: /tr/cpp/managing-ranges/
description: Aspose.Cells kullanarak Excel dosyalarında aralıkları nasıl yöneteceğinizi öğrenin. Programatik olarak aralıklar oluşturun, düzenleyin ve biçimlendirin.
---

## **Giriş**

Excel'de fare kutu seçimi ile birden fazla hücre seçebilirsiniz, seçilen hücrelerin setine "Aralık" denir.

Örneğin, Excel'in "A1" hücresine sol fare düğmesiyle tıklayıp ardından "C4" hücresine sürükleyebilirsiniz. Seçtiğiniz dikdörtgen alanı, Aspose.Cells kullanarak kolayca bir nesne olarak da oluşturulabilir.

Aralık oluşturma, değer koyma, stil ayarlama ve "Aralık" nesnesine daha fazla işlem yapmanın yolları.

## **Aspose.Cells kullanarak Aralıkları Yönetme**

Aspose.Cells, Microsoft Excel dosyasını temsil eden bir sınıf, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sağlar. [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) sınıfı, bir Excel dosyasındaki her çalışsayfaya erişim sağlayan [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) koleksiyonunu içerir. Bir çalışsayfa [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfı tarafından temsil edilir. [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) sınıfı bir [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) koleksiyonu sağlar.

### **Aralık Oluştur**

A1:C4 üzerine uzanan bir dikdörtgen alan oluşturmak istediğinizde aşağıdaki kodu kullanabilirsiniz:

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a Workbook
    Workbook workbook;

    // Get Cells from the first worksheet
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();

    // Create a Range from A1 to C4
    Range range = cells.CreateRange(u"A1:C4");

    Aspose::Cells::Cleanup();
}
```

### **Aralık Hücrelerine Değer Atama**

Örneğin, A1:C4'e uzanan bir hücre aralığınız var. Matris, 4 * 3 = 12 hücre oluşturur. Aralık hücreleri sıralı bir şekilde düzenlenir: Aralık[0,0], Aralık[0,1], Aralık[0,2], Aralık[1,0], Aralık[1,1], Aralık[1,2], Aralık[2,0], Aralık[2,1], Aralık[2,2], Aralık[3,0], Aralık[3,1], Aralık[3,2].

Aşağıdaki örnek, Aralık hücrelerine bazı değerleri girme işlemini göstermektedir.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a Workbook
    Workbook workbook;

    // Get Cells from the first worksheet
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();

    // Create a Range from A1 to C4
    Range range = cells.CreateRange(u"A1:C4");

    // Put values in specific cells
    range.Get(0, 0).PutValue(u"A1");
    range.Get(0, 1).PutValue(u"B1");
    range.Get(0, 2).PutValue(u"C1");
    range.Get(3, 0).PutValue(u"A4");
    range.Get(3, 1).PutValue(u"B4");
    range.Get(3, 2).PutValue(u"C4");

    // Save the Workbook
    workbook.Save(u"RangeValueTest.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Aralık Hücrelerinin Stilini Belirleme**

Aşağıdaki örnek, Aralığın hücrelerinin stilini ayarlamanın nasıl yapıldığını göstermektedir.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a Workbook
    Workbook workbook;

    // Get Cells
    WorksheetCollection sheets = workbook.GetWorksheets();
    Cells cells = sheets.Get(0).GetCells();

    // Create Range
    Range range = cells.CreateRange(u"A1:C4");

    // Put value
    range.Get(0, 0).PutValue(u"A1");
    range.Get(3, 2).PutValue(u"C4");

    // Set Style
    Style style00 = workbook.CreateStyle();
    style00.SetPattern(BackgroundType::Solid);
    style00.SetForegroundColor(Color::Red());
    range.Get(0, 0).SetStyle(style00);

    Style style32 = workbook.CreateStyle();
    style32.SetPattern(BackgroundType::HorizontalStripe);
    style32.SetForegroundColor(Color::Green());
    range.Get(3, 2).SetStyle(style32);

    // Save the Workbook
    workbook.Save(u"RangeStyleTest.xlsx");

    std::cout << "Workbook saved successfully with range styles applied!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Aralık 'ın Mevcut Bölgesini Al**

CurrentRegion, mevcut bir bölgeyi temsil eden bir Aralık nesnesi döndüren bir özelliktir. 

Mevcut bölge, herhangi bir kombinasyonla sınırlandırılmış bir aralıktır. Salt okunur.

Excel'de, CurrentRegion alanını şu şekilde alabilirsiniz:
1. Fare kutusu ile bir alan (range1) seçin.
2. "Ana Sayfa - Düzenleme - Bul & Seç - Özel Git - Gelen bölge" yi tıklayın veya "Ctrl+Shift+*" kullanarak, excel otomatik olarak bir bölge (range2) seçmenize yardımcı olacaktır, şimdi başardınız, range2 range1'in CurrentRegion'ıdır.

Aspose.Cells kullanarak aynı işlemi yapmak için "Range.CurrentRegion" özelliğini kullanabilirsiniz.

Lütfen aşağıdaki test dosyasını indirin, excel'de açın, bir alanı seçmek için fare kutusunu kullanın "A1:D7", sonra "Ctrl+Shift+*" tıklayın, "A1:C3" alanının seçildiğini göreceksiniz.

[current_region.xlsx](current_region.xlsx)

Şimdi lütfen aşağıdaki örneği çalıştırın, Aspose.Cells içinde nasıl çalıştığını görün:

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a Workbook
    Workbook workbook(u"current_region.xlsx");

    // Get Cells from the first worksheet
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();

    // Create a Range from A1 to D7
    Range src = cells.CreateRange(u"A1:D7");

    // Get the CurrentRegion of the created range
    Range A1C3 = src.GetCurrentRegion();

    Aspose::Cells::Cleanup();
}
```


## **Gelişmiş Konular**
- [Excel dosyasının Otomatik Doldurması](/cells/tr/cpp/autofill-ranges/)
- [Excel'in Aralıklarını Kopyala](/cells/tr/cpp/copy-ranges-of-Excel/)
- [Yalnızca Aralık Verisini Kopyala](/cells/tr/cpp/copy-range-data-only/)
- [Yalnızca Aralık Verisiyle Kopyala](/cells/tr/cpp/copy-range-data-with-style/)
- [Yalnızca Aralık Stiliyle Kopyala](/cells/tr/cpp/copy-range-style-only/)
- [Birleşik Aralık Oluştur](/cells/tr/cpp/create-union-range/)
- [Aralığı Kes ve Yapıştır](/cells/tr/cpp/cut-and-paste-cells/)
- [Aralıkları Sil](/cells/tr/cpp/delete-ranges-from-Excel/)
- [Aralığın Adresini, Hücre Sayısını ve Konumunu, Tüm Sütunu ve Tüm Satırı Al](/cells/tr/cpp/get-address-cell-count-offset-entire-column-and-entire-row-of-the-range/)
- [Aralık Ekle](/cells/tr/cpp/insert-ranges-to-Excel/)
- [Hücreleri Birleştir veya Birleşikliği Kaldır](/cells/tr/cpp/merge-or-unmerge-range-of-cells/)
- [Çalışma Sayfasında Hücre Aralığını Taşıma](/cells/tr/cpp/move-range-of-cells-in-a-worksheet/)
- [Çalışma Kitabı ve Çalışma Sayfası Kapsamlı Adlandırılan Aralıkları Oluştur](/cells/tr/cpp/create-workbook-and-worksheet-scoped-named-ranges/)
- [Aralıktaki Veriyi Arama ve Değiştirme](/cells/tr/cpp/search-and-replace-data-in-a-range/)
