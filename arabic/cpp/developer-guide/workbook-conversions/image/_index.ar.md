---
title: تحويل إكسل إلى صورة باستخدام C++
linktitle: تحويل ملف إكسل إلى صورة
type: docs
weight: 300
url: /ar/cpp/convert-excel-to-image/
description: تعرّف على كيفية تحويل أوراق عمل إكسل إلى صور، بما في ذلك تنسيقات TIFF و SVG، باستخدام Aspose.Cells for C++.
---

{{% alert color="primary" %}}

تتيح Aspose.Cells لك تصدير ورقة عمل من دفتر عمل وتحويلها إلى تنسيقات مختلفة. يشرح هذا المقال كيفية تحويل ورقة عمل إلى تنسيقات مختلفة.

{{% /alert %}}

## تحويل دفتر العمل إلى TIFF

قد يحتوي ملف إكسل على عدة أوراق مع صفحات متعددة. يسمح [**WorkbookRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookrender/) لك بتحويل إكسل إلى TIFF بعدة صفحات. كما يمكنك التحكم في خيارات متعددة لـ TIFF، مثل [الضغط](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/tiffcompression/)، [GetTiffColorDepth()](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/gettiffcolordepth/)، الدقة ([GetHorizontalResolution()](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/gethorizontalresolution/)، [GetVerticalResolution()](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getverticalresolution/)).

يوضح مقتطف الكود التالي كيفية تحويل Excel إلى TIFF مع عدة صفحات. المرفقات تشمل [ملف الإكسل المصدر](workbook-to-tiff-with-mulitiple-pages.xlsx) و [صورة TIFF المولدة](workbook-to-tiff-with-mulitiple-pages.tiff) للرجوع اليها.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main() {
    Aspose::Cells::Startup();

    // Load the workbook
    Workbook wb(u"workbook-to-tiff-with-mulitiple-pages.xlsx");

    // Create image options
    ImageOrPrintOptions imgOptions;
    imgOptions.SetImageType(ImageType::Tiff);

    // Set resolution to 200 DPI
    imgOptions.SetHorizontalResolution(200);
    imgOptions.SetVerticalResolution(200);

    // Set TIFF compression to LZW
    imgOptions.SetTiffCompression(TiffCompression::CompressionLZW);

    // Render the workbook to TIFF
    WorkbookRender workbookRender(wb, imgOptions);
    workbookRender.ToImage(u"workbook-to-tiff-with-mulitiple-pages.tiff");

    std::cout << "Workbook rendered to TIFF successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **تحويل ورقة عمل إلى صورة**

تحتوي الأوراق العمل على البيانات التي ترغب في تحليلها. على سبيل المثال، يمكن أن تحتوي ورقة العمل على معلمات وإجماليات ونسب واستثناءات وحسابات.

كمطور، قد تحتاج إلى عرض الأوراق العمل كصور. على سبيل المثال، قد تحتاج إلى استخدام صورة لورقة عمل في تطبيق أو صفحة ويب. قد ترغب في إدراج صورة في مستند Microsoft Word أو ملف PDF أو عرض PowerPoint أو نوع مستند آخر. ببساطة، ترغب في عرض ورقة عمل كصورة حتى تتمكن من استخدامها في مكان آخر.

يدعم Aspose.Cells تحويل أوراق عمل إكسل إلى صور. لاستخدام هذه الميزة، تحتاج إلى استيراد مساحة الاسم [**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/) إلى برنامجك أو مشروعك. يوجد العديد من الفئات القيمة للرسم والطباعة، على سبيل المثال [**SheetRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/)، [**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/)، [**WorkbookRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookrender/)، وغيرها.

تمثل فئة [**SheetRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/) ورقة عمل يمكن تصييرها كصور. لديها طريقة محملة، [**ToImage**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/toimage/)، التي يمكنها تحويل ورقة العمل إلى ملف أو ملفات صورة مع سمات أو خيارات مختلفة. تعيد كائن `System.Drawing.Bitmap` ويمكنك حفظ ملف صورة على القرص أو التدفق. يدعم عدة تنسيقات صور، على سبيل المثال BMP، PNG، GIF، JPG، JPEG، TIFF، EMF.

يوضح مقتطف الكود التالي كيفية تحويل ورقة عمل في ملف Excel إلى ملف صورة.

```cpp
#include <iostream>
#include <string>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook book(srcDir + u"sampleConvertWorksheetToImageByPage.xlsx");
    Worksheet sheet = book.GetWorksheets().Get(0);

    ImageOrPrintOptions options;
    options.SetHorizontalResolution(200);
    options.SetVerticalResolution(200);
    options.SetImageType(ImageType::Tiff);

    SheetRender sr(sheet, options);
    for (int j = 0; j < sr.GetPageCount(); j++)
    {
        std::wstring numStr = std::to_wstring(j + 1);
        U16String numU16Str(reinterpret_cast<const char16_t*>(numStr.c_str()));
        U16String outputPath = outDir + U16String(u"outputConvertWorksheetToImageByPage_") + numU16Str + U16String(u".tif");
        sr.ToImage(j, outputPath);
    }

    std::cout << "Worksheet converted to images by page successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

حاليًا، لا يدعم الواجهة البرمجية لتحويل ورقة عمل إلى صور دعم مخططات الفقاعات ثلاثية الأبعاد.

{{% /alert %}}

## **تحويل ورقة عمل إلى SVG**

تعني SVG Scalable Vector Graphics. SVG هو مواصفة تعتمد على معايير XML للرسومات الناقلة ثنائية الأبعاد. إنها معيار مفتوح تحت تطوير من قبل الجمعية العالمية للويب (W3C) منذ عام 1999.

تمكن Aspose.Cells for C++ من تحويل أوراق العمل إلى صورة SVG منذ النسخة 7.1.0. يُظهر مقتطف الكود التالي كيفية تحويل ورقة عمل في ملف إكسل إلى ملف صورة SVG.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Output directory
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a workbook
    Workbook workbook;

    // Put sample text in the first cell of first worksheet in the newly created workbook
    workbook.GetWorksheets().Get(0).GetCells().Get(u"A1").SetValue(u"DEMO TEXT ON SHEET1");

    // Add second worksheet in the workbook
    workbook.GetWorksheets().Add(SheetType::Worksheet);

    // Set text in first cell of the second sheet
    workbook.GetWorksheets().Get(1).GetCells().Get(u"A1").SetValue(u"DEMO TEXT ON SHEET2");

    // Set currently active sheet index to 1 i.e. Sheet2
    workbook.GetWorksheets().SetActiveSheetIndex(1);

    // Save workbook to SVG. It shall render the active sheet only to SVG
    workbook.Save(outDir + u"ConvertWorksheetToSVG_out.svg");

    std::cout << "Worksheet converted to SVG successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **مواضيع متقدمة**
- [تحويل مخطط Excel إلى صورة](/cells/ar/cpp/convert-an-excel-chart-to-image/)
- [تحويل مخطط إلى صورة بتنسيق SVG](/cells/ar/cpp/converting-chart-to-image-in-svg-format/)
- [تصدير مخطط إلى SVG باستخدام سمة viewBox](/cells/ar/cpp/export-chart-to-svg-with-viewbox-attribute/)
- [تتبع تقدّم تحويل Excel إلى TIFF](/cells/ar/cpp/track-conversion-progress-of-excel-to-tiff/)
{{< app/cells/assistant language="cpp" >}}
