---
title: Aggiorna il controllo ActiveX ComboBox con C++
linktitle: Aggiorna il controllo ComboBox ActiveX
type: docs
weight: 170
url: /it/cpp/update-activex-combobox-control/
description: Impara come leggere o scrivere i valori del controllo ActiveX ComboBox usando Aspose.Cells con C++.
---

## **Possibili Scenari di Utilizzo**
Puoi leggere o scrivere i valori del controllo ActiveX ComboBox usando Aspose.Cells. Accedi al controllo ActiveX tramite la proprietà [Shape.ActiveXControl](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.activexcontrols/activexcontrol/) e verifica il suo tipo tramite la proprietà [ActiveXControl.GetType()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.activexcontrols/activexcontrolbase/gettype/). Dovrebbe restituire il valore [ControlType.ComboBox](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.activexcontrols/controltype/), quindi esegui una conversione di tipo in [ComboBoxActiveXControl](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.activexcontrols/comboboxactivexcontrol/) per leggere o modificare le sue varie proprietà.

Si prega di scaricare il [file Excel di esempio](5115124.xlsx) utilizzato nel seguente codice di esempio.

## **Aggiorna il controllo ComboBox ActiveX**
Lo screenshot seguente mostra l'effetto del codice di esempio sul [file Excel di esempio](5115124.xlsx). Come si può vedere, il valore del ComboBox ActiveX è stato aggiornato a "Questo è un controllo combobox".

|![todo:image_alt_text](update-activex-combobox-control_1.png)|
| :- |

## **Codice di Esempio**
Il seguente codice di esempio aggiorna il valore del controllo ActiveX ComboBox presente all'interno del [file Excel di esempio](5115124.xlsx).

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
