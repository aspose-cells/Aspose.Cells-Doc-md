---
title: C++ ile Çerçeve Çalışması ve Belge Özelliklerini Devre Dışı Bırakın
type: docs
weight: 310
url: /tr/cpp/disable-exporting-frame-scripts-and-document-properties/
description: Aspose.Cells kullanarak C++ ile çerçeve çalışması ve belge özelliklerini devre dışı bırakma.
---

{{% alert color="primary" %}}

Aspose.Cells, çalışma kitabını HTML'ye dönüştürürken çerçeve çalışması ve belge özelliklerini dışa aktarır. Aspose.Cells for C++ sürümünün 8.6.0, çerçeve çalışması ve belge özelliklerini isteğe bağlı olarak devre dışı bırakma seçeneği sunar. Lütfen çeviriyi devre dışı bırakmak için HtmlSaveOptions.ExportFrameScriptsAndProperties özelliğini kullanın.

{{% /alert %}}

## **Çerçeve betikleri ve belge özelliklerinin dışa aktarılmasını devre dışı bırak**

Aşağıdaki örnek kod, çerçeve betikleri ve belge özelliklerinin dışa aktarılmasını devre dışı bırakmanıza olanak tanır. Bir çalışma kitabını HTML'e dönüştürdüğünüzde, çıktı dosyası herhangi bir çerçeve betiği ve belge özelliği içermez.

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

    // Open the required workbook to convert
    U16String inputFilePath = srcDir + u"Sample1.xlsx";
    Workbook workbook(inputFilePath);

    // Disable exporting frame scripts and document properties
    HtmlSaveOptions options;
    options.SetExportFrameScriptsAndProperties(false);

    // Save workbook as HTML
    workbook.Save(outDir + u"output.out.html", options);

    std::cout << "Workbook saved successfully as HTML!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
