---
title: إدارة كائنات OLE باستخدام C++
linktitle: إدارة كائنات OLE
type: docs
weight: 50
url: /ar/cpp/managing-ole-objects/
description: تعلم كيفية إضافة واستخراج والتعامل مع كائنات OLE في أوراق العمل باستخدام Aspose.Cells مع C++.
---

## **مقدمة**

OLE (Object Linking and Embedding) هي إطار عمل مايكروسوفت لتكنولوجيا المستند المركب. باختصار، المستند المركب هو شيء مثل سطح مكتب العرض الذي يمكن أن يحتوي على كائنات بصرية ومعلوماتية من جميع الأنواع: نص، تقويمات، رسوم متحركة، صوت، فيديو متحرك، ثلاثي الأبعاد، أخبار متجددة باستمرار، تحكمات، وما إلى ذلك. كل كائن على سطح المكتب هو كيان برنامج مستقل يمكنه التفاعل مع مستخدم وأيضا التواصل مع كائنات أخرى على سطح المكتب.

يتم دعم OLE (Object Linking and Embedding) من قِبل العديد من البرامج المختلفة ويتم استخدامه لجعل المحتوى الذي تم إنشاؤه في برنامج متاح في برنامج آخر. على سبيل المثال، يمكنك إدراج مستند Microsoft Word في Microsoft Excel. لمعرفة أنواع المحتوى التي يمكنك إدراجها، انقر على **كائن** في قائمة **إدراج**. يظهر البرامج التي تم تثبيتها على الكمبيوتر والتي تدعم كائنات OLE في مربع نوع **الكائن** فقط.

### **إدراج كائنات OLE في ورقة العمل**

يدعم Aspose.Cells إضافة واستخراج والتعامل مع كائنات OLE في أوراق العمل. لهذا السبب، يحتوي Aspose.Cells على فئة [**OleObjectCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobjectcollection/)، المستخدمة لإضافة كائن OLE جديد إلى قائمة التجميع. فئة أخرى، [**OleObject**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/)، تمثل كائن OLE. لديها بعض الأعضاء المهمة:

- تحدد الخاصية [**ImageData**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getimagedata/) بيانات الصورة (الأيقونة) من نوع مصفوفة البايت. سيتم عرض الصورة لعرض كائن OLE في ورقة العمل.
- تحدد الخاصية [**ObjectData**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getobjectdata/) بيانات الكائن على شكل مصفوفة البايت. سيتم عرض هذه البيانات في البرنامج المعني عند النقر المزدوج على أيقونة كائن OLE.

المثال التالي يوضح كيفية إضافة كائنات OLE إلى ورقة العمل.

```c++
#include <iostream>
#include <fstream>
#include <vector>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

std::vector<uint8_t> ReadFileToVector(const U16String& filePath) {
    std::ifstream file(filePath.ToUtf8(), std::ios::binary | std::ios::ate);
    if (!file) return {};
    std::streamsize size = file.tellg();
    file.seekg(0, std::ios::beg);
    std::vector<uint8_t> buffer(size);
    if (size > 0)
        file.read(reinterpret_cast<char*>(buffer.data()), size);
    return buffer;
}

int main() {
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    U16String imagePath = srcDir + u"logo.jpg";
    std::vector<uint8_t> imageData = ReadFileToVector(imagePath);

    U16String objectPath = srcDir + u"book1.xls";
    std::vector<uint8_t> objectData = ReadFileToVector(objectPath);
    Vector<uint8_t> data(objectData.data(), static_cast<int32_t>(objectData.size()));
    sheet.GetOleObjects().Add(14, 3, 200, 220, data);
    if (sheet.GetOleObjects().GetCount() > 0) {
        sheet.GetOleObjects().Get(0).SetObjectData(data);
    }

    workbook.Save(outDir + u"output.out.xls");
    std::cout << "OLE object added successfully." << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **استخراج كائنات OLE في الدفتر**

المثال التالي يوضح كيفية استخراج كائنات OLE في كتاب العمل. يقوم المثال بالحصول على كائنات OLE مختلفة من ملف XLS موجود ويحفظ ملفات مختلفة (DOC، XLS، PPT، PDF، إلخ) استنادًا إلى نوع تنسيق ملف كائن OLE.

بعد تشغيل الكود، يمكننا حفظ ملفات مختلفة استنادًا إلى أنواع تنسيق كائنات OLE الخاصة بها.

```c++
#include <iostream>
#include <fstream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Open the template file
    Workbook workbook(srcDir + u"book1.xls");

    // Get the OleObject Collection in the first worksheet
    OleObjectCollection oles = workbook.GetWorksheets().Get(0).GetOleObjects();

    // Loop through all the oleobjects and extract each object
    for (int32_t i = 0; i < oles.GetCount(); i++)
    {
        OleObject ole = oles.Get(i);

        // Specify the output filename
        U16String fileName = srcDir + u"ole_" + U16String(std::to_string(i).c_str()) + u".";

        // Specify each file format based on the oleobject format type
        switch (ole.GetFileFormatType())
        {
        case FileFormatType::Doc:
            fileName += u"doc";
            break;
        case FileFormatType::Xlsx:
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
            Workbook oleBook(objectData);
            oleBook.GetSettings().SetIsHidden(false);
            oleBook.Save(srcDir + u"Excel_File" + U16String(std::to_string(i).c_str()) + u".out.xlsx");
        }
        else
        {
            // Create the files based on the oleobject format types
            std::ofstream fs(fileName.ToUtf8().c_str(), std::ios::binary);
            Vector<uint8_t> objectData = ole.GetObjectData();
            fs.write(reinterpret_cast<const char*>(objectData.GetData()), objectData.GetLength());
            fs.close();
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **استخراج ملف MOL المضمن**

يدعم Aspose.Cells استخراج كائنات غير مألوفة مثل MOL (ملف بيانات جزيئية يحتوي على معلومات عن الذرات والروابط). يوضح مقتطف الشفرة التالي كيفية استخراج ملف MOL مدمج وحفظه على القرص باستخدام [ملف إكسل العينة](94896196.xlsx).

```c++
#include <iostream>
#include <fstream>
#include <string>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook(srcDir + u"EmbeddedMolSample.xlsx");

    int index = 1;

    WorksheetCollection sheets = workbook.GetWorksheets();
    for (int i = 0; i < sheets.GetCount(); i++)
    {
        Worksheet sheet = sheets.Get(i);
        OleObjectCollection oles = sheet.GetOleObjects();

        for (int j = 0; j < oles.GetCount(); j++)
        {
            OleObject ole = oles.Get(j);

            std::wstring indexWStr = std::to_wstring(index);
            U16String fileName = outDir + u"OleObject" + U16String(reinterpret_cast<const char16_t*>(indexWStr.c_str())) + u".mol";

            std::ofstream fs(fileName.ToUtf8(), std::ios::binary);
            if (fs.is_open())
            {
                Vector<uint8_t> objectData = ole.GetObjectData();
                fs.write(reinterpret_cast<const char*>(objectData.GetData()), objectData.GetLength());
                fs.close();
                index++;
            }
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **الموضوعات المتقدمة**
- [الوصول إلى وتعديل التسمية العرضية لكائن Ole المرتبط](/cells/ar/cpp/access-and-modify-the-display-label-of-the-linked-ole-object/)
- [تحديث كائن Ole تلقائيًا عبر Microsoft Excel باستخدام Aspose.Cells](/cells/ar/cpp/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/)
- [استخراج كائنات OLE من كتاب العمل](/cells/ar/cpp/extract-ole-objects-from-workbook/)
- [الحصول على معرف الفئة الخاص بكائن OLE المضمّن أو تعيينه](/cells/ar/cpp/get-or-set-the-class-identifier-of-the-embedded-ole-object/)
- [إدراج ملف WAV ككائن Ole](/cells/ar/cpp/inserting-a-wav-file-as-an-ole-object/)
{{< app/cells/assistant language="cpp" >}}
