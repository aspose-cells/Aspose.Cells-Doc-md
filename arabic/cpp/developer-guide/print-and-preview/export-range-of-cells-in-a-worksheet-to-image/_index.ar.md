---
title: تصدير نطاق خلايا في ورقة عمل إلى صورة باستخدام C++
linktitle: تصدير نطاق الخلايا إلى صورة
type: docs
weight: 60
url: /ar/cpp/export-range-of-cells-in-a-worksheet-to-image/
description: تعلم كيفية تصدير نطاق معين من الخلايا في ورقة عمل إلى صورة باستخدام Aspose.Cells مع C++.
---

## **سيناريوهات الاستخدام المحتملة**

يمكنك إنشاء صورة لورقة عمل باستخدام Aspose.Cells. ومع ذلك، في بعض الأحيان، تحتاج إلى تصدير مجموعة من الخلايا فقط في ورقة عمل إلى صورة. تشرح هذه المقالة كيفية تحقيق ذلك.

## **تصدير مجموعة من الخلايا في ورقة عمل إلى صورة**

لالتقاط صورة من مجموعة، قم بتعيين منطقة الطباعة إلى المجال المطلوب ثم قم بتعيين جميع الهوامش إلى 0. كما قم بتعيين [**ImageOrPrintOptions.GetOnePagePerSheet()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getonepagepersheet/) إلى **صحيح**. يأخذ الكود التالي صورة للمدى D8:G16. أدناه، صورة لل[ملف الإكسل عينة](47153160.xlsx) المستخدم في الكود. يمكنك تجربة الكود مع أي ملف إكسل.

## **صورة للملف الإكسل العيني وصورته المصدرية**

**![todo:image_alt_text](export-range-of-cells-in-a-worksheet-to-image_1.png)**

تنفيذ الكود ينشئ صورة للمدى D8:G16 فقط.

**![todo:image_alt_text](Output-Image.png)**

## **الكود المثالي**

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

    // Create workbook from source file
    Workbook workbook(srcDir + u"sampleExportRangeOfCellsInWorksheetToImage.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set the print area with the desired range
    worksheet.GetPageSetup().SetPrintArea(u"D8:G16");

    // Set all margins to 0
    worksheet.GetPageSetup().SetLeftMargin(0);
    worksheet.GetPageSetup().SetRightMargin(0);
    worksheet.GetPageSetup().SetTopMargin(0);
    worksheet.GetPageSetup().SetBottomMargin(0);

    // Set OnePagePerSheet option as true
    ImageOrPrintOptions options;
    options.SetOnePagePerSheet(true);
    options.SetImageType(Aspose::Cells::Drawing::ImageType::Jpeg);
    options.SetHorizontalResolution(200);
    options.SetVerticalResolution(200);

    // Take the image of the worksheet
    SheetRender sr(worksheet, options);
    sr.ToImage(0, outDir + u"outputExportRangeOfCellsInWorksheetToImage.jpg");

    std::cout << "Worksheet image exported successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
