---  
title: Définir les marges du commentaire ou de la forme à l intérieur de la feuille de calcul avec C++  
linktitle: Définir les marges du commentaire ou de la forme à l intérieur de la feuille de calcul  
type: docs  
weight: 1500  
url: /fr/cpp/set-margins-of-comment-or-shape-inside-the-worksheet/  
description: Apprenez comment définir les marges des commentaires ou des formes à l intérieur d une feuille de calcul en utilisant Aspose.Cells avec C++.  
---  

## **Scénarios d'utilisation possibles**  

Aspose.Cells vous permet de définir les marges de n'importe quelle forme ou commentaire à l'aide de la propriété [**Shape.GetTextAlignment()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/fontsettingcollection/gettextalignment/). Cette propriété retourne l'objet de la classe [**Aspose.Cells.Drawing.Texts.ShapeTextAlignment**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment) qui possède différentes propriétés, par exemple [**GetTopMarginPt()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment/gettopmarginpt/), [**GetLeftMarginPt()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment/getleftmarginpt/), [**GetBottomMarginPt()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment/getbottommarginpt/), [**GetRightMarginPt()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment/getrightmarginpt/), etc., pouvant être utilisées pour définir les marges du haut, gauche, bas et droite.  

## **Définir les marges du commentaire ou de la forme à l'intérieur de la feuille de calcul**  

Veuillez voir le code d'exemple suivant. Il charge le [fichier Excel d'exemple](61767851.xlsx) contenant deux formes. Le code accède aux formes une par une et définit leurs marges en haut, à gauche, en bas et à droite. Veuillez voir le [fichier Excel de sortie](61767852.xlsx) généré par le code et une capture d'écran montrant l'effet du code sur le fichier Excel de sortie.  

![todo:image_alt_text](set-margins-of-comment-or-shape-inside-the-worksheet_1.png)  

## **Code d'exemple**  

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load the sample Excel file
    Workbook workbook(u"sampleSetMarginsOfCommentOrShapeInsideTheWorksheet.xlsx");

    // Access first worksheet
    Worksheet ws = workbook.GetWorksheets().Get(0);

    // Iterate through each shape in the worksheet
    for (int32_t i = 0; i < ws.GetShapes().GetCount(); i++)
    {
        Shape sh = ws.GetShapes().Get(i);

        // Access the text alignment
        ShapeTextAlignment txtAlign = sh.GetTextBody().GetTextAlignment();

        // Set auto margin false
        txtAlign.SetIsAutoMargin(false);

        // Set the top, left, bottom and right margins
        txtAlign.SetTopMarginPt(10);
        txtAlign.SetLeftMarginPt(10);
        txtAlign.SetBottomMarginPt(10);
        txtAlign.SetRightMarginPt(10);
    }

    // Save the output Excel file
    workbook.Save(u"outputSetMarginsOfCommentOrShapeInsideTheWorksheet.xlsx");

    std::cout << "Margins set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```  

{{< app/cells/assistant language="cpp" >}}
