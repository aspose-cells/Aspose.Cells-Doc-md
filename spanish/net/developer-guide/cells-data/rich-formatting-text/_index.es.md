---
title: Acceder y Actualizar las Partes de Texto Enriquecido de la Celda
linktitle: Texto con Formato Enriquecido
type: docs
weight: 40
url: /es/net/access-and-update-the-portions-of-rich-text-of-cell/
description: Aprende cómo acceder y actualizar las porciones de texto enriquecido de la celda a través de la API Aspose.Cells for .NET.
keywords: Acceder y Actualizar Texto Enriquecido de la Celda, Obtener Texto Enriquecido de la Celda, Editar Texto Enriquecido de la Celda, Acceder a Texto Enriquecido de la Celda, Actualizar Texto Enriquecido de la Celda, Cambiar Texto Enriquecido de la Celda
---

{{% alert color="primary" %}}

Aspose.Cells te permite acceder y actualizar las porciones de texto enriquecido de la celda. Para este propósito, puedes usar los métodos [**Cell.GetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters/index) y [**Cell.SetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters). Estos métodos devolverán y aceptarán el arreglo de objetos [**FontSetting**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting), que puedes usar para acceder y actualizar varias propiedades de fuente como el nombre de la fuente, color de la fuente, negrita, etc.

{{% /alert %}}

## **Acceder y actualizar partes de texto enriquecido de la celda**

El siguiente código demuestra el uso del método [**Cell.GetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters/index) y [**Cell.SetCharacters()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters) utilizando el [archivo de Excel fuente](5112369.xlsx) que puedes descargar desde el enlace proporcionado. El archivo de Excel fuente tiene un texto enriquecido en la celda A1. Tiene 3 porciones y cada porción tiene una fuente diferente. El siguiente fragmento de código accede a estas porciones y actualiza la primera porción con un nuevo nombre de fuente. Finalmente, guarda el libro de trabajo como [archivo de Excel de salida](5112366.xlsx). Cuando lo abras, verás que la fuente de la primera porción del texto se ha cambiado a 'Arial'.

### Código C# para acceder y actualizar las partes del Texto Enriquecido de la Celda

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UpdateRichTextCells-1.cs" >}}

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

