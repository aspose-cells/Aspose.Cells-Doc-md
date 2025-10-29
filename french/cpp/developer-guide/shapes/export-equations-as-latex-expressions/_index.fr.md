---
title: Comment exporter les équations Excel vers d autres types d expressions avec C++
linktitle: exporter une équation
type: docs
weight: 100
url: /fr/cpp/export-equation/
description: Exporter les formules Excel vers LaTeX et MathML en utilisant Aspose.Cells for C++.
---

Parfois, vous pouvez avoir besoin d'exporter les formules Excel vers d'autres formats dans votre code pour répondre aux exigences du travail. La bibliothèque Aspose.Cells for C++ peut satisfaire ces besoins. Le contenu suivant présente des méthodes pour exporter les formules Excel vers d'autres formats en utilisant C++.

Nous fournissons un code d'exemple pour aider à atteindre ces objectifs en utilisant Aspose.Cells for C++. Les fichiers d'exemple nécessaires sont inclus.

Fichier d'exemple : [Sample.xlsx](Sample.xlsx)

## Exporter des équations en expressions LaTeX

Pour exporter des équations en expressions LaTeX, utilisez la méthode [ToLaTeX()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.equations/equationnode/tolatex/). 

L'exemple suivant montre comment utiliser [ToLaTeX()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.equations/equationnode/tolatex/) et insérer les résultats dans HTML :

### C++-Vers-LaTeX

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

## Exporter des équations en expressions MathML

Pour exporter des équations en expressions MathML, utilisez la méthode [ToMathML()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.equations/equationnode/tomathml/).

L'exemple suivant montre comment utiliser [ToMathML()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.equations/equationnode/tomathml/) et insérer les résultats dans HTML :

### C++-Vers-MathML

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
