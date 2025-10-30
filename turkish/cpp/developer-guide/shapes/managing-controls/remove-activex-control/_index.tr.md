---
title: C++ kullanarak ActiveX Kontrolünü Kaldırma
linktitle: AktifX Kontrolü Kaldır
type: docs
weight: 1000
url: /tr/cpp/remove-activex-control/
description: Aspose.Cells for C++ kullanarak dosyalardan ActiveX Kontrolü nasıl kaldırılacağını öğrenin.
---

## **ActiveX Kontrolü Kaldırma**

Aspose.Cells, dosyalardan ActiveX Kontrolü kaldırma yeteneği sağlar. Bunun için API [**Shape.RemoveActiveXControl**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/removeactivexcontrol/) yöntemini sunar. Aşağıdaki kod parçası, [**Shape.RemoveActiveXControl**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/removeactivexcontrol/) yöntemini kullanarak ActiveX Kontrolü kaldırmayı gösterir.

## **Örnek Kod**

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

    // Create a workbook
    Workbook wb(srcDir + u"sampleUpdateActiveXComboBoxControl.xlsx");

    // Access first shape from first worksheet
    Shape shape = wb.GetWorksheets().Get(0).GetShapes().Get(0);

    // Remove Shape ActiveX Control
    shape.RemoveActiveXControl();

    // Save the workbook
    wb.Save(outDir + u"RemoveActiveXControl_out.xlsx");

    std::cout << "ActiveX Control removed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
