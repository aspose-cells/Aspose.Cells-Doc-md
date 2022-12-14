---
title: Devolver un rango de valores usando AbstractCalculationEngine
type: docs
weight: 275
url: /es/java/returning-a-range-of-values-using-abstractcalculationengine/
---
{{% alert color="primary" %}}

 Aspose.Cells proporciona[**ResumenCálculoMotor**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) clase que se utiliza para implementar funciones personalizadas o definidas por el usuario que no son compatibles con Microsoft Excel como funciones integradas.

 Este artículo explicará cómo devolver el rango de valores de[**ResumenCálculoMotor**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine).

{{% /alert %}}

 El siguiente código demuestra el uso de la[**ResumenCálculoMotor**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine)y devuelve el rango de valores a través de su método.

Crear una clase con una función.*CalculateCustomFunction* . Esta clase se extiende[**ResumenCálculoMotor**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-CustomFunctionStaticValue-CustomFunctionStaticValue.java" >}}

Ahora use la función anterior en su programa.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ReturningRangeOfValues-1.java" >}}
