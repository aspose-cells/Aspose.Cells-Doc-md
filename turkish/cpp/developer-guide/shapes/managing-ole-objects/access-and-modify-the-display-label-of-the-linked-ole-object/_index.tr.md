---
title: Bağlantılı Ole Nesnesinin Ekran Etiketini C++ ile Erişip Değiştirme
linktitle: Bağlantılı Ole Nesnesinin Görüntü Etiketini Erişme ve Değiştirme
type: docs
weight: 100
url: /tr/cpp/access-and-modify-the-display-label-of-the-linked-ole-object/
description: Bağlantılı Ole Nesnelerinin ekran etiketlerini Excel dosyalarında nasıl erişip değiştireceğinizi öğrenin Aspose.Cells for C++ kullanarak.
---

## **Olası Kullanım Senaryoları**

Microsoft Excel, aşağıdaki ekran görüntüsünde gösterildiği gibi Ole Nesnesinin ekran etiketini değiştirmeye izin verir. Ayrıca, Aspose.Cells API’leri kullanarak [**GetLabel()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getlabel/) ve [**SetLabel(const U16String\& value)**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/setlabel/) metodlarıyla Ole nesnesinin ekran etiketine erişebilir veya değiştirebilirsiniz.

![todo:image_alt_text](access-and-modify-the-display-label-of-the-linked-ole-object_1.png)

## **Bağlı Ole Nesnesinin Görüntü Etiketini Erişme ve Değiştirme**

Lütfen aşağıdaki örnek kodu inceleyin, Ole Nesnesini içeren [örnek Excel dosyasını](64716810.xlsx) yükler. Kod, Ole Nesnesine erişir ve etiketini Sample APIs'ten Aspose APIs olarak değiştirir. Referans için aşağıda verilen konsol çıktısına bakın, bu çıktı örneğin etkisini göstermektedir.

## **Örnek Kod**

```cpp
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Load the sample Excel file
    U16String inputFilePath = u"sampleAccessAndModifyLabelOfOleObject.xlsx";
    Workbook wb(inputFilePath);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first Ole Object
    OleObject oleObject = ws.GetOleObjects().Get(0);

    // Display the Label of the Ole Object
    std::cout << "Ole Object Label - Before: " << oleObject.GetLabel().ToUtf8() << std::endl;

    // Modify the Label of the Ole Object
    oleObject.SetLabel(u"Aspose APIs");

    // Save workbook to memory stream
    auto ms = wb.SaveToStream();

    // Set the workbook reference to null
    wb = Workbook();

    // Load workbook from memory stream
    wb = Workbook(ms);

    // Access first worksheet
    ws = wb.GetWorksheets().Get(0);

    // Access first Ole Object
    oleObject = ws.GetOleObjects().Get(0);

    // Display the Label of the Ole Object that has been modified earlier
    std::cout << "Ole Object Label - After: " << oleObject.GetLabel().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Konsol Çıktısı**

{{< highlight java >}}

Ole Object Label - Before: Sample APIs

Ole Object Label - After: Aspose APIs

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
