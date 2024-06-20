---
title: Cálculo de la fórmula de arreglo de tablas de datos
type: docs
weight: 550
url: /es/java/calculation-of-array-formula-of-data-tables/
---

{{% alert color="primary" %}} 

Se puede crear una Tabla de Datos en Microsoft Excel usando Datos > Análisis ¿Qué pasaría si? > Tabla de Datos... Aspose.Cells ahora te permite calcular la fórmula de matriz de la tabla de datos. Por favor, utiliza [Workbook.calculateFormula()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula\(\)) como de costumbre para calcular cualquier tipo de fórmulas.

{{% /alert %}} 
## **Cálculo de fórmulas de matriz de tablas de datos**
En el siguiente código de muestra, usamos este [archivo de Excel fuente](5472579.xlsx) que también se muestra en la siguiente imagen.

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_1.png)

Si cambias el valor de la celda B1 a 100, los valores de la Tabla de Datos que están rellenados con color amarillo se convertirán en 120. El código de muestra genera el [PDF de salida](5472577.pdf) que muestra 120 como valores en la Tabla de Datos como se muestra en esta imagen.

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_2.png)

Aquí está el código de muestra usado para generar el [PDF de salida](5472577.pdf) desde el [archivo de Excel fuente](5472579.xlsx). Por favor, lee los comentarios para más información.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CalculationOfArrayFormula-CalculationOfArrayFormula.java" >}}
