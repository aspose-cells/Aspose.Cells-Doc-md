---  
title: Imposta i margini del commento o forma all’interno del foglio di lavoro con C++  
linktitle: Imposta i margini del commento o della forma all interno del foglio di lavoro  
type: docs  
weight: 1500  
url: /it/cpp/set-margins-of-comment-or-shape-inside-the-worksheet/  
description: Impara come impostare i margini di commenti o forme all’interno di un foglio di lavoro usando Aspose.Cells con C++.  
---  

## **Possibili Scenari di Utilizzo**  

Aspose.Cells consente di impostare i margini di qualsiasi forma o commento usando la proprietà [**Shape.GetTextAlignment()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/fontsettingcollection/gettextalignment/). Questa proprietà restituisce l’oggetto della classe [**Aspose.Cells.Drawing.Texts.ShapeTextAlignment**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment) che ha diverse proprietà, ad esempio [**GetTopMarginPt()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment/gettopmarginpt/), [**GetLeftMarginPt()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment/getleftmarginpt/), [**GetBottomMarginPt()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment/getbottommarginpt/), [**GetRightMarginPt()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment/getrightmarginpt/), ecc., che possono essere usate per impostare i margini superiore, sinistro, inferiore e destro.  

## **Imposta i Margini del Commento o della Forma all'interno del Foglio di Lavoro**  

Vedi il seguente esempio di codice. Carica il [file Excel di esempio](61767851.xlsx) che contiene due forme. Il codice accede alle forme una alla volta e imposta i loro margini superiore, sinistro, inferiore e destro. Vedi il [file Excel di output](61767852.xlsx) generato dal codice e uno screenshot che mostra l’effetto del codice sul file di output.  

![todo:image_alt_text](set-margins-of-comment-or-shape-inside-the-worksheet_1.png)  

## **Codice di Esempio**  

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
