---
title: Bloquear o desbloquear formas
linktitle: Bloquear o desbloquear formas
type: docs
weight: 200
url: /es/python-net/lock-or-unlock-shapes/
---

{{% alert color="primary" %}}

A veces, es necesario proteger todas las formas en ciertas hojas de cálculo para evitar que sean destruidas por situaciones no deseadas. En este caso, es necesario bloquear todas las formas en la hoja de cálculo especificada.

A veces, es necesario poder modificar ciertas formas en ciertas hojas de cálculo protegidas, en cuyo caso, es necesario desbloquear estas formas.

Este artículo introducirá en detalle cómo bloquear y desbloquear formas especificadas.

{{% /alert %}}

## **Proteger todas las formas en una hoja de cálculo especificada**

Para proteger todas las formas en una hoja de cálculo especificada, utiliza el método [Worksheet.Protect(type)](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/protect/#aspose.cells.ProtectionType), como se muestra en el siguiente código de ejemplo.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Lock-Or-Unlock-Shapes-1.py" >}}

## **Desbloquear formas especificadas en una hoja de cálculo protegida**

Para desbloquear una forma especificada en una hoja de cálculo protegida, utiliza [shape.is_locked](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/is_locked/), como se muestra en el siguiente código de ejemplo.

Nota: [shape.is_locked](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/is_locked/) solo tiene sentido cuando la hoja de cálculo está protegida.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Lock-Or-Unlock-Shapes-2.py" >}}

{{< app/cells/assistant language="python-net" >}}
