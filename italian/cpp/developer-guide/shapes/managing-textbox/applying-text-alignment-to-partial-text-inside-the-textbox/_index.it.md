---
title: Come applicare/impostare l allineamento del testo nella casella di testo con C++
linktitle: Applicare/impostare l allineamento del testo alla casella di testo
type: docs
weight: 20
url: /it/cpp/applying-text-alignment-to-partial-text-inside-the-textbox/
description: Come applicare/impostare l allineamento del testo nella casella di testo in Aspose.Cells con C++.
keywords: applicare/impostare allineamento casella di testo foglio di lavoro Excel Aspose
---

Le caselle di testo possono migliorare l'espressività dei nostri documenti e diagrammi, e applicare diversi allineamenti a diverse parti di una TextBox può aiutare a evidenziare punti di interesse per i lettori. Ma l'allineamento predefinito della TextBox non soddisfa tutte le esigenze. Per questo, potrebbe essere necessario regolare ogni TextBox per soddisfare le tue specifiche. Se non hai molti oggetti TextBox da modificare, sei fortunato. Se ci sono molte TextBox da regolare, credo che potresti avere dei problemi. Non preoccuparti ora, [Aspose.Cells](https://products.aspose.com/cells/) fornisce un'interfaccia API per aiutarti a fare proprio questo.

Il seguente codice di esempio applica l'allineamento del testo a una casella di testo.

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

Puoi anche modificare l'allineamento del testo di alcune parti di una forma TextBox usando il testo HTML appropriato. Il seguente esempio di codice applica l'allineamento del testo a parte del testo all’interno della TextBox.

[file origine](SampleTextboxExcel2016.xlsx)

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
{{< app/cells/assistant language="cpp" >}}
