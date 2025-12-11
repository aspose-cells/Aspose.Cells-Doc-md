---  
title: Setting Shadow of Text Effects of Shape or TextBox with C++  
linktitle: Setting Shadow of Text Effects  
type: docs  
weight: 250  
url: /cpp/setting-shadow-of-text-effects-of-shape-or-textbox/  
description: Learn how to set the shadow of text effects for shapes or textboxes using Aspose.Cells for C++.  
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

{{% alert color="primary" %}}

You can set the **Shadow** of **Text Effects** of any Shape or TextBox. Please use the [**Shape.GetTextBody()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettextbody/) property. It represents the settings of the shape's text and returns [**FontSetting**](https://reference.aspose.com/cells/cpp/aspose.cells/fontsetting/) objects. After accessing it, please set the **Shadow** via the [**FontSetting.GetPresetType()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/getpresettype/) property. This property is of the type [**PresetShadowType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/presetshadowtype/) which has several values. Some of these are:

- OffsetDiagonalBottomRight  
- OffsetBottom  
- OffsetDiagonalTopRight  
- InsideLeft  
- InsideCenter  
- PerspectiveDiagonalUpperLeft  
- PerspectiveDiagonalLowerRight  

{{% /alert %}}

The following code snippet demonstrates the use of [**FontSetting.GetPresetType()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shadoweffect/getpresettype/) property to set the shadow of text effects of a Shape or TextBox.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Output directory
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook object
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Add text box with these dimensions
    TextBox tb = ws.GetShapes().AddTextBox(2, 0, 2, 0, 100, 400);

    // Set the text of the textbox
    tb.SetText(u"This text has the following settings.\n\nText Effects > Shadow > Offset Bottom");

    // Set the shadow of all text runs to preset offset bottom
    for (int i = 0; i < tb.GetTextBody().GetCount(); i++)
    {
        tb.GetTextBody().Get(i).GetTextOptions().GetShadow().SetPresetType(PresetShadowType::OffsetBottom);
    }

    // Set the font color and size of the textbox
    tb.GetFont().SetColor(Color::Red());
    tb.GetFont().SetSize(16);

    // Save the output file
    wb.Save(outDir + u"outputSettingTextEffectsShadowOfShapeOrTextbox.xlsx", SaveFormat::Xlsx);

    std::cout << "Text effects shadow of shape or textbox set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
