---  
title: إزالة الأنماط غير المستخدمة داخل دفتر العمل باستخدام C++  
linktitle: إزالة الأنماط الغير مستخدمة في دفتر العمل  
type: docs  
weight: 340  
url: /ar/cpp/remove-unused-styles-inside-the-workbook/  
description: إزالة الأنماط غير المستخدمة في دفتر عمل Excel باستخدام Aspose.Cells مع C++.  
---  

{{% alert color="primary" %}}  

تستهلك الأنماط غير المستخدمة في ملفات Excel مساحة وتسبب أيضًا مشاكل في الأداء أثناء التحويل إلى تنسيقات مختلفة مثل PDF و HTML وغيرها. يوفر Aspose.Cells خاصية [**Workbook.RemoveUnusedStyles()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/removeunusedstyles/) لإزالة جميع الأنماط غير المستخدمة داخل دفتر العمل.  

{{% /alert %}}  

يوضح الكود التالي طريقة استخدام [**Workbook.RemoveUnusedStyles()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/removeunusedstyles/). يقوم الكود بتحميل ملف Excel النموذجي ([ملف القالب](5115520.xlsx)) الذي يمكنك تنزيله من الرابط المقدم. يحتوي على نمط غير مستخدم يُدعى **AsposeStyle**؛ سيتم حذف هذا النمط وجميع الأنماط غير المستخدمة الأخرى بعد تشغيل الكود.  

![todo:image_alt_text](remove-unused-styles-inside-the-workbook_1.png)  

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C
    // Path to the documents directory.
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load template Excel file containing unused styles
    U16String templateFilePath = srcDir + u"Template-With-Unused-Custom-Style.xlsx";
    Workbook workbook(templateFilePath);

    // Remove all unused styles inside the template
    // This will also remove AsposeStyle which is an unused style inside the template
    workbook.RemoveUnusedStyles();

    // Save the file
    U16String outputFilePath = srcDir + u"output_out.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Unused styles removed and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
