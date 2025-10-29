---  
title: 用C++设置工作表中的评论或形状的边距  
linktitle: 在工作表内设置评论或形状的边距  
type: docs  
weight: 1500  
url: /zh/cpp/set-margins-of-comment-or-shape-inside-the-worksheet/  
description: 学习如何使用Aspose.Cells在C++中设置工作表内评论或形状的边距。  
---  

## **可能的使用场景**  

Aspose.Cells允许你使用[**Shape.GetTextAlignment()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/fontsettingcollection/gettextalignment/)属性设置任何形状或评论的边距。该属性返回一个[**Aspose.Cells.Drawing.Texts.ShapeTextAlignment**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment)类的对象，该类具有不同的属性例如[**GetTopMarginPt()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment/gettopmarginpt/)、[**GetLeftMarginPt()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment/getleftmarginpt/)、[**GetBottomMarginPt()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment/getbottommarginpt/)、[**GetRightMarginPt()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment/getrightmarginpt/)等，用于设置顶部、左侧、底部和右侧边距。  

## **设置工作表内批注或形状的边距**  

请查看以下示例代码。它加载包含两个形状的[示例Excel文件](61767851.xlsx)，代码逐个访问这些形状并设置它们的顶部、左侧、底部和右侧边距。请参阅由代码生成的[输出Excel文件](61767852.xlsx)以及显示代码对输出Excel文件影响的截图。  

![todo:image_alt_text](set-margins-of-comment-or-shape-inside-the-worksheet_1.png)  

## **示例代码**  

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
