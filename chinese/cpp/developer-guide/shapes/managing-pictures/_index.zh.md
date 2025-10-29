---
title: 用C++管理图片
linktitle: 管理图片
type: docs
weight: 10
url: /zh/cpp/managing-pictures/
description: 使用 Aspose.Cells for C++ API 添加、定位和管理电子表格中的图像。
---

Aspose.Cells允许开发人员在运行时向电子表格添加图片。此外，可以在运行时控制这些图片的定位，更多细节将在接下来的章节中讨论。

本文章介绍了如何添加图片，以及如何插入显示特定单元格内容的图片。

## **添加图片**

向电子表格中添加图片非常简单。只需几行代码：
只需调用 [**Add**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picturecollection/add/) 方法（封装在 [**PictureCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picturecollection/) 对象中）的 [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) 方法。[**Add**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picturecollection/add/) 方法接受以下参数：

- **左上角行索引**，左上角行的索引。
- **左上角列索引**，左上角列的索引。
- **图像文件名**，图像文件的名称，包括完整路径。

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

## **定位图片**

使用Aspose.Cells控制图片定位有两种可能的方法：

- 比例定位：定义相对于行高和列宽的位置。
- 绝对定位：定义图像插入页面的确切位置，例如距离单元格边缘左侧40像素，下面20像素。

### **比例定位**

开发者可以使用 [**UpperDeltaX**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getupperdeltax/) 和 [**UpperDeltaY**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getupperdeltay/) 属性（来自 [**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/) 对象）按比例定位图片。可以通过传递其图片索引，从 [**PictureCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picturecollection/) 获取 [**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/) 对象。此示例在F6单元格放置一张图片。

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

### **绝对定位**

开发人员还可以使用[**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/)对象的[**Left**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getleft/)和[**Top**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettop/)属性绝对定位图片。此示例将图像放置在F6单元格中，离左侧60像素，离顶部10像素。

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

## **基于单元格引用插入图片**

Aspose.Cells允许您在图像形状中显示工作表单元格的内容。您可以将图片链接到包含您要显示数据的单元格。由于单元格或单元格范围与图形对象链接，因此您对该单元格或单元格范围中的数据所做的更改将自动显示在图形对象中。

通过调用 [**AddPicture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addpicture/) 方法（封装在 [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) 对象中）向工作表添加图片。使用 [**GetFormula**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/getformula/) 属性指定单元格范围。

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

## **高级主题**
- [使用单元格文本添加条件图标集](/cells/zh/cpp/add-conditional-icons-set-with-the-cell-text/)
- [从网址插入链接图片](/cells/zh/cpp/insert-a-linked-picture-from-web-address/)
- [基于单元格引用插入图片](/cells/zh/cpp/insert-a-picture-based-on-cell-reference/)
- [从URL中加载Web图像到Excel工作表](/cells/zh/cpp/load-a-web-image-from-a-url-into-an-excel-worksheet/)
{{< app/cells/assistant language="cpp" >}}
