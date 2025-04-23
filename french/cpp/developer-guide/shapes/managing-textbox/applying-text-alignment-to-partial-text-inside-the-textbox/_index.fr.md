---
title: Comment appliquer/définir l’alignement du texte dans la boîte de texte avec C++
linktitle: Appliquer/Définir l alignement du texte à une zone de texte
type: docs
weight: 20
url: /fr/cpp/applying-text-alignment-to-partial-text-inside-the-textbox/
description: Comment appliquer/définir l’alignement du texte dans la boîte de texte dans Aspose.Cells avec C++.
keywords: Appliquer/Définir l alignement de la zone de texte Feuille de calcul Excel Aspose
---

Les zones de texte peuvent améliorer l'expressivité de nos documents et diagrammes, et appliquer différents alignements à différentes parties d'une zone de texte peut aider à mettre en évidence des points d'intérêt pour les lecteurs. Mais l'alignement par défaut de la zone de texte ne répond pas à tous nos besoins. Pour cela, vous devrez peut-être ajuster chaque zone de texte pour répondre à vos exigences cibles. Si vous n'avez pas beaucoup d'objets Zone de texte à ajuster, cela ne vous posera pas de problème. Si vous avez tellement de zones de texte à ajuster, je pense que vous aurez des difficultés. Ne vous inquiétez pas maintenant, [Aspose.Cells](https://products.aspose.com/cells/) offre une API pour vous aider à faire cela.

Le code d'exemple suivant applique l'alignement du texte à une zone de texte.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new workbook
    Workbook workbook;

    // Get the shapes collection from the first worksheet
    ShapeCollection shapes = workbook.GetWorksheets().Get(0).GetShapes();

    // Add a TextBox to the worksheet
    Shape shape = shapes.AddTextBox(2, 0, 2, 0, 50, 120);

    // Set the text of the TextBox
    shape.SetText(u"This is a test.");

    // Set the horizontal and vertical alignment of the text
    shape.SetTextHorizontalAlignment(TextAlignmentType::Center);
    shape.SetTextVerticalAlignment(TextAlignmentType::Center);

    // Save the workbook to the output directory
    workbook.Save(outDir + u"result.xlsx");

    std::cout << "TextBox added and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Vous pouvez également modifier l'alignement du texte à l'intérieur d'une zone de texte avec le code HTML approprié. Le code exemple suivant applique l'alignement du texte à un texte partiel à l'intérieur de la zone de texte.

[fichier source](SampleTextboxExcel2016.xlsx)

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"SampleTextboxExcel2016.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"Output.xlsx";

    // Initialize an object of the Workbook class to load template file
    Workbook sourceWb(inputFilePath);

    // Access the target textbox whose text is to be aligned
    auto sourceTextBox = sourceWb.GetWorksheets().Get(0).GetShapes().Get(0);

    // Create an object of the target workbook
    Workbook destWb;

    // Access first worksheet from the collection
    auto sheet = destWb.GetWorksheets().Get(0);

    // Create new textbox
    TextBox textBox = sheet.GetShapes().AddShape(MsoDrawingType::TextBox, 1, 0, 1, 0, 200, 200);

    // Alternatively text box can be added using following line as well
    // TextBox textBox = sheet.GetShapes().AddTextBox(1, 0, 1, 0, 200, 200);

    // Use Html string from a template file textbox
    textBox.SetHtmlText(sourceTextBox.GetHtmlText());

    // Save the workbook on disc
    destWb.Save(outputFilePath);

    std::cout << "Textbox copied and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
