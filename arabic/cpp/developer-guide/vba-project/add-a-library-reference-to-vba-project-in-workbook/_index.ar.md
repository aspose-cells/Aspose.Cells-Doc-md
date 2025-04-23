---
title: إضافة مرجع مكتبة إلى مشروع VBA في دفتر عمل باستخدام C++
linktitle: أضف مرجعًا إلى مشروع VBA في سجل العمل
type: docs
weight: 80
url: /ar/cpp/add-a-library-reference-to-vba-project-in-workbook/
description: تعلم كيفية إضافة أو تسجيل مراجع المكتبة لمشروع VBA في دفتر عمل باستخدام Aspose.Cells for C++.
---

{{% alert color="primary" %}}

أحيانًا ، قد تحتاج إلى إضافة أو تسجيل مرجع المكتبة إلى مشروع VBA من خلال الكود. يمكنك القيام بذلك باستخدام طريقة Aspose.Cells [**VbaProject.References.AddRegisteredReference()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaprojectreferencecollection/addregisteredreference/).

{{% /alert %}}

## **أضف مرجع مكتبة إلى مشروع VBA في Microsoft Excel**

في Microsoft Excel ، يمكنك إضافة مرجع مكتبة إلى مشروع VBA عن طريق النقر على ** الأدوات > مراجع... ** يدوياً.

## **أضف مرجعًا إلى مشروع VBA في سجل العمل باستخدام Aspose.Cells**

الشيفرة الزمنية العينية التالية تضيف أو تسجل اثنين من مراجع المكتبات إلى مشروع VBA لسجل العمل باستخدام طريقة [**VbaProject.References.AddRegisteredReference()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaprojectreferencecollection/addregisteredreference/).

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

    // Path of output excel file
    U16String outputPath = outDir + u"Output_out.xlsm";

    // Create a new workbook
    Workbook workbook;

    // Get the VBA project from the workbook
    VbaProject vbaProj = workbook.GetVbaProject();

    // Add registered references to the VBA project
    vbaProj.GetReferences().AddRegisteredReference(u"stdole", u"*\\G{00020430-0000-0000-C000-000000000046}#2.0#0#C:\\Windows\\system32\\stdole2.tlb#OLE Automation");
    vbaProj.GetReferences().AddRegisteredReference(u"Office", u"*\\G{2DF8D04C-5BFA-101B-BDE5-00AA0044DE52}#2.0#0#C:\\Program Files\\Common Files\\Microsoft Shared\\OFFICE14\\MSO.DLL#Microsoft Office 14.0 Object Library");

    // Save the workbook
    workbook.Save(outputPath);

    std::cout << "VBA project references added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
