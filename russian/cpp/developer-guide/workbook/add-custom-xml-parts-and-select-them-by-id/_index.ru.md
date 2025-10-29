---
title: Добавляйте пользовательские XML части и выбирайте их по ID с помощью C++
linktitle: Добавление пользовательских XML частей и выбор их по идентификатору
type: docs
weight: 70
url: /ru/cpp/add-custom-xml-parts-and-select-them-by-id/
description: Узнайте, как добавлять и выбирать пользовательские XML части в файлах Excel, используя Aspose.Cells и C++.
---

## **Возможные сценарии использования**

Пользовательские XML-части — это XML-данные, хранящиеся внутри документов Microsoft Excel и используемые приложениями, взаимодействующими с ними. В настоящее время нет прямого способа добавления их через пользовательский интерфейс Microsoft Excel. Однако их можно добавлять программным способом различными способами, например, с помощью VSTO или Aspose.Cells. Используйте метод [**Workbook.CustomXmlParts.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpartcollection/add/) для добавления пользовательской XML-части с помощью API Aspose.Cells. Также можно установить её ID с помощью свойства [**CustomXmlPart.GetID()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpart/getid/). Аналогично, если вы хотите выбрать пользовательскую XML-часть по ID, используйте метод [**Workbook.CustomXmlParts.SelectByID()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpartcollection/selectbyid/).

## **Добавление пользовательских XML-частей и выбор их по идентификатору**

Следующий пример кода сначала добавляет четыре пользовательские XML-части с помощью метода [**Workbook.CustomXmlParts.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpartcollection/add/). Затем он устанавливает их ID с помощью свойства [**CustomXmlPart.GetID()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpart/getid/). В конце он находит или выбирает одну из добавленных пользовательских XML-частей с помощью метода [**Workbook.CustomXmlParts.SelectByID()**](https://reference.aspose.com/cells/cpp/aspose.cells.markup/customxmlpartcollection/selectbyid/). Также для справки приводится вывод кода в консоли ниже.

## **Образец кода**

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

## **Вывод в консоль**

{{< highlight java >}}
Found: CustomXmlPart ID Sport
{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
