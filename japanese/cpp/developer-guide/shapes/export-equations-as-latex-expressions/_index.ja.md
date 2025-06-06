---
title: Excelの式を他の表現型にエクスポートする方法（C++を使用）
linktitle: 数式をエクスポート
type: docs
weight: 100
url: /ja/cpp/export-equation/
description: Aspose.Cells for C++を使用してExcelの数式をLaTeXやMathMLにエクスポートします。
---

時には、作業要件を満たすためにExcelの数式を他のフォーマットにエクスポートする必要があります。Aspose.Cells for C++ライブラリはこれらのニーズを満たすことができます。以下の内容は、C++を使ったExcelの数式の他フォーマットへのエクスポート方法を紹介しています。

これらの目標を達成するために、Aspose.Cells for C++を使用したサンプルコードを提供しています。必要なサンプルファイルも含まれています。

サンプルファイル：[Sample.xlsx](Sample.xlsx)

## 数式をLaTeX表現としてエクスポート

[ToLaTeX()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.equations/equationnode/tolatex/)メソッドを使用して式をLaTeX式にエクスポートします。 

以下のサンプルは、[ToLaTeX()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.equations/equationnode/tolatex/)の使用例と結果をHTMLに挿入する方法を示しています。

### C++-To-LaTeX

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

## 数式をMathML表現としてエクスポート

[ToMathML()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.equations/equationnode/tomathml/)メソッドを使用して数式をMathML式にエクスポートします。

以下のサンプルは、[ToMathML()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.equations/equationnode/tomathml/)の使用例と結果をHTMLに挿入する方法を示しています。

### C++-To-MathML

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
