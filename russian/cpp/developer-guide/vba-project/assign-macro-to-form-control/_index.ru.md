---
title: Назначение макроса на элемент управления формы с помощью C++
linktitle: Назначить макрос на элемент управления формы
type: docs
weight: 60
url: /ru/cpp/assign-macro-to-form-control/
description: Узнайте, как назначить код макроса на элемент управления формы, такой как кнопка, используя Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells позволяет назначить код макроса элементу управления формы, такому как кнопка. Используйте свойство [**Shape.GetMacroName()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getmacroname/), чтобы назначить новый код макроса элементу управления формы внутри книги.

{{% /alert %}}

Следующий пример создает новую рабочую книгу, назначает код макроса на кнопку формы и сохраняет результат в формате XLSM. После открытия файла XLSM в Microsoft Excel вы увидите следующий код макроса.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## **Назначение макроса элементу управления формы с помощью C++**

Вот пример кода для создания вывода в формате XLSM с кодом макроса.

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
