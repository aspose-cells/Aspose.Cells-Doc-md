---
title: Mostrar fórmulas en lugar de valores en una hoja de cálculo
type: docs
weight: 100
url: /es/java/show-formulas-instead-of-values-in-a-worksheet/
---

{{% alert color="primary" %}}

Es posible mostrar fórmulas en lugar de valores calculados en Microsoft Excel utilizando la opción *Mostrar fórmulas* de la pestaña **Fórmulas**. Cuando se muestran las fórmulas, Microsoft Excel las muestra en la hoja de cálculo. Puede lograr lo mismo utilizando Aspose.Cells.

{{% /alert %}} 

Aspose.Cells proporciona una propiedad [**Worksheet.setShowFormulas()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ShowFormulas). Establézcala en **true** para que Microsoft Excel muestre las fórmulas.

La siguiente imagen muestra la hoja de cálculo que tiene una fórmula en la celda A3: =Suma(A1:A2).

**Hoja de cálculo con fórmula en la celda A3**

![todo:image_alt_text](show-formulas-instead-of-values-in-a-worksheet_1.png)

La siguiente imagen muestra la fórmula en lugar del valor calculado, habilitado al establecer la propiedad [**Worksheet.setShowFormulas()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#ShowFormulas) en **true** con Aspose.Cells.

**La hoja de cálculo ahora muestra la fórmula en lugar del valor calculado**

![todo:image_alt_text](show-formulas-instead-of-values-in-a-worksheet_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ShowFormulas-ShowFormulas.java" >}}
{{< app/cells/assistant language="java" >}}
