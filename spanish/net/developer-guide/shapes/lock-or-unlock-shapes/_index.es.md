---
title: Bloquear o desbloquear formas
linktitle: Bloquear o desbloquear formas
type: docs
weight: 200
url: /es/net/lock-or-unlock-shapes/
---

{{% alert color="primary" %}}

A veces, es necesario proteger todas las formas en ciertas hojas de cálculo para evitar que sean destruidas por situaciones no deseadas. En este caso, es necesario bloquear todas las formas en la hoja de cálculo especificada.

A veces, es necesario poder modificar ciertas formas en ciertas hojas de cálculo protegidas, en cuyo caso, es necesario desbloquear estas formas.

Este artículo introducirá en detalle cómo bloquear y desbloquear formas especificadas.

{{% /alert %}}

## **Proteger todas las formas en una hoja de cálculo especificada**

Para proteger todas las formas en una hoja de cálculo específica, utilice el método [Worksheet.Protect( ProtectionType.Objects)](https://reference.aspose.com/cells/net/aspose.cells/worksheet/protect/#protect), como se muestra en el siguiente código de ejemplo.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Lock-Or-Unlock-Shapes-1.cs" >}}

## **Desbloquear formas especificadas en una hoja de cálculo protegida**

Para desbloquear una forma específica en una hoja de cálculo protegida, use [shape.IsLocked](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/islocked/), como se muestra en el siguiente código de ejemplo.

Nota: [shape.IsLocked](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/islocked/) solo tiene sentido cuando la hoja de cálculo está protegida.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Lock-Or-Unlock-Shapes-2.cs" >}}

