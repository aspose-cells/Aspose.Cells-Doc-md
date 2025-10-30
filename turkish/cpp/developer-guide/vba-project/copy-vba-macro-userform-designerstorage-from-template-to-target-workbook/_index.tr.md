---
title: Template den Hedef Çalışma Kitabına VBA Macro UserForm DesignerStorage Kopyala (C++)
linktitle: VBA Macro UserForm DesignerStorage Kopyala
type: docs
weight: 130
url: /tr/cpp/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/
description: Aspose.Cells for C++ kullanarak şablondan hedef çalışma kitabına VBA Macro UserForm DesignerStorage nasıl kopyalanır öğrenin.
---

## **Olası Kullanım Senaryoları**

 Aspose.Cells, bir Excel dosyasından başka bir Excel dosyasına VBA projesi kopyalamanıza olanak tanır. Bir VBA projesi, Document, Procedural, Designer gibi çeşitli modüllerden oluşur. Tüm modüller basit kodlar kullanılarak kopyalanabilir, fakat Designer modülü için Designer Storage adında ek veriler vardır ve bunlara erişip kopyalamak gerekir. Aşağıdaki iki yöntem, Designer Storage ile ilgilidir:

- [**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbamodulecollection/getdesignerstorage/)
- [**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbamodulecollection/adddesignerstorage/)

## **Taslak ve Hedef Çalışbook Arasında VBA Makro Kullanıcı Formu Tasarımcı Depolama Alanını Kopyalama**

Lütfen aşağıdaki örnek kodu inceleyin. Bu kod, [şablon Excel dosyasından](50528345.xlsm) VBA projesini boş bir çalışma kitabına kopyalar ve [çıktı Excel dosyası](50528346.xlsm) olarak kaydeder. Şablon Excel dosyasının içindeki VBA projesini açarsanız, aşağıda gösterildiği gibi bir Kullanıcı Formu göreceksiniz. Kullanıcı Formu, Tasarımcı Depolama içerir, bu nedenle [**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbamodulecollection/getdesignerstorage/) ve [**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbamodulecollection/adddesignerstorage/) metodları kullanılarak kopyalanacaktır.

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_1.png)**

Aşağıdaki ekran görüntüsü, kopyalanan şablon Excel dosyasından çıktı Excel dosyasını ve içeriğini gösterir. Buton 1'e tıkladığınızda VBA Kullanıcı Formu açılır ve kendisi de tıklamada mesaj kutusu gösteren bir komut düğmesine sahiptir.

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_2.png)**

## **Örnek Kod**

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
