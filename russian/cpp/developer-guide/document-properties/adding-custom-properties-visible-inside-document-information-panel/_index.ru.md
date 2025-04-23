---
title: Добавление пользовательских свойств, видимых в панели информации о документе с C++
linktitle: Добавление пользовательских свойств, видимых в панели информации о документе
type: docs
weight: 300
url: /ru/cpp/adding-custom-properties-visible-inside-document-information-panel/
description: Узнайте, как добавить пользовательские свойства, видимые в панели информации о документе, с помощью Aspose.Cells и C++.
---

## **Добавление пользовательских свойств, видимых в панели информации о документе**

Aspose.Cells можно использовать для добавления пользовательских свойств внутри объекта книги, которые видны внутри панели информации о документе. Вы можете открыть панель информации о документе в Microsoft Excel, используя команды меню Файл > Сведения > Свойства > Показать панель документа.

Пожалуйста, используйте метод [**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/contenttypepropertycollection/add/) для добавления пользовательского свойства, которое будет отображаться в Панели информации о документе.

Следующий пример кода добавляет два пользовательских свойства. Первое свойство без типа, а второе с типом DateTime. После открытия созданного этим кодом файла Excel вы увидите эти два свойства в Панели информации о документе.

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

    // Create workbook object with specified format
    Workbook workbook(FileFormatType::Xlsx);

    // Add simple property without any type
    workbook.GetContentTypeProperties().Add(u"MK31", u"Simple Data");

    // Add date time property with type
    workbook.GetContentTypeProperties().Add(u"MK32", u"04-Mar-2015", u"DateTime");

    // Save the workbook
    workbook.Save(srcDir + u"AddingCustomPropertiesVisible_out.xlsx");

    std::cout << "Custom properties added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Связанная статья**

{{% alert color="primary" %}}

- [Использование пользовательских XML-частей в Aspose.Cells](/cells/ru/cpp/use-custom-xml-parts-in-aspose-cells/)

{{% /alert %}}
