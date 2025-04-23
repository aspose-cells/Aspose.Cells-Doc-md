---
title: تحويل ورقة العمل إلى صورة  إزالة المسافات الفارغة حول البيانات باستخدام C++
linktitle: تحويل ورقة العمل إلى صورة  إزالة المسافات الفارغة حول البيانات
type: docs
weight: 40
url: /ar/cpp/convert-worksheet-to-image-remove-whitespace-around-data/
description: تعلّم كيفية تحويل ورقة العمل إلى صورة وإزالة المساحات حول البيانات باستخدام Aspose.Cells for C++.
---

{{% alert color="primary" %}}

أحيانًا، قد تحتاج إلى عرض صور ورق العمل في التطبيقات أو صفحات الويب. على سبيل المثال، قد تحتاج إلى إدراج صور في مستند Word، ملف PDF، عرض PowerPoint، أو مستند آخر. بشكل أساسي، ترغب في عرض ورقة العمل كصورة بحيث يمكن لصقها في تطبيقات أخرى. تُسمح لك Aspose.Cells بتحويل جداول بيانات Microsoft Excel إلى صور.

{{% /alert %}}

## **إزالة الفراغات حول البيانات**

[**SheetRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/) API يحول ورقة عمل إلى ملف صورة مع أي سمات محددة، على سبيل المثال، تنسيق الصورة، الصفحات المقسمة، وما إلى ذلك. تدعم عدة صيغ للصور، بما في ذلك BMP، GIF، JPG، TIFF، و EMF.

عند استخدام ميزة ورقة العمل إلى صورة، تكون الصورة الناتجة بها مسافات فارغة، أي حدود، حولها بشكل افتراضي. يمكنك إزالتها عن طريق ضبط هوامش إعداد الصفحة العلوية والسفلية واليمنى واليسرى للورقة المصدر إلى 0 وتحديد خصائص [**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/) وفقًا لذلك.

الكود التالي يزيل الفراغات حول البيانات في الصورة الناتجة.

```c++
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

    // Open the template file
    Workbook book(srcDir + u"Book1.xlsx");

    // Get the first worksheet
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Define LoadOptions and set LoadFilter
    LoadOptions options;
    options.SetLoadFilter(new LoadFilter(LoadDataFilterOptions::All));

    // Specify your print area if you want
    // sheet.GetPageSetup().SetPrintArea(u"A1:H8");

    // To remove the white border around the image.
    sheet.GetPageSetup().SetLeftMargin(0);
    sheet.GetPageSetup().SetRightMargin(0);
    sheet.GetPageSetup().SetBottomMargin(0);
    sheet.GetPageSetup().SetTopMargin(0);

    // Define ImageOrPrintOptions
    ImageOrPrintOptions imgOptions;
    imgOptions.SetImageType(Aspose::Cells::Drawing::ImageType::Emf);

    // Set only one page would be rendered for the image
    imgOptions.SetOnePagePerSheet(true);
    imgOptions.SetPrintingPage(PrintingPageType::IgnoreBlank);

    // Create the SheetRender object based on the sheet with its
    // ImageOrPrintOptions attributes
    SheetRender sr(sheet, imgOptions);

    // Convert the image
    sr.ToImage(0, outDir + u"outputRemoveWhitespaceAroundData.emf");

    std::cout << "Image converted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
