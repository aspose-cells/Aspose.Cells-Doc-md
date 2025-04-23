---
title: Çalışma Sayfasına İkonlar Ekleme ile C++
linktitle: Simgeleri Yönetme
type: docs
weight: 100
url: /tr/cpp/insert-svg-to-excel/
description: Aspose.Cells kullanarak Excel çalışma sayfalarına ikonlar nasıl eklenir öğrenin.
---

## Aspose.Cells'te Çalışma Sayfasına Simgeler Ekleme

Eğer bir Excel dosyasına 'simgeler' eklemek için [Aspose.Cells](https://products.aspose.com/cells/) kullanmanız gerekiyorsa, bu belge size bazı yardımlar sağlayabilir.

Ekle simgesine karşılık gelen Excel arayüzü aşağıdaki gibidir:

![](1.png)

- Çalışma sayfasına eklemek istediğiniz simgenin konumunu seçin
- *Ekle*->*Simgeler*ü tıklayın
- Açılan pencerede, yukarıdaki resimde kırmızı dikdörtgen içindeki simgeyi seçin
- Sol tıklama *Ekle* seçimine tıklayın, Excel dosyasına eklenecektir.

Efekt aşağıdaki gibidir:

![](2.png)

Burada, simgeleri [Aspose.Cells](https://products.aspose.com/cells/) kullanarak eklemenize yardımcı olacak *örnek kod* hazırlandı. Ayrıca gerekli [örnek dosya](sample.xlsx) ve bir ikon [kaynak dosyası](icon.zip) bulunmaktadır. Aynı görüntü efektini vermek için Excel arayüzünü kullanarak, [kaynak dosyası](icon.zip) içinden bir ikon ekledik ve [örnek dosya](sample.xlsx).

### C++

```cpp
#include <iostream>
#include <fstream>
#include <vector>
#include <memory>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    U16String fileName = u"icon.svg";
    std::ifstream fsSource(fileName.ToUtf8(), std::ios::binary);
    if (!fsSource) {
        std::cerr << "Failed to open file: " << fileName.ToUtf8() << std::endl;
        return -1;
    }

    fsSource.seekg(0, std::ios::end);
    size_t fileSize = fsSource.tellg();
    fsSource.seekg(0, std::ios::beg);

    std::vector<uint8_t> bytes(fileSize);
    fsSource.read(reinterpret_cast<char*>(bytes.data()), fileSize);
    fsSource.close();

    Aspose::Cells::Vector<uint8_t> asposeBytes(bytes.size());
    if (!bytes.empty()) {
        memcpy(asposeBytes.GetData(), bytes.data(), bytes.size());
    }

    Workbook workbook(u"sample.xlsx");
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    sheet.GetShapes().AddIcons(3, 0, 7, 0, 100, 100, asposeBytes, Aspose::Cells::Vector<uint8_t>());

    Cell c = sheet.GetCells().Get(8, 7);
    c.PutValue(u"Insert via Aspose.Cells");
    Style s = c.GetStyle();
    s.GetFont().SetColor(Color::Blue());
    c.SetStyle(s);

    workbook.Save(u"sample2.xlsx", SaveFormat::Xlsx);

    Aspose::Cells::Cleanup();
    return 0;
}
```

Yukarıdaki kodu projenizde çalıştırdığınızda aşağıdaki sonuçları elde edersiniz:

![](3.png)
