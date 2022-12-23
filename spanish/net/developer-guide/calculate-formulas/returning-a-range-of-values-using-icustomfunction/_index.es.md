---
title: Devolver un rango de valores usando ICustomFunction
type: docs
weight: 50
url: /es/net/returning-a-range-of-values-using-icustomfunction/
---
{{% alert color="primary" %}}

 Él[**IFunciónPersonalizada**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction) está en desuso desde el lanzamiento de Aspose.Cells for Java 20.8. Por favor use el[**ResumenCálculoMotor**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine) clase. el uso de la[**ResumenCálculoMotor**](https://reference.aspose.com/cells/net/aspose.cells/abstractcalculationengine) La clase se describe en el siguiente artículo.

[Devolver un rango de valores usando AbstractCalculationEngine](/cells/es/net/returning-a-range-of-values-using-abstractcalculationengine/).

{{% /alert %}}

{{% alert color="primary" %}}

 Aspose.Cells proporciona[**IFunciónPersonalizada**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction)interfaz que se utiliza para implementar funciones personalizadas o definidas por el usuario que no son compatibles con Microsoft Excel como funciones integradas.

 Sobre todo cuando implementas el[**IFunciónPersonalizada**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction) método de interfaz, debe devolver un valor de celda única. Pero a veces, necesita devolver un rango de valores. Este artículo explicará cómo devolver el rango de valores de[**IFunciónPersonalizada**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction).

{{% /alert %}}

 El siguiente código implementa[**IFunciónPersonalizada**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction)y devuelve el rango de valores a través de su método.

 Crear una clase con una función.*CalculateCustomFunction*. Esta clase implementa[**IFunciónPersonalizada**](https://reference.aspose.com/cells/net/aspose.cells/icustomfunction).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingICustomFunction-CustomFunctionStaticValue.cs" >}}

Ahora use la función anterior en su programa

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithCalculationEngine-ReturnRangeOfValuesUsingICustomFunction-1.cs" >}}
