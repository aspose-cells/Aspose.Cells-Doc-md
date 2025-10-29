---
title: Получить или установить идентификатор класса встроенного Ole объекта с помощью C++
linktitle: Получение или установка идентификатора класса встроенного объекта OLE
type: docs
weight: 200
url: /ru/cpp/get-or-set-the-class-identifier-of-the-embedded-ole-object/
description: Узнайте, как получать или устанавливать идентификатор класса встроенных Ole объектов с помощью Aspose.Cells и C++.
---

## **Возможные сценарии использования**
Aspose.Cells предоставляет свойство [OleObject.GetClassIdentifier()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getclassidentifier/), которое можно использовать для получения или установки идентификатора класса встроенного Ole-объекта. Идентификаторы класса Ole-объектов — это фактически GUIDы, то есть глобальные уникальные идентификаторы. GUID всегда имеет длину 16 байт, и идентификаторы классов тоже длиной 16 байт. Они часто находятся внутри реестра Windows и предоставляют информацию хост-приложению о том, как открывать встроенные Ole-объекты, содержащие разные встроенные ресурсы внутри клиентского приложения.

## **Получение или установка идентификатора класса встроенного объекта OLE**
Следующий скриншот показывает идентификатор класса Ole-объекта, то есть GUID, который был прочитан из [образца файла Excel](5115190.xls), содержащего встроенный Ole-объект PowerPoint.

![todo:image_alt_text](get-or-set-the-class-identifier-of-the-embedded-ole-object_1.png)

### **Образец кода**
Посмотрите следующий пример кода, выполненный с помощью [образца файла Excel](5115190.xls), и его вывод в консоль, который показывает идентификатор класса Ole-объекта, то есть GUID. Выведенный GUID точно такой же, как указано внутри скриншота.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
#include <guiddef.h>

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    Workbook wb(srcDir + u"sample.xls");
    Worksheet ws = wb.GetWorksheets().Get(0);
    OleObject oleObj = ws.GetOleObjects().Get(0);

    Vector<uint8_t> classIdentifier = oleObj.GetClassIdentifier();
    GUID guid;
    memcpy(&guid, classIdentifier.GetData(), sizeof(GUID));

    char guidStr[39];
    snprintf(guidStr, sizeof(guidStr), "{%08X-%04X-%04X-%02X%02X-%02X%02X%02X%02X}",
             guid.Data1, guid.Data2, guid.Data3,
             guid.Data4[0], guid.Data4[1], guid.Data4[2], guid.Data4[3],
             guid.Data4[4], guid.Data4[5], guid.Data4[6], guid.Data4[7]);

    std::cout << guidStr << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Вывод в консоль**
Это консольный вывод вышеуказанного образца кода при выполнении с [образцовым файлом Excel](5115190.xls).

{{< highlight java >}}
DC020317-E6E2-4A62-B9FA-B3EFE16626F4
{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
