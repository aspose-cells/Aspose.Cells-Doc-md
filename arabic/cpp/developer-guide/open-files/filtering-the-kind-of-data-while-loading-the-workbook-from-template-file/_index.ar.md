---
title: تصفية نوع البيانات أثناء تحميل دفتر العمل من ملف القالب باستخدام C++
linktitle: تصفية البيانات أثناء تحميل دفتر العمل
type: docs
weight: 400
url: /ar/cpp/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/
description: تعلم كيفية تصفية أنواع البيانات المحددة أثناء تحميل دفتر عمل من ملف قالب باستخدام Aspose.Cells مع C++.
---

{{% alert color="primary" %}}

 أحيانًا، تريد تحديد نوع البيانات الذي يجب تحميله عند إنشاء دفتر العمل من ملف القالب. يمكن أن يؤدي تصفية البيانات المحملة إلى تحسين الأداء لغرضك الخاص، خاصة عند استخدام [واجهة برمجة تطبيقات LightCells](/cells/ar/cpp/using-lightcells-api/). يرجى استخدام الخاصية [**LoadOptions.GetLoadFilter()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getloadfilter/) لهذا الغرض.

{{% /alert %}}

يقوم الكود العيني التالي بتحميل كائنات الشكل فقط أثناء تحميل الدفتر من ملف النموذج الذي يمكنك تحميله من الرابط المتوفر. توضح اللقطة الشاشية التالية محتويات ملف النموذج وتشرح أيضًا أنه لن يتم تحميل البيانات ذات اللون الأحمر والخلفية الصفراء لأن الخاصية [**LoadOptions.GetLoadFilter()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getloadfilter/) تم تعيينها على [**LoadDataFilterOptions.Shape**](https://reference.aspose.com/cells/cpp/aspose.cells/loaddatafilteroptions/).

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)

تُظهر اللقطة الشاشية التالية ال [PDF الناتج](5115555.pdf) الذي يمكنك تحميله من الرابط المقدم. هنا يمكنك أن ترى، البيانات ذات اللون الأحمر والخلفية الصفراء غير موجودة لكن جميع الأشكال موجودة.

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_2.png)

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

    // Set the load options, we only want to load shapes and do not want to load data
    LoadOptions loadOptions(LoadFormat::Xlsx);
    loadOptions.SetLoadFilter(new LoadFilter(LoadDataFilterOptions::All & ~LoadDataFilterOptions::Chart));

    // Create workbook object from sample excel file using load options
    Workbook workbook(srcDir + u"sampleFilterChars.xlsx", loadOptions);

    // Save the output in pdf format
    workbook.Save(outDir + u"sampleFilterChars_out.pdf", SaveFormat::Pdf);

    std::cout << "File saved successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
