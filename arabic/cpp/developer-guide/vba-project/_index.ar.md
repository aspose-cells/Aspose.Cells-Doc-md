---
title: إدارة رموز VBA لمصنف Excel مع تفعيل الماكرو باستخدام C++
linktitle: مشروع الماكرو
type: docs
weight: 200
url: /ar/cpp/manage-vba-project/
description: أضف وحدة VBA و عدل VBA أو الماكرو باستخدام مكتبة Aspose.Cells in C++.
---

## **إضافة وحدة VBA في C++**
{{% alert color="primary" %}}

يسمح لك Aspose.Cells بإضافة وحدة VBA جديدة وكتابة رمز الماكرو باستخدام Aspose.Cells. يُرجى استخدام طريقة [**Workbook.VbaProject.Modules.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbamodulecollection/add/) لإضافة وحدة VBA الجديدة داخل المصنف.

{{% /alert %}}

يتضمن المثال التالي إنشاء مصنف جديد وإضافة وحدة VBA ورمز الماكرو الجديدة وحفظ الناتج بصيغة XLSM. بمجرد فتح ملف XLSM الناتج في Microsoft Excel والنقر على أوامر القائمة **مطور > محرر Visual Basic**، سترى وحدة باسم "TestModule" وداخلها رمز الماكرو التالي.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

فيما يلي رمز العينة لإنشاء ملف إكسيل الناتج بتنسيق XLSM مع وحدة VBA وكود الماكرو.

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

    // Create new workbook
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add VBA Module
    int32_t idx = workbook.GetVbaProject().GetModules().Add(worksheet);

    // Access the VBA Module, set its name and codes
    VbaModule module = workbook.GetVbaProject().GetModules().Get(idx);
    module.SetName(u"TestModule");

    U16String codes = u"Sub ShowMessage()\r\n"
                      u"    MsgBox \"Welcome to Aspose!\"\r\n"
                      u"End Sub";
    module.SetCodes(codes);

    // Save the workbook
    U16String outputPath = outDir + u"output_out.xlsm";
    workbook.Save(outputPath, SaveFormat::Xlsm);

    std::cout << "VBA module added and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **تعديل VBA أو الماكرو باستخدام C++**

{{% alert color="primary" %}} 

يمكنك تعديل الكود الخاص ب VBA أو الماكرو باستخدام Aspose.Cells. لقد قامت Aspose.Cells بإضافة مساحة الاسم التالية والفئات لقراءة وتعديل مشروع VBA في ملف الإكسيل.

- Aspose::Cells::Vba
- VbaProject
- VbaModuleCollection
- VbaModule

سيعرض هذا المقال لك كيفية تغيير رمز VBA أو الماكرو داخل ملف Excel المصدر باستخدام Aspose.Cells.

{{% /alert %}} 

يعرض المثال التالي كود تحميل ملف Excel المصدر الذي يحتوي على رمز VBA أو الماكرو التالي داخله:

{{< highlight java >}}

 Sub Button1_Click()

    MsgBox "This is test message."

End Sub

{{< /highlight >}}

بعد تنفيذ كود Aspose.Cells، سيتم تعديل رمز VBA أو الماكرو على النحو التالي:

{{< highlight java >}}

 Sub Button1_Click()

    MsgBox "This is Aspose.Cells message."

End Sub

{{< /highlight >}}

يمكنك تنزيل [ملف Excel المصدر](5112508.xlsm) و[ملف Excel الناتج](5112511.xlsm) من الروابط المعطاة.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    U16String inputFilePath = srcDir + u"sample.xlsm";
    U16String outputFilePath = outDir + u"output_out.xlsm";

    Workbook workbook(inputFilePath);

    VbaProject vbaProject = workbook.GetVbaProject();
    VbaModuleCollection modules = vbaProject.GetModules();

    for (int i = 0; i < modules.GetCount(); ++i)
    {
        VbaModule module = modules.Get(i);
        U16String code = module.GetCodes();
        U16String searchStr = u"This is test message.";
        U16String replaceStr = u"This is Aspose.Cells message.";

        if (code.IndexOf(searchStr) != -1)
        {
            U16String newCode;
            const char16_t* codeData = code.GetData();
            const char16_t* searchData = searchStr.GetData();
            int codeLen = code.GetLength();
            int searchLen = searchStr.GetLength();

            int pos = 0;
            int searchPos;

            while ((searchPos = code.IndexOf(searchStr)) != -1)
            {
                for (int j = pos; j < searchPos; j++)
                {
                    newCode += codeData[j];
                }

                newCode += replaceStr;

                pos = searchPos + searchLen;
            }

            for (int j = pos; j < codeLen; j++)
            {
                newCode += codeData[j];
            }

            module.SetCodes(newCode);
        }
    }

    workbook.Save(outputFilePath);

    std::cout << "VBA module codes updated successfully." << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **الموضوعات المتقدمة**
- [إضافة مرجع مكتبة لمشروع VBA في المصنف](/cells/ar/cpp/add-a-library-reference-to-vba-project-in-workbook/)
- [تعيين الماكرو إلى عنصر تحكم النموذج](/cells/ar/cpp/assign-macro-to-form-control/)
- [التحقق مما إذا كان التوقيع الرقمي لرمز VBA صالحًا](/cells/ar/cpp/check-if-digital-signature-of-vba-code-is-valid/)
- [فحص ما إذا كان رمز VBA موقعًا](/cells/ar/cpp/check-if-vba-code-is-signed/)
- [تحقق مما إذا كان مشروع VBA في المصنف موقّعًا](/cells/ar/cpp/check-if-vba-project-in-a-workbook-is-signed/)
- [فحص ما إذا كان مشروع VBA محميًا ومقفلاً للعرض](/cells/ar/cpp/check-if-vba-project-is-protected-and-locked-for-viewing/)
- [نسخ تصميم الاستوديو Form UserForm VBA Macro من القالب إلى دفتر العمل الهدف](/cells/ar/cpp/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/)
- [توقيع رقمي لمشروع رمز VBA باستخدام شهادة](/cells/ar/cpp/digitally-sign-a-vba-code-project-with-certificate/)
- [تصدير شهادة VBA إلى ملف أو تيار](/cells/ar/cpp/export-vba-certificate-to-file-or-stream/)
- [تصفية مشروع VBA أثناء تحميل المصنف](/cells/ar/cpp/filter-vba-project-while-loading-a-workbook/)
- [معرفة ما إذا كان مشروع VBA محميًا](/cells/ar/cpp/find-out-if-vba-project-is-protected/)
- [حماية كلمة المرور لمشروع VBA لمصنف عمل Excel](/cells/ar/cpp/password-protect-the-vba-project-of-excel-workbook/)
{{< app/cells/assistant language="cpp" >}}
