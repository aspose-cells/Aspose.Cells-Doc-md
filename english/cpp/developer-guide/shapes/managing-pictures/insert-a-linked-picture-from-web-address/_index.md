---
title: Insert a Linked Picture from Web Address with C++
linktitle: Insert a Linked Picture from Web Address
type: docs
weight: 450
url: /cpp/insert-a-linked-picture-from-web-address/
description: Learn how to insert a linked picture from a web address into a worksheet using Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Sometimes you need to insert a picture from the web (http://) into a worksheet. To do so, specify the picture’s URL and the picture will be downloaded every time the spreadsheet is opened in Microsoft Excel. The image is not physically embedded into the Excel document, but points to a web resource.

{{% /alert %}}

## **Using Microsoft Excel**

In Microsoft Excel (for example 2007):

1. Click the **Insert** menu and select **Picture**.
1. Specify the web address for the picture in the Insert Picture dialog.

## **Using Aspose.Cells for C++**

Aspose.Cells for C++ supports adding a linked image using the [**ShapeCollection::AddLinkedPicture(int upperLeftRow, int upperLeftColumn, int heightPixels, int widthPixels, System::String sourceFullName)**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addlinkedpicture/) method. The method returns a [**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/) object.

The following example shows how to add a linked picture from a web address to a worksheet.

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

    // Instantiate a new Workbook
    Workbook workbook;

    // Insert a linked picture (from Web Address) to B2 Cell
    U16String imageUrl(u"http://www.aspose.com/Images/aspose-logo.jpg");
    Picture pic = workbook.GetWorksheets().Get(0).GetShapes().AddLinkedPicture(1, 1, 100, 100, imageUrl);

    // Set the height and width of the inserted image
    pic.SetHeightInch(1.04);
    pic.SetWidthInch(2.6);

    // Save the Excel file
    U16String outputPath = outDir + u"outLinkedPicture.out.xlsx";
    workbook.Save(outputPath);

    std::cout << "Linked picture inserted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```