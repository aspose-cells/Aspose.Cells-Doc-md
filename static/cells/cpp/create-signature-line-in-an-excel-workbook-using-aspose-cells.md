##Create Signature Line in an Excel Workbook with C++ using Aspose.Cells
This article describes how to Create Signature Line in an Excel Workbook using C++ codes with Aspose.Cells for C++.
## **Introduction**
Microsoft Excel provides a feature to add **Signature Line** in Excel workbooks. You can add a Signature Line by clicking the **Insert** Tab and then selecting **Signature Line** from the **Text** group.
## **How to Create Signature Line for Excel**
Aspose.Cells also provides this feature and has exposed the [**Picture.SignatureLine**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/signatureline/) property for this purpose. This article will explain how to use this property to add a Signature Line using Aspose.Cells.
The following sample code adds a Signature Line using [**Picture.SignatureLine**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/signatureline/) property and saves the workbook.
```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main()
{
Aspose::Cells::Startup();
// Source directory path
U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
// Output directory path
U16String outDir(u"..\\Data\\02_OutputDirectory\\");
// Create workbook object
Workbook workbook;
// Create signature line object
SignatureLine s;
s.SetSigner(u"John Doe");
s.SetTitle(u"Development Lead");
s.SetEmail(u"john.doe@aspose.com");
// Adds a Signature Line to the worksheet.
workbook.GetWorksheets().Get(0).GetShapes().AddSignatureLine(1, 1, s);
// Save the workbook
U16String outputFilePath = outDir + u"output_out.xlsx";
workbook.Save(outputFilePath);
std::cout << "Workbook saved successfully with signature line!" << std::endl;
Aspose::Cells::Cleanup();
}
```
