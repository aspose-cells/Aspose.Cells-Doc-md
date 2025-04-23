---
title: C++でActiveXコントロールを削除します。
linktitle: ActiveXコントロールを削除
type: docs
weight: 1000
url: /ja/cpp/remove-activex-control/
description: Aspose.Cells for C++を使用してワークブックからActiveXコントロールを削除する方法を学ぶ。
---

## **ActiveXコントロールを削除**

Aspose.Cellsは、ワークブックからActiveXコントロールを削除する機能を提供します。これにはAPIが [**Shape.RemoveActiveXControl**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/removeactivexcontrol/) メソッドを提供します。次のコードスニペットは、ActiveXコントロールを削除するために [**Shape.RemoveActiveXControl**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/removeactivexcontrol/) メソッドの使用例を示しています。

## **サンプルコード**

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
