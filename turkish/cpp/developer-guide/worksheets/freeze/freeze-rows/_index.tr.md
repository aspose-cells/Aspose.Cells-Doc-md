---
title: C++ ile Excel Çalışma Sayfasının Üst Satır(lar)ını Dondurun
linktitle: Satırları Sabitle
type: docs
weight: 190
url: /tr/cpp/how-to-freeze-rows-of-excel-worksheet
description: Bu makalede, Aspose.Cells API kullanarak C++ Kütüphanesi ile Excel Çalışma Sayfalarının üst satırlarını programlı olarak nasıl donduracağınızı öğreneceksiniz.
keywords: Üst satırları dondurun, Üst satırı dondurun.
---

## **Giriş**

Bu makalede, üst satırları nasıl donduracağınızı öğreneceğiz. Bir başlık altında büyük miktarda veri olduğunda, çalışma sayfasını aşağı kaydırdığınızda başlığı göremezsiniz. Üst satır(lar)ı dondurabilirsiniz ve böylece kaydırma işlemine devam ederken bile bu donmuş kısmı görebilirsiniz. Üst satırlardaki başlıkları kolayca görebilirsiniz.

## **Excel'de Satırları Dondur**

![Excel'de üst satır(ları) dondur](Freeze-Rows.png)

1. Üst satır(lar)ı dondurmak istiyorsanız, önce dondurulması gereken satırın altındaki satırı seçin.
2. Görünüm > Panoları Dondur'a tıklayın.
3. Açılır menüden Üst Satırı Dondur'a tıklayın.
4. Aşağı kaydırırsanız, ilk satır her zaman üst görünümde kalır.

**![Dondurulmuş satır](Frozen-Row.png)**

Gördüğünüz gibi, ilk satır dondurulmuştur ve aşağı kaydırırken ilk satır her zaman görünümün en üstünde kalır.

Satırları Dondurun, büyük verilerinize satır etiketi kaybetmeden bakmanızı sağlar.

## **Aspose.Cells for C++ ile Satırları Dondurun**
Satır(lar)ı Aspose.Cells for C++ ile dondurmak çok basittir. 
Lütfen seçilen satırda satır(lar)ı dondurmak için [**Worksheet.FreezePanes**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/) metodunu kullanın.
1. Bir çalışma kitabı oluşturun ya da dosyayı açmak veya boş bir dosya oluşturmak.
2. Worksheet.FreezePanes() yöntemiyle ilk satırı dondurun.
3. Dosyayı kaydedin.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook
    Workbook workbook(u"Freeze.xlsx");

    // Freezing panes at the cell B2
    workbook.GetWorksheets().Get(0).FreezePanes(u"A2", 1, 0);

    // Saving the file
    workbook.Save(u"frozen.xlsx");

    std::cout << "Panes frozen successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Ekli [örnek kaynak Excel dosyası](../Freeze.xlsx).
