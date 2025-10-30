---
title: C++ ile Çalışma Sayfasının Bağlantılarını Düzenleme
linktitle: Çalışma Sayfasının Bağlantılarını Düzenleme
type: docs
weight: 330
url: /tr/cpp/editing-hyperlinks-of-worksheet/
description: Aspose.Cells for C++ API ile Çalışma Sayfası bağlantılarını nasıl düzenleyeceğinizi öğrenin.
keywords: Bağlantıları Düzenle, Çalışma Sayfası Bağlantılarını Düzenle, Hücre Bağlantısını Düzenle, Çalışma sayfasının tüm bağlantılarına eriş
---

{{% alert color="primary" %}}

Aspose.Cells, [**GetHyperlinks()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/gethyperlinks/) koleksiyonunu kullanarak çalışma sayfasının tüm bağlantılarına erişmenizi sağlar. Bu koleksiyondan her bir bağlantıya sırayla erişebilir ve özelliklerini düzenleyebilirsiniz.

{{% /alert %}}

Aşağıdaki örnek kod, çalışma sayfasındaki tüm bağlantılara erişir ve onların [**GetAddress()**](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlink/getaddress/) özelliğini Aspose web sitesine değiştirir.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook from input file
    Workbook workbook(srcDir + u"Sample.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Iterate through all hyperlinks in the worksheet
    for (int32_t i = 0; i < worksheet.GetHyperlinks().GetCount(); i++)
    {
        Hyperlink hl = worksheet.GetHyperlinks().Get(i);
        hl.SetAddress(u"http://www.aspose.com");
    }

    // Save the modified workbook to the output file
    workbook.Save(outDir + u"output_out.xlsx");

    std::cout << "Hyperlinks updated successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
