---
title: ضبط مستوى ضغط ملف العمل باستخدام C++
linktitle: ضبط مستوى ضغط ملف العمل
type: docs
weight: 180
url: /ar/cpp/adjust-workbook-compression-level/
description: تعلم كيفية ضبط مستوى ضغط ملف العمل باستخدام Aspose.Cells for C++ لتحسين حجم الملف ووقت المعالجة.
---

## **ضبط مستوى ضغط الورقة العمل**

يمكن للمطورين تعديل مستوى الضغط لسجل العمل عند العمل مع سجلات عمل أكبر حجمًا. قد يضع المطورون حجم الملفات الأصغر أولويةً على وقت المعالجة أو العكس. توفر Aspose.Cells تعداد [**OoxmlCompressionType**](https://reference.aspose.com/cells/cpp/aspose.cells/ooxmlcompressiontype/) الذي يمكنك استخدامه لتعيين مستوى الضغط لسجل العمل. توفر التعداد [**OoxmlCompressionType**](https://reference.aspose.com/cells/cpp/aspose.cells/ooxmlcompressiontype/) الأعضاء التالية.

- المستوى 1: أسرع ولكن أقل فعالية في الضغط.
- المستوى 2: أبطأ قليلاً، ولكن أفضل من المستوى 1.
- المستوى 3: أبطأ قليلاً، ولكن أفضل من المستوى 2.
- المستوى 4: أبطأ قليلاً، ولكن أفضل من المستوى 3.
- المستوى 5: أبطأ قليلاً من المستوى 4، لكن مع ضغط أفضل.
- المستوى 6: توازن جيد بين السرعة وكفاءة الضغط.
- المستوى 7: ضغط جيد جدًا!
- المستوى8: ضغط أفضل من المستوى7!
- المستوى9: الضغط "الأفضل"، حيث الأفضل يعني أكبر حجم للاختزال في تيار بيانات الإدخال. هذا أيضًا الضغط الأبطأ.

يوضح الشريحة الكودية التالية استخدام تعداد [**OoxmlCompressionType**](https://reference.aspose.com/cells/cpp/aspose.cells/ooxmlcompressiontype/) ومقارنة وقت التحويل للمستوى 1 والمستوى 6 والمستوى 9. يمكنك أيضًا مقارنة أحجام الملفات المولدة.

```cpp
#include <iostream>
#include <chrono>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std::chrono;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load the workbook
    Workbook workbook(srcDir + u"LargeSampleFile.xlsx");

    // Create XlsbSaveOptions object
    XlsbSaveOptions options;

    // Set compression level to 1 and save the workbook
    options.SetCompressionType(OoxmlCompressionType::Level1);
    auto start = high_resolution_clock::now();
    workbook.Save(outDir + u"LargeSampleFile_level_1_out.xlsb", options);
    auto stop = high_resolution_clock::now();
    auto duration = duration_cast<milliseconds>(stop - start);
    std::cout << "Level 1 Elapsed Time: " << duration.count() << std::endl;

    // Set compression level to 6 and save the workbook
    options.SetCompressionType(OoxmlCompressionType::Level6);
    start = high_resolution_clock::now();
    workbook.Save(outDir + u"LargeSampleFile_level_6_out.xlsb", options);
    stop = high_resolution_clock::now();
    duration = duration_cast<milliseconds>(stop - start);
    std::cout << "Level 6 Elapsed Time: " << duration.count() << std::endl;

    // Set compression level to 9 and save the workbook
    options.SetCompressionType(OoxmlCompressionType::Level9);
    start = high_resolution_clock::now();
    workbook.Save(outDir + u"LargeSampleFile_level_9_out.xlsb", options);
    stop = high_resolution_clock::now();
    duration = duration_cast<milliseconds>(stop - start);
    std::cout << "Level 9 Elapsed Time: " << duration.count() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
