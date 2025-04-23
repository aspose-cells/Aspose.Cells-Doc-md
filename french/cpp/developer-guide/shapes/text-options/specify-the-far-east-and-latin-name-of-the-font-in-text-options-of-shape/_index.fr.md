---
title: Spécifier le nom de la police de l Est lointain et de l Latin dans les options de texte de la forme avec C++
linktitle: Spécifier le nom Extrême Orient et Latin de la police dans les options de texte de la Forme
type: docs
weight: 1600
url: /fr/cpp/specify-the-far-east-and-latin-name-of-the-font-in-text-options-of-shape/
description: Apprenez comment spécifier les noms de police de l Est lointain et de Latin dans les options de texte d une forme en utilisant Aspose.Cells for C++.
---

## **Scénarios d'utilisation possibles**

Parfois, vous souhaitez afficher du texte dans une police de langue de l'Est lointain, par exemple japonais, chinois, thaï, etc. Aspose.Cells fournit la propriété [**TextOptions.GetFarEastName()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/textoptions/getfareastname/) qui peut être utilisée pour spécifier le nom de la police de la langue de l'Est lointain. De plus, vous pouvez également spécifier le nom de la police latino en utilisant la propriété [**TextOptions.GetLatinName()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/textoptions/getlatinname/).

## **Spécifier le nom Extrême-Orient et Latin de la police dans les options de texte de la Forme**

Le code d'exemple suivant crée une zone de texte et y ajoute du texte japonais. Il spécifie ensuite les noms de polices Latin et Far East du texte, puis enregistre le classeur en tant que [fichier Excel de sortie](67338274.xlsx). La capture d'écran suivante montre les noms de police Latin et Far East de la zone de texte en sortie dans Microsoft Excel.

![todo:image_alt_text](specify-the-far-east-and-latin-name-of-the-font-in-text-options-of-shape_1.png)

## **Code d'exemple**

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
