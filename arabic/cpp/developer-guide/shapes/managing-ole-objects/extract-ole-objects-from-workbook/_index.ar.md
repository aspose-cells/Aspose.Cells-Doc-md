---
title: استخراج كائنات OLE من دفتر العمل باستخدام C++
linktitle: استخراج كائنات Ole من الدفتر
type: docs
weight: 110
url: /ar/cpp/extract-ole-objects-from-workbook/
description: تعلم كيفية استخراج كائنات OLE من دفتر العمل باستخدام Aspose.Cells مع C++.
---

{{% alert color="primary" %}}

في بعض الأحيان، تحتاج إلى استخراج كائنات OLE من دفتر العمل. يدعم Aspose.Cells استخراج وتخزين تلك الكائنات OLE.

توضح هذه المقالة كيفية إنشاء تطبيق وحدة تحكم في Visual Studio واستخراج كائنات OLE المختلفة من دفتر العمل مع بضع أسطر بسيطة من التعليمات البرمجية.

{{% /alert %}}

## **استخراج كائنات Ole من دفتر عمل**

### **إنشاء دفتر عمل قالب**

1. أنشئ دفتر عمل في Microsoft Excel.
1. أضف مستند Word، ودفتر عمل Excel، ومستند PDF كعناصر تحكم OLE على الورقة الأولى.

|**مستند القالب مع كائنات OLE (OleFile.xls)**|
| :- |
|![todo:image_alt_text](extract-ole-objects-from-workbook_1.png)|

التالي، استخرج كائنات OLE واحفظها على القرص الصلب مع أنواع ملفاتها الخاصة.

### **تنزيل وتثبيت Aspose.Cells**

1. [تحميل Aspose.Cells for C++](https://downloads.aspose.com/cells/cpp).
1. قم بتثبيته على كمبيوتر التطوير الخاص بك.

جميع مكونات Aspose، عند التثبيت، تعمل في وضع التقييم. وضع التقييم لا يحتوي على حد زمني ويقوم فقط بحقن العلامات المائية إلى الوثائق المنتجة.

### **إنشاء مشروع**

ابدأ **Visual Studio** وأنشئ تطبيق وحدة تحكم جديد. سوف يُظهر هذا المثال تطبيق وحدة تحكم C++.

1. إضافة المراجع
   1. أضف مرجعًا إلى مكون Aspose.Cells إلى مشروعك، على سبيل المثال، أضف مرجعًا إلى ...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll.

### **استخراج كائنات Ole**

الرمز أدناه يقوم بالعمل الفعلي للبحث واستخراج كائنات OLE. يتم حفظ كائنات الـ OLE (ملفات DOC، XLS، و PDF) على القرص.

```cpp
#include <iostream>
#include <fstream>
#include <memory>
#include <string>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Open the template file
    Workbook workbook(srcDir + u"oleFile.xlsx");

    // Get the OleObject Collection in the first worksheet
    OleObjectCollection oles = workbook.GetWorksheets().Get(0).GetOleObjects();

    // Loop through all the oleobjects and extract each object in the worksheet
    for (int i = 0; i < oles.GetCount(); i++)
    {
        OleObject ole = oles.Get(i);

        // Specify the output filename
        U16String fileName = srcDir + u"outOle" + U16String(std::to_string(i).c_str()) + u".";

        // Specify each file format based on the oleobject format type
        switch (ole.GetFileFormatType())
        {
            case FileFormatType::Doc:
                fileName += u"doc";
                break;
            case FileFormatType::Excel97To2003:
                fileName += u"Xlsx";
                break;
            case FileFormatType::Ppt:
                fileName += u"Ppt";
                break;
            case FileFormatType::Pdf:
                fileName += u"Pdf";
                break;
            case FileFormatType::Unknown:
                fileName += u"Jpg";
                break;
            default:
                // Handle other formats if needed
                break;
        }

        // Save the oleobject as a new excel file if the object type is xls
        if (ole.GetFileFormatType() == FileFormatType::Xlsx)
        {
            Vector<uint8_t> objectData = ole.GetObjectData();
            if (objectData.GetLength() > 0)
            {
                Workbook oleBook(objectData);
                oleBook.GetSettings().SetIsHidden(false);
                oleBook.Save(srcDir + u"outOle" + U16String(std::to_string(i).c_str()) + u".out.xlsx");
            }
        }
        // Create the files based on the oleobject format types
        else
        {
            Vector<uint8_t> objectData = ole.GetObjectData();
            if (objectData.GetLength() > 0)
            {
                std::ofstream fs(fileName.ToUtf8().c_str(), std::ios::binary);
                fs.write(reinterpret_cast<const char*>(objectData.GetData()), objectData.GetLength());
                fs.close();
            }
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
