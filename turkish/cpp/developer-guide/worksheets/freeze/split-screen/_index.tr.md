---
title: Excel Çalışma Sayfasını C++ ile Bölmeli Ekran
linktitle: Bölünmüş Ekran
type: docs
weight: 190
url: /tr/cpp/how-to-split-screen-of-excel-worksheet
description: Bu makalede, çalışma sayfasını iki veya dört parçaya bölerek belirli satır ve/veya sütunları ayrı bölmelerde görüntülemenin C++ kullanılarak programatik olarak nasıl yapılacağı gösterilecektir.
keywords: Üst satırları dondurun, Üst satırı dondurun.
---

## **Giriş**

Bu makalede, çalışma sayfasını iki veya dört parçaya bölerek belirli satır ve/veya sütunları ayrı bölmelerde görüntülemenin C++ kullanılarak programatik olarak nasıl yapılacağı anlatılacaktır. Büyük veri setleriyle çalışırken, aynı çalışma sayfasındaki birkaç alanı aynı anda görmemiz gerekebilir, böylece farklı alt kümeleri karşılaştırabiliriz. Bölme ekran fonksiyonu ihtiyacınızı karşılayabilir.

## **Excel'de ekranı nasıl bölebilirsiniz**
Bir elektronik tabloyu ikiye veya dörde bölmek için aşağıdakileri yapın:

1. Bölme yapmak istediğiniz satır/sütun/hücreyi seçin.
2. Görünüm sekmesinde, Pencereler grubunda, Böl düğmesini tıklayın.

**![Bölünmüş Ekran](Bölünmüş-Ekran.png)**

## **Excel'de sütunlara dik olarak elektronik tabloyu bölmek**

Elektronik tablonun farklı alanlarını dikey olarak ayırmak için, bölmenin görünmesini istediğiniz sütunun sağındaki sütunu seçin ve Excel'de Böl düğmesini tıklayın.

Aspose.Cells for C++ ile çalışma sayfasını dikey olarak sütunlar üzerinde bölmek oldukça kolaydır, yalnızca en üst satırda aktif hücre olarak bir hücre seçmemiz yeterlidir, ardından
[**Worksheet.Split**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/split/) yöntemi ile bölmek.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook.
    Workbook workbook(u"Book1.xlsx");

    // Get the first worksheet in the workbook.
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Sets C1 cell in the top row as the active cell.
    sheet.SetActiveCell(u"C1");

    // Split worksheet vertically on columns.
    sheet.Split();

    std::cout << "Worksheet processed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Satırlara yatay olarak elektronik tabloyu bölmek**
Excel'de pencerenizi yatay olarak ayırmak için, bölmeyi istediğiniz satırın altındaki satırı seçin.

Aspose.Cells for C++ ile çalışma sayfasını yatay olarak satırlar üzerinde bölmek oldukça kolaydır, yalnızca sol sütunda bir hücreyi aktif hücre olarak seçmemiz yeterlidir, sonra
[**Worksheet.Split**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/split/) yöntemi ile bölmek.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook and load an existing Excel file.
    Workbook workbook(u"Book1.xlsx");

    // Access the first worksheet in the workbook.
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Set the A6 cell in the left column as the active cell.
    sheet.SetActiveCell(u"A6");

    // Split the worksheet horizontally on rows.
    sheet.Split();

    // Save the modified workbook to a new file.
    workbook.Save(u"dest.xlsx");

    std::cout << "Workbook processed and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Elektronik tabloyu dört bölüme ayırmak**
Aynı elektronik tablonun dört farklı bölümünü aynı anda görüntülemek için, Excel'de ekranınızı hem dikey hem yatay olarak bölebilirsiniz.

Aspose.Cells for C++ ile çalışma sayfasını dikey olarak sütunlar üzerinde bölmek oldukça kolaydır, yalnızca ilk satır ve sütun dışında bir hücreyi aktif hücre olarak seçmemiz yeterlidir, sonra
[**Worksheet.Split**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/split/) yöntemi ile bölmek.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook.
    Workbook workbook(u"Book1.xlsx");

    // Get the first worksheet.
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Set E6 cell as the active cell.
    sheet.SetActiveCell(u"E6");

    // Split worksheet into four parts.
    sheet.Split();

    Aspose::Cells::Cleanup();
}
```

## **Bölünmüş bölgeyi kaldırmak için**
Elektronik tabloyu bölme ayarını kaldırmak için, sadece Böl düğmesini tekrar tıklayın.

Aspose.Cells for C++, bölme ayarını kaldırmak için [**Worksheet.RemoveSplit**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/removesplit/) yöntemini sağlar.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook
    Workbook workbook(u"Book1.xlsx");

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Remove split
    sheet.RemoveSplit();

    // Split worksheet into four parts
    sheet.Split();

    std::cout << "Worksheet split successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
