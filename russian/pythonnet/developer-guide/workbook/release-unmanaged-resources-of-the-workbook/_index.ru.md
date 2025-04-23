---
title: Освободить неуправляемые ресурсы рабочей книги с помощью Python via .NET
linktitle: Освободить неуправляемые ресурсы
type: docs
weight: 310
url: /ru/python-net/release-unmanaged-resources-of-the-workbook/
description: Узнайте, как правильно освобождать неуправляемые ресурсы при работе с рабочими книгами Excel с использованием Aspose.Cells для Python via .NET.
---

{{% alert color="primary" %}}

Aspose.Cells предоставляет метод [**workbook.close()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/close/) для освобождения неуправляемых ресурсов объекта [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook). Этот паттерн важен для обработки неуправляемых ресурсов, таких как файловые дескрипторы, потоки или выделение памяти, которые не управляются автоматически сборщиком мусора Python.

{{% /alert %}}

Класс [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) реализует протокол менеджера контекста Python для управления ресурсами. Вы можете явно вызвать метод [**close()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/close/) или использовать оператор `with` Python для обеспечения правильной очистки.

```python
from aspose.cells import Workbook

# Create workbook object
    with aspose.cells.Workbook() as wb:
         wb.save("dispose.xlsx")
         pass
```
