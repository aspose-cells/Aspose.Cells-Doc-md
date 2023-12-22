---
title: Cálculo de fórmula matricial de tablas de datos
description: Cómo utilizar la biblioteca Aspose.Cells para calcular fórmulas matriciales para una tabla de datos en Microsoft Excel. Al cargar un archivo de Excel existente o crear un nuevo archivo de Excel, podemos usar el método proporcionado por Aspose.Cells para calcular la fórmula matricial de la tabla de datos y obtener el resultado. Finalmente, guardamos el archivo Excel modificado en el disco.
keywords: Aspose.Cells, Excel, data tables, array formulas, calculations
type: docs
weight: 70
url: /es/net/calculation-of-array-formula-of-data-tables/
---
{{% alert color="primary" %}}

Puede crear una tabla de datos en Microsoft Excel usando Datos > Análisis hipotético > Tabla de datos.... Aspose.Cells ahora le permite calcular la fórmula matricial de una tabla de datos. Por favor use[**Libro de trabajo.CalcularFórmula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) como es habitual para calcular cualquier tipo de fórmulas.

{{% /alert %}}

En el siguiente código de muestra, utilizamos el[archivo excel fuente](5115535.xlsx) . Si cambia el valor de la celda B1 a 100, los valores de la tabla de datos que están llenos de color amarillo pasarán a ser 120 como se muestra en las siguientes imágenes. El código de muestra genera el[salida PDF](5115538.pdf).

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_1.png)

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_2.png)

 Aquí está el código de muestra utilizado para generar el[salida PDF](5115538.pdf) desde el[archivo excel fuente](5115535.xlsx). Por favor lea los comentarios para más información.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-CalculationOfArrayFormula-CalculateArrayFormula.cs" >}}
