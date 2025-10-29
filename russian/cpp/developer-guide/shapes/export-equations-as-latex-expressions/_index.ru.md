---
title: Как экспортировать уравнения Excel в другие типы выражений с помощью C++
linktitle: экспорт уравнения
type: docs
weight: 100
url: /ru/cpp/export-equation/
description: Экспорт формул Excel в LaTeX и MathML с помощью Aspose.Cells for C++.
---

Иногда вам может понадобиться экспортировать формулы Excel в другие форматы в вашем коде для соответствия требованиям работы. Библиотека Aspose.Cells for C++ может выполнить эти задачи. Ниже представлены методы экспорта формул Excel в другие форматы с использованием C++.

Мы предоставляем пример кода, помогающий достигнуть этих целей с использованием Aspose.Cells for C++. Необходимые примерные файлы включены.

Образец файла: [Sample.xlsx](Sample.xlsx)

## Экспорт уравнений как LaTeX выражений

Для экспорта уравнений как LaTeX выражений используйте метод [ToLaTeX()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.equations/equationnode/tolatex/). 

Следующий пример демонстрирует использование [ToLaTeX()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.equations/equationnode/tolatex/) и вставку результатов в HTML:

### C++-Для-LaTeX

```c++
#include <iostream>
#include <fstream>
#include <sstream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook(srcDir + u"Sample.xlsx");

    std::stringstream htmlContent;
    htmlContent << "<!DOCTYPE html>\r\n<html lang=\"en\">\r\n<head>\r\n    <meta charset=\"UTF-8\">\r\n    <title>Title</title>\r\n    <script type=\"text/javascript\" async src=\"https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML\"></script>\r\n    <script type=\"text/x-mathjax-config\">\r\n        MathJax.Hub.Config({\r\n\t    tex2jax: {\r\n\t        inlineMath: [['$','$'], ['\\\\(','\\\\)']],\r\n\t        processEscapes: true\r\n\t    }\r\n\t});\r\n    </script>\r\n</head>\r\n<body>";

    WorksheetCollection worksheets = workbook.GetWorksheets();
    ShapeCollection shapes = worksheets.Get(0).GetShapes();

    if (shapes.GetCount() > 0)
    {
        TextBox textBox(shapes.Get(0));
        EquationNode mathNode = textBox.GetEquationParagraph().GetChild(0);
        U16String latexFormula = mathNode.ToLaTeX();

        std::string utf8Formula = latexFormula.ToUtf8();

        htmlContent << "<p>$" << utf8Formula << "$</p>\r\n";
    }

    htmlContent << "</body>\r\n</html>";

    U16String outputPath = outDir + u"result.html";
    std::ofstream outputFile(outputPath.ToUtf8().c_str(), std::ios::binary);
    outputFile << htmlContent.str();
    outputFile.close();

    Aspose::Cells::Cleanup();
    return 0;
}
```

## Экспорт уравнений как MathML выражений

Для экспорта уравнений как MathML выражений используйте метод [ToMathML()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.equations/equationnode/tomathml/).

Следующий пример демонстрирует использование [ToMathML()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.equations/equationnode/tomathml/) и вставку результатов в HTML:

### C++-Для-MathML

```c++
#include <iostream>
#include <fstream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;
using namespace Aspose::Cells::Drawing::Equations;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");
    U16String inputFilePath = srcDir + u"Sample.xlsx";

    Workbook workbook(inputFilePath);
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    ShapeCollection shapes = worksheet.GetShapes();

    TextBox textBox = static_cast<TextBox>(shapes.Get(0));
    EquationNode mathNode = textBox.GetEquationParagraph().GetChild(0);

    U16String htmlContent = u"<!DOCTYPE html>\r\n<html lang=\"en\">\r\n<head>\r\n    <meta charset=\"UTF-8\">\r\n    <title>Title</title>\r\n    <script type=\"text/javascript\" async src=\"https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML\"></script>\r\n</head>\r\n<body>";
    htmlContent += mathNode.ToMathML();
    htmlContent += u"</body>\r\n</html>";

    U16String outputFilePath = outDir + u"result.html";
    std::ofstream outFile(outputFilePath.ToUtf8().c_str());
    outFile << htmlContent.ToUtf8();
    outFile.close();

    std::cout << "HTML file created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
