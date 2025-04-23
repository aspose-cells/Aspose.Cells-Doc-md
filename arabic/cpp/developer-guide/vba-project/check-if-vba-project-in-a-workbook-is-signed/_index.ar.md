---
title: تحقق مما إذا كان مشروع VBA في دفتر عمل الموقع باستخدام C++
linktitle: التحقق مما إذا كان مشروع VBA في كتاب عمل موقع بالتوقيع
type: docs
weight: 70
url: /ar/cpp/check-if-vba-project-in-a-workbook-is-signed/
description: تحقق مما إذا كان مشروع VBA في دفتر عمل الموقع باستخدام Aspose.Cells و C++.
---

{{% alert color="primary" %}}

يمكنك التحقق مما إذا كان مشروع VBA الخاص بك في Microsoft Excel موقعًا أم لا عبر قائمة **الأدوات > التوقيعات الرقمية...**. بالمثل، يمكنك التحقق منه برمجياً باستخدام Aspose.Cells [**Workbook.VbaProject.IsSigned**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/issigned).

{{% /alert %}}

## **تحقق مما إذا كان مشروع VBA في دفتر عمل الموقع في C++**

يحمّل الكود التالي دفتر العمل ويفحص ما إذا كان مشروع VBA الخاص به موقعًا باستخدام الخاصية [**Workbook.VbaProject.IsSigned**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/issigned). ستُرجع الخاصية **true** إذا كان المشروع موقعًا، وإلا ستُرجع **false**.

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

    // Path of input excel file
    U16String sampleFilePath = srcDir + u"Sample1.xlsx";

    // Create workbook
    Workbook workbook(sampleFilePath);

    // Check if the VBA project is signed
    bool isSigned = workbook.GetVbaProject().IsSigned();
    std::wcout << u"VBA Project is Signed: " << (isSigned ? u"true" : u"false") << std::endl;

    Aspose::Cells::Cleanup();
}
```
