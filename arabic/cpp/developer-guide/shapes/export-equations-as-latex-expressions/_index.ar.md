---
title: كيفية تصدير معادلات إكسل إلى أنواع أخرى من التعبيرات باستخدام ++C
linktitle: تصدير المعادلة
type: docs
weight: 100
url: /ar/cpp/export-equation/
description: تصدير صيغ إكسل إلى LaTeX و MathML باستخدام Aspose.Cells for C++.
---

أحيانًا قد تحتاج إلى تصدير صيغ إكسل إلى تنسيقات أخرى في رمزك لتلبية متطلبات العمل. مكتبة Aspose.Cells for C++ يمكنها تلبية هذه الاحتياجات. المحتوى التالي يقدم طرقًا لتصدير صيغ إكسل إلى تنسيقات أخرى باستخدام ++C.

نقدم رمزًا نموذجيًا للمساعدة في تحقيق هذه الأهداف باستخدام Aspose.Cells for C++. تتضمن الملفات النموذجية الضرورية.

ملف عينة: [Sample.xlsx](Sample.xlsx)

## تصدير المعادلات كتعابير LaTeX

لتصدير المعادلات كتعابير LaTeX، استخدم طريقة [ToLaTeX()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.equations/equationnode/tolatex/). 

يعرض المثال التالي استخدام [ToLaTeX()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.equations/equationnode/tolatex/) وإدراج النتائج في HTML:

### C++-إلى-LaTeX

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

## تصدير المعادلات كتعابير MathML

لتصدير المعادلات كتعابير MathML، استخدم طريقة [ToMathML()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.equations/equationnode/tomathml/).

يعرض المثال التالي استخدام [ToMathML()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.equations/equationnode/tomathml/) وإدراج النتائج في HTML:

### C++-إلى-MathML

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
