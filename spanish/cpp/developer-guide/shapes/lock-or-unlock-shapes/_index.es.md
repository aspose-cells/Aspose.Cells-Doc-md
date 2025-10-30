---
title: Bloquear o desbloquear formas
linktitle: Bloquear o desbloquear formas
type: docs
weight: 200
url: /es/cpp/lock-or-unlock-shapes/
---

{{% alert color="primary" %}}

A veces, es necesario proteger todas las formas en ciertas hojas de cálculo para evitar que sean destruidas por situaciones no deseadas. En este caso, es necesario bloquear todas las formas en la hoja de cálculo especificada.

A veces, es necesario poder modificar ciertas formas en ciertas hojas de cálculo protegidas, en cuyo caso, es necesario desbloquear estas formas.

Este artículo introducirá en detalle cómo bloquear y desbloquear formas especificadas.

{{% /alert %}}

## **Proteger todas las formas en una hoja de cálculo especificada**

Para proteger todas las formas en una hoja de cálculo específica, use el método [Worksheet.Protect(ProtectionType)](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/protect/), como se muestra en el siguiente código de muestra.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Lock-Or-Unlock-Shapes-1.cpp" >}}

## **Desbloquear formas especificadas en una hoja de cálculo protegida**

Para desbloquear una forma específica en una hoja de cálculo protegida, use [shape.IsLocked](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/islocked/) y [shape.SetIsLocked](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/setislocked/), como se muestra en el siguiente código de muestra.

Nota: [shape.IsLocked](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/islocked/) y [shape.SetIsLocked](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/setislocked/) son significativos solo cuando la hoja de cálculo está protegida.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Lock-Or-Unlock-Shapes-2.cpp" >}}

{{< app/cells/assistant language="cpp" >}}
