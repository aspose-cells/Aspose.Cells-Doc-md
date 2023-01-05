---
title: Actualizar y calcular tabla dinámica con elementos calculados
type: docs
weight: 40
url: /es/net/refresh-and-calculate-pivot-table-having-calculated-items/
---
{{% alert color="primary" %}}

 Aspose.Cells ahora admite la actualización y el cálculo de tablas dinámicas con elementos calculados. Por favor use el[**Tabla dinámica.RefreshData()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/refreshdata) y[**Tabla dinámica.CaclulateData()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/calculatedata) como de costumbre para realizar esta función.

{{% /alert %}}

## **Actualizar y calcular tabla dinámica con elementos calculados**

 El siguiente código de ejemplo carga el[archivo fuente excel](5115238.xlsx)que contiene una tabla dinámica con tres elementos calculados, como "agregar", "div", "div2". Primero cambiamos el valor de la celda D2 a 20 y luego actualizamos y calculamos la tabla dinámica usando las API Aspose.Cells y guardamos el libro de trabajo en formato PDF. Los resultados en el[salida PDF](5115229.pdf) muestra que Aspose.Cells actualizó y calculó la tabla dinámica con elementos calculados correctamente. Puede verificarlo usando Microsoft Excel poniendo manualmente el valor 20 en la celda D2 y luego actualizando la tabla dinámica con la tecla de método abreviado Alt+F5 o haciendo clic en el botón Actualizar de la tabla dinámica.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-RefreshAndCalculateItems-1.cs" >}}
