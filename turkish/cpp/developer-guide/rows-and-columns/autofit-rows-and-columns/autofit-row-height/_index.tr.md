---
title: C++ ile Otomatik Satır Yüksekliğini Ayarla, Dosya Yüklenirken
linktitle: Dosya Yüklenirken Otomatik Satır Yüksekliğini Ayarla
type: docs
weight: 120
url: /tr/cpp/autofit-row-height/
description: Aspose.Cells kullanarak, yüklenen dosyalarda satırların yüksekliğinin otomatik olarak uydurulmasını nasıl sağlayacağınızı öğrenin.
keywords: Dosya yüklenirken satır yüksekliğini otomatik olarak ayarlayarak Excel dosyası açıldığında otomatik olarak satır yüksekliğini ayarlar.
---

## **Olası Kullanım Senaryoları**
Satır yüksekliği, içeriğin fontu ile otomatik olarak eşleşir, ancak önbelleğe alınmış satırın yüksekliği dosyadaki içerikle eşleşmiyorsa, MS Excel dosyayı yüklerken satır yüksekliğini otomatik olarak ayarlar, ancak Aspose.Cells performansı artırmak için otomatik ayarlamaz. Dosyaları yüklerken Satır yüksekliğini otomatik ayarlamak için Aspose.Cells programını kullanmak istiyorsanız, hedefinizi [LoadOptions.GetOnlyAuto()](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/getonlyauto/) parametresiyle gerçekleştirebilirsiniz.

Lütfen aşağıdaki resim verilerine bakınız. 11. satırda önbellek satır yüksekliğinin 15 olduğunu gözlemleyebiliriz, ancak Excel dosyası yüklenirken satır yüksekliği otomatik olarak ayarlandı.
<br>
<img src="1.png" width=70% />

## **Aspose.Cells Kullanarak Satır Yüksekliğini Ayarlayın**
Dosyayı doğrudan yüklerseniz ve PDF olarak kaydederseniz, önbellek satır yüksekliği yalnızca 15 olduğu için veri PDF'de tamamen görüntülenmeyecektir.
<br>
<img src="2.png" width=70% />
<br>
Dosyayı yüklerken [LoadOptions.GetOnlyAuto()](https://reference.aspose.com/cells/cpp/aspose.cells/autofitteroptions/getonlyauto/) parametresini true yaparsanız, Aspose.Cells otomatik olarak satır yüksekliğini ayarlayacaktır. Ayarlanmış satır yüksekliği, metnin görüntüleme gereksinimlerini karşılamak için etkili olur.
<br>
<img src="3.png" width=70% />

## **C++ Örnek Kodu**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Define the file path
    U16String filePath(u"..\\Data\\01_SourceDirectory\\");

    // Open an existing Excel file and save it as PDF
    {
        Workbook wb(filePath + u"sample.xlsx");
        wb.Save(filePath + u"out.pdf");
    }

    // Set load options for the second workbook
    LoadOptions loadOptions;
    {
        AutoFitterOptions autoFitterOptions;
        autoFitterOptions.SetOnlyAuto(true);
        loadOptions.SetAutoFitterOptions(autoFitterOptions);
    }

    // Open the existing Excel file with load options and save it as PDF
    {
        Workbook book(filePath + u"sample.xlsx", loadOptions);
        book.Save(filePath + u"out2.pdf");
    }

    std::cout << "PDF files created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
