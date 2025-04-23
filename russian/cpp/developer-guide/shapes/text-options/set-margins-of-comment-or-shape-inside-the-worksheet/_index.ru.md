---  
title: Установка полей комментария или фигуры внутри рабочего листа с помощью C++  
linktitle: Установить поля комментария или формы внутри таблицы  
type: docs  
weight: 1500  
url: /ru/cpp/set-margins-of-comment-or-shape-inside-the-worksheet/  
description: Узнайте, как установить поля комментариев или фигур внутри рабочего листа, используя Aspose.Cells с C++.  
---  

## **Возможные сценарии использования**  

Aspose.Cells позволяет устанавливать поля любой фигуры или комментария, используя свойство [**Shape.GetTextAlignment()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/fontsettingcollection/gettextalignment/). Оно возвращает объект класса [**Aspose.Cells.Drawing.Texts.ShapeTextAlignment**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment), у которого есть различные свойства, например [**GetTopMarginPt()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment/gettopmarginpt/), [**GetLeftMarginPt()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment/getleftmarginpt/), [**GetBottomMarginPt()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment/getbottommarginpt/), [**GetRightMarginPt()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment/getrightmarginpt/) и др., которые можно использовать для установки верхних, левых, нижних и правых полей.  

## **Задать поля комментария или формы внутри рабочего листа**  

Пример кода ниже. Он загружает [пример файла Excel](61767851.xlsx), содержащего две фигуры. Код обращается к фигурам по очереди и устанавливает их верхние, левое, нижние и правые поля. Посмотрите [сгенерированный файл Excel](61767852.xlsx) и скриншот, показывающий эффект работы кода на выходном файле Excel.  

![todo:image_alt_text](set-margins-of-comment-or-shape-inside-the-worksheet_1.png)  

## **Образец кода**  

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

