---
title: Запереть или разблокировать формы
linktitle: Запереть или разблокировать формы
type: docs
weight: 200
url: /ru/cpp/lock-or-unlock-shapes/
---

{{% alert color="primary" %}}

Иногда вам нужно защитить все формы в определенных листах, чтобы предотвратить их уничтожение нежелательными ситуациями. В этом случае вам нужно запереть все формы на указанном листе.

Иногда вам нужно иметь возможность изменять определенные формы на определенных защищенных листах, в этом случае вам нужно разблокировать эти формы.

Эта статья подробно расскажет, как запереть и разблокировать определенные формы.

{{% /alert %}}

## **Защитить все формы на указанном листе**

Чтобы защитить все формы на указанном листе, используйте метод [Worksheet.Protect(ProtectionType)](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/protect/), как показано в следующем образцовом коде.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Lock-Or-Unlock-Shapes-1.cpp" >}}

## **Разблокировать указанные формы на защищенном листе**

Чтобы разблокировать указанную форму на защищенном листе, используйте [shape.IsLocked](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/islocked/) и [shape.SetIsLocked](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/setislocked/), как показано в следующем образцовом коде.

Примечание: [shape.IsLocked](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/islocked/) и [shape.SetIsLocked](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/setislocked/) имеют смысл только при защищенном листе.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Lock-Or-Unlock-Shapes-2.cpp" >}}

{{< app/cells/assistant language="cpp" >}}
