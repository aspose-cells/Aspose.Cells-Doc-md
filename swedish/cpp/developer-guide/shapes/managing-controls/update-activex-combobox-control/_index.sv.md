---
title: Uppdatera ActiveX ComboBox Control med C++
linktitle: Uppdatera ActiveX ComboBox kontroll
type: docs
weight: 170
url: /sv/cpp/update-activex-combobox-control/
description: Lära sig hur man läser eller skriver värden för ActiveX ComboBox Control med Aspose.Cells och C++.
---

## **Möjliga användningsscenario**
Du kan läsa och skriva värden för ActiveX ComboBox Control med Aspose.Cells. Vänligen få tillgång till ActiveX-kontrollen via egenskapen [Shape.ActiveXControl](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.activexcontrols/activexcontrol/) och kontrollera dess typ via [ActiveXControl.GetType()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.activexcontrols/activexcontrolbase/gettype/) egenskapen. Den bör returnera [ControlType.ComboBox](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.activexcontrols/controltype/), och sedan typcastas till [ComboBoxActiveXControl](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.activexcontrols/comboboxactivexcontrol/) objekt för att läsa eller modifiera dess olika egenskaper.

Vänligen ladda ner den [provexemplet Excel-fil](5115124.xlsx) som används i följande provkod.

## **Uppdatera ActiveX ComboBox Control**
Följande skärmbild visar effekten av provkoden på den [provexemplet Excel-filen](5115124.xlsx). Som du kan se har ActiveX ComboBox-värdet uppdaterats till "Detta är kombinationsruta-kontroll".

|![todo:image_alt_text](update-activex-combobox-control_1.png)|
| :- |

## **Exempelkod**
Följande provkod uppdaterar värdet för ActiveX ComboBox Control som finns i [provexemplet Excel-filen](5115124.xlsx).

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
