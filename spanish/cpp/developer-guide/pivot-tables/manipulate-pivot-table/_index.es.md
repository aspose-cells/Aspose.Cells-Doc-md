---
title: Manipular Tabla Dinámica
type: docs
weight: 20
url: /es/cpp/manipulate-pivot-table/
---

## **Escenarios de uso posibles**
Además de crear nuevas tablas dinámicas, puedes manipular las tablas dinámicas nuevas y existentes. Puedes cambiar los datos en el rango de origen de la tabla dinámica y luego actualizarlos y calcularlos para obtener los nuevos valores de las celdas de la tabla dinámica. Por favor, utiliza los métodos [PivotTable.RefreshData()](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/refreshdata/) y [PivotTable.CalculateData()](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/calculatedata/) después de haber cambiado los valores en el rango de origen de la tabla dinámica para actualizarla.
## **Manipular Tabla Dinámica**
El siguiente código de ejemplo carga el [archivo de Excel de ejemplo](23167013.xlsx) y accede a la tabla dinámica existente en su primera hoja de cálculo. Cambia el valor de la celda B3 que está dentro del rango de origen de la tabla dinámica y luego actualiza la tabla dinámica. Antes de actualizarla, accede al valor de la celda de la tabla dinámica H8, que es 15 y después de actualizarla, su valor cambia a 6. Por favor, revisa el [archivo de Excel de salida](23167014.xlsx) generado con este código y la captura de pantalla que muestra el efecto del código de ejemplo en el archivo de Excel de ejemplo. También revisa la salida en consola que muestra el valor de la celda de la tabla dinámica H8 antes y después de actualizar la tabla dinámica.

![todo:image_alt_text](manipulate-pivot-table_1.png)
## **Código de muestra**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-PivotTables-ManipulatePivotTable-new.cpp" >}}
## **Salida de la consola**
A continuación se muestra la salida en consola del código de ejemplo anterior al ejecutarlo con el [archivo de Excel de ejemplo](23167013.xlsx).

{{< highlight java >}}

 Before refreshing Pivot Table value of cell H8: 15

After refreshing Pivot Table value of cell H8: 6

{{< /highlight >}}
