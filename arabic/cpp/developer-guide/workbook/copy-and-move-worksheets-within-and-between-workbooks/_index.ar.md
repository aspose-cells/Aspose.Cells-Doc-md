---
title: نسخ وتحريك أوراق العمل داخل وبين دفاتر العمل باستخدام C++
linktitle: نسخ وتحريك أوراق العمل
type: docs
weight: 80
url: /ar/cpp/copy-and-move-worksheets-within-and-between-workbooks/
description: تعلم كيفية نسخ وتحريك أوراق العمل داخل وبين دفاتر العمل Excel باستخدام Aspose.Cells for C++.
---

{{% alert color="primary" %}}

أحيانًا، تحتاج إلى أوراق عمل متعددة ذات تصميم وبيانات مشتركة. على سبيل المثال، إذا كنت تعمل على ميزانيات فصليّة، قد ترغب في إنشاء دفتر عمل يحتوي على أوراق تحتوي على رؤوس أعمدة، رؤوس صفوف، وصيغ متطابقة. هناك طريقة للقيام بذلك: عن طريق إنشاء ورقة واحدة ثم نسخها عدة مرات.

يدعم Aspose.Cells نسخ أو نقل الأوراق داخل أو بين أوراق العمل. تتم نسخ الأوراق بما في ذلك البيانات والتنسيق والجداول والمصفوفات والرسومات والصور والكائنات الأخرى بأعلى درجة من الدقة.

{{% /alert %}}

## **نسخ ونقل أوراق العمل**

### **نسخ ورقة عمل داخل دفتر عمل**

الخطوات الأولية متطابقة لجميع الأمثلة:

1. أنشئ دفترين عمل ببعض البيانات في Microsoft Excel. لأغراض هذا المثال، أنشأنا دفترين عمل جديدين في Microsoft Excel وأدخلنا بعض البيانات في أوراق العمل:
   - FirstWorkbook.xlsx (3 أوراق عمل)
   - SecondWorkbook.xlsx (ورقة عمل واحدة)

1. قم بتنزيل وتثبيت Aspose.Cells:
   1. [تحميل Aspose.Cells for C++](https://downloads.aspose.com/cells/cpp)
   1. قم بتثبيته على جهاز التطوير الخاص بك

1. أنشئ مشروعًا:
   1. أنشئ مشروع C++ جديد في بيئة تطويرك المفضلة

1. أضف مراجع:
   1. أضف مكتبة Aspose.Cells for C++ إلى مشروعك

1. نسخ ورقة العمل داخل دفتر العمل
   المثال الأول يقوم بنسخ الورقة الأولى (نسخ) داخل FirstWorkbook.xlsx.

عند تنفيذ الكود، يتم نسخ ورقة العمل التي تحمل اسم نسخ داخل FirstWorkbook.xlsx بإسم الورقة الأخيرة.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directory paths
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook from input file
    Workbook excelWorkbook1(srcDir + u"FirstWorkbook.xlsx");

    // Get worksheet collection reference
    WorksheetCollection worksheets = excelWorkbook1.GetWorksheets();

    // Copy third worksheet (index 2) within the workbook
    worksheets.AddCopy(worksheets.Get(2).GetName());

    // Save modified workbook
    excelWorkbook1.Save(outDir + u"FirstWorkbookCopied_out.xlsx");

    std::cout << "Worksheet copied successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **نقل ورقة العمل داخل دفتر العمل**

يظهر الكود أدناه كيفية نقل ورقة العمل من موقع إلى آخر في دفتر العمل. عند تنفيذ الكود، يتم نقل ورقة العمل التي تسمى Move من المؤشر 1 إلى المؤشر 2 في FirstWorkbook.xlsx.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directory paths
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create input and output file paths
    U16String inputFilePath = srcDir + u"FirstWorkbook.xlsx";
    U16String outputFilePath = outDir + u"FirstWorkbookMoved_out.xlsx";

    // Load source workbook
    Workbook excelWorkbook2(inputFilePath);

    // Access worksheet collection and move target sheet
    WorksheetCollection sheets = excelWorkbook2.GetWorksheets();
    sheets.Get(u"Move").MoveTo(2);

    // Save modified workbook
    excelWorkbook2.Save(outputFilePath);

    std::cout << "Worksheet moved successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **نسخ ورقة العمل بين دفاتر العمل**

تنفيذ الكود ينسخ ورقة العمل المسماة Copy إلى SecondWorkbook.xlsx باسم Sheet2.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directories
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Open source workbooks
    Workbook excelWorkbook3(srcDir + u"FirstWorkbook.xlsx");
    Workbook excelWorkbook4(srcDir + u"SecondWorkbook.xlsx");

    // Access worksheets collection from second workbook
    WorksheetCollection sheets4 = excelWorkbook4.GetWorksheets();

    // Add new worksheet to destination workbook
    sheets4.Add();

    // Copy specified worksheet from source to destination
    Worksheet sourceSheet = excelWorkbook3.GetWorksheets().Get(u"Copy");
    sheets4.Get(1).Copy(sourceSheet);

    // Save modified workbook
    excelWorkbook4.Save(outDir + u"CopyWorksheetsBetweenWorkbooks_out.xlsx");

    std::cout << "Worksheets copied successfully between workbooks." << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **نقل ورقة العمل بين دفاتر العمل**

عند تنفيذ الكود، يتم نقل ورقة العمل المسماة Move من FirstWorkbook.xlsx إلى SecondWorkbook.xlsx بإسم Sheet3.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directories
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Open first workbook
    Workbook excelWorkbook5(srcDir + u"FirstWorkbook.xlsx");

    // Open second workbook and add new worksheet
    Workbook excelWorkbook6(srcDir + u"SecondWorkbook.xlsx");
    excelWorkbook6.GetWorksheets().Add();

    // Copy third worksheet from first workbook to third position in second workbook
    WorksheetCollection sheets5 = excelWorkbook5.GetWorksheets();
    WorksheetCollection sheets6 = excelWorkbook6.GetWorksheets();
    sheets6.Get(2).Copy(sheets5.Get(2));

    // Remove copied worksheet from source workbook
    sheets5.RemoveAt(2);

    // Save modified workbooks
    excelWorkbook5.Save(outDir + u"FirstWorkbookWithMove_out.xlsx");
    excelWorkbook6.Save(outDir + u"SecondWorkbookWithMove_out.xlsx");

    std::cout << "Worksheets moved successfully between workbooks." << std::endl;

    Aspose::Cells::Cleanup();
}
```
