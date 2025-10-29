---
title: تحويل ورقة العمل إلى صورة باستخدام خيارات الصورة أو الطباعة مع C++
linktitle: تحويل ورقة العمل إلى صورة
type: docs
weight: 90
url: /ar/cpp/converting-worksheet-to-image-using-imageorprint-options/
description: تعلم كيفية تحويل ورقة عمل إلى ملف صورة وتطبيق خيارات مختلفة للصورة والطباعة باستخدام Aspose.Cells مع C++.
---

{{% alert color="primary" %}}

تم تصميم هذا الوثيقة لتوفير فهم تفصيلي لكيفية تحويل ورقة العمل إلى ملف صورة وتطبيق خيارات مختلفة للصورة والطباعة للصور، مثل الدقة، وضغط TIFF، وتنسيق الصورة، وجودة الصفحة.

{{% /alert %}}

## **حفظ الأوراق العمل إلى صور - نهج مختلفة**

أحيانًا، قد يتطلب الأمر تقديم أوراق العمل الخاصة بك كمجموعة تصويرية. قد تحتاج إلى عرض صور أوراق العمل في تطبيقاتك أو صفحات الويب الخاصة بك، إدراجها في مستند Word، ملف PDF، عرض PowerPoint، أو استخدامها في سيناريو آخر. ببساطة، تريد ورقة عمل تُعرض كصورة لاستخدامها في مكان آخر. يدعم Aspose.Cells تحويل أوراق العمل في ملفات Excel إلى صور. بالإضافة إلى ذلك، يدعم Aspose.Cells تحديد خيارات مختلفة مثل تنسيق الصورة، الدقة (عموديًا وأفقيًا)، جودة الصورة، وخيارات الصورة والطباعة الأخرى.

قد تفكر في أتمتة Office، لكنها لها عيوبها. هناك العديد من الأسباب والمشكلات، مثل الأمان، الاستقرار، القابلية للتوسع، السرعة، السعر، والميزات. باختصار، هناك العديد من الأسباب، وأهمها أن شركة مايكروسوفت نفسها توصي بقوة بعدم اعتماد الأتمتة من خلال الحلول البرمجية.

توضح هذه المقالة كيفية إنشاء تطبيق سطري في Visual Studio، أداء تحويل ورقة العمل إلى صورة باستخدام خيارات مختلفة للصورة والطباعة مع بعض وأسهل الأسطر من الشفرة باستخدام API Aspose.Cells.

تحتاج إلى تضمين مساحة الاسم [**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/) في برنامجك/مشروعك. تحتوي على العديد من الفئات القيمة، على سبيل المثال، [**SheetRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/)، [**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/)، [**WorkbookRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookrender/)، وغيرها.

تمثل فئة [**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/) ورقة العمل التي تُستخدم لإنشاء صور لورقة العمل. لديها طريقة [**ToImage**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/toimage/) محمّلة بشكل زائد والتي يمكنها تحويل ورقة العمل مباشرة إلى ملف (ملفات) صورة حسب السمات أو الخيارات التي تحددها. يمكنها إرجاع كائن صورة bitmap، ويمكنك حفظ ملف صورة على القرص/السريان. تدعم عدة تنسيقات صور، مثل BMP، PNG، GIF، JPEG، TIFF، EMF، وغيرها.

## **استخدام Aspose.Cells لتحويل ورقة العمل إلى صورة باستخدام خيارات ImageOrPrint**

### **إنشاء دفتر عمل قالب في Microsoft Excel**

قمت بإنشاء دفتر عمل جديد في MS Excel وأضفت بعض البيانات في الورقة الأولى. الآن، سأقوم بتحويل ورقة عمل القالب “Sheet1” إلى ملف صورة “SheetImage.tiff” وسأطبق خيارات صورة مختلفة مثل الدقة الأفقية والرأسية، ضغط TIFF، وغيرها.

### **تنزيل وتثبيت Aspose.Cells**

أولاً، تحتاج إلى [تحميل](https://downloads.aspose.com/cells/cpp) Aspose.Cells for C++. تثبيته على حاسوب التطوير الخاص بك. جميع مكونات [Aspose](http://www.aspose.com/)، عند تثبيتها، تعمل في وضع التقييم. وضع التقييم لا يحده وقت وي Inject فقط علامات مائية في المستندات المنتجة.

### **إنشاء مشروع**

ابدأ Visual Studio وأنشئ تطبيق وحدة تحكم جديد. سيُظهر هذا المثال تطبيق وحدة تحكم بلغة C++.

### **إضافة الإشارات**

سيستخدم هذا المشروع Aspose.Cells. لذا، يجب أن تضيف مرجعًا إلى مكون Aspose.Cells في مشروعك. على سبيل المثال، أضف مرجعًا إلى `...\Program Files\Aspose\Aspose.Cells for C++\Bin\Aspose.Cells.lib`.

### **تحويل ورقة العمل إلى ملف صورة**

```c++
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

    Workbook book(srcDir + u"sampleWorksheetToAnImage.xlsx");

    Worksheet sheet = book.GetWorksheets().Get(0);

    ImageOrPrintOptions options;
    options.SetHorizontalResolution(300);
    options.SetVerticalResolution(300);
    options.SetTiffCompression(TiffCompression::CompressionLZW);
    options.SetImageType(ImageType::Tiff);
    options.SetPrintingPage(PrintingPageType::Default);

    SheetRender sr(sheet, options);

    int pageIndex = 3;
    int pageNumber = pageIndex + 1;
    std::wstring pageStr = std::to_wstring(pageNumber);
    U16String pageNumberStr(reinterpret_cast<const char16_t*>(pageStr.c_str()));
    U16String outputPath = outDir + U16String(u"outputWorksheetToAnImage_") + pageNumberStr + U16String(u".tiff");
    sr.ToImage(pageIndex, outputPath);

    std::cout << "Worksheet converted to image successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **خيارات التحويل**

من الممكن حفظ صفحات معينة إلى صورة. الكود التالي يحول الورقتين الأولى والثانية في دفتر العمل إلى صور JPG.

```c++
#include <iostream>
#include <fstream>
#include <sstream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    U16String inputPath = srcDir + u"sampleSpecificPagesToImages.xlsx";
    Workbook workbook(inputPath);

    WorksheetCollection worksheets = workbook.GetWorksheets();
    Worksheet worksheet = worksheets.Get(0);

    ImageOrPrintOptions imgOptions;
    imgOptions.SetImageType(Aspose::Cells::Drawing::ImageType::Jpeg);

    SheetRender sr(worksheet, imgOptions);

    int32_t pageIndex = 3;

    Vector<uint8_t> imageData = sr.ToImage(pageIndex);

    std::wstringstream ws;
    ws << (pageIndex + 1);
    U16String pageNumStr(reinterpret_cast<const char16_t*>(ws.str().c_str()));

    U16String outputPath = outDir + u"outputSpecificPagesToImage_" + pageNumStr + u".jpg";
    std::ofstream outputFile(outputPath.ToUtf8(), std::ios::binary);
    outputFile.write(reinterpret_cast<const char*>(imageData.GetData()), imageData.GetLength());
    outputFile.close();

    std::cout << "Page rendered successfully to: " << outputPath.ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **تحويل الصورة باستخدام WorkbookRender**

يمكن أن تحتوي صورة TIFF على أكثر من إطار واحد. يمكنك حفظ دفتر العمل بأكمله إلى صورة TIFF واحدة متعددة الإطارات أو الصفحات:

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

    // Load the workbook
    Workbook wb(srcDir + u"sampleUseWorkbookRenderForImageConversion.xlsx");

    // Set image options
    ImageOrPrintOptions opts;
    opts.SetImageType(ImageType::Tiff);

    // Render workbook to image
    WorkbookRender wr(wb, opts);
    wr.ToImage(outDir + u"outputUseWorkbookRenderForImageConversion.tiff");

    std::cout << "Workbook rendered to image successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
