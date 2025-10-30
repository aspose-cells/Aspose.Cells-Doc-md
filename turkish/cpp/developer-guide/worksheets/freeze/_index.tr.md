---
title: C++ ile Excel Çalışma Sayfası Dondurma
linktitle: Pano Dondur
type: docs
weight: 190
url: /tr/cpp/how-to-freeze-panes-of-excel-worksheet
description: Bu makalede, Aspose.Cells API si kullanarak C++ ile Excel çalışma sayfalarının dondurulmasını programlı olarak nasıl yapacağınızı öğreneceksiniz.
keywords: Panelleri dondur, Pencereyi dondur.
---

## **Giriş**

Bu makalede, Panelleri Dondurmayı Öğreneceğiz. Bir anlamlı başlık altındaki büyük veri kümesine sahipseniz ve kaydırırken başlığı göremiyorsanız, veya her kayıtta birçok veri varsa, panelleri dondurabilir ve kaydırılan diğer verilerle birlikte donmuş bölümü görebilirsiniz. Üst satırlarda veya ilk sütunlarda başlıkları kolayca görebilirsiniz. Panelleri dondurma veya çözme, verilerin görünümünü değiştirir, veriyi değil.

## **Excel'de**

**![Excel'de Panoları Dondur](Freeze-panes.png)**

1. Panelleri dondurmak, satır ve sütunları dondurmak istiyorsanız, önce bir hücre seçin (örneğin B2).
2. Görünüm > Panoları Dondur'a tıklayın.
3. Açılır menüden Panoları Dondur'a tıklayın.
4. Kaydırdığınızda veya sağa kaydırdığınızda, ilk satır ve sütun donmuş kalır.

**![Donmuş Paneller](Frozen-Panes.png)**

Gördüğünüz gibi, 1. Satır ve sütun A Donmuş, ikinci satır 32 ve ikinci görünür sütun D'dir.

Pane donma özelliği, büyük verilerinizi Satır veya Sütun etiketlerini takip etmeksizin görüntülemenizi sağlar.

## **Aspose.Cells for C++ ile Pane Donma**
Aspose.Cells for C++ ile pane donmak çok basittir. Lütfen seçilen Hücrede pane donmak için [**Worksheet.FreezePanes**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/) yöntemini kullanın.
1. Bir çalışma kitabı oluşturun ya da dosyayı açmak veya boş bir dosya oluşturmak.
2. Worksheet.FreezePanes() yöntemi ile pane donma yapın.
3. Dosyayı kaydedin.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook
    U16String inputFilePath(u"Freeze.xlsx");
    Workbook workbook(inputFilePath);

    // Freeze panes at the cell B2
    WorksheetCollection sheets = workbook.GetWorksheets();
    sheets.Get(0).FreezePanes(u"B2", 1, 1);

    // Save the file
    U16String outputFilePath(u"frozen.xlsx");
    workbook.Save(outputFilePath);

    std::cout << "Panes frozen successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Ekli [örnek kaynak Excel dosyası](Freeze.xlsx).
{{< app/cells/assistant language="cpp" >}}
