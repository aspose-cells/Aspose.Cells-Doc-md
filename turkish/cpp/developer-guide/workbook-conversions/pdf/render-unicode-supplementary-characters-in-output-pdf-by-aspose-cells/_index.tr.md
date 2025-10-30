---
title: Aspose.Cells ile C++ kullanarak Unicode Yardımcı karakterlerini çıktı PDF sinde Göster
linktitle: Unicode Yardımcı Karakterleri Göster
type: docs
weight: 350
url: /tr/cpp/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/
description: Aspose.Cells for C++ kullanarak Unicode Yardımcı karakterlerini çıktı PDF sinde nasıl göstereceğinizi öğrenin.
---

{{% alert color="primary" %}}

Normal Unicode karakterleri 2 bayt uzunluğunda iken Unicode Ek Sayısal karakterleri 4 bayt uzunluğundadır. Aspose.Cells şimdi bu 4 bayt Unicode karakterlerin oluşturulmasını destekliyor.

Unicode Karakter Standartında, Ek Sayısal Karakterler U+10000'den U+10FFFF'e kadar olan kod noktalarına atanmış karakterlerdir. Diğer bir deyişle, bunlar U+FFFF'den büyük Unicode karakterlerdir.

- UTF-8'de bu karakterlerin her biri 4 bayt uzunluğundadır.
- UTF-16'da bu karakterler 2 takyeyi (16 bit birimler) gerektirir.

{{% /alert %}}

## Aspose.Cells ile çıktı PDF'de Unicode Ek Sayısal karakterlerin oluşturulması

Aşağıdaki ekran görüntüsü, Aspose.Cells'ın [kaynak excel dosyasını](5115563.xlsx) [çıktı PDF'ye](5115564.pdf) nasıl dönüştürdüğünü göstermektedir. Görebileceğiniz gibi, tüm üç Unicode Ek Sayısal karakter Microsoft Excel tarafından yapılan gibi tam olarak oluşturulmuştur.

![todo:image_alt_text](output.png)

## Örnek Kod

[Kaynak excel dosyasını](5115563.xlsx) [çıktı PDF'ye](5115564.pdf) dönüştürmek için bu örnek kodu kullanabilirsiniz.

```c++
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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"unicode-supplementary-characters.xlsx";

    // Path of output PDF file
    U16String outputFilePath = outDir + u"RenderUnicodeInOutput_out.pdf";

    // Load the source excel file containing Unicode Supplementary characters
    Workbook wb(inputFilePath);

    // Save the workbook as PDF
    wb.Save(outputFilePath, SaveFormat::Pdf);

    std::cout << "Workbook saved successfully with Unicode Supplementary characters!" << std::endl;

    Aspose::Cells::Cleanup();

    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
