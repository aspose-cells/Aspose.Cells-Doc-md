---
title: Обновить элемент ActiveX ComboBox с помощью C++
linktitle: Обновить элемент управления ActiveX ComboBox
type: docs
weight: 170
url: /ru/cpp/update-activex-combobox-control/
description: Узнайте, как считывать или записывать значения элемента ActiveX ComboBox с помощью Aspose.Cells и C++.
---

## **Возможные сценарии использования**
Вы можете читать или записывать значения контроллера ActiveX ComboBox с помощью Aspose.Cells. Пожалуйста, получите доступ к ActiveX-контролю через свойство [Shape.ActiveXControl](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.activexcontrols/activexcontrol/) и проверьте его тип с помощью свойства [ActiveXControl.GetType()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.activexcontrols/activexcontrolbase/gettype/). Оно должно возвращать значение [ControlType.ComboBox](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.activexcontrols/controltype/), затем приведите его к объекту [ComboBoxActiveXControl](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.activexcontrols/comboboxactivexcontrol/), чтобы читать или изменять его свойства.

Пожалуйста, загрузите [образец файла Excel](5115124.xlsx), используемый в следующем примере кода.

## **Обновление элемента управления ComboBox ActiveX**
На следующем скриншоте показан эффект примера кода на [образец файла Excel](5115124.xlsx). Как видно, значение элемента управления ActiveX ComboBox было обновлено на "This is combo box control".

|![todo:image_alt_text](update-activex-combobox-control_1.png)|
| :- |

## **Образец кода**
Следующий образец кода обновляет значение элемента управления ActiveX ComboBox, находящегося внутри [образца файла Excel](5115124.xlsx).

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;
using namespace Aspose::Cells::Drawing::ActiveXControls;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook wb(srcDir + u"SourceFile.xlsx");

    Shape shape = wb.GetWorksheets().Get(0).GetShapes().Get(0);

    ActiveXControl c = shape.GetActiveXControl();

    if (c.GetType() == ControlType::ComboBox)
    {
        ComboBoxActiveXControl comboBoxActiveX = static_cast<ComboBoxActiveXControl>(c);
        comboBoxActiveX.SetValue(u"This is combo box control with updated value.");
    }

    wb.Save(outDir + u"OutputFile_out.xlsx");

    std::cout << "Workbook saved successfully with updated ComboBox value!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
