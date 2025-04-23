---
title: Retorno de un rango de valores usando ICustomFunction
type: docs
weight: 270
url: /es/java/returning-a-range-of-values-using-icustomfunction/
---

{{% alert color="primary" %}}

El [**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction) está obsoleto desde el lanzamiento de Aspose.Cells for Java 20.8. Por favor, utiliza la clase [**AbstractCalculationEngine**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine). El uso de la clase [**AbstractCalculationEngine**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) se describe en el siguiente artículo.

[Devolver un rango de valores usando AbstractCalculationEngine](/cells/es/java/returning-a-range-of-values-using-abstractcalculationengine/).

{{% /alert %}}

{{% alert color="primary" %}}

Aspose.Cells proporciona la interfaz [**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction) que se utiliza para implementar funciones personalizadas definidas por el usuario que no son compatibles con las funciones integradas de Microsoft Excel.

Mayormente, cuando se implementa el método de la interfaz [**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction), es necesario devolver un valor de celda única. Pero a veces, es necesario devolver un rango de valores. Este artículo explicará cómo devolver el rango de valores desde [**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction).

{{% /alert %}}

## **Devolver un rango de valores utilizando ICustomFunction**

El siguiente código implementa [**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction) y devuelve el rango de valores a través de su método. Por favor, verifica el [archivo excel de salida](5472922.xlsx) y el [pdf](5472925.pdf) generado con el código para tu referencia.

Crear una clase con una función *CalculateCustomFunction*. Esta clase implementa [**ICustomFunction**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-CustomFunctionStaticValue-CustomFunctionStaticValue.java" >}}

Ahora usa la función anterior en tu programa.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReturningRangeOfValues-ReturningRangeOfValues.java" >}}
{{< app/cells/assistant language="java" >}}
