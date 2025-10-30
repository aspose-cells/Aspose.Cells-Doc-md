---
title: Actualizar valores de formas vinculadas
type: docs
weight: 3200
url: /es/python-net/refresh-values-of-linked-shapes/
---

{{% alert color="primary" %}}

A veces, tienes una forma vinculada en tu archivo de Excel que está vinculada a alguna celda. En Microsoft Excel, cambiar el valor de la celda vinculada también cambia el valor de la forma vinculada. Esto también funciona bien con Aspose.Cells para Python via .NET si deseas guardar tu libro en formato XLS o XLSX. Sin embargo, si quieres guardar tu libro en formato PDF o HTML, entonces tendrás que llamar al método [**Worksheet.Shapes.update_selected_value()**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/update_selected_value) para actualizar el valor de la forma vinculada.

{{% /alert %}}

## Ejemplo

La siguiente captura de pantalla muestra el archivo Excel fuente utilizado en el código de ejemplo a continuación. Tiene una imagen vinculada vinculada a las celdas A1 a E4. Cambiaremos el valor de la celda B4 con Aspose.Cells para Python via .NET y luego llamaremos al método [**Worksheet.Shapes.update_selected_value()**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/update_selected_value) para actualizar el valor de la imagen y guardarla en formato PDF.

![todo:image_alt_text](refresh-values-of-linked-shapes_1.jpg)

Puedes descargar el [archivo de Excel de origen](95584291.xlsx) y el [PDF de salida](95584292.pdf) a través de los enlaces proporcionados.

### Código C# para actualizar los valores de las formas vinculadas

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-RefreshValueOfLinkedShapes-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
