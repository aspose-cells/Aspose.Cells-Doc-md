---
title: Mostrar fórmulas en lugar de valores en una hoja de trabajo
type: docs
weight: 100
url: /es/java/show-formulas-instead-of-values-in-a-worksheet/
---
{{% alert color="primary" %}}

Es posible mostrar fórmulas en lugar de valores calculados en Microsoft Excel usando t*Mostrar fórmulas* opción de la**Fórmulas**cinta. Cuando se muestran fórmulas, Microsoft Excel muestra fórmulas en la hoja de cálculo. Puede lograr lo mismo usando Aspose.Cells.

{{% /alert %}} 

Aspose.Cells proporciona un[**Hoja de trabajo.setMostrarFórmulas()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ShowFormulas) propiedad. Establezca esto en**verdadero**para configurar Microsoft Excel para mostrar fórmulas.

La siguiente imagen muestra la hoja de cálculo que tiene una fórmula en la celda A3: =Suma(A1:A2).

**Hoja de cálculo con fórmula en la celda A3**

![todo:imagen_alternativa_texto](show-formulas-instead-of-values-in-a-worksheet_1.png)

 La siguiente imagen muestra la fórmula en lugar del valor calculado, habilitado configurando el[**Hoja de trabajo.setMostrarFórmulas()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ShowFormulas) propiedad a**verdadero** con Aspose.Cells.

**La hoja de trabajo ahora muestra la fórmula en lugar del valor calculado**

![todo:imagen_alternativa_texto](show-formulas-instead-of-values-in-a-worksheet_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ShowFormulas-ShowFormulas.java" >}}
