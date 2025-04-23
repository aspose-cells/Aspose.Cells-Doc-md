---
title: عرض وإخفاء أوراق العمل وعناصر التبويب باستخدام C++
linktitle: إظهار وإخفاء الأوراق والألسنة
type: docs
weight: 10
url: /ar/cpp/show-and-hide-worksheets-and-tabs/
description: يقدم هذا المقال مثالاً برمجيًا على استخدام واجهة برمجة التطبيقات أو المكتبة C++ لعرض وإخفاء ورقة عمل إكسل برمجياً. بالإضافة إلى ذلك، كيفية عرض وإخفاء علامات التبويب في مصنف إكسل.
---

{{% alert color="primary" %}}

تسمح Aspose.Cells للمستخدم بإظهار وإخفاء عناصر دفتر العمل بما في ذلك الأوراق والألسنة.

{{% /alert %}}

## **إظهار وإخفاء ورقة عمل**

يمكن أن يحتوي ملف إكسل على ورقة عمل واحدة أو أكثر. كلما أنشأنا ملف إكسل، نضيف أوراق عمل إلى الملف إكسل الذي نعمل فيه. تكون كل ورقة عمل في ملف إكسل مستقلة عن الورقة العمل الأخرى بوجود بياناتها الخاصة وإعدادات التنسيق وما إلى ذلك. في بعض الأحيان، قد يحتاج المطورون إلى إخفاء بعض الأوراق العمل وجعل البعض الآخر مرئية في ملف إكسل لمصلحتهم الخاصة. لذا، **Aspose.Cells** يتيح للمطورين التحكم في رؤية أوراق العمل في ملفاتهم إكسل.

توفر Aspose.Cells فئة، [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)، التي تمثل ملف إكسل. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) على مجموعة [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) تمكن من الوصول إلى كل ورقة عمل في الملف.

تمثل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). تقدم فئة [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) مجموعة واسعة من الخصائص والطرق لإدارة أوراق العمل. للتحكم في رؤية ورقة العمل، استخدم خاصية [**IsVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isvisible/) من فئة [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). [**IsVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isvisible/) هي خاصية منطقية، مما يعني أنها يمكن أن تخزن فقط قيمة **صحيح** أو **خطأ**.

### **جعل ورقة العمل مرئية**

اجعل ورقة عمل مرئية عن طريق تعيين خاصية [**IsVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isvisible/) لفئة [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) إلى **صحيح**.

### **إخفاء ورقة عمل**

أخفِ ورقة عمل عن طريق تعيين خاصية [**IsVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/isvisible/) لفئة [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) إلى **خطأ**.

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Create workbook from file
    Workbook workbook(inputFilePath);

    // Access the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Hide the first worksheet of the Excel file
    worksheet.SetIsVisible(false);

    // Save the modified Excel file in default (Excel 2003) format
    U16String outputFilePath = outDir + u"output.out.xls";
    workbook.Save(outputFilePath);

    std::cout << "Worksheet hidden and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **إظهار وإخفاء الألسنة**

إذا نظرت عن كثب في أسفل ملف Microsoft Excel، سترى عددًا من الضوابط. تشمل هذه:

- ألسنة الصفحات.
- أزرار تمرير الألسنة.

تمثل ألسنة الصفحات الأوراق العمل في ملف الإكسل. انقر على أي علامة تبويب للانتقال إلى تلك الورقة العمل. كلما زاد عدد الأوراق العمل في الدفتر الحسابي، زادت ألسنة الصفحة. إذا كان لديك عدد جيد من الأوراق العمل في دفتر العمل، يلزمك الأزرار للتنقل خلالها. لذا، يوفر مايكروسوفت إكسل أزرار تمرير الألسنة للتمرير من خلال ألسنة الصفحات.

باستخدام Aspose.Cells، يمكن للمطورين التحكم في رؤية علامات الجدول وأزرار التمرير في ملفات Excel.

توفر Aspose.Cells فئة، [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)، التي تمثل ملف إكسل. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) على مجموعة واسعة من الخصائص والطرق لإدارة ملف إكسل. للتحكم في رؤية علامات التبويب في ملف إكسل، يمكن للمطورين استخدام خاصية [**WorkbookSettings.GetShowTabs()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getshowtabs/) من فئة [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/). [**WorkbookSettings.GetShowTabs()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getshowtabs/) هي خاصية منطقية، مما يعني أنها يمكن أن تخزن فقط قيمة **صحيح** أو **خطأ**.

### **جعل علامات التبويب مرئية**

اجعل علامات التبويب مرئية باستخدام خاصية [**WorkbookSettings.GetShowTabs()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getshowtabs/) من فئة [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) لتكون **صحيح**.

### **إخفاء علامات التبويب**

اخفِ علامات التبويب في ملف إكسل عن طريق تعيين خاصية [**WorkbookSettings.GetShowTabs()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getshowtabs/) من فئة [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) إلى **خطأ**.

فيما يلي مثال كامل يفتح ملف Excel (book1.xls)، يخفي علاماته ويحفظ الملف المعدل بصيغة output.xls. بعد تنفيذ الكود، سترى أن تبويبات الدفتر مخفية.

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get workbook settings
    WorkbookSettings settings = workbook.GetSettings();

    // Hiding the tabs of the Excel file
    settings.SetShowTabs(false);

    // Shows the tabs of the Excel file
    // settings.SetShowTabs(true);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Excel file modified successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **السيطرة على عرض شريط التبويب**

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get workbook settings
    WorkbookSettings settings = workbook.GetSettings();

    // Show tabs in the Excel file
    settings.SetShowTabs(true);

    // Adjust the sheet tab bar width
    settings.SetSheetTabBarWidth(800);

    // Save the modified Excel file
    workbook.Save(outputFilePath);

    std::cout << "Excel file modified successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
