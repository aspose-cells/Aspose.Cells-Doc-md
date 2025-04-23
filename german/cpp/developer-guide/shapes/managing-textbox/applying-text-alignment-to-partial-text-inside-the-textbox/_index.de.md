---
title: Wie man Textausrichtung auf Textfeld mit C++ anwendet/einstellt
linktitle: Textausrichtung für Textfeld anwenden/einstellen
type: docs
weight: 20
url: /de/cpp/applying-text-alignment-to-partial-text-inside-the-textbox/
description: Wie man Textausrichtung auf Textfeld in Aspose.Cells mit C++ anwendet/einstellt.
keywords: Anwendung/ Einstellung der Ausrichtung des Textfelds Arbeitsblatt Excel Aspose
---

TextBoxen können die Ausdruckskraft unserer Dokumente und Diagramme verbessern, und das Anwenden verschiedener Ausrichtungen auf unterschiedliche Teile eines TextBox kann helfen, interessante Punkte für die Leser hervorzuheben. Aber die Standardausrichtung einer TextBox erfüllt nicht alle unsere Bedürfnisse. Für diesen Zweck müssen Sie jede TextBox an Ihre Zielanforderungen anpassen. Wenn Sie nicht viele TextBox-Objekte zum Anpassen haben, haben Sie Glück. Wenn es jedoch sehr viele TextBoxen gibt, denke ich, könnten Sie Probleme bekommen. Keine Sorge, [Aspose.Cells](https://products.aspose.com/cells/) bietet eine API-Schnittstelle, die Ihnen genau dabei hilft.

Der folgende Beispielcode wendet die Textausrichtung auf ein TextBox an.

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

Sie können auch die Textausrichtung einiger Texte innerhalb einer TextBox-Form anhand des entsprechenden HTML-Texts ändern. Das folgende Beispiel wendet die Textausrichtung auf den Teiltext innerhalb der TextBox an.

[Quelldatei](SampleTextboxExcel2016.xlsx)

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
