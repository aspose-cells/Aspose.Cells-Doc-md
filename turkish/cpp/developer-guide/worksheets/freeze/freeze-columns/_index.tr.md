---
title: C++ ile Excel Çalışma Sayfasının İlk Sütun(ları)nı Dondurun
linktitle: Sütunları Sabitle
type: docs
weight: 190
url: /tr/cpp/how-to-freeze-columns-of-excel-worksheet
description: Bu makalede, Aspose.Cells API ile C++ Kütüphanesini kullanarak Excel Çalışma Sayfalarının sol sütunlarını programlı olarak nasıl donduracağınızı öğreneceksiniz.
keywords: Sol sütunları dondurun, ilk sütunları dondurun, sütunu(sütunları) kilitleyin
---

## **Giriş**

Bu makalede, sol sütunu(sütunları) nasıl donduracağınızı öğreneceğiz. Bir satırda büyük miktarda veri olduğunda, çalışma sayfasını yatayca kaydırdığınızda sol sütunları göremezsiniz. İlk sütunu(sütunları) dondurabilir ve kilitleyebilirsiniz, böylece veri kaydırılırken bile donmuş kısmı görebilirsiniz. Sol sütunlardaki başlıkları kolayca görebilirsiniz.

## **Excel'de Sütunları Sabitle**

**![Excel'de sol sütunları sabitle](freeze-columns.png)**

1. Sol sütunu(sütunları) dondurmak istiyorsanız, önce dondurulması gereken sütunun altındaki sütunu seçin.
2. Görünüm > Panoları Dondur'a tıklayın.
3. Açılır menüde, "İlk Sütunu Dondur"ye tıklayın.
4. Aşağı kaydırırsanız, ilk sütun her zaman sol görünümde kalır.

**![Dondurulmuş sütun](frozen-columns.png)**

Gördüğünüz gibi, ilk sütun dondurulmuştur, yatay kaydırırken ilk sütun her zaman görünümün üstünde kilitlidir.

Sütunları Dondurun, uzun verilerinize ilk sütunu izlemek zorunda kalmadan göz atmanızı sağlar.

## **Aspose.Cells for C++ ile Sütunları Dondurun**
Aspose.Cells for C++ ile ilk sütunu(sütunları) dondurmak çok kolaydır. 
Seçilen sütunu dondurmak için lütfen [**Worksheet.FreezePanes**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/) metodunu kullanın.
1. Dosyayı açmak veya boş bir dosya oluşturmak için Workbook'u oluşturun.
2. Worksheet.FreezePanes() yöntemiyle ilk sütunu dondurun.
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

    // Freezing panes at the second column
    workbook.GetWorksheets().Get(0).FreezePanes(u"B1", 0, 1);

    // Saving the file
    workbook.Save(u"frozen.xlsx");

    std::cout << "Panes frozen successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Ekli [örnek kaynak Excel dosyası](Freeze.xlsx).
{{< app/cells/assistant language="cpp" >}}
