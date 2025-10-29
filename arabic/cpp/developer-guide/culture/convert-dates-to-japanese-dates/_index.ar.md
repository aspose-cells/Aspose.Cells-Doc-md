---
title: تحويل التواريخ إلى التواريخ اليابانية باستخدام C++
linktitle: تحويل التواريخ إلى تواريخ يابانية
type: docs
weight: 350
url: /ar/cpp/convert-dates-to-japanese-dates/
description: تعلم كيفية تحويل التواريخ الميلادية إلى تواريخ يابانية باستخدام Aspose.Cells for C++.
---

{{% alert color="primary" %}}

في التقويم الياباني، يبدأ عصر جديد مع عهد إمبراطور جديد. في 1 مايو 2019، تولى إمبراطور جديد الحكم، والتي انتهى معها عهد هيسي وبدأ عهد ريو وا.

{{% /alert %}}

توفر Aspose.Cells وسيلة لتحويل تواريخ الميلادي إلى تواريخ يابانية. أثناء هذا التحويل، يتم أيضًا أخذ تغييرات العهد في الاعتبار. يُحوّل مقتطف الكود التالي ملف [Excel المصدر](90112015.xlsx) الذي يحتوي على تواريخ ميلادية إلى ملف [PDF الناتج](90112016.pdf) بتواريخ يابانية كما هو موضح في الصورة أدناه.

![todo:image_alt_text](convert-dates-to-japanese-dates_1.jpg)

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

    // Create load options for XLSX format
    LoadOptions options(LoadFormat::Xlsx);

    // Set culture info to Japanese
    options.SetLanguageCode(CountryCode::Japan);

    // Load the workbook with Japanese dates
    Workbook workbook(srcDir + u"JapaneseDates.xlsx", options);

    // Save the workbook as PDF
    workbook.Save(outDir + u"JapaneseDates.pdf", SaveFormat::Pdf);

    std::cout << "Workbook saved successfully as PDF with Japanese dates!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
