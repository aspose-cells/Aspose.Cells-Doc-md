---
title: Manipular tabla dinámica
type: docs
weight: 20
url: /es/cpp/manipulate-pivot-table/
---
## **Posibles escenarios de uso**
Además de crear nuevas tablas dinámicas, puede manipular las tablas dinámicas nuevas y existentes. Puede cambiar los datos en el rango de origen de la tabla dinámica y luego actualizarlos y calcularlos y obtener los nuevos valores de las celdas de la tabla dinámica. Por favor use[IPivotTable.RefreshData()](https://reference.aspose.com/cells/cpp/class/aspose.cells.pivot.i_pivot_table#ab6d71ded346508a1d4a93c59680ddaf6) y[IPivotTable.CalculateData()](https://reference.aspose.com/cells/cpp/class/aspose.cells.pivot.i_pivot_table#a3d6ffec8ce2a7a4ccb58e0452a1733dd)después de haber cambiado los valores en el rango de origen de la tabla dinámica para actualizar la tabla dinámica.
## **Manipular tabla dinámica**
 El siguiente código de ejemplo carga el[ejemplo de archivo de Excel](23167013.xlsx) y accede a la tabla dinámica existente dentro de su primera hoja de trabajo. Cambia el valor de la celda B3 que está dentro del rango de origen de la tabla dinámica y luego actualiza la tabla dinámica. Antes de actualizar la tabla dinámica, accede al valor de la celda H8 de la tabla dinámica, que es 15 y, después de actualizar la tabla dinámica, su valor cambia a 6. Consulte la[archivo de salida de Excel](23167014.xlsx)generado con este código y la captura de pantalla que muestra el efecto del código de muestra en el archivo de Excel de muestra. Consulte también el resultado de la consola a continuación, que muestra el valor de la celda H8 de la tabla dinámica antes y después de actualizar la tabla dinámica.

![todo:imagen_alternativa_texto](manipulate-pivot-table_1.png)
## **Código de muestra**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-PivotTables-ManipulatePivotTable.cpp" >}}
## **Salida de consola**
 A continuación se muestra la salida de la consola del código de ejemplo anterior cuando se ejecuta con el proporcionado[ejemplo de archivo de Excel](23167013.xlsx).

{{< highlight "java" >}}

 Before refreshing Pivot Table value of cell H8: 15

After refreshing Pivot Table value of cell H8: 6

{{< /highlight >}}
