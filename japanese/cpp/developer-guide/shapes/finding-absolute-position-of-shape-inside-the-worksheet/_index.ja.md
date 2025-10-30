---
title: シート内の図形の絶対位置をC++で見つける
linktitle: ワークシート内の形状の絶対位置を検索
type: docs
weight: 8000
url: /ja/cpp/finding-absolute-position-of-shape-inside-the-worksheet/
description: Aspose.Cellsを使って、シート内の図形の絶対位置を特定します。
---

{{% alert color="primary" %}}

時々、ワークシート内の形状の絶対位置を知る必要があります。Aspose.Cellsはこの目的のために[**Shape.GetLeftToCorner()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getlefttocorner/)および[**Shape.GetTopToCorner()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettoptocorner/)プロパティを提供しています。これらのプロパティは、ワークシート内の形状の絶対位置をピクセル単位で返します。

{{% /alert %}}

次のサンプルコードは、ワークシート内の最初の形状の絶対位置をピクセル単位で表示します。サンプルコードは、次のコンソール出力を表示します:

{{< highlight java >}}

Absolute Position of this Shape is (320 , 183)

{{< /highlight >}}

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

    // Load the sample Excel file inside the workbook object
    Workbook workbook(srcDir + u"sample.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the first shape inside the worksheet
    Shape shape = worksheet.GetShapes().Get(0);

    // Displays the absolute position of the shape
    std::wcout << L"Absolute Position of this Shape is (" << shape.GetLeftToCorner() << L" , " << shape.GetTopToCorner() << L")" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
