---
title: Запереть или разблокировать формы
linktitle: Запереть или разблокировать формы
type: docs
weight: 200
url: /ru/net/lock-or-unlock-shapes/
---

{{% alert color="primary" %}}

Иногда вам нужно защитить все формы в определенных листах, чтобы предотвратить их уничтожение нежелательными ситуациями. В этом случае вам нужно запереть все формы на указанном листе.

Иногда вам нужно иметь возможность изменять определенные формы на определенных защищенных листах, в этом случае вам нужно разблокировать эти формы.

Эта статья подробно расскажет, как запереть и разблокировать определенные формы.

{{% /alert %}}

## **Защитить все формы на указанном листе**

Чтобы защитить все формы на указанном листе, используйте метод [Worksheet.Protect( ProtectionType.Objects)](https://reference.aspose.com/cells/net/aspose.cells/worksheet/protect/#protect), как показано в следующем примере кода.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Lock-Or-Unlock-Shapes-1.cs" >}}

## **Разблокировать указанные формы на защищенном листе**

Чтобы разблокировать указанную форму в защищенном листе, используйте [shape.IsLocked](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/islocked/), как показано в следующем примере кода.

Примечание: [shape.IsLocked](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/islocked/) имеет смысл только при защищенном листе.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Lock-Or-Unlock-Shapes-2.cs" >}}

