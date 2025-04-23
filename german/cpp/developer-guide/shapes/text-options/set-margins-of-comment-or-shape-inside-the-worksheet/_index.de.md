---  
title: Ränder der Kommentare oder Formen innerhalb des Arbeitsblatts mit C++ einstellen  
linktitle: Abstände von Kommentaren oder Formen im Arbeitsblatt festlegen  
type: docs  
weight: 1500  
url: /de/cpp/set-margins-of-comment-or-shape-inside-the-worksheet/  
description: Lernen Sie, wie man Ränder von Kommentaren oder Formen innerhalb eines Arbeitsblatts mit Aspose.Cells und C++ festlegt.  
---  

## **Mögliche Verwendungsszenarien**  

Aspose.Cells ermöglicht es, die Ränder jeder Form oder jedes Kommentars mit der [**Shape.GetTextAlignment()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/fontsettingcollection/gettextalignment/)-Eigenschaft festzulegen. Diese Eigenschaft gibt das Objekt der Klasse [**Aspose.Cells.Drawing.Texts.ShapeTextAlignment**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment) zurück, das verschiedene Eigenschaften hat, z.B. [**GetTopMarginPt()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment/gettopmarginpt/), [**GetLeftMarginPt()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment/getleftmarginpt/), [**GetBottomMarginPt()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment/getbottommarginpt/), [**GetRightMarginPt()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment/getrightmarginpt/), usw., die verwendet werden können, um die Ober-, Links-, Unter- und rechten Ränder einzustellen.  

## **Ränder des Kommentars oder der Form innerhalb des Arbeitsblatts festlegen**  

Bitte sehen Sie sich den folgenden Beispielcode an. Er lädt die [Beispiel-Excel-Datei](61767851.xlsx), die zwei Formen enthält. Der Code greift auf die Formen einzeln zu und setzt ihre Ober-, Links-, Unter- und Rechständer. Bitte sehen Sie sich die [Ausgabedatei](61767852.xlsx) an, die vom Code erstellt wurde, sowie einen Screenshot, der die Wirkung des Codes auf die Ausgabedatei zeigt.  

![todo:image_alt_text](set-margins-of-comment-or-shape-inside-the-worksheet_1.png)  

## **Beispielcode**  

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

