---
title: Actualizar y Calcular tabla dinámica con elementos calculados
type: docs
weight: 40
url: /es/nodejs-cpp/refresh-and-calculate-pivot-table-having-calculated-items/
---

{{% alert color="primary" %}}

Aspose.Cells for Node.js via C++ ahora soporta la actualización y el cálculo de tablas dinámicas con elementos calculados. Por favor, usa los métodos [**PivotTable.refreshData**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#refreshdata--) y [**PivotTable.calculateData**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#calculatedata--) como de costumbre para realizar esta función.

{{% /alert %}}

## **Actualizar y Calcular Tabla Dinámica con Elementos Calculados**

El siguiente código de ejemplo carga el archivo de Excel fuente ([source excel file](5115238.xlsx)) que contiene una tabla dinámica con tres elementos calculados como "add", "div", "div2". Primero cambiamos el valor de la celda D2 a 20 y luego actualizamos y calculamos la tabla dinámica usando las API de Aspose.Cells for Node.js via C++ y guardamos el libro en formato PDF. Los resultados en el [PDF generado](5115229.pdf) muestran que Aspose.Cells for Node.js via C++ actualizó y calculó correctamente la tabla dinámica con elementos calculados. Puedes verificarlo usando Microsoft Excel ingresando manualmente el valor 20 en la celda D2 y luego actualizando la tabla dinámica con la tecla de método abreviado Alt+F5 o haciendo clic en el botón de actualización de la tabla dinámica.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTable-RefreshAndCalculateItems-1.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
