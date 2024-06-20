---
title: Bloquear o desbloquear formas
linktitle: Bloquear o desbloquear formas
type: docs
weight: 200
url: /es/java/lock-or-unlock-shapes/
---

{{% alert color="primary" %}}

A veces, es necesario proteger todas las formas en ciertas hojas de cálculo para evitar que sean destruidas por situaciones no deseadas. En este caso, es necesario bloquear todas las formas en la hoja de cálculo especificada.

A veces, es necesario poder modificar ciertas formas en ciertas hojas de cálculo protegidas, en cuyo caso, es necesario desbloquear estas formas.

Este artículo introducirá en detalle cómo bloquear y desbloquear formas especificadas.

{{% /alert %}}

## **Proteger todas las formas en una hoja de cálculo especificada**

Para proteger todas las formas en una hoja de cálculo especificada, utilice el método [Worksheet.protect(int tipo)](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet/#protect-int-), como se muestra en el siguiente código de ejemplo.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Lock-Or-Unlock-Shapes-1.java" >}}

## **Desbloquear formas especificadas en una hoja de cálculo protegida**

Para desbloquear una forma especificada en una hoja de cálculo protegida, utilice [shape.IsLocked](https://reference.aspose.com/cells/java/com.aspose.cells/shape/#isLocked--) y [shape.setLocked](https://reference.aspose.com/cells/java/com.aspose.cells/shape/#setLocked-boolean-), como se muestra en el siguiente código de ejemplo.

Nota: [shape.IsLocked](https://reference.aspose.com/cells/java/com.aspose.cells/shape/#isLocked--) y [shape.setLocked](https://reference.aspose.com/cells/java/com.aspose.cells/shape/#setLocked-boolean-) solo tienen sentido cuando la hoja de cálculo está protegida.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Lock-Or-Unlock-Shapes-2.java" >}}

