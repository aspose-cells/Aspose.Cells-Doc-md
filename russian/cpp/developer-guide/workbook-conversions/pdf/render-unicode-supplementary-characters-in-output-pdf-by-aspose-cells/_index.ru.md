---
title: Отрисовка дополнительных символов Юникода в выходном PDF с помощью C++ и Aspose.Cells
linktitle: Отрисовка дополнительных символов Юникода
type: docs
weight: 350
url: /ru/cpp/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/
description: Узнайте, как отображать дополнительные символы Юникода в выходном PDF с помощью Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Обычные символы Юникода имеют длину 2 байта, а дополнительные символы Юникода - 4 байта. Aspose.Cells теперь поддерживает отображение этих дополнительных символов Юникода длиной 4 байта.

В стандарте символов Юникода дополнительные символы - это символы, которым назначены кодовые точки от U+10000 до U+10FFFF. Другими словами, это символы Юникода, большие чем U+FFFF.

- В UTF-8 каждый из этих символов имеет длину 4 байта.
- В UTF-16 для этих символов требуются 2 заместителя (16-битные единицы).

{{% /alert %}}

## Отображение дополнительных символов Юникода в выходном PDF при использовании Aspose.Cells

На следующем скриншоте показано, как Aspose.Cells преобразовал [исходный файл Excel](5115563.xlsx) в [выходной PDF](5115564.pdf). Как видно, все три дополнительных символа Юникода отображены точно так же, как это делает Microsoft Excel.

![todo:image_alt_text](output.png)

## Образец кода

Вы можете использовать этот образец кода для преобразования [исходного файла Excel](5115563.xlsx) в [выходной PDF](5115564.pdf).

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"unicode-supplementary-characters.xlsx";

    // Path of output PDF file
    U16String outputFilePath = outDir + u"RenderUnicodeInOutput_out.pdf";

    // Load the source excel file containing Unicode Supplementary characters
    Workbook wb(inputFilePath);

    // Save the workbook as PDF
    wb.Save(outputFilePath, SaveFormat::Pdf);

    std::cout << "Workbook saved successfully with Unicode Supplementary characters!" << std::endl;

    Aspose::Cells::Cleanup();

    return 0;
}
```
