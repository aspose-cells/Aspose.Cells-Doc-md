---
title: Acceder y Actualizar las Partes de Texto Enriquecido de la Celda
linktitle: Texto con Formato Enriquecido
type: docs
weight: 40
url: /es/nodejs-cpp/access-and-update-the-portions-of-rich-text-of-cell/
description: Aprende cómo acceder y actualizar las porciones del texto enriquecido de una celda mediante la API Aspose.Cells for Node.js via C++.
keywords: Acceder y Actualizar Texto Enriquecido de la Celda, Obtener Texto Enriquecido de la Celda, Editar Texto Enriquecido de la Celda, Acceder a Texto Enriquecido de la Celda, Actualizar Texto Enriquecido de la Celda, Cambiar Texto Enriquecido de la Celda
---

{{% alert color="primary" %}}

Aspose.Cells for Node.js via C++ permite acceder y actualizar las porciones del texto enriquecido de la celda. Para ello, puedes usar los métodos [**Cell.getCharacters()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getCharacters--) y [**Cell.setCharacters()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setCharacters-fontsettingarray-). Estos métodos devolverán y aceptarán un arreglo de objetos [**FontSetting**](https://reference.aspose.com/cells/nodejs-cpp/fontsetting) que puedes usar para acceder y actualizar varias propiedades de la fuente, como nombre de fuente, color de fuente, negrita, etc.

{{% /alert %}}

## **Acceder y actualizar partes de texto enriquecido de la celda**

El siguiente código demuestra el uso de los métodos [**Cell.getCharacters()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getCharacters--) y [**Cell.setCharacters()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setCharacters-fontsettingarray-) usando el [archivo Excel fuente](5112369.xlsx) que puedes descargar desde el enlace proporcionado. El archivo Excel fuente tiene texto enriquecido en la celda A1 con 3 porciones, cada una con una fuente diferente. El código accede a estas porciones y actualiza la primera con un nuevo nombre de fuente. Finalmente, guarda el libro como [archivo Excel de salida](5112366.xlsx). Cuando lo abras, notarás que la fuente de la primera porción del texto ha cambiado a **"Arial"**.

### Código Nodejs para acceder y actualizar las porciones del Texto Enriquecido de una Celda

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "UpdateRichTextCells-1.js" >}}

### Salida de consola generada por el código de ejemplo

Aquí está la salida de la consola del código de ejemplo anterior utilizando el [archivo de Excel fuente](5112369.xlsx).

{{< highlight java >}}

Before updating the font settings....

Century

Courier New

Verdana

After updating the font settings....

Arial

Courier New

Verdana

{{< /highlight >}}

