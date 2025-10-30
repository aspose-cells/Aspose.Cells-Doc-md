---
title: Acceder a la Caja de Texto por Nombre con Golang a través de C++
linktitle: Acceda al cuadro de texto por el nombre
type: docs
weight: 230
url: /es/go-cpp/access-the-text-box-by-the-name/
description: Aprenda cómo acceder a un cuadro de texto por su nombre usando Aspose.Cells for C++.
---

## Acceda al cuadro de texto por el nombre

Anteriormente, los cuadros de texto se accedían por índice desde la colección [**Worksheet.GetTextBoxes()**](https://reference.aspose.com/cells/go-cpp/worksheet/gettextboxes/), pero ahora también puede acceder al cuadro de texto por su nombre en esta colección. Esto es una forma conveniente y rápida de acceder a su cuadro de texto si ya conoce su nombre.

El siguiente código de ejemplo primero crea un cuadro de texto y le asigna un texto y un nombre. Luego, en las siguientes líneas, accedemos al mismo cuadro de texto por su nombre y imprimimos su texto.

### Código C++ para acceder al cuadro de texto por nombre

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AccessTheTextBoxByTheName.go" >}}
### Salida de consola generada por el código de ejemplo

Aquí está la salida en consola del código de muestra anterior.

{{< highlight java >}}

This is MyTextBox

{{< /highlight >}}
