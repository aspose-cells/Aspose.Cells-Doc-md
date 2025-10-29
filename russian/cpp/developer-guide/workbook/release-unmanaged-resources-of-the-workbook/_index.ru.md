---
title: Освободить неуправляемые ресурсы рабочей книги с помощью C++
linktitle: Освобождение неуправляемых ресурсов книги
type: docs
weight: 310
url: /ru/cpp/release-unmanaged-resources-of-the-workbook/
description: Узнайте, как освободить неуправляемые ресурсы рабочей книги с использованием Aspose.Cells и C++.
---

{{% alert color="primary" %}}

Aspose.Cells предоставляет метод [**Workbook.Dispose()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/dispose/) для освобождения неуправляемых ресурсов объекта [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/). Шаблон утилизации используется только для объектов, которые имеют доступ к неуправляемым ресурсам, таким как файлы и дескрипторы каналов, дескрипторы реестра, дескрипторы ожидания или указатели на блоки неуправляемой памяти. Это связано с тем, что сборщик мусора очень эффективен в извлечении неиспользуемых управляемых объектов, но он не способен извлекать неуправляемые объекты.

{{% /alert %}}

[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) объект теперь реализует интерфейс *IDisposable*, который имеет один метод [**Dispose()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/dispose/). Вы можете либо напрямую вызвать метод [**Workbook.Dispose()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/dispose/), либо использовать оператор *Using* для автоматического вызова этого метода.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook object
    Workbook wb1;

    // Call Dispose method
    wb1.Dispose();

    // Call Dispose method via RAII (Resource Acquisition Is Initialization)
    {
        Workbook wb2;
        // Any other code goes here
    } // wb2 is automatically disposed when it goes out of scope

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
