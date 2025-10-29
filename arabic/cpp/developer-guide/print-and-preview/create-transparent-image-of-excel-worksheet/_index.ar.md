--- 
title: إنشاء صورة شفافة من ورقة عمل Excel باستخدام C++ 
linktitle: Create Transparent Image of Excel Worksheet 
type: docs 
weight: 170 
url: /ar/cpp/create-transparent-image-of-excel-worksheet/ 
description: إنشاء صور شفافة لورق عمل Excel باستخدام Aspose.Cells مع C++. 
--- 

{{% alert color="primary" %}} 

أحيانًا، تحتاج إلى إنشاء صورة لورقة عملك كصورة شفافة. ترغب في تطبيق الشفافية على جميع الخلايا التي ليس لها ألوان تعبئة. توفر Aspose.Cells خاصية الشفافية لتطبيق الشفافية على صورة الورقة العمل. عندما تكون هذه الخاصية كاذبة، فإن الخلايا التي ليس لها ألوان تعبئة تُرسم بلون أبيض وعندما تكون صحيحة، تُرسم الخلايا التي ليس لها ألوان تعبئة كشفافة. 

{{% /alert %}} 

في صورة ورقة العمل التالية، لم يتم تطبيق الشفافية. الخلايا التي ليس لها ألوان تعبئة تُرسم باللون الأبيض.

|**الإخراج بدون شفافية: خلفية الخلية بيضاء**| 
| :- | 
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_1.png)| 

بينما، في صورة ورقة العمل التالية، تم تطبيق الشفافية. الخلايا التي ليس لها ألوان تعبئة هي شفافة.

|**الإخراج مع تمكين الشفافية**| 
| :- | 
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_2.png)| 

الكود العيني التالي يولِّد صورة شفافة من ورقة عمل Excel.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String sourceDir = u"..\\Data\\01_SourceDirectory\\";

    // Output directory path
    U16String outputDir = u"..\\Data\\02_OutputDirectory\\";

    // Create workbook object from source file
    Workbook workbook(sourceDir + u"sampleCreateTransparentImage.xlsx");

    // Apply different image or print options
    ImageOrPrintOptions imgOption;
    imgOption.SetImageType(static_cast<ImageType>(5)); // Png
    imgOption.SetHorizontalResolution(200);
    imgOption.SetVerticalResolution(200);
    imgOption.SetOnePagePerSheet(true);

    // Apply transparency to the output image
    imgOption.SetTransparent(true);

    // Create image after applying image or print options
    SheetRender sr(workbook.GetWorksheets().Get(0), imgOption);
    sr.ToImage(0, outputDir + u"outputCreateTransparentImage.png");

    std::cout << "Image created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
