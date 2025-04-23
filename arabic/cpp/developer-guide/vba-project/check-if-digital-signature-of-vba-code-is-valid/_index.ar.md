---
title: تحقق مما إذا كانت التوقيع الرقمي لرمز VBA صالحًا باستخدام C++
linktitle: تحقق ما إذا كان التوقيع الرقمي لشيفر آلي VBA صالحًا
type: docs
weight: 120
url: /ar/cpp/check-if-digital-signature-of-vba-code-is-valid/
description: تعلم كيفية التحقق من صلاحية التوقيع الرقمي في رمز VBA باستخدام Aspose.Cells و C++.
---

{{% alert color="primary" %}}

يسمح Aspose.Cells بالتحقق مما إذا كان التوقيع الرقمي لرمز VBA صالحًا باستخدام الخاصية [**Workbook.VbaProject.IsValidSigned**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/isvalidsigned/). ستُرجع **true** إذا كان التوقيع صالحًا؛ وإذا لم يكن كذلك، فسيُرجع **false**. يصبح التوقيع الرقمي أو رمز VBA غير صالح عند تغيير رمز VBA.

{{% /alert %}}

## **تحقق مما إذا كان التوقيع الرقمي لرمز VBA صالحًا في C++**

يوضح الكود التالي استخدام هذه الخاصية باستخدام [ملف إكسل النموذجي](5115030.xlsm) الذي يمكنك تنزيله من الرابط المقدم. يحتوي نفس ملف إكسل على توقيع صالح، ولكن عند تعديل رمز VBA الخاص به وحفظ دفتر العمل وإعادة التحقق، نلاحظ أن توقيعه أصبح غير صالح.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load the workbook from an existing Excel file with VBA project
    Workbook workbook(srcDir + u"sampleVBAProjectSigned.xlsm");

    // Check if the VBA Code Project is valid signed
    std::cout << "Is VBA Code Project Valid Signed: " << (workbook.GetVbaProject().IsValidSigned() ? "True" : "False") << std::endl;

    // Modify the VBA Code
    U16String code = workbook.GetVbaProject().GetModules().Get(1).GetCodes();
    code = u"Welcome to Aspose.Cells"; // Directly setting new code here
    workbook.GetVbaProject().GetModules().Get(1).SetCodes(code);

    // Save the workbook
    workbook.Save(srcDir + u"output_out.xlsm");

    // Reload the workbook
    workbook = Workbook(srcDir + u"output_out.xlsm");

    // Now the signature is invalid
    std::cout << "Is VBA Code Project Valid Signed: " << (workbook.GetVbaProject().IsValidSigned() ? "True" : "False") << std::endl;

    Aspose::Cells::Cleanup();
}
```
