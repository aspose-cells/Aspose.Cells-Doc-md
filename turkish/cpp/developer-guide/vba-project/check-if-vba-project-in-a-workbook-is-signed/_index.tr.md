---
title: Bir Çalışma Kitabındaki VBA projesinin İmzalanıp İmzalanmadığını C++ kullanarak kontrol edin.
linktitle: Bir Çalışmada VBA Projesinin İmzalı Olup Olmadığını Kontrol Edin
type: docs
weight: 70
url: /tr/cpp/check-if-vba-project-in-a-workbook-is-signed/
description: Aspose.Cells kullanarak, bir çalışma kitabındaki VBA projesinin imzalanıp imzalanmadığını kontrol edin.
---

{{% alert color="primary" %}}

 Microsoft Excel kullanarak, VBA projenizin imzalanıp imzalanmadığını **Araçlar > Dijital İmzalar...** menüsü aracılığıyla kontrol edebilirsiniz. Benzer şekilde, Aspose.Cells [**Workbook.VbaProject.IsSigned**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/issigned) kullanılarak programatik olarak da kontrol edebilirsiniz.

{{% /alert %}}

## ** C++ ile Bir Çalışma Kitabındaki VBA Projesinin İmzalanıp İmzalanmadığını Kontrol Edin**

 Aşağıdaki kod çalışma kitabını yükler ve VBA projesinin imzalanıp imzalanmadığını [**Workbook.VbaProject.IsSigned**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/issigned) özelliği kullanarak kontrol eder. Proje imzalanmışsa **true**, değilse **false** döner.

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

    // Path of input excel file
    U16String sampleFilePath = srcDir + u"Sample1.xlsx";

    // Create workbook
    Workbook workbook(sampleFilePath);

    // Check if the VBA project is signed
    bool isSigned = workbook.GetVbaProject().IsSigned();
    std::wcout << u"VBA Project is Signed: " << (isSigned ? u"true" : u"false") << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
