---
title: Devolver un rango de valores usando ICustomFunction
type: docs
weight: 270
url: /es/java/returning-a-range-of-values-using-icustomfunction/
---
{{% alert color="primary" %}}

 los[**IFunciónPersonalizada**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction) está en desuso desde el lanzamiento de Aspose.Cells for Java 20.8. Por favor use el[**ResumenCálculoMotor**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) clase. el uso de la[**ResumenCálculoMotor**](https://reference.aspose.com/cells/java/com.aspose.cells/AbstractCalculationEngine) La clase se describe en el siguiente artículo.

[Devolver un rango de valores usando AbstractCalculationEngine](/cells/es/java/returning-a-range-of-values-using-abstractcalculationengine/).

{{% /alert %}}

{{% alert color="primary" %}}

 Aspose.Cells proporciona[**IFunciónPersonalizada**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction)interfaz que se utiliza para implementar funciones personalizadas o definidas por el usuario que no son compatibles con Microsoft Excel como funciones integradas.

 Sobre todo cuando implementas el[**IFunciónPersonalizada**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction) método de interfaz, debe devolver un valor de celda única. Pero a veces, necesita devolver un rango de valores. Este artículo explicará cómo devolver el rango de valores de[**IFunciónPersonalizada**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction).

{{% /alert %}}

## **Devolver un rango de valores usando ICustomFunction**

 El siguiente código implementa[**IFunciónPersonalizada**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction) y devuelve el rango de valores a través de su método. Por favor, checa el[archivo de salida de Excel](5472922.xlsx) y[pdf](5472925.pdf) generado con el código para su referencia.

Crear una clase con una función.*CalculateCustomFunction*. Esta clase implementa[**IFunciónPersonalizada**](https://reference.aspose.com/cells/java/com.aspose.cells/ICustomFunction).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-CustomFunctionStaticValue-CustomFunctionStaticValue.java" >}}

Ahora use la función anterior en su programa.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReturningRangeOfValues-ReturningRangeOfValues.java" >}}
