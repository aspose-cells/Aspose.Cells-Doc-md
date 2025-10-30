---
title: ActiveX ComboBox Control mit C++ aktualisieren
linktitle: Aktualisieren Sie die ActiveX ComboBox Steuerelemente
type: docs
weight: 170
url: /de/cpp/update-activex-combobox-control/
description: Lernen Sie, wie Sie Werte von ActiveX ComboBox Control mit Aspose.Cells in C++ lesen oder schreiben.
---

## **Mögliche Verwendungsszenarien**
Sie können die Werte des ActiveX-ComboBox-Control mit Aspose.Cells lesen oder schreiben. Greifen Sie auf das ActiveX-Control über die Property [Shape.ActiveXControl](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.activexcontrols/activexcontrol/) zu und überprüfen Sie seinen Typ über die Property [ActiveXControl.GetType()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.activexcontrols/activexcontrolbase/gettype/). Es sollte den Wert [ControlType.ComboBox](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.activexcontrols/controltype/) zurückgeben, und dann wandeln Sie es in das Objekt [ComboBoxActiveXControl](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.activexcontrols/comboboxactivexcontrol/) um, um dessen Eigenschaften zu lesen oder zu ändern.

Bitte laden Sie die im folgenden Beispielcode verwendete [Beispieldatei](5115124.xlsx) herunter.

## **Aktualisieren Sie das ActiveX-ComboBox-Steuerelement**
Der folgende Screenshot zeigt die Auswirkung des Beispielcodes auf die [Beispieldatei](5115124.xlsx). Wie Sie sehen können, wurde der Wert der ActiveX-ComboBox auf "Dies ist die Kombinationsfeldsteuerung" aktualisiert.

|![todo:image_alt_text](update-activex-combobox-control_1.png)|
| :- |

## **Beispielcode**
Der folgende Beispielcode aktualisiert den Wert des ActiveX-ComboBox-Steuerungselements, das sich in der [Beispieldatei Excel](5115124.xlsx) befindet.

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
