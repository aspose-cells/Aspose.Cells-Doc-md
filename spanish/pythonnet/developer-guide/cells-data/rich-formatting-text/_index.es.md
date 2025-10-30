---
title: Acceder y Actualizar las Partes de Texto Enriquecido de la Celda
linktitle: Texto con Formato Enriquecido
type: docs
weight: 40
url: /es/python-net/access-and-update-the-portions-of-rich-text-of-cell/
description: Aprenda a acceder y actualizar las partes de texto enriquecido de la celda a través de la API Aspose.Cells para Python via .NET.
keywords: Biblioteca de Python para Excel, Acceso y Actualización de Texto Enriquecido de Celda en Python, Obtener Texto Enriquecido de Celda en Python, Editar Texto Enriquecido de Celda en Python, Acceder a Texto Enriquecido de Celda en Python, Actualizar Texto Enriquecido de Celda en Python, Cambiar Texto Enriquecido de Celda en Python.
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET le permite acceder y actualizar las partes del texto enriquecido de la celda. Para este propósito, puede utilizar los métodos [**Cell.get_characters()**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_characters/#) y [**Cell.set_characters()**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_characters/#list). Estos métodos devolverán y aceptarán la matriz de objetos [**FontSetting**](https://reference.aspose.com/cells/python-net/aspose.cells/fontsetting) que puede utilizar para acceder y actualizar varias propiedades de fuente como el nombre de la fuente, el color de la fuente, la negrita, etc.

{{% /alert %}}

## **Acceder y actualizar partes de texto enriquecido de la celda**

El siguiente código demuestra el uso de los métodos [**Cell.get_characters()**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_characters/#) y [**Cell.set_characters()**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/set_characters/#list) utilizando el [archivo de Excel fuente](5112369.xlsx) que puede descargar desde el enlace proporcionado. El archivo de Excel fuente tiene un texto enriquecido en la celda A1. Tiene 3 partes y cada parte tiene una fuente diferente. El fragmento de código siguiente accede a estas partes y actualiza la primera parte con un nuevo nombre de fuente. Finalmente, guarda el libro de trabajo como [archivo de Excel de salida](5112366.xlsx). Cuando lo abra, encontrará que la fuente de la primera parte del texto ha cambiado a **"Arial"**.

### Código C# para acceder y actualizar las partes del Texto Enriquecido de la Celda

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-UpdateRichTextCells-1.py" >}}

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

{{< app/cells/assistant language="python-net" >}}
