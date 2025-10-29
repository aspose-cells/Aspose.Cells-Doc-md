---
title: تحديث عنصر تحكم ComboBox لـ ActiveX باستخدام ++C
linktitle: تحديث عنصر التحكم ActiveX ComboBox
type: docs
weight: 170
url: /ar/cpp/update-activex-combobox-control/
description: تعلم كيفية قراءة أو كتابة قيم عنصر تحكم ComboBox لـ ActiveX باستخدام Aspose.Cells مع ++C++.
---

## **سيناريوهات الاستخدام المحتملة**
يمكنك قراءة أو كتابة قيم عنصر تحكم ComboBox لـ ActiveX باستخدام Aspose.Cells. من فضلك، استعرض عنصر تحكم ActiveX عبر خاصية [Shape.ActiveXControl](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.activexcontrols/activexcontrol/) وتحقق من نوعه عبر خاصية [ActiveXControl.GetType()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.activexcontrols/activexcontrolbase/gettype/). يجب أن يُرجع قيمة [ControlType.ComboBox](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.activexcontrols/controltype/)، ثم قم بتحويل النوع إلى كائن [ComboBoxActiveXControl](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.activexcontrols/comboboxactivexcontrol/) لقراءة أو تعديل خصائصه المختلفة.

يرجىتنزيل[ملف الإكسل العيني](5115124.xlsx) المستخدمفيالكود العينيالتالي.

## **تحديث عنصر تحكم ActiveX ComboBox**
الصورة التي تلي تظهر تأثير كود العينة على [ملف الإكسل عينة](5115124.xlsx). كما يمكنك رؤية أن قيمة عنصر التحكم ComboBox في ActiveX تم تحديثها إلى "هذا عنصر التحكم في مربع القائمة"

|![todo:image_alt_text](update-activex-combobox-control_1.png)|
| :- |

## **الكود المثالي**
تحديث قيمة عنصر التحكم في مربع القائمة ActiveX داخل [ملف الإكسل عينة](5115124.xlsx).

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
{{< app/cells/assistant language="cpp" >}}
