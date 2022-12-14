---
title: Actualizar valores de formas vinculadas
type: docs
weight: 3200
url: /es/net/refresh-values-of-linked-shapes/
---
{{% alert color="primary" %}}

 veces, tiene una forma vinculada en su archivo de Excel que está vinculada a alguna celda. En Microsoft Excel, cambiar el valor de la celda vinculada también cambia el valor de la forma vinculada. Esto también funciona bien con Aspose.Cells si desea guardar su libro de trabajo en formato XLS o XLSX. Sin embargo, si desea guardar su libro de trabajo en formato PDF o HTML, deberá llamar[**Hoja de trabajo.Formas.ActualizarValorSeleccionado()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/updateselectedvalue) para actualizar el valor de la forma vinculada.

{{% /alert %}}

## Ejemplo

 La siguiente captura de pantalla muestra el archivo fuente de Excel utilizado en el código de ejemplo a continuación. Tiene una imagen vinculada vinculada a las celdas A1 a E4. Cambiaremos el valor de la celda B4 con Aspose.Cells y luego llamaremos[**Hoja de trabajo.Formas.ActualizarValorSeleccionado()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/updateselectedvalue)para actualizar el valor de la imagen y guardarla en formato PDF.

![todo:imagen_alternativa_texto](refresh-values-of-linked-shapes_1.jpg)

Puedes descargar el[archivo fuente de Excel](95584291.xlsx) y el[PDF de salida](95584292.pdf) de los enlaces dados.

### C# código para actualizar los valores de las formas vinculadas

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-RefreshValueOfLinkedShapes-1.cs" >}}
