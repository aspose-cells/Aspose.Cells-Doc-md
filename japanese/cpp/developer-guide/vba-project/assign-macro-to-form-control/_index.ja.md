---
title: C++でフォームコントロールにマクロを割り当てる
linktitle: フォームコントロールにマクロを割り当てる
type: docs
weight: 60
url: /ja/cpp/assign-macro-to-form-control/
description: Aspose.Cells for C++を使用して、ボタンなどのフォームコントロールにマクロコードを割り当てる方法を学びます。
---

{{% alert color="primary" %}}

Aspose.Cellsを使用して、ボタンなどのフォームコントロールにマクロコードを割り当てることができます。Workbook内のフォームコントロールに新しいマクロコードを割り当てるには、[**Shape.GetMacroName()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getmacroname/)プロパティを使用してください。

{{% /alert %}}

 以下のサンプルコードは、新しいワークブックを作成し、フォームボタンにマクロコードを割り当て、その出力をXLSM形式で保存します。Microsoft Excelで出力されたXLSMファイルを開くと、次のマクロコードが見えます。

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## **C++でフォームコントロールにマクロを割り当てる**

新しいXLSM ファイルとマクロコードを生成するサンプルコードを以下に示します。

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;
using namespace Aspose::Cells::Vba;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    int moduleIdx = workbook.GetVbaProject().GetModules().Add(sheet);
    VbaModule module = workbook.GetVbaProject().GetModules().Get(moduleIdx);
    module.SetCodes(
        u"Sub ShowMessage()\r\n"
        u"    MsgBox \"Welcome to Aspose!\"\r\n"
        u"End Sub"
    );

    Button button = sheet.GetShapes().AddButton(2, 0, 2, 0, 28, 80);
    button.SetPlacement(PlacementType::FreeFloating);
    button.GetFont().SetName(u"Tahoma");
    button.GetFont().SetIsBold(true);
    button.GetFont().SetColor(Color::Blue());
    button.SetText(u"Aspose");

    button.SetMacroName(sheet.GetName() + u".ShowMessage");

    U16String outputPath = outDir + u"Output.out.xlsm";
    workbook.Save(outputPath);

    std::cout << "VBA button added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
