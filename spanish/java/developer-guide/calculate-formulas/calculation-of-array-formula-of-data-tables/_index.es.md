---
title: Cálculo de fórmula de matriz de tablas de datos
type: docs
weight: 550
url: /es/java/calculation-of-array-formula-of-data-tables/
---
{{% alert color="primary" %}} 

 Puede crear una tabla de datos en Microsoft Excel usando Datos > Análisis hipotético > Tabla de datos.... Aspose.Cells ahora le permite calcular la fórmula de matriz de la tabla de datos. Por favor use[Workbook.calculateFormula()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula\(\)) como normal para el cálculo de cualquier tipo de fórmulas.

{{% /alert %}} 
## **Cálculo de fórmula de matriz de tablas de datos**
 En el siguiente código de ejemplo, usamos este[archivo fuente excel](5472579.xlsx) que también se muestra en la siguiente imagen.

![todo:imagen_alternativa_texto](calculation-of-array-formula-of-data-tables_1.png)

 Si cambia el valor de la celda B1 a 100, los valores de la tabla de datos que se llenan de color amarillo se convertirán en 120. El código de ejemplo genera el[PDF de salida](5472577.pdf) que muestra 120 como valores en la tabla de datos como se muestra en esta imagen.

![todo:imagen_alternativa_texto](calculation-of-array-formula-of-data-tables_2.png)

Aquí está el código de muestra utilizado para generar el[PDF de salida](5472577.pdf) desde el[archivo fuente excel](5472579.xlsx). Por favor, lea los comentarios para obtener más información.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CalculationOfArrayFormula-CalculationOfArrayFormula.java" >}}
