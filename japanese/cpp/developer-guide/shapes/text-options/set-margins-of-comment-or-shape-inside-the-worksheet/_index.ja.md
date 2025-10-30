---  
title: C++を使用してワークシート内のコメントや図形のマージンを設定する方法を学びます。  
linktitle: ワークシート内のコメントまたは図形の余白を設定する  
type: docs  
weight: 1500  
url: /ja/cpp/set-margins-of-comment-or-shape-inside-the-worksheet/  
description: Aspose.Cellsを使用してC++でワークシート内のコメントや図形のマージンを設定する方法を学びます。  
---  

## **可能な使用シナリオ**  

Aspose.Cellsでは、[**Shape.GetTextAlignment()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/fontsettingcollection/gettextalignment/)プロパティを使用して任意の図形やコメントのマージンを設定できます。このプロパティは[**Aspose.Cells.Drawing.Texts.ShapeTextAlignment**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment)クラスのオブジェクトを返し、[**GetTopMarginPt()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment/gettopmarginpt/)、[**GetLeftMarginPt()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment/getleftmarginpt/)、[**GetBottomMarginPt()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment/getbottommarginpt/)、[**GetRightMarginPt()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment/getrightmarginpt/)などのさまざまなプロパティを持ち、上、左、下、右のマージンを設定可能です。  

## **ワークシート内のコメントまたは図形の余白を設定する**  

以下のサンプルコードをご覧ください。これは、2つの図形を含むサンプルExcelファイル（61767851.xlsx）を読み込み、それぞれの図形の上、左、下、右のマージンを設定します。コードによって生成された[出力Excelファイル](61767852.xlsx)と、その効果を示すスクリーンショットを参照してください。  

![todo:image_alt_text](set-margins-of-comment-or-shape-inside-the-worksheet_1.png)  

## **サンプルコード**  

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
