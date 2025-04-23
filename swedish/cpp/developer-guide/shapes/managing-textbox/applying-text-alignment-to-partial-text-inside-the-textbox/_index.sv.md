---
title: Hur man tillämpar/inställer textjustering till textbox med C++
linktitle: Tillämpa / ställa in textjustering för textrutan
type: docs
weight: 20
url: /sv/cpp/applying-text-alignment-to-partial-text-inside-the-textbox/
description: Hur man tillämpar/inställer textjustering till textbox i Aspose.Cells med C++.
keywords: tillämpa / ställa in justering Rutkontroll Excel Aspose
---

TextBoxar kan förbättra uttryckssättet i våra dokument och diagram, och att tillämpa olika justeringar på olika delar av en TextBox kan hjälpa till att lyfta fram intressanta punkter för läsare. Men standardjusteringen av TextBox möter inte alla våra behov. För detta kan du behöva justera varje TextBox för att möta dina målkrav. Om du inte har många TextBox-objekt att finjustera är du lyckligt lottad. Om det finns så många TextBoxar att justera, tror jag att du kommer att ha problem. Oroa dig inte nu, [Aspose.Cells](https://products.aspose.com/cells/) tillhandahåller ett API-gränssnitt för att hjälpa dig med just detta.

Följande kodexempel tillämpar textjustering på en TextBox.

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

Du kan också ändra textjusteringen för vissa delar av en TextBox-form med rätt HTML-text. Följande exempel kod tillämpar textjustering på del av texten i TextBoxen.

[källfil](SampleTextboxExcel2016.xlsx)

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
