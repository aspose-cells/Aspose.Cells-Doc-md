---
title: إزالة عنصر تحكم ActiveX باستخدام ++C
linktitle: إزالة عنصر تحكم ActiveX
type: docs
weight: 1000
url: /ar/cpp/remove-activex-control/
description: تعلم كيف تزيل عنصر تحكم ActiveX من دفاتر العمل باستخدام Aspose.Cells for C++.
---

## **إزالة عنصر تحكم ActiveX**

توفر Aspose.Cells القدرة على إزالة عنصر تحكم ActiveX من دفاتر العمل. لهذا، يوفر API الطريقة [**Shape.RemoveActiveXControl**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/removeactivexcontrol/). يوضح مقتطف التعليمات البرمجية التالي استخدام طريقة [**Shape.RemoveActiveXControl**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/removeactivexcontrol/) لإزالة عنصر تحكم ActiveX.

## **الكود المثالي**

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
