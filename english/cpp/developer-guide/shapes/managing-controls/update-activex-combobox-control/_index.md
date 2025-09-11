---
title: Update ActiveX ComboBox Control with C++
linktitle: Update ActiveX ComboBox Control
type: docs
weight: 170
url: /cpp/update-activex-combobox-control/
description: Learn how to read or write values of ActiveX ComboBox Control using Aspose.Cells with C++.
---

## **Possible Usage Scenarios**
You can read or write the values of ActiveX ComboBox Control using Aspose.Cells. Please access the ActiveX Control via [Shape.ActiveXControl](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.activexcontrols/activexcontrol/) property and check its type via [ActiveXControl.GetType()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.activexcontrols/activexcontrolbase/gettype/) property. It should return [ControlType.ComboBox](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.activexcontrols/controltype/) value, and then typecast it into [ComboBoxActiveXControl](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.activexcontrols/comboboxactivexcontrol/) object to read or modify its various properties.

Please download the [sample excel file](5115124.xlsx) used in the following sample code.

## **Update ActiveX ComboBox Control**
The following screenshot shows the effect of the sample code on the [sample excel file](5115124.xlsx). As you can see, the ActiveX ComboBox value has been updated to "This is combo box control".

|![todo:image_alt_text](update-activex-combobox-control_1.png)|
| :- |

## **Sample Code**
The following sample code updates the value of ActiveX ComboBox Control present inside the [sample excel file](5115124.xlsx).

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