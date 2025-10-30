---
title: Excel den HTML ye Dönüştürme  Daha İyi Düzen İçin PresentationPreference Seçeneğini Kullanma C++ ile
linktitle: Excel den HTML ye  Daha İyi Düzen İçin Presentasyon Tercihi Seçeneğini Kullanın
type: docs
weight: 220
url: /tr/cpp/excel-to-html-use-presentationpreference-option-for-better-layout/
description: C++ kullanarak Excel dosyalarını HTML ye kaydederken daha iyi düzenler nasıl render edilirse öğrenin.
---

{{% alert color="primary" %}} 

Aspose.Cells, bir Microsoft Excel dosyasını HTML veya MHT formatına kaydederken daha iyi düzen elde etmek isteyen geliştiriciler için kullanışlı bir HtmlSaveOptions.PresentationPreference özelliği sağlar. Özelliğin varsayılan değeri false'dur. Excel raporlarının daha çekici bir sunumunu almak için bu özelliği true olarak ayarlamanızı öneririz.

{{% /alert %}} 

Lütfen aşağıdaki örnek kodu inceleyin, bu kod Excel raporundan HTML dosyasını nasıl presentasyon tercihi ile oluşturduğunu gösterir.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
#include "Aspose.Cells/HtmlSaveOptions.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"sample.xlsx";

    // Instantiate the Workbook and load an Excel file
    Workbook workbook(inputFilePath);

    // Create HtmlSaveOptions object
    HtmlSaveOptions options;

    // Set the Presentation preference option
    options.SetPresentationPreference(true);

    // Save the Excel file to HTML with specified option
    U16String outputFilePath = srcDir + u"outPresentationlayout1.out.html";
    workbook.Save(outputFilePath, options);

    std::cout << "Excel file saved as HTML successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{< app/cells/assistant language="cpp" >}}
