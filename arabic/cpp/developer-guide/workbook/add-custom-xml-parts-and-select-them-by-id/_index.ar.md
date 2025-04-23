---
title: إضافة أجزاء XML مخصصة وتحديدها بواسطة معرف ID باستخدام C++
linktitle: إضافة أجزاء XML مخصصة وتحديدها حسب الهوية
type: docs
weight: 70
url: /ar/cpp/add-custom-xml-parts-and-select-them-by-id/
description: تعلم كيفية إضافة أجزاء XML مخصصة وتحديدها في ملفات إكسل باستخدام Aspose.Cells مع C++.
---

## **سيناريوهات الاستخدام المحتملة**

أجزاء XML مخصصة هي بيانات XML مخزنة داخل مستندات Microsoft Excel وتستخدمها التطبيقات التي تتفاعل معها. لا توجد طريقة مباشرة لإضافتها باستخدام واجهة مستخدم Microsoft Excel في الوقت الحالي. ومع ذلك، يمكنك إضافتها برمجياً بطرق مختلفة، مثل استخدام VSTO أو Aspose.Cells. استخدم طريقة [**Workbook.CustomXmlParts.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpartcollection/add/) لإضافة جزء XML مخصص باستخدام واجهة برمجة تطبيقات Aspose.Cells. يمكنك أيضًا تعيين معرفها باستخدام الخاصية [**CustomXmlPart.GetID()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpart/getid/). بالمثل، إذا كنت تريد تحديد جزء XML مخصص باستخدام المعرف، يمكنك استخدام طريقة [**Workbook.CustomXmlParts.SelectByID()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpartcollection/selectbyid/).

## **إضافة أجزاء XML مخصصة وتحديدها حسب الهوية**

في المثال التالي، تضاف أولاً أربعة أجزاء XML مخصصة باستخدام طريقة [**Workbook.CustomXmlParts.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpartcollection/add/). ثم يتم تعيين معرفاتها باستخدام الخاصية [**CustomXmlPart.GetID()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpart/getid/). أخيرًا، يتم العثور على أحد أجزاء XML المخصصة المضافة أو تحديده باستخدام طريقة [**Workbook.CustomXmlParts.SelectByID()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpartcollection/selectbyid/). يرجى أيضًا الاطلاع على مخرجات وحدة التحكم للكود المقدم أدناه للمرجعية.

## **الكود المثالي**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Markup;

int main()
{
    Aspose::Cells::Startup();

    // Create empty workbook
    Workbook wb;

    // Some data in the form of byte array
    // Please use correct XML and Schema instead
    Vector<uint8_t> btsData = { 1, 2, 3 };
    Vector<uint8_t> btsSchema = { 1, 2, 3 };

    // Create four custom xml parts
    wb.GetCustomXmlParts().Add(btsData, btsSchema);
    wb.GetCustomXmlParts().Add(btsData, btsSchema);
    wb.GetCustomXmlParts().Add(btsData, btsSchema);
    wb.GetCustomXmlParts().Add(btsData, btsSchema);

    // Assign ids to custom xml parts
    wb.GetCustomXmlParts().Get(0).SetID(u"Fruit");
    wb.GetCustomXmlParts().Get(1).SetID(u"Color");
    wb.GetCustomXmlParts().Get(2).SetID(u"Sport");
    wb.GetCustomXmlParts().Get(3).SetID(u"Shape");

    // Specify search custom xml part id
    U16String srchID = u"Fruit";
    srchID = u"Color";
    srchID = u"Sport";

    // Search custom xml part by the search id
    CustomXmlPart cxp = wb.GetCustomXmlParts().SelectByID(srchID);

    // Print the found or not found message on console
    if (cxp.IsNull())
    {
        std::cout << "Not Found: CustomXmlPart ID " << srchID.ToUtf8() << std::endl;
    }
    else
    {
        std::cout << "Found: CustomXmlPart ID " << srchID.ToUtf8() << std::endl;
    }

    std::cout << "AddCustomXMLPartsAndSelectThemByID executed successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **مخرجات الوحدة**

{{< highlight java >}}
Found: CustomXmlPart ID Sport
{{< /highlight >}}
