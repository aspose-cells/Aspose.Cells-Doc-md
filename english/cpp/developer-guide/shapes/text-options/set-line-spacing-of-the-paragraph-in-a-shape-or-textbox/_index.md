---  
title: Set Line Spacing of the Paragraph in a Shape or Textbox with C++  
linktitle: Set Line Spacing of the Paragraph  
type: docs  
weight: 290  
url: /cpp/set-line-spacing-of-the-paragraph-in-a-shape-or-textbox/  
description: Learn how to set line spacing, space before, and space after in a paragraph within a shape or textbox using Aspose.Cells for C++.  
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

{{% alert color="primary" %}}  

You can set the line spacing of the paragraph, its space before, and its space after using the [**TextParagraph.GetLineSpace()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/textparagraph/getlinespace/), [**TextParagraph.GetSpaceBefore()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/textparagraph/getspacebefore/) and [**TextParagraph.GetSpaceAfter()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/textparagraph/getspaceafter/) properties of the [**TextParagraph**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/textparagraph/) class.  

{{% /alert %}}  

The following sample code explains the usage of the mentioned properties.  

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;
using namespace Aspose::Cells::Drawing::Texts;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a workbook
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Add a text box inside the sheet
    ws.GetShapes().AddTextBox(2, 0, 2, 0, 100, 200);

    // Access the first shape, which is a text box, and set its text
    Shape shape = ws.GetShapes().Get(0);
    shape.SetText(u"Sign up for your free phone number.\nCall and text online for free.");

    // Access the first paragraph
    TextParagraph p = shape.GetTextBody().GetTextParagraphs().Get(1);

    // Set the line spacing
    p.SetLineSpaceSizeType(LineSpaceSizeType::Points);
    p.SetLineSpace(20);

    // Set the space after
    p.SetSpaceAfterSizeType(LineSpaceSizeType::Points);
    p.SetSpaceAfter(10);

    // Set the space before
    p.SetSpaceBeforeSizeType(LineSpaceSizeType::Points);
    p.SetSpaceBefore(10);

    // Save the workbook in xlsx format
    wb.Save(outDir + u"output_out.xlsx", SaveFormat::Xlsx);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```  
{{< app/cells/assistant language="cpp" >}}
