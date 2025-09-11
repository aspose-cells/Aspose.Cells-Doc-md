---
title: Managing Pictures with C++
linktitle: Managing Pictures
type: docs
weight: 10
url: /cpp/managing-pictures/
description: Add, position, and manage images in spreadsheets using Aspose.Cells for C++ API.
---

Aspose.Cells allows developers to add pictures to spreadsheets at runtime. Moreover, the positioning of these pictures can be controlled at runtime, which is discussed in more detail in the coming sections.

This article explains how to add pictures, and how to insert an image that shows the content of certain cells.

## **Adding Pictures**

Adding pictures to a spreadsheet is very easy. It only takes a few lines of code:
Simply call the [**Add**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picturecollection/add/) method of the [**PictureCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picturecollection/) (encapsulated in the [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) object). The [**Add**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picturecollection/add/) method takes the following parameters:

- **Upper left row index**, the index of the upper left row.
- **Upper left column index**, the index of the upper left column.
- **Image file name**, the name of the image file, complete with path.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directories
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create new workbook
    Workbook workbook;

    // Add worksheet and get reference
    int sheetIndex = workbook.GetWorksheets().Add();
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Add image to worksheet at F6 (row 5, column 5)
    U16String imagePath = srcDir + u"logo.jpg";
    worksheet.GetPictures().Add(5, 5, imagePath);

    // Save workbook
    U16String outputPath = outDir + u"output.xls";
    workbook.Save(outputPath);

    std::cout << "Worksheet with image created successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Positioning Pictures**

There are two possible ways to control the positioning of pictures using Aspose.Cells:

- Proportional positioning: define a position proportional to the row height and width.
- Absolute positioning: define the exact position on the page where the image will be inserted, for example, 40 pixels to the left and 20 pixels below the edge of the cell.

### **Proportional Positioning**

Developers can position the pictures proportional to row height and column width using the [**UpperDeltaX**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getupperdeltax/) and [**UpperDeltaY**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getupperdeltay/) properties of the [**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/) object. A [**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/) object can be obtained from the [**PictureCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picturecollection/) by passing its picture index. This example places an image in the F6 cell.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook object
    Workbook workbook;

    // Add new worksheet and get reference
    int sheetIndex = workbook.GetWorksheets().Add();
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Add picture to worksheet at (5,5) position
    U16String imagePath = outDir + u"logo.jpg";
    int pictureIndex = worksheet.GetPictures().Add(5, 5, imagePath);

    // Access added picture and set positioning
    Drawing::Picture picture = worksheet.GetPictures().Get(pictureIndex);
    picture.SetUpperDeltaX(200);
    picture.SetUpperDeltaY(200);

    // Save modified workbook
    U16String outputPath = outDir + u"book1.out.xls";
    workbook.Save(outputPath);

    std::cout << "Picture added and positioned successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Absolute Positioning**

Developers can also position the pictures absolutely by using the [**Left**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getleft/) and [**Top**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettop/) properties of the [**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/) object. This example places an image in cell F6, 60 pixels from the left and 10 pixels from the top of the cell.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directories
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create new workbook
    Workbook workbook;
    
    // Access worksheet collection and add new sheet
    WorksheetCollection worksheets = workbook.GetWorksheets();
    int sheetIndex = worksheets.Add();
    
    // Get reference to newly added worksheet
    Worksheet worksheet = worksheets.Get(sheetIndex);
    
    // Add picture to worksheet at row 5, column 5 (cell F6)
    PictureCollection pictures = worksheet.GetPictures();
    int pictureIndex = pictures.Add(5, 5, srcDir + u"logo.jpg");
    
    // Access added picture and set position
    Picture picture = pictures.Get(pictureIndex);
    picture.SetLeft(60);
    picture.SetTop(10);
    
    // Save modified workbook
    workbook.Save(outDir + u"book1.out.xls");
    
    std::cout << "Workbook with inserted picture saved successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Inserting a Picture Based on Cell Reference**

Aspose.Cells lets you display the contents of a worksheet cell in an image shape. You can link the picture to the cell that contains the data that you want to display. Since the cell, or cell range, is linked to the graphic object, changes that you make to the data in that cell or cell range automatically appear in the graphic object.

Add a picture to the worksheet by calling the [**AddPicture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addpicture/) method of the [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) (encapsulated in the [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) object). Specify the cell range by using the [**GetFormula**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/getformula/) attribute of the [**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/) object.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directories
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create new workbook
    Workbook workbook;

    // Access first worksheet and cells collection
    WorksheetCollection worksheets = workbook.GetWorksheets();
    Worksheet worksheet = worksheets.Get(0);
    Cells cells = worksheet.GetCells();

    // Set cell values
    cells.Get(u"A1").PutValue(U16String(u"A1"));
    cells.Get(u"C10").PutValue(U16String(u"C10"));

    // Add picture to worksheet
    auto shapes = worksheet.GetShapes();
    Picture pic = shapes.AddPicture(0, 3, 10, 6, Vector<uint8_t>());

    // Set picture formula and update values
    pic.SetFormula(u"A1:C10");
    shapes.UpdateSelectedValue();

    // Save workbook
    U16String outputPath = outDir + u"output.out.xls";
    workbook.Save(outputPath);

    std::cout << "File saved successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Advance topics**
- [Add Conditional Icons Set with the Cell Text](/cells/cpp/add-conditional-icons-set-with-the-cell-text/)
- [Insert a Linked Picture from Web Address](/cells/cpp/insert-a-linked-picture-from-web-address/)
- [Insert a Picture Based on Cell Reference](/cells/cpp/insert-a-picture-based-on-cell-reference/)
- [Load a Web Image from a URL into an Excel Worksheet](/cells/cpp/load-a-web-image-from-a-url-into-an-excel-worksheet/)
{{< app/cells/assistant language="cpp" >}}