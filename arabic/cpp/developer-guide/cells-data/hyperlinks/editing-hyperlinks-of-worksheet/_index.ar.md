---
title: تحرير روابط العناوين لورقة العمل باستخدام C++
linktitle: تحرير الارتباطات التشعبية لورقة العمل
type: docs
weight: 330
url: /ar/cpp/editing-hyperlinks-of-worksheet/
description: تعلم كيفية تحرير روابط العناوين لورقة العمل من خلال API Aspose.Cells for C++.
keywords: تحرير الروابط الفائقة، تحرير الروابط الفائقة للورقة العمل، تحرير الروابط الفائقة للخلية، الوصول إلى كافة الروابط الفائقة في الورقة العمل
---

{{% alert color="primary" %}}

تتيح Aspose.Cells لك الوصول إلى كل روابط الصفحة العمل باستخدام مجموعة [**GetHyperlinks()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/gethyperlinks/). يمكنك الوصول إلى كل رابط فائقة من هذه المجموعة وتحرير خصائصه.

{{% /alert %}}

 يتيح الرمز النموذجي التالي الوصول إلى جميع الروابط التشعبية للورقة وتغيير الخاصية [**GetAddress()**](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlink/getaddress/) إلى موقع Aspose الإلكتروني.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook from input file
    Workbook workbook(srcDir + u"Sample.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Iterate through all hyperlinks in the worksheet
    for (int32_t i = 0; i < worksheet.GetHyperlinks().GetCount(); i++)
    {
        Hyperlink hl = worksheet.GetHyperlinks().Get(i);
        hl.SetAddress(u"http://www.aspose.com");
    }

    // Save the modified workbook to the output file
    workbook.Save(outDir + u"output_out.xlsx");

    std::cout << "Hyperlinks updated successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
