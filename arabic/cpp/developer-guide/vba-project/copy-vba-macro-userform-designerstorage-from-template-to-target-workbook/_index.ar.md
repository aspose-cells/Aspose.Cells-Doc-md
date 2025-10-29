---
title: نسخ مصمم نموذج VBA UserForm من القالب إلى دفتر عمل الهدف باستخدام C++
linktitle: نسخ مصمم نموذج VBA UserForm
type: docs
weight: 130
url: /ar/cpp/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/
description: تعلم كيفية نسخ مصمم نموذج VBA UserForm من قالب إلى دفتر عمل الهدف باستخدام Aspose.Cells for C++.
---

## **سيناريوهات الاستخدام المحتملة**

يسمح Aspose.Cells بنسخ مشروع VBA من ملف إكسل إلى آخر. يتكون مشروع VBA من أنواع مختلفة من الوحدات، مثل المستند، الإجرائية، المصمم، وغيرها. يمكن نسخ جميع الوحدات باستخدام كود بسيط، ولكن لنسخة وحدة المصمم هناك بعض البيانات الإضافية تسمى Designer Storage تحتاج إلى الوصول أو النسخ. تتناول الطريقتان التاليتان Designer Storage:

- [**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbamodulecollection/getdesignerstorage/)
- [**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbamodulecollection/adddesignerstorage/)

## **نسخ تصميم الاستوديو Form UserForm VBA Macro من القالب إلى دفتر العمل الهدف**

يرجى الاطلاع على نموذج الشفرة التالي. ينسخ مشروع VBA من [ملف إكسل النموذجي](50528345.xlsm) إلى مصنف فارغ ويقوم بحفظه كـ [ملف إكسل الإخراج](50528346.xlsm). إذا قمت بفتح مشروع VBA داخل ملف إكسل النموذجي، سترى نموذج مستخدم كما هو موضح أدناه. يتكون نموذج المستخدم من تخزين المصمم، لذلك سيتم نسخه باستخدام طريقتي [**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbamodulecollection/getdesignerstorage/) و [**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbamodulecollection/adddesignerstorage/).

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_1.png)**

تُظهر لقطة الشاشة التالية ملف إكسل الناتج ومحتوياته التي تم نسخها من ملف إكسل النموذجي. عند النقر على الزر 1، يفتح نموذج VBA المستخدم الذي يحتوي على زر أمر يظهر رسالة عند النقر عليه.

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_2.png)**

## **الكود المثالي**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook target;

    Workbook templateFile(srcDir + u"sampleDesignerForm.xlsm");

    WorksheetCollection templateSheets = templateFile.GetWorksheets();
    WorksheetCollection targetSheets = target.GetWorksheets();

    for (int i = 0; i < templateSheets.GetCount(); ++i)
    {
        Worksheet ws = templateSheets.Get(i);
        if (ws.GetType() == SheetType::Worksheet)
        {
            Worksheet s = targetSheets.Add(ws.GetName());
            s.Copy(ws);
            s.GetCells().Get(u"A2").PutValue(u"VBA Macro and User Form copied from template to target.");
        }
    }

    VbaProject templateVbaProject = templateFile.GetVbaProject();
    VbaProject targetVbaProject = target.GetVbaProject();
    VbaModuleCollection templateModules = templateVbaProject.GetModules();

    for (int i = 0; i < templateModules.GetCount(); ++i)
    {
        VbaModule vbaItem = templateModules.Get(i);
        if (vbaItem.GetName() == u"ThisWorkbook")
        {
            targetVbaProject.GetModules().Get(u"ThisWorkbook").SetCodes(vbaItem.GetCodes());
        }
        else
        {
            std::wcout << reinterpret_cast<const wchar_t*>(vbaItem.GetName().GetData()) << std::endl;

            int vbaMod = 0;
            Worksheet sheet = targetSheets.GetSheetByCodeName(vbaItem.GetName());
            if (sheet.IsNull())
            {
                vbaMod = targetVbaProject.GetModules().Add(vbaItem.GetType(), vbaItem.GetName());
            }
            else
            {
                vbaMod = targetVbaProject.GetModules().Add(sheet);
            }

            targetVbaProject.GetModules().Get(vbaMod).SetCodes(vbaItem.GetCodes());

            if (vbaItem.GetType() == VbaModuleType::Designer)
            {
                Vector<uint8_t> designerStorage = templateVbaProject.GetModules().GetDesignerStorage(vbaItem.GetName());
                targetVbaProject.GetModules().AddDesignerStorage(vbaItem.GetName(), designerStorage);
            }
        }
    }

    target.Save(outDir + u"outputDesignerForm.xlsm", SaveFormat::Xlsm);

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
