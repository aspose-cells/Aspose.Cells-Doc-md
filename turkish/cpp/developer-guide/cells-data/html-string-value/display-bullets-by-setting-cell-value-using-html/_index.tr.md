---
title: HTML kullanarak Hücre Değeri ayarlayarak Madde İşaretleri Gösterimi ile C++
linktitle: HTML kullanarak Hücre Değeri Ayarıyla Madde İmleri Göster
type: docs
weight: 130
url: /tr/cpp/display-bullets-by-setting-cell-value-using/
description: HTML ve kullanıcı dostu Aspose.Cells for C++ API kullanarak Excel Hücrelerine madde işaretleri ekleyin.
keywords: Excel e madde işaretleri ekle, Excel e madde işaretleri ekle c++, Excel de madde işaretleri göster, Excel de madde işaretleri göster c++, HTML ile Excel e madde işaretleri ekle, HTML ile Excel e madde işaretleri ekle c++, HTML ile Excel de madde işaretleri göster, HTML ile Excel de madde işaretleri göster c++, HTML kullanarak Excel de madde işaretleri göster, HTML kullanarak Excel de madde işaretleri ekle
---

{{% alert color="primary" %}}

Aspose.Cells, HTML kodu ile işaretli listeleri göstermeyi destekler. Bu makale, hücre değerini HTML kullanarak işaretli listeleri görüntülemeyi açıklayacaktır. Hücre değerini HTML ile ayarlamak için [**Cell.GetHtmlString()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gethtmlstring/) özelliğini kullanacağız.

{{% /alert %}}

## HTML kullanarak Hücre değeri ayarlayarak Madde İşaretleri gösterimi ile C++

Aşağıdaki kod, hücre değerini ayarlamak için HTML kodunu kullanır. Bu kodu çalıştırdığınızda, aşağıdaki resimde gösterildiği gibi çıktı alırsınız.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C
    // Create workbook object
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access cell A1
    Cell cell = worksheet.GetCells().Get("A1");

    // Set the HTML string
    cell.SetHtmlString(u"<font style='font-family:Arial;font-size:10pt;color:#666666;vertical-align:top;text-align:left;'>Text 1 </font>"
                       u"<font style='font-family:Wingdings;font-size:8.0pt;color:#009DD9;mso-font-charset:2;'>l</font>"
                       u"<font style='font-family:Arial;font-size:10pt;color:#666666;vertical-align:top;text-align:left;'> Text 2 </font>"
                       u"<font style='font-family:Wingdings;font-size:8.0pt;color:#009DD9;mso-font-charset:2;'>l</font>"
                       u"<font style='font-family:Arial;font-size:10pt;color:#666666;vertical-align:top;text-align:left;'> Text 3 </font>"
                       u"<font style='font-family:Wingdings;font-size:8.0pt;color:#009DD9;mso-font-charset:2;'>l</font>"
                       u"<font style='font-family:Arial;font-size:10pt;color:#666666;vertical-align:top;text-align:left;'> Text 4 </font>");

    // Auto fit the Columns
    worksheet.AutoFitColumns();

    // Save the workbook
    U16String outputFilePath = u"BulletsInCells_out.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Örneğin ürettiği çıktı

Yukarıdaki örnek kodun çıktısını aşağıdaki ekran görüntüsünde görebilirsiniz.

![todo:image_alt_text](display-bullets-by-setting-cell-value-using-html_1.png)
{{< app/cells/assistant language="cpp" >}}
