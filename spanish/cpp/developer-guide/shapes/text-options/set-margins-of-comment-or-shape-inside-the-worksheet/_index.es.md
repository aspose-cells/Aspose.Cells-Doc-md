---  
title: Establecer márgenes de comentario o forma dentro de la hoja de cálculo con C++  
linktitle: Establecer márgenes de comentario o forma dentro de la hoja de cálculo  
type: docs  
weight: 1500  
url: /es/cpp/set-margins-of-comment-or-shape-inside-the-worksheet/  
description: Aprenda cómo establecer márgenes de comentarios o formas dentro de una hoja de cálculo usando Aspose.Cells con C++.  
---  

## **Escenarios de uso posibles**  

Aspose.Cells le permite configurar los márgenes de cualquier forma o comentario usando la propiedad [**Shape.GetTextAlignment()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/fontsettingcollection/gettextalignment/). Esta propiedad devuelve el objeto de la clase [**Aspose.Cells.Drawing.Texts.ShapeTextAlignment**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment) que tiene diferentes propiedades, por ejemplo, [**GetTopMarginPt()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment/gettopmarginpt/), [**GetLeftMarginPt()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment/getleftmarginpt/), [**GetBottomMarginPt()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment/getbottommarginpt/), [**GetRightMarginPt()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment/getrightmarginpt/), etc., que se pueden usar para establecer los márgenes superior, izquierdo, inferior y derecho.  

## **Establecer márgenes de comentario o forma dentro de la hoja de cálculo**  

Por favor, vea el siguiente código de ejemplo. Carga el [archivo de Excel de ejemplo](61767851.xlsx) que contiene dos formas. El código accede a las formas una por una y establece sus márgenes superior, izquierdo, inferior y derecho. Por favor, vea el [archivo de Excel de salida](61767852.xlsx) generado por el código y una captura de pantalla que muestra el efecto del código en el archivo de Excel de salida.  

![todo:image_alt_text](set-margins-of-comment-or-shape-inside-the-worksheet_1.png)  

## **Código de muestra**  

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

