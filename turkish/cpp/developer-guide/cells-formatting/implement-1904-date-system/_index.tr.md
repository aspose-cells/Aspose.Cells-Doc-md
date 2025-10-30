---
title: C++ ile 1904 Tarih Sistemini Uygula
linktitle: 1904 Tarih Sistemi Uygulama
description: Aspose.Cells, elektronik tablo dosyalarıyla çalışma konusunda C++ için bir kütüphanedir. 1904 tarih sisteminin uygulanmasını destekler, kullanıcıların 1 Ocak 1904 tarihine göre hesaplama ve biçimlendirme yapmasına olanak tanır. Bu makale, Aspose.Cells kütüphanesi ile 1904 tarih sistemini nasıl uygularsınız anlatmaktadır.
keywords: Aspose.Cells, 1904 tarih sistemi, elektronik tablo, hesaplama, biçimlendirme
type: docs
weight: 7000
url: /tr/cpp/implement-1904-date-system/
---

{{% alert color="primary" %}}

Microsoft Excel, 1900 tarih sistemi (Windows için Excel'de varsayılan olarak uygulanan tarih sistemi) ve 1904 tarih sistemi olmak üzere iki tarih sistemi destekler. 1904 tarih sistemi, genellikle Macintosh Excel dosyalarıyla uyumluluk sağlamak için kullanılır ve Excel'i Macintosh için kullanıyorsanız varsayılan sistemdir. Aspose.Cells kullanarak Excel dosyaları için 1904 tarih sistemini ayarlayabilirsiniz.

{{% /alert %}}

Microsoft Excel'de (örneğin Microsoft Excel 2003) 1904 tarih sistemini uygulamak için:

1. **Araçlar** menüsünden **Seçenekler**'i seçin ve **Hesaplama** sekmesini seçin.
1. **1904 tarih sistemi** seçeneğini belirleyin.
1. **Tamam**'a tıklayın.

|**Microsoft Excel'de 1904 tarih sistemini seçme**|
| :- |
|![todo:image_alt_text](implement-1904-date-system_1.png)|
Bunu, Aspose.Cells API'lerini kullanarak nasıl başarılır gösteren örnek kodu görün.

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
    U16String inputFilePath = srcDir + u"book1.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"Mybook.out.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Implement 1904 date system
    WorkbookSettings settings = workbook.GetSettings();
    settings.SetDate1904(true);

    // Save the excel file
    workbook.Save(outputFilePath);

    std::cout << "Excel file saved successfully with 1904 date system!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
