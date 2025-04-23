---
title: Разработать кастомный размер бумаги листа для отображения с помощью C++
linktitle: Реализация пользовательского размера бумаги для рендеринга листа
type: docs
weight: 70
url: /ru/cpp/implement-custom-paper-size-of-worksheet-for-rendering/
description: Эта статья объясняет, как использовать C++ API для установки пользовательского размера бумаги выбранных листов при рендеринге файла Excel в PDF программным путем.
keywords: установить пользовательский размер бумаги при рендеринге Excel в PDF c++
---

## **Возможные сценарии использования**

В MS Excel нет прямой возможности создавать пользовательские размеры бумаги, однако вы можете установить пользовательский размер бумаги для желаемых листов при рендеринге файлов Excel в PDF. Этот документ объясняет, как установить пользовательский размер бумаги листа, используя API Aspose.Cells.

## **Настройка пользовательского размера бумаги для отображения на листе**

Aspose.Cells позволяет реализовать желаемый размер бумаги листа. Вы можете использовать метод [**CustomPaperSize**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/custompapersize/) класса [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/), чтобы задать пользовательский размер страницы. В следующем примере кода показано, как задать пользовательский размер бумаги для первого листа книги. Также смотрите [выходной PDF](45056028.pdf), созданный этим кодом, для справки.

## **Снимок экрана**

![todo:image_alt_text](implement-custom-paper-size-of-worksheet-for-rendering_1.png)

## **Образец кода**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Create workbook object
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Set custom paper size in unit of inches
    ws.GetPageSetup().CustomPaperSize(6, 4);

    // Access cell B4
    Cell b4 = ws.GetCells().Get("B4");

    // Add the message in cell B4
    b4.PutValue(u"Pdf Page Dimensions: 6.00 x 4.00 in");

    // Save the workbook in pdf format
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");
    wb.Save(outputDir + u"outputCustomPaperSize.pdf");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
