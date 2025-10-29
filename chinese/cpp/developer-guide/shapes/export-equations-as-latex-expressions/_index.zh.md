---
title: 如何将Excel中的公式导出为其他类型的表达式，使用C++
linktitle: 导出公式
type: docs
weight: 100
url: /zh/cpp/export-equation/
description: 使用Aspose.Cells for C++将Excel公式导出为LaTeX和MathML。
---

有时，你可能需要在代码中将Excel公式导出为其他格式以满足工作需求。Aspose.Cells for C++库能满足这些需求。以下内容介绍如何使用C++将Excel公式导出为其他格式的方法。

我们提供示例代码，帮助你使用Aspose.Cells for C++实现这些目标。所需的示例文件已包含在内。

示例文件：[Sample.xlsx](Sample.xlsx)

## 将公式导出为LaTeX表达式

要将公式导出为LaTeX表达式，请使用 [ToLaTeX()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.equations/equationnode/tolatex/) 方法。 

以下示例演示如何使用 [ToLaTeX()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.equations/equationnode/tolatex/) 及将结果插入HTML：

### C++-转LaTeX

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

## 将公式导出为MathML表达式

要将公式导出为MathML表达式，请使用 [ToMathML()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.equations/equationnode/tomathml/) 方法。

以下示例演示如何使用 [ToMathML()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.equations/equationnode/tomathml/) 及将结果插入HTML：

### C++-转MathML

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
