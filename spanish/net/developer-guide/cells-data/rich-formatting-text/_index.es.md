---
title: Acceda y actualice las porciones de texto enriquecido de Cell
linktitle: Texto con formato enriquecido
type: docs
weight: 40
url: /es/net/access-and-update-the-portions-of-rich-text-of-cell/
---
{{% alert color="primary" %}}

 Aspose.Cells le permite acceder y actualizar las partes del texto enriquecido de la celda. Para este propósito, puede utilizar[**Cell.ObtenerCaracteres()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters/index) y[**Cell.Establecer caracteres()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters) métodos. Estos métodos devolverán y aceptarán la matriz de[**Configuración de fuente**](https://reference.aspose.com/cells/net/aspose.cells/fontsetting)objetos que puede usar para acceder y actualizar varias propiedades de la fuente, como el nombre de la fuente, el color de la fuente, la negrita, etc.

{{% /alert %}}

## **Acceda y actualice las porciones de texto enriquecido de Cell**

 El siguiente código demuestra el uso de[**Cell.ObtenerCaracteres()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getcharacters/index) y[**Cell.Establecer caracteres()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/setcharacters) método usando el[archivo fuente excel](5112369.xlsx)que puede descargar desde el enlace proporcionado. El archivo fuente de Excel tiene un texto enriquecido en la celda A1. Tiene 3 porciones y cada porción tiene una fuente diferente. El siguiente fragmento de código accede a estas partes y actualiza la primera parte con un nuevo nombre de fuente. Finalmente, guarda el libro de trabajo como[archivo de salida de Excel](5112366.xlsx) . Cuando lo abra, encontrará que la fuente de la primera parte del texto ha cambiado a**"arial"**.

### C# código para acceder y actualizar las partes de texto enriquecido de Cell

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UpdateRichTextCells-1.cs" >}}

### Salida de la consola generada por el código de muestra

 Aquí está la salida de la consola del código de muestra anterior usando el[archivo fuente excel](5112369.xlsx).

{{< highlight "java" >}}

Before updating the font settings....

Century

Courier New

Verdana

After updating the font settings....

Arial

Courier New

Verdana

{{< /highlight >}}

