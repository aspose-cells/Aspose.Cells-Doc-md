---
title: Actualizar valores de formas vinculadas
type: docs
weight: 3200
url: /es/net/refresh-values-of-linked-shapes/
---

{{% alert color="primary" %}}

A veces, tienes una forma vinculada en tu archivo de Excel que está vinculada a alguna celda. En Microsoft Excel, cambiar el valor de la celda vinculada también cambia el valor de la forma vinculada. Esto también funciona bien con Aspose.Cells si quieres guardar tu libro de trabajo en formato XLS o XLSX. Sin embargo, si deseas guardar tu libro de trabajo en formato PDF o HTML, entonces tendrás que llamar al método [**Worksheet.Shapes.UpdateSelectedValue()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/updateselectedvalue) para actualizar el valor de la forma vinculada.

{{% /alert %}}

## Ejemplo

La siguiente captura de pantalla muestra el archivo de Excel de origen utilizado en el código de ejemplo a continuación. Tiene una imagen vinculada a las celdas A1 a E4. Vamos a cambiar el valor de la celda B4 con Aspose.Cells y luego llamar al método [**Worksheet.Shapes.UpdateSelectedValue()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/updateselectedvalue) para actualizar el valor de la imagen y guardarlo en formato PDF.

![todo:image_alt_text](refresh-values-of-linked-shapes_1.jpg)

Puedes descargar el [archivo de Excel de origen](95584291.xlsx) y el [PDF de salida](95584292.pdf) a través de los enlaces proporcionados.

### Código C# para actualizar los valores de las formas vinculadas

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-RefreshValueOfLinkedShapes-1.cs" >}}
