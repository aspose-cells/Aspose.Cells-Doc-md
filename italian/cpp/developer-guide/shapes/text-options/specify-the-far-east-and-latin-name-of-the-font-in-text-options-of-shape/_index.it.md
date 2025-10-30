---
title: Specifica il nome del font in Estremo Oriente e Latin nelle Opzioni di testo di una forma con C++
linktitle: Specificare il Nome Estremo Orientale e Latino del Carattere nelle Opzioni di Testo della Forma
type: docs
weight: 1600
url: /it/cpp/specify-the-far-east-and-latin-name-of-the-font-in-text-options-of-shape/
description: Impara come specificare i nomi dei font Estremo Oriente e Latin nelle opzioni di testo di una forma usando Aspose.Cells for C++.
---

## **Possibili Scenari di Utilizzo**

A volte vuoi visualizzare il testo in un font di lingua Estremo Oriente, ad esempio Giapponese, Cinese, Thailandese, ecc. Aspose.Cells fornisce la proprietà [**TextOptions.GetFarEastName()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/textoptions/getfareastname/) che può essere usata per specificare il nome del font di lingua Estremo Oriente. Inoltre, puoi specificare anche il nome del font Latin usando la proprietà [**TextOptions.GetLatinName()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/textoptions/getlatinname/).

## **Specificare il Nome Estremo Orientale e Latino del Carattere nelle Opzioni di Testo della Forma**

Il seguente esempio di codice crea una casella di testo e vi aggiunge del testo giapponese. Poi specifica i nomi dei caratteri Latin e Far East del testo e salva il libro di lavoro come [file Excel di output](67338274.xlsx). La schermata seguente mostra i nomi dei caratteri Latin e Far East della casella di testo di output in Microsoft Excel.

![todo:image_alt_text](specify-the-far-east-and-latin-name-of-the-font-in-text-options-of-shape_1.png)

## **Codice di Esempio**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    Workbook wb;

    Worksheet ws = wb.GetWorksheets().Get(0);

    int idx = ws.GetTextBoxes().Add(5, 5, 50, 200);
    TextBox tb = ws.GetTextBoxes().Get(idx);

    tb.SetText(u"\u3053\u3093\u306B\u3061\u306F\u4E16\u754C");

    tb.GetTextOptions().SetLatinName(u"Comic Sans MS");
    tb.GetTextOptions().SetFarEastName(u"KaiTi");

    wb.Save(u"outputSpecifyFarEastAndLatinNameOfFontInTextOptionsOfShape.xlsx", SaveFormat::Xlsx);

    std::cout << "Textbox created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
