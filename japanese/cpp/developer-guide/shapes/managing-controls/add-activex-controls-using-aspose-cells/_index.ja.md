---
title: Aspose.Cells for C++を使用してActiveXコントロールを追加します。
linktitle: ActiveXコントロールを追加
type: docs
weight: 260
url: /ja/cpp/add-activex-controls-using-aspose-cells/
description: Aspose.Cells for C++を使ってExcelシートにプログラムでActiveXコントロールを追加する方法を学びます。
---

{{% alert color="primary" %}}

Aspose.Cellsの[**ShapeCollection::AddActiveXControl()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addactivexcontrol/)メソッドを使ってActiveXコントロールを追加できます。このメソッドはパラメータ[**ControlType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.activexcontrols/controltype/)を受け取り、シート内に追加するActiveXコントロールの種類を指定します。以下の値があります：

- ControlType::CheckBox
- ControlType::ComboBox
- ControlType::CommandButton
- ControlType::Image
- ControlType::Label
- ControlType::ListBox
- ControlType::RadioButton
- ControlType::ScrollBar
- ControlType::SpinButton
- ControlType::TextBox
- ControlType::ToggleButton
- ControlType::Unknown

ActiveXコントロールをシェイプコレクションに追加したら、[**Shape::get_ActiveXControl()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getactivexcontrol/)メソッドを通じてActiveXコントロールオブジェクトにアクセスし、さまざまなプロパティを設定できます。

{{% /alert %}}

以下のサンプルコードはAspose.Cells for C++を使ってトグルボタンActiveXコントロールを追加します。

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;
using namespace Aspose::Cells::Drawing::ActiveXControls;

int main() {
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook object
    Workbook wb;

    // Access first worksheet
    Worksheet sheet = wb.GetWorksheets().Get(0);

    // Add Toggle Button ActiveX Control inside the Shape Collection
    Shape s = sheet.GetShapes().AddActiveXControl(ControlType::ToggleButton, 4, 0, 4, 0, 100, 30);

    // Access the ActiveX control object and set its linked cell property
    ActiveXControl c = s.GetActiveXControl();
    c.SetLinkedCell(u"A1");

    // Save the workbook in xlsx format
    wb.Save(outDir + u"AddActiveXControls_out.xlsx", SaveFormat::Xlsx);

    std::cout << "ActiveX control added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
