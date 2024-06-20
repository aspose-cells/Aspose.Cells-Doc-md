---
title: Bloquear o desbloquear formas
linktitle: Bloquear o desbloquear formas
type: docs
weight: 200
url: /es/python-java/lock-or-unlock-shapes/
---

{{% alert color="primary" %}}

A veces, es necesario proteger todas las formas en ciertas hojas de cálculo para evitar que sean destruidas por situaciones no deseadas. En este caso, es necesario bloquear todas las formas en la hoja de cálculo especificada.

A veces, es necesario poder modificar ciertas formas en ciertas hojas de cálculo protegidas, en cuyo caso, es necesario desbloquear estas formas.

Este artículo introducirá en detalle cómo bloquear y desbloquear formas especificadas.

{{% /alert %}}

## **Proteger todas las formas en una hoja de cálculo especificada**

Para proteger todas las formas en una hoja de cálculo especificada, use el método [Worksheet.Protect(type)](https://reference.aspose.com/cells/python-java/asposecells.api/worksheet#protect(int)), como se muestra en el siguiente código de ejemplo.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Lock-Or-Unlock-Shapes-1.py" >}}

## **Desbloquear formas especificadas en una hoja de cálculo protegida**

Para desbloquear una forma especificada en una hoja de cálculo protegida, use [shape.IsLocked](https://reference.aspose.com/cells/python-java/asposecells.api/shape#IsLocked), como se muestra en el siguiente código de ejemplo.

Nota: [shape.IsLocked](https://reference.aspose.com/cells/python-java/asposecells.api/shape#IsLocked) solo tiene sentido cuando la hoja de cálculo está protegida.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Lock-Or-Unlock-Shapes-2.py" >}}

