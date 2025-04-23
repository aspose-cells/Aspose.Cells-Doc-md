---
title: إدراج صورة مربوطة من عنوان ويب باستخدام C++
linktitle: إدراج صورة ربط من عنوان الويب
type: docs
weight: 450
url: /ar/cpp/insert-a-linked-picture-from-web-address/
description: تعلم كيفية إدراج صورة مربوطة من عنوان ويب في ورقة عمل باستخدام Aspose.Cells for C++.
---

{{% alert color="primary" %}}

في بعض الأحيان قد تحتاج إلى إدراج صورة من الويب (http://) في ورقة عمل. للقيام بذلك، حدد عنوان URL للصورة وستتم تنزيل الصورة في كل مرة يتم فيها فتح جدول البيانات في Microsoft Excel. لا تُضاف الصورة بشكل مادي إلى مستند Excel، وإنما تشير إلى مورد ويب.

{{% /alert %}}

## **استخدام Microsoft Excel**

في Microsoft Excel (على سبيل المثال 2007):

1. انقر فوق قائمة **إدراج** وحدد **صورة**.
1. حدد عنوان الويب للصورة في مربع حوار إدراج صورة.

## **باستخدام Aspose.Cells for C++**

يدعم Aspose.Cells for C++ إضافة صورة مربوطة باستخدام طريقة [**ShapeCollection::AddLinkedPicture(int upperLeftRow, int upperLeftColumn, int heightPixels, int widthPixels, System::String sourceFullName)**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addlinkedpicture/). تعيد الطريقة كائن [**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/).

يظهر المثال التالي كيفية إضافة صورة مرتبطة من عنوان ويب إلى ورقة عمل.

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
