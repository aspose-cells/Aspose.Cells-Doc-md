---
title: C++ ile Timeline Ekle
linktitle: Zaman çizelgeleri
type: docs
weight: 170
url: /tr/cpp/create-timeline/
description: Aspose.Cells kullanarak C++ ile bir zaman çizelgesi nasıl oluşturulur öğrenin.
---

## **Olası Kullanım Senaryoları**

Tarihleri göstermek için filtreleri ayarlamak yerine, PivotTable Zaman Çizelgesi — tarih/zaman ile kolayca filtre yapmanızı ve kaydırıcı kontrolü ile istediğiniz döneme yakınlaşmanızı sağlayan dinamik filtre seçeneğini kullanabilirsiniz. Microsoft Excel, bir pivot tabloyu seçip ardından *Ekle > Zaman Çizelgesi* tıklayarak bir zaman çizelgesi oluşturmanıza izin verir. Aspose.Cells ayrıca [**Worksheet.Timelines.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells.timelines/timelinecollection/add/) yöntemi kullanılarak zaman çizelgesi oluşturmanıza da olanak tanır.

## **Bir Pivot Tablosuna Zaman Çizelgesi Oluştur**

Aşağıdaki örnek kodu inceleyin. İçinde Pivot tablosu bulunan [örnek Excel dosyasını](input.xlsx) yükler. Ardından, ilk temel Pivot alanına dayalı olarak zaman çizelgesi oluşturur. Son olarak, çalışma kitabını [çıktı XLSX](output.xlsx) biçiminde kaydeder. Aşağıdaki ekran resmi, Aspose.Cells tarafından oluşturulan zaman çizelgesini çıktı Excel dosyasında göstermektedir.

![todo:image_alt_text](create-timeline-to-a-pivot-table_1.png)

### **Örnek Kod**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load sample Excel file containing pivot table
    U16String inputFilePath = u"input.xlsx";
    Workbook wb(inputFilePath);

    // Access second worksheet (index 1)
    Worksheet sheet = wb.GetWorksheets().Get(1);

    // Access first pivot table inside the worksheet
    PivotTable pivot = sheet.GetPivotTables().Get(0);

    // Add timeline relating to pivot table
    int index = sheet.GetTimelines().Add(pivot, 15, 1, u"Ship Date");

    // Access the newly added timeline from timeline collection
    Timeline timeline = sheet.GetTimelines().Get(index);

    // Save the modified workbook
    U16String outputFilePath = u"output.xlsx";
    wb.Save(outputFilePath);

    std::cout << "Timeline added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
