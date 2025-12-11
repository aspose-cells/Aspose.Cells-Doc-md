---  
title: Create a TextBox in which each line has a different Horizontal Alignment with C++  
linktitle: Create TextBox with Different Horizontal Alignment  
type: docs  
weight: 310  
url: /cpp/create-textbox-in-which-each-line-is-having-different-horizontal-alignment/  
description: Learn how to create a TextBox with different horizontal alignment for each line using Aspose.Cells with C++.  
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

{{% alert color="primary" %}}  

You can set the horizontal alignment of your paragraph text using the [**TextParagraph.GetAlignmentType()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/textparagraph/getalignmenttype/) property.  

{{% /alert %}}  

The following sample code creates three lines and sets the horizontal alignment of each of them.  

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a workbook
    Workbook wb;

    // Access the first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Add a text box inside the sheet
    ws.GetShapes().AddTextBox(2, 0, 2, 0, 80, 400);

    // Access the first shape, which is a text box, and set its text
    Shape shape = ws.GetShapes().Get(0);
    shape.SetText(u"Sign up for your free phone number.\nCall and text online for free.\nCall your friends and family.");

    // Access the first paragraph and set its horizontal alignment to left
    TextParagraph p = shape.GetTextBody().GetTextParagraphs().Get(0);
    p.SetAlignmentType(TextAlignmentType::Left);

    // Access the second paragraph and set its horizontal alignment to center
    p = shape.GetTextBody().GetTextParagraphs().Get(1);
    p.SetAlignmentType(TextAlignmentType::Center);

    // Access the third paragraph and set its horizontal alignment to right
    p = shape.GetTextBody().GetTextParagraphs().Get(2);
    p.SetAlignmentType(TextAlignmentType::Right);

    // Save the workbook in XLSX format
    wb.Save(outDir + u"output_out.xlsx", SaveFormat::Xlsx);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```  
{{< app/cells/assistant language="cpp" >}}
