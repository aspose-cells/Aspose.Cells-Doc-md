---  
title: Working with the Reflection Effect of Shape or Chart with C++  
linktitle: Working with the Reflection Effect of Shape or Chart  
type: docs  
weight: 210  
url: /cpp/working-with-the-reflection-effect-of-shape-or-chart/  
description: Learn how to work with the reflection effect of shapes or charts using Aspose.Cells with C++.  
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

## **Possible Usage Scenarios**  
Aspose.Cells provides the [Shape.Reflection](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getreflection/) property along with the [ReflectionEffect](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/reflectioneffect/) class to work with the reflection effect of a shape or chart. The [ReflectionEffect](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/reflectioneffect/) class contains the following properties, which can be set to achieve different results according to application requirements.  

- [Blur](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/reflectioneffect/getblur/)  
- [Direction](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/reflectioneffect/getdirection/)  
- [Distance](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/reflectioneffect/getdistance/)  
- [FadeDirection](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/reflectioneffect/getfadedirection/)  
- [RotWithShape](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/reflectioneffect/getrotwithshape/)  
- [Size](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/reflectioneffect/getsize/)  
- [Transparency](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/reflectioneffect/gettransparency/)  
- [Type](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/reflectioneffect/gettype/)  

## **Working with the Reflection Effect of Shape or Chart**  
The following sample code loads the source Excel file, accesses the first shape in the default worksheet, sets various properties of the `Shape.Reflection` class, and then saves the workbook to the output Excel file.  

```cpp
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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"sample.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output_out.xlsx";

    // Load your source Excel file
    Workbook wb(inputFilePath);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first shape
    Shape sh = ws.GetShapes().Get(0);

    // Set the reflection effect of the shape: its Blur, Size, Transparency, and Distance properties
    ReflectionEffect re = sh.GetReflection();
    re.SetBlur(30);
    re.SetSize(90);
    re.SetTransparency(0);
    re.SetDistance(80);

    // Save the workbook in XLSX format
    wb.Save(outputFilePath);

    std::cout << "Reflection effect applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```  
{{< app/cells/assistant language="cpp" >}}
