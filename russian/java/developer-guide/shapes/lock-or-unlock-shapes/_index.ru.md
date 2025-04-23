---
title: Запереть или разблокировать формы
linktitle: Запереть или разблокировать формы
type: docs
weight: 200
url: /ru/java/lock-or-unlock-shapes/
---

{{% alert color="primary" %}}

Иногда вам нужно защитить все формы в определенных листах, чтобы предотвратить их уничтожение нежелательными ситуациями. В этом случае вам нужно запереть все формы на указанном листе.

Иногда вам нужно иметь возможность изменять определенные формы на определенных защищенных листах, в этом случае вам нужно разблокировать эти формы.

Эта статья подробно расскажет, как запереть и разблокировать определенные формы.

{{% /alert %}}

## **Защитить все формы на указанном листе**

Чтобы защитить все формы на указанном листе, используйте метод [Worksheet.protect(int type)](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet/#protect-int-), как показано в следующем образце кода.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Lock-Or-Unlock-Shapes-1.java" >}}

## **Разблокировать указанные формы на защищенном листе**

Чтобы разблокировать указанную форму на защищенном листе, используйте [shape.IsLocked](https://reference.aspose.com/cells/java/com.aspose.cells/shape/#isLocked--) и [shape.setLocked](https://reference.aspose.com/cells/java/com.aspose.cells/shape/#setLocked-boolean-), как показано в следующем образце кода.

Примечание: [shape.IsLocked](https://reference.aspose.com/cells/java/com.aspose.cells/shape/#isLocked--) и [shape.setLocked](https://reference.aspose.com/cells/java/com.aspose.cells/shape/#setLocked-boolean-) имеют смысл только в том случае, если лист защищен.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Lock-Or-Unlock-Shapes-2.java" >}}

{{< app/cells/assistant language="java" >}}
