---
title: Запереть или разблокировать формы
linktitle: Запереть или разблокировать формы
type: docs
weight: 200
url: /ru/python-net/lock-or-unlock-shapes/
---

{{% alert color="primary" %}}

Иногда вам нужно защитить все формы в определенных листах, чтобы предотвратить их уничтожение нежелательными ситуациями. В этом случае вам нужно запереть все формы на указанном листе.

Иногда вам нужно иметь возможность изменять определенные формы на определенных защищенных листах, в этом случае вам нужно разблокировать эти формы.

Эта статья подробно расскажет, как запереть и разблокировать определенные формы.

{{% /alert %}}

## **Защитить все формы на указанном листе**

Чтобы защитить все формы на указанном листе, используйте метод [Worksheet.Protect(type)](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/protect/#aspose.cells.ProtectionType), как показано в следующем примере кода.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Lock-Or-Unlock-Shapes-1.py" >}}

## **Разблокировать указанные формы на защищенном листе**

Чтобы разблокировать определенную форму в защищенном листе, используйте [shape.is_locked](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/is_locked/), как показано в следующем образце кода.

Примечание: [shape.is_locked](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/is_locked/) имеет смысл только при защищенном листе.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Lock-Or-Unlock-Shapes-2.py" >}}

{{< app/cells/assistant language="python-net" >}}
