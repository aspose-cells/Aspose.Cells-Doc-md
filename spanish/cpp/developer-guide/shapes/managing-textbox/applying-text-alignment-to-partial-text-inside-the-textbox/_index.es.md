---
title: Cómo aplicar/configurar la alineación del texto en un cuadro de texto con C++
linktitle: Aplicar/Configurar alineación de texto al cuadro de texto
type: docs
weight: 20
url: /es/cpp/applying-text-alignment-to-partial-text-inside-the-textbox/
description: Cómo aplicar/configurar la alineación del texto en un cuadro de texto en Aspose.Cells con C++.
keywords: Aplicar/configurar alineación Cuadro de texto Hoja de cálculo Excel Aspose
---

Los cuadros de texto pueden mejorar la expresividad de nuestros documentos y diagramas, y aplicar diferentes alineaciones a distintas partes de un cuadro de texto puede ayudar a resaltar puntos de interés para los lectores. Pero la alineación predeterminada del cuadro de texto no cumple todas nuestras necesidades. Para esto, es posible que deba ajustar cada cuadro de texto para cumplir con sus requisitos. Si no tiene muchos objetos de cuadro de texto para ajustar, tiene suerte. Si hay tantos cuadros de texto que ajustar, creo que tendrá problemas. No se preocupe ahora, [Aspose.Cells](https://products.aspose.com/cells/) proporciona una interfaz API para ayudarle a hacer precisamente eso.

El siguiente código de ejemplo aplica la alineación de texto a un cuadro de texto.

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

También puede cambiar la alineación del texto dentro de una forma de cuadro de texto con el texto HTML apropiado. El siguiente código de ejemplo aplica la alineación del texto al texto parcial dentro del cuadro de texto.

[archivo fuente](SampleTextboxExcel2016.xlsx)

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
