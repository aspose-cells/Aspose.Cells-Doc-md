---
title: إضافة روابط الصور باستخدام C++
linktitle: إضافة روابط فائقة النص للصور
type: docs
weight: 140
url: /ar/cpp/add-image-hyperlinks/
description: تعلم كيفية إضافة روابط الصور من خلال API Aspose.Cells for C++.
keywords: إضافة روابط تشعبية للصور, إدراج روابط تشعبية للصور
---

{{% alert color="primary" %}} 

الروابط التشعبية مفيدة للوصول إلى المعلومات في جداول البيانات الأخرى، أو على مواقع الويب. يتيح للمستخدمين برنامج مايكروسوفت إكسل إضافة روابط تشعبية على النص في الخلايا، وعلى الصور. يمكن أن تجعل الروابط التشعبية للصور التنقل في ورقة البيانات أسهل، على سبيل المثال، كأزرار التالي والسابق، أو الشعارات التي تقوم بربطها بمواقع معينة. يشرح هذا المستند كيفية إدراج روابط تشعبية للصور في ورقة البيانات باستخدام Aspose.Cells.

{{% /alert %}} 

Aspose.Cells تسمح لك بإضافة روابط تشعبية للصور في جداول البيانات أثناء التشغيل. من الممكن تعيين وتعديل تلميح الشاشة والعنوان للرابط. يوضح الكود النموذجي التالي كيفية إضافة رابط تشعبي لصورة في ورقة البيانات.

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

    // Instantiate a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Insert a string value to a cell
    worksheet.GetCells().Get(u"C2").PutValue(u"Image Hyperlink");

    // Set the 4th row height
    worksheet.GetCells().SetRowHeight(3, 100);

    // Set the C column width
    worksheet.GetCells().SetColumnWidth(2, 21);

    // Add a picture to the C4 cell
    int index = worksheet.GetPictures().Add(3, 2, 4, 3, srcDir + u"aspose-logo.jpg");

    // Get the picture object
    Picture pic = worksheet.GetPictures().Get(index);

    // Set the placement type
    pic.SetPlacement(PlacementType::FreeFloating);

    // Add an image hyperlink
    Hyperlink hlink = pic.AddHyperlink(u"http://www.aspose.com/");

    // Specify the screen tip
    hlink.SetScreenTip(u"Click to go to Aspose site");

    // Save the Excel file
    workbook.Save(outDir + u"ImageHyperlink_out.xls");

    std::cout << "Image hyperlink added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
