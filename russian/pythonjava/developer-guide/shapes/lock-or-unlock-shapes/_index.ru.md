---
title: Запереть или разблокировать формы
linktitle: Запереть или разблокировать формы
type: docs
weight: 200
url: /ru/python-java/lock-or-unlock-shapes/
---

{{% alert color="primary" %}}

Иногда вам нужно защитить все формы в определенных листах, чтобы предотвратить их уничтожение нежелательными ситуациями. В этом случае вам нужно запереть все формы на указанном листе.

Иногда вам нужно иметь возможность изменять определенные формы на определенных защищенных листах, в этом случае вам нужно разблокировать эти формы.

Эта статья подробно расскажет, как запереть и разблокировать определенные формы.

{{% /alert %}}

## **Защитить все формы на указанном листе**

Чтобы защитить все фигуры в указанном листе, используйте метод [Worksheet.Protect(type)](https://reference.aspose.com/cells/python-java/asposecells.api/worksheet#protect(int)), как показано в следующем образце кода.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Lock-Or-Unlock-Shapes-1.py" >}}

## **Разблокировать указанные формы на защищенном листе**

Чтобы разблокировать указанную форму в защищенном листе, используйте [shape.IsLocked](https://reference.aspose.com/cells/python-java/asposecells.api/shape#IsLocked), как показано в следующем образце кода.

Примечание: [shape.IsLocked](https://reference.aspose.com/cells/python-java/asposecells.api/shape#IsLocked) имеет смысл только тогда, когда лист защищен.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Lock-Or-Unlock-Shapes-2.py" >}}

