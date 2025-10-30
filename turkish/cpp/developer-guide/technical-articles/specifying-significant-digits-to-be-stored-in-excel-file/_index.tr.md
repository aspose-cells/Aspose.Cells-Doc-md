---
title: C++ ile Excel Dosyasına Kaydedilecek Önemli Haneler Sayısını Belirtme
linktitle: Önemli Basamakların Belirtilmesi
type: docs
weight: 30
url: /tr/cpp/specifying-significant-digits-to-be-stored-in-excel-file/
description: Aspose.Cells ile C++ kullanarak Excel dosyalarına kaydedilecek önemli basamakları nasıl belirleyeceğinizi öğrenin.
---

## **Olası Kullanım Senaryoları**

Varsayılan olarak, Aspose.Cells, double değerlerin 17 önemli basamağını Excel dosyasında saklar; MS-Excel ise yalnızca 15 önem taşıyan basamağı saklar. Aspose.Cells'in varsayılan davranışını 17 yerine 15 önemli basamağa değiştirebilirsiniz, [**GetSignificantDigits()**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/getsignificantdigits/) özelliğini kullanarak.

## **Excel dosyasında saklanacak anlamlı basamakları belirtme**

Aşağıdaki örnek kod, Double değerleri Excel dosyasına kaydederken Aspose.Cells'in 15 önemli basamağı kullanmasını sağlar. Lütfen [çıktı Excel dosyasını](22774105.xlsx) inceleyin. Uzantısını .zip yapıp açarsanız, sadece 15 önemli basamağının saklandığını göreceksiniz. Aşağıdaki ekran görüntüsü, [**GetSignificantDigits()**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/getsignificantdigits/) özelliğinin çıktı Excel dosyasına etkisini gösterir.

![todo:image_alt_text](specifying-significant-digits-to-be-stored-in-excel-file_1.png)

## **Örnek Kod**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // By default, Aspose.Cells stores 17 significant digits unlike
    // MS-Excel which stores only 15 significant digits
    CellsHelper::SetSignificantDigits(15);

    // Create workbook
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access cell A1
    Cell c = worksheet.GetCells().Get(u"A1");

    // Put double value, only 15 significant digits as specified by
    // CellsHelper.SignificantDigits above will be stored in excel file just like MS-Excel does
    c.PutValue(1234567890.123451711);

    // Save the workbook
    workbook.Save(outDir + u"out_SignificantDigits.xlsx");

    std::cout << "Workbook saved successfully with significant digits set to 15!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
