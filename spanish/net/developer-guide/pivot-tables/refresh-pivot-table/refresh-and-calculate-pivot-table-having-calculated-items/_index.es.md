---
title: Actualizar y Calcular tabla dinámica con elementos calculados
type: docs
weight: 40
url: /es/net/refresh-and-calculate-pivot-table-having-calculated-items/
---

{{% alert color="primary" %}}

Ahora Aspose.Cells admite refrescar y calcular tabla dinámica con elementos calculados. Utilice [**PivotTable.RefreshData()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/refreshdata) y [**PivotTable.CaclulateData()**](https://reference.aspose.com/cells/net/aspose.cells.pivot/pivottable/methods/calculatedata) como de costumbre para realizar esta función.

{{% /alert %}}

## **Actualizar y Calcular Tabla Dinámica con Elementos Calculados**

El siguiente código de muestra carga el [archivo de Excel de origen](5115238.xlsx) que contiene una tabla dinámica con tres elementos calculados como "sumar", "dividir", "dividir2". Primero cambiamos el valor de la celda D2 a 20 y luego refrescamos y calculamos la tabla dinámica usando las API de Aspose.Cells y guardamos el libro de trabajo en formato PDF. Los resultados en el [PDF de salida](5115229.pdf) muestran que Aspose.Cells refrescó y calculó la tabla dinámica con elementos calculados correctamente. Puede verificarlo utilizando Microsoft Excel poniendo manualmente el valor 20 en la celda D2 y luego actualizando la tabla dinámica mediante la tecla de acceso directo Alt+F5 o haciendo clic en el botón Actualizar tabla dinámica.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-RefreshAndCalculateItems-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
