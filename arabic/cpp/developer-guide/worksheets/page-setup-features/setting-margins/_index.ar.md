---
title: تعيين الهوامش باستخدام C++
linktitle: ضبط الهوامش
type: docs
weight: 20
url: /ar/cpp/setting-margins/
description: تعرف على كيفية تعيين هوامش ورقة عمل Excel باستخدام C++. يغطي هذا الدليل تعيين هوامش الصفحة، تركيز المحتوى، وتكوين هوامش الرأس والتذييل برمجياً باستخدام Aspose.Cells for C++.
keywords: تعيين هامش ورقة عمل Excel للتمركز C++، تعيين هامش رأس وتذييل الورقة بـ C++
---

{{% alert color="primary" %}}

تدعم Aspose.Cells تماماً خيارات إعداد الصفحة في Microsoft Excel. قد يحتاج المطورون إلى تكوين إعدادات إعداد الصفحة للوظائف للتحكم في عملية الطباعة. يناقش هذا الموضوع كيفية استخدام Aspose.Cells لتكوين هوامش الصفحة.

{{% /alert %}}

## **ضبط الهوامش**

 توفر Aspose.Cells فئة، [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)، تمثل ملف Excel. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) على مجموعة [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel. تمثل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/).

 توفر فئة [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) الخاصية [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) التي تُستخدم لتعيين خيارات إعداد الصفحة لورقة العمل. الخاصية [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) كائن من فئة [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) يتيح للمطورين تعيين خيارات تخطيط الصفحة المختلفة لورقة عمل مطبوعة. تقدم فئة [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) خصائص وأساليب متعددة تستخدم لتعيين خيارات إعداد الصفحة.

### **هوامش الصفحة**

تعيين هوامش الصفحة (يسار، يمين، أعلى، أسفل) باستخدام أعضاء فئة [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/). بعض الطرق تستخدم لتحديد هوامش الصفحة مذكورة أدناه:

- [**GetLeftMargin()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getleftmargin/)
- [**GetRightMargin()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getrightmargin/)
- [**GetTopMargin()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/gettopmargin/)
- [**GetBottomMargin()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getbottommargin/)

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

    // Create a workbook object
    Workbook workbook;

    // Get the worksheets in the workbook
    WorksheetCollection worksheets = workbook.GetWorksheets();

    // Get the first (default) worksheet
    Worksheet worksheet = worksheets.Get(0);

    // Get the pagesetup object
    PageSetup pageSetup = worksheet.GetPageSetup();

    // Set bottom, left, right, and top page margins
    pageSetup.SetBottomMargin(2);
    pageSetup.SetLeftMargin(1);
    pageSetup.SetRightMargin(1);
    pageSetup.SetTopMargin(3);

    // Save the Workbook
    workbook.Save(outDir + u"SetMargins_out.xls");

    std::cout << "Margins set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **توسيط على الصفحة**

 من الممكن تمركز شيء ما بشكل أفقي وعمودي على الصفحة. لهذا، هناك بعض الأعضاء المفيدة في فئة [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/)، [**GetCenterHorizontally()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getcenterhorizontally/) و [**GetCenterVertically()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getcentervertically/).

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

    // Create a workbook object
    Workbook workbook;

    // Get the worksheets in the workbook
    WorksheetCollection worksheets = workbook.GetWorksheets();

    // Get the first (default) worksheet
    Worksheet worksheet = worksheets.Get(0);

    // Get the pagesetup object
    PageSetup pageSetup = worksheet.GetPageSetup();

    // Specify Center on page Horizontally and Vertically
    pageSetup.SetCenterHorizontally(true);
    pageSetup.SetCenterVertically(true);

    // Save the Workbook
    workbook.Save(outDir + u"CenterOnPage_out.xls");

    std::cout << "Workbook saved successfully with centered page setup!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **هوامش الرأس والتذييل**

تعيين هوامش الرأس والتذييل مع أعضاء فئة [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) مثل [**GetHeaderMargin()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getheadermargin/) و [**GetFooterMargin()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getfootermargin/).

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

    // Create a workbook object
    Workbook workbook;

    // Get the worksheets in the workbook
    WorksheetCollection worksheets = workbook.GetWorksheets();

    // Get the first (default) worksheet
    Worksheet worksheet = worksheets.Get(0);

    // Get the pagesetup object
    PageSetup pageSetup = worksheet.GetPageSetup();

    // Specify Header / Footer margins
    pageSetup.SetHeaderMargin(2);
    pageSetup.SetFooterMargin(2);

    // Save the Workbook
    workbook.Save(outDir + u"CenterOnPage_out.xls");

    std::cout << "Workbook saved successfully with centered header and footer margins!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
